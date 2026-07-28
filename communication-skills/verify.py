"""Validate the generated PDF and extract text so layout can be checked."""
import re
import sys
import zlib

from pdfkit import text_width


def load(path):
    data = open(path, "rb").read()
    m = re.search(rb"startxref\s+(\d+)", data)
    assert m, "no startxref"
    start = int(m.group(1))
    assert data[start:start + 4] == b"xref", "xref not at startxref"
    body = data[start:].split(b"trailer")[0].decode("latin-1")
    lines = body.splitlines()
    count = int(lines[1].split()[1])
    offsets = {}
    for i in range(count):
        parts = lines[2 + i].split()
        if parts[2] == "n":
            offsets[i] = int(parts[0])
    bad = []
    for num, off in offsets.items():
        head = data[off:off + 32]
        if not head.startswith(("%d 0 obj" % num).encode()):
            bad.append((num, head[:20]))
    assert not bad, "broken xref entries: %r" % bad[:5]
    return data, offsets


def obj_body(data, off):
    start = data.index(b"obj", off) + 3
    end = data.index(b"endobj", start)
    return data[start:end]


def pages(data, offsets):
    out = []
    for num in sorted(offsets):
        b = obj_body(data, offsets[num])
        if b"/Type /Page" in b and b"/Pages" not in b:
            cm = re.search(rb"/Contents (\d+) 0 R", b)
            out.append((num, int(cm.group(1))))
    return out


TJ = re.compile(rb"BT /(F\d) ([\d.]+) Tf ([-\d.]+) Tc 1 0 0 1 ([-\d.]+) ([-\d.]+) Tm \((.*?)\) Tj ET",
                re.S)
STATEFUL = re.compile(rb"\bTc\b|\bTw\b|\bTz\b|\bTL\b|\bTr\b")

STYLE = {"F1": "R", "F2": "B", "F3": "I", "F4": "BI"}


def page_items(data, offsets, cnum):
    """Return [(x, y, size, font, charspace, text)] plus the raw stream.

    Every text run must carry its own Tc: character spacing survives ET, so a
    run that omits it inherits whatever the previous run set.
    """
    b = obj_body(data, offsets[cnum])
    raw = b.split(b"stream\n", 1)[1].rsplit(b"\nendstream", 1)[0]
    s = zlib.decompress(raw)
    n_bt = s.count(b"BT ")
    items = []
    for m in TJ.finditer(s):
        txt = m.group(6).replace(b"\\(", b"(").replace(b"\\)", b")").replace(b"\\\\", b"\\")
        items.append((float(m.group(4)), float(m.group(5)), float(m.group(2)),
                      m.group(1).decode(), float(m.group(3)),
                      txt.decode("cp1252")))
    if len(items) != n_bt:
        raise AssertionError("stream has %d text runs but only %d carry an "
                             "explicit Tc -- graphics state will leak" %
                             (n_bt, len(items)))
    # any stateful text operator outside the run pattern is a leak risk
    stray = len(STATEFUL.findall(s)) - len(items)
    if stray:
        raise AssertionError("%d stray text-state operators in stream" % stray)
    return items, s


def run_width(txt, style, size, charspace):
    """Width as a reader will draw it, including per-glyph character spacing."""
    return text_width(txt, style, size) + charspace * len(txt)


def main(path, pw=432.0, ph=648.0, ml=58.0, mr=52.0, mt=62.0, mb=58.0, dump=()):
    data, offsets = load(path)
    pg = pages(data, offsets)
    print("valid xref, objects=%d, pages=%d, size=%.1f KB"
          % (len(offsets), len(pg), len(data) / 1024.0))
    problems = []
    total_words = 0
    for i, (pnum, cnum) in enumerate(pg):
        items, _ = page_items(data, offsets, cnum)
        for (x, y, size, f, cs, txt) in items:
            total_words += len(txt.split())
            right = x + run_width(txt, STYLE[f], size, cs)
            if right > pw - mr + 4 and x > ml - 1:
                problems.append(("past right margin", i + 1, round(right, 1), txt[:30]))
            if x < -1 or x > pw:
                problems.append(("x out of page", i + 1, x, txt[:30]))
            if y < 4 or y > ph - 4:
                problems.append(("y out of page", i + 1, y, txt[:30]))
            if y < mb - 46 and y > 8:
                problems.append(("below text block", i + 1, y, txt[:30]))

        # collision check: on a shared baseline, no run may start before the
        # previous one ends, and word gaps must be roughly a space wide
        rows = {}
        for it in items:
            rows.setdefault(round(it[1], 1), []).append(it)
        for y, row in rows.items():
            row.sort(key=lambda t: t[0])
            for a, b in zip(row, row[1:]):
                a_end = a[0] + run_width(a[5], STYLE[a[3]], a[2], a[4])
                gap = b[0] - a_end
                if gap < -0.4:
                    problems.append(("runs overlap by %.1fpt" % -gap, i + 1,
                                     round(y, 1), "%r|%r" % (a[5][-14:], b[5][:14])))
                else:
                    # words that neither overlap nor leave a full space between
                    # them: the signature of an advance/render width mismatch.
                    # Wider gaps are legitimate layout (columns, indents, folios).
                    sp = text_width(" ", STYLE[a[3]], a[2])
                    if 0.4 < gap < sp * 0.6:
                        problems.append(("words nearly touching (gap %.1f, "
                                         "space %.1f)" % (gap, sp), i + 1,
                                         round(y, 1),
                                         "%r|%r" % (a[5][-14:], b[5][:14])))
        if i + 1 in dump:
            print("\n----- page %d -----" % (i + 1))
            for (x, y, size, f, cs, txt) in sorted(items, key=lambda t: (-t[1], t[0])):
                print("  %6.1f..%6.1f %6.1f %4.1f %s Tc=%.1f | %s"
                      % (x, x + run_width(txt, STYLE[f], size, cs), y, size, f,
                         cs, txt))
    print("text runs total words:", total_words)
    if problems:
        print("PROBLEMS (%d):" % len(problems))
        for p in problems[:25]:
            print("  ", p)
    else:
        print("no layout problems detected")
    return len(problems)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "communication-course.pdf"
    dump = tuple(int(a) for a in sys.argv[2:])
    sys.exit(1 if main(path, dump=dump) else 0)
