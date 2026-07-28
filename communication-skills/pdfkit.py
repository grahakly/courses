"""
pdfkit.py -- a tiny, dependency-free PDF typesetting engine.

Supports: base-14 fonts (Helvetica family), accurate text measurement,
word wrapping with inline **bold** / *italic* markup, headings, bullets,
numbered lists, shaded call-out boxes, rules, tables, grids, running
headers/footers, page folios, internal links and PDF bookmarks (outlines).

Written for the "100 Days of Practical Communication Skills" course book.
"""

import zlib

# ---------------------------------------------------------------------------
# Font metrics (Adobe AFM widths, units of 1/1000 em)
# ---------------------------------------------------------------------------

def _table(groups):
    flat = []
    for g in groups:
        flat.extend(g)
    assert len(flat) == 95, len(flat)
    return {chr(c): w for c, w in zip(range(32, 127), flat)}


_HELV = _table([
    [278, 278, 355, 556, 556, 889, 667, 191, 333, 333, 389, 584, 278, 333, 278, 278],
    [556] * 10,
    [278, 278, 584, 584, 584, 556, 1015],
    [667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722, 778,
     667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611],
    [278, 278, 278, 469, 556, 333],
    [556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222, 833, 556, 556,
     556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500],
    [334, 260, 334, 584],
])

_BOLD = _table([
    [278, 333, 474, 556, 556, 889, 722, 238, 333, 333, 389, 584, 278, 333, 278, 278],
    [556] * 10,
    [333, 333, 584, 584, 584, 611, 975],
    [722, 722, 722, 722, 667, 611, 778, 722, 278, 556, 722, 611, 833, 722, 778,
     667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611],
    [333, 278, 333, 584, 556, 333],
    [556, 611, 556, 611, 556, 333, 611, 611, 278, 278, 556, 278, 889, 611, 611,
     611, 611, 389, 556, 333, 611, 556, 778, 556, 556, 500],
    [389, 280, 389, 584],
])

# A few WinAnsi extras used by the book.
for _t, _extra in ((_HELV, {"\u2018": 222, "\u2019": 222, "\u201c": 333, "\u201d": 333,
                            "\u2022": 350, "\u2013": 556, "\u2014": 1000, "\u00b7": 278,
                            "\u00a0": 278, "\u00e9": 556, "\u2026": 1000}),
                   (_BOLD, {"\u2018": 278, "\u2019": 278, "\u201c": 500, "\u201d": 500,
                            "\u2022": 350, "\u2013": 556, "\u2014": 1000, "\u00b7": 278,
                            "\u00a0": 278, "\u00e9": 556, "\u2026": 1000})):
    _t.update(_extra)

# Regular / Bold / Italic / BoldItalic -> metric table + PDF resource name
FONTS = {
    "R":  ("F1", _HELV),
    "B":  ("F2", _BOLD),
    "I":  ("F3", _HELV),
    "BI": ("F4", _BOLD),
}


def text_width(s, style, size):
    tab = FONTS[style][1]
    return sum(tab.get(ch, 556) for ch in s) * size / 1000.0


# ---------------------------------------------------------------------------
# Low level helpers
# ---------------------------------------------------------------------------

def esc(s):
    """Escape a string for a PDF literal and encode as WinAnsi (cp1252)."""
    out = []
    for ch in s:
        if ch in "()\\":
            out.append("\\" + ch)
        else:
            out.append(ch)
    return "".join(out).encode("cp1252", "replace")


def fmt(x):
    return ("%.2f" % x).rstrip("0").rstrip(".") or "0"


# ---------------------------------------------------------------------------
# Inline markup: **bold**, *italic*, ``literal`` (rendered italic + colour)
# ---------------------------------------------------------------------------

def parse_runs(text, base="R"):
    """Return a list of (text, style) tuples."""
    runs, buf, i = [], "", 0
    bold = italic = False

    def cur_style():
        if bold and italic:
            return "BI"
        if bold:
            return "B"
        if italic:
            return "I"
        return base

    while i < len(text):
        if text.startswith("**", i):
            if buf:
                runs.append((buf, cur_style()))
                buf = ""
            bold = not bold
            i += 2
        elif text[i] == "*":
            if buf:
                runs.append((buf, cur_style()))
                buf = ""
            italic = not italic
            i += 1
        else:
            buf += text[i]
            i += 1
    if buf:
        runs.append((buf, cur_style()))
    if base in ("B", "BI"):
        runs = [(t, ("BI" if s in ("I", "BI") else "B")) for t, s in runs]
    return runs


def runs_to_tokens(runs):
    """Split runs into whitespace-delimited tokens.

    A token is a list of (text, style) segments, so that a word may change
    style part-way through (e.g. *italic*, immediately followed by a comma)
    without gaining a spurious space.
    """
    tokens, fresh = [], True
    for txt, st in runs:
        parts = txt.split(" ")
        for i, p in enumerate(parts):
            if i > 0:
                fresh = True
            if p == "":
                continue
            if fresh or not tokens:
                tokens.append([(p, st)])
                fresh = False
            else:
                tokens[-1].append((p, st))
    return tokens


def token_width(token, size):
    return sum(text_width(t, s, size) for t, s in token)


def line_width(line, size):
    if not line:
        return 0.0
    w = sum(token_width(t, size) for t in line)
    return w + text_width(" ", line[0][0][1], size) * (len(line) - 1)


def wrap_runs(runs, width, size):
    """Greedy wrap. Returns a list of lines; each line is a list of tokens."""
    lines, line, w = [], [], 0.0
    for token in runs_to_tokens(runs):
        tw = token_width(token, size)
        sw = text_width(" ", token[0][1], size)
        if line and w + sw + tw > width:
            lines.append(line)
            line, w = [token], tw
        else:
            if line:
                w += sw
            line.append(token)
            w += tw
    if line:
        lines.append(line)
    return lines


# ---------------------------------------------------------------------------
# Document
# ---------------------------------------------------------------------------

class Doc:
    def __init__(self, pw=432.0, ph=648.0):
        self.pw, self.ph = pw, ph
        self.pages = []
        self.outline = []          # (title, level, page_index, y)
        self._page = None

    # -- page management ---------------------------------------------------
    def add_page(self, header=None, folio=True):
        self._page = {"ops": [], "annots": [], "header": header, "folio": folio}
        self.pages.append(self._page)
        return len(self.pages) - 1

    @property
    def page_index(self):
        return len(self.pages) - 1

    def op(self, s):
        self._page["ops"].append(s)

    def link(self, x, y, w, h, dest_page, dest_y):
        self._page["annots"].append((x, y, w, h, dest_page, dest_y))

    def bookmark(self, title, level, y=None):
        self.outline.append((title, level, self.page_index,
                             self.ph if y is None else y))

    # -- primitives --------------------------------------------------------
    def set_fill(self, c):
        self.op("%s %s %s rg" % (fmt(c[0]), fmt(c[1]), fmt(c[2])))

    def set_stroke(self, c):
        self.op("%s %s %s RG" % (fmt(c[0]), fmt(c[1]), fmt(c[2])))

    def rect(self, x, y, w, h, fill=None, stroke=None, lw=0.6):
        if fill:
            self.set_fill(fill)
        if stroke:
            self.set_stroke(stroke)
            self.op("%s w" % fmt(lw))
        mode = "f" if fill and not stroke else ("S" if stroke and not fill else "B")
        self.op("%s %s %s %s re %s" % (fmt(x), fmt(y), fmt(w), fmt(h), mode))

    def line(self, x1, y1, x2, y2, color=(0, 0, 0), lw=0.6):
        self.set_stroke(color)
        self.op("%s w %s %s m %s %s l S" % (fmt(lw), fmt(x1), fmt(y1), fmt(x2), fmt(y2)))

    def draw_line(self, x, y, line, size, color=(0, 0, 0)):
        """Draw one wrapped line (list of tokens) starting at x."""
        for token in line:
            for t, s in token:
                self.show(x, y, t, s, size, color)
                x += text_width(t, s, size)
            x += text_width(" ", token[0][1], size)
        return x

    def show(self, x, y, s, style="R", size=10, color=(0, 0, 0), charspace=0):
        if not s:
            return
        self.set_fill(color)
        name = FONTS[style][0]
        cs = (" %s Tc" % fmt(charspace)) if charspace else ""
        self.op("BT /%s %s Tf%s 1 0 0 1 %s %s Tm (%s) Tj ET" %
                (name, fmt(size), cs, fmt(x), fmt(y), esc(s).decode("latin-1")))

    # -- output ------------------------------------------------------------
    def output(self, path):
        n = len(self.pages)
        FIRST = 7
        pnum = lambda i: FIRST + 2 * i
        cnum = lambda i: FIRST + 2 * i + 1
        out_first = FIRST + 2 * n

        # ---- outline tree
        items = []
        for title, level, pi, y in self.outline:
            items.append({"title": title, "level": level, "page": pi, "y": y,
                          "kids": []})
        tree = []
        stack = []
        for it in items:
            while stack and stack[-1]["level"] >= it["level"]:
                stack.pop()
            if stack:
                stack[-1]["kids"].append(it)
            else:
                tree.append(it)
            stack.append(it)

        numbered = []

        def assign(nodes):
            for nd in nodes:
                nd["num"] = out_first + 1 + len(numbered)
                numbered.append(nd)
                assign(nd["kids"])
        assign(tree)

        objs = {}

        def outline_obj(nd, parent):
            parts = ["<< /Title (%s) /Parent %d 0 R" %
                     (esc(nd["title"]).decode("latin-1"), parent)]
            sibs = nd["_sibs"]
            idx = sibs.index(nd)
            if idx > 0:
                parts.append("/Prev %d 0 R" % sibs[idx - 1]["num"])
            if idx < len(sibs) - 1:
                parts.append("/Next %d 0 R" % sibs[idx + 1]["num"])
            if nd["kids"]:
                parts.append("/First %d 0 R /Last %d 0 R /Count %d" %
                             (nd["kids"][0]["num"], nd["kids"][-1]["num"],
                              -len(nd["kids"])))
            parts.append("/Dest [%d 0 R /XYZ 0 %s 0]" % (pnum(nd["page"]), fmt(nd["y"])))
            parts.append(">>")
            return " ".join(parts).encode("latin-1")

        def mark_sibs(nodes):
            for nd in nodes:
                nd["_sibs"] = nodes
                mark_sibs(nd["kids"])
        mark_sibs(tree)

        def emit(nodes, parent):
            for nd in nodes:
                objs[nd["num"]] = outline_obj(nd, parent)
                emit(nd["kids"], nd["num"])
        emit(tree, out_first)

        if tree:
            objs[out_first] = ("<< /Type /Outlines /First %d 0 R /Last %d 0 R /Count %d >>"
                               % (tree[0]["num"], tree[-1]["num"], len(tree))).encode()
        else:
            objs[out_first] = b"<< /Type /Outlines /Count 0 >>"

        # ---- catalog / pages / fonts
        objs[1] = ("<< /Type /Catalog /Pages 2 0 R /Outlines %d 0 R "
                   "/PageMode /UseOutlines >>" % out_first).encode()
        kids = " ".join("%d 0 R" % pnum(i) for i in range(n))
        objs[2] = ("<< /Type /Pages /Count %d /Kids [%s] >>" % (n, kids)).encode()
        for num, base in ((3, "Helvetica"), (4, "Helvetica-Bold"),
                          (5, "Helvetica-Oblique"), (6, "Helvetica-BoldOblique")):
            objs[num] = ("<< /Type /Font /Subtype /Type1 /BaseFont /%s "
                         "/Encoding /WinAnsiEncoding >>" % base).encode()

        # ---- pages
        folio = 0
        for i, pg in enumerate(self.pages):
            ops = list(pg["ops"])
            stream = ("\n".join(ops)).encode("latin-1")
            comp = zlib.compress(stream, 9)
            objs[cnum(i)] = (("<< /Length %d /Filter /FlateDecode >>\nstream\n"
                              % len(comp)).encode() + comp + b"\nendstream")
            annots = ""
            if pg["annots"]:
                arr = []
                for (x, y, w, h, dp, dy) in pg["annots"]:
                    arr.append("<< /Type /Annot /Subtype /Link /Border [0 0 0] "
                               "/Rect [%s %s %s %s] /Dest [%d 0 R /XYZ 0 %s 0] >>"
                               % (fmt(x), fmt(y), fmt(x + w), fmt(y + h),
                                  pnum(dp), fmt(dy)))
                annots = " /Annots [%s]" % " ".join(arr)
            objs[pnum(i)] = ("<< /Type /Page /Parent 2 0 R /MediaBox [0 0 %s %s] "
                             "/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R "
                             "/F4 6 0 R >> >> /Contents %d 0 R%s >>"
                             % (fmt(self.pw), fmt(self.ph), cnum(i), annots)).encode("latin-1")

        # ---- serialise
        buf = bytearray(b"%PDF-1.5\n%\xe2\xe3\xcf\xd3\n")
        offsets = {}
        for num in sorted(objs):
            offsets[num] = len(buf)
            buf += ("%d 0 obj\n" % num).encode() + objs[num] + b"\nendobj\n"
        maxnum = max(objs)
        xref = len(buf)
        buf += ("xref\n0 %d\n" % (maxnum + 1)).encode()
        buf += b"0000000000 65535 f \n"
        for num in range(1, maxnum + 1):
            if num in offsets:
                buf += ("%010d 00000 n \n" % offsets[num]).encode()
            else:
                buf += b"0000000000 65535 f \n"
        buf += ("trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n"
                % (maxnum + 1, xref)).encode()
        with open(path, "wb") as f:
            f.write(bytes(buf))
        return len(buf)


# ---------------------------------------------------------------------------
# Book: a flowing layout engine on top of Doc
# ---------------------------------------------------------------------------

INK = (0.13, 0.13, 0.15)
MUTED = (0.42, 0.44, 0.46)
ACCENT = (0.04, 0.35, 0.42)
ACCENT2 = (0.72, 0.36, 0.12)
TINT = (0.925, 0.953, 0.957)
TINT2 = (0.98, 0.945, 0.91)
RULE = (0.80, 0.83, 0.84)


class Book(Doc):
    def __init__(self, pw=432.0, ph=648.0, ml=58.0, mr=52.0, mt=62.0, mb=58.0):
        Doc.__init__(self, pw, ph)
        self.ml, self.mr, self.mt, self.mb = ml, mr, mt, mb
        self.tw = pw - ml - mr
        self.y = ph - mt
        self.header = None
        self.body = 9.8
        self.lead = 14.2

    # -- page plumbing -----------------------------------------------------
    def start_page(self, header=None, folio=True, top=None):
        self.add_page(header if header is not None else self.header, folio)
        self.y = self.ph - (self.mt if top is None else top)
        return self.page_index

    def ensure(self, h):
        if self.y - h < self.mb:
            self.start_page()
            return True
        return False

    def space(self, h):
        if self.y - h > self.mb:
            self.y -= h

    # -- text blocks -------------------------------------------------------
    def para(self, text, size=None, lead=None, style="R", color=None,
             indent=0, right=0, space_after=None, align="left"):
        size = size or self.body
        lead = lead or self.lead
        color = color or INK
        width = self.tw - indent - right
        lines = wrap_runs(parse_runs(text, style), width, size)
        for ln in lines:
            self.ensure(lead)
            x = self.ml + indent
            if align == "center":
                x = self.ml + indent + (width - line_width(ln, size)) / 2.0
            self.y -= lead
            self.draw_line(x, self.y, ln, size, color)
        if space_after:
            self.space(space_after)
        return lines

    def _block_height(self, text, size, lead, width, style="R"):
        return len(wrap_runs(parse_runs(text, style), width, size)) * lead

    # -- headings ----------------------------------------------------------
    def part_opener(self, num, title, kicker, blurb, outcomes):
        self.header = None
        self.start_page(folio=True, top=self.mt)
        self.bookmark("Part %s: %s" % (num, title), 1)
        band = self.ph * 0.42
        self.rect(0, self.ph - band, self.pw, band, fill=ACCENT)
        self.show(self.ml, self.ph - 120, ("PART %s" % num).upper(), "B", 12,
                  (1, 1, 1), charspace=3.6)
        self.line(self.ml, self.ph - 138, self.ml + 52, self.ph - 138, (1, 1, 1), 1.8)
        self.y = self.ph - 178
        for ln in wrap_runs(parse_runs(title, "B"), self.tw - 40, 29):
            self.y -= 34
            self.draw_line(self.ml, self.y, ln, 29, (1, 1, 1))
        self.y -= 30
        self.show(self.ml, self.y, kicker.upper(), "B", 9.2,
                  (0.76, 0.88, 0.90), charspace=2.0)
        self.y = self.ph - band - 46
        self.para(blurb, size=11.2, lead=17.4)
        self.space(24)
        self.show(self.ml, self.y, "BY THE END OF THIS PART YOU CAN", "B", 8.8,
                  ACCENT2, charspace=1.6)
        self.y -= 8
        self.bullets(outcomes, size=10.4, lead=15.6, gap=6)

    def day_heading(self, num, title, focus):
        need = 120
        if self.y - need < self.mb:
            self.start_page()
        self.space(6)
        self.line(self.ml, self.y + 6, self.ml + self.tw, self.y + 6, RULE, 0.7)
        self.space(4)
        self.show(self.ml, self.y - 11, "DAY %d" % num, "B", 9.0, ACCENT2,
                  charspace=2.0)
        w = text_width("DAY %d OF 100" % num, "R", 8.2) + 1.4 * 12
        self.show(self.ml + self.tw - w, self.y - 11, "DAY %d OF 100" % num, "R",
                  8.2, (0.62, 0.64, 0.66), charspace=1.4)
        self.y -= 28
        for ln in wrap_runs(parse_runs(title, "B"), self.tw, 17.5):
            self.draw_line(self.ml, self.y, ln, 17.5, ACCENT)
            self.y -= 21
        self.y += 3
        self.space(4)
        self.para("*Focus:* " + focus, size=9.8, lead=13.8, color=MUTED)
        self.space(8)
        self.bookmark("Day %d - %s" % (num, title), 2, self.y + 60)

    def h2(self, text, space_before=13, space_after=5, color=None, size=12.4):
        self.ensure(space_before + size + space_after + self.lead)
        self.space(space_before)
        self.y -= size
        self.show(self.ml, self.y, text, "B", size, color or ACCENT)
        self.space(space_after)

    def h3(self, text, space_before=10, space_after=3):
        self.ensure(space_before + 22 + self.lead)
        self.space(space_before)
        self.y -= 9.6
        self.show(self.ml, self.y, text.upper(), "B", 8.5, ACCENT2, charspace=1.5)
        self.space(space_after)

    # -- lists -------------------------------------------------------------
    def bullets(self, items, size=None, lead=None, gap=4, indent=0, marker="\u2022",
                color=None):
        size = size or self.body
        lead = lead or self.lead
        color = color or INK
        mw = 11.0
        for it in items:
            lines = wrap_runs(parse_runs(it), self.tw - indent - mw, size)
            self.ensure(min(2, len(lines)) * lead)
            first = True
            for ln in lines:
                self.ensure(lead)
                self.y -= lead
                if first:
                    self.show(self.ml + indent, self.y, marker, "R", size, ACCENT)
                    first = False
                self.draw_line(self.ml + indent + mw, self.y, ln, size, color)
            self.space(gap)

    def numbered(self, items, size=None, lead=None, gap=4, indent=0, start=1):
        size = size or self.body
        lead = lead or self.lead
        mw = 15.0
        for k, it in enumerate(items, start):
            lines = wrap_runs(parse_runs(it), self.tw - indent - mw, size)
            self.ensure(min(2, len(lines)) * lead)
            first = True
            for ln in lines:
                self.ensure(lead)
                self.y -= lead
                if first:
                    self.show(self.ml + indent, self.y, "%d." % k, "B", size, ACCENT)
                    first = False
                self.draw_line(self.ml + indent + mw, self.y, ln, size, INK)
            self.space(gap)

    def checkboxes(self, items, size=9.6, lead=14.0, gap=5):
        for it in items:
            lines = wrap_runs(parse_runs(it), self.tw - 18, size)
            self.ensure(lead * min(2, len(lines)))
            first = True
            for ln in lines:
                self.ensure(lead)
                self.y -= lead
                if first:
                    self.rect(self.ml, self.y - 0.5, 8.4, 8.4, stroke=ACCENT, lw=0.8)
                    first = False
                self.draw_line(self.ml + 18, self.y, ln, size, INK)
            self.space(gap)

    # -- call-outs ---------------------------------------------------------
    def box(self, label, blocks, fill=TINT, bar=ACCENT, size=9.5, lead=13.6):
        """blocks: list of ('p'|'b'|'n', payload)."""
        pad = 10.0
        inner = self.tw - 2 * pad - 4
        h = pad * 2 + 14
        for kind, payload in blocks:
            if kind == "p":
                h += self._block_height(payload, size, lead, inner) + 3
            else:
                for it in payload:
                    h += self._block_height(it, size, lead, inner - 14) * 1.0 + 3.5
                h += 2
        if self.y - h < self.mb:
            if h < (self.ph - self.mt - self.mb):
                self.start_page()
        top = self.y
        drawn_h = min(h, top - self.mb)
        self.rect(self.ml, top - drawn_h, self.tw, drawn_h, fill=fill)
        self.rect(self.ml, top - drawn_h, 3.0, drawn_h, fill=bar)
        self.y = top - pad
        save_ml, save_tw = self.ml, self.tw
        self.ml += pad + 4
        self.tw = inner
        if label:
            self.y -= 9.4
            self.show(self.ml, self.y, label.upper(), "B", 8.4, bar, charspace=1.5)
            self.space(5)
        for kind, payload in blocks:
            if kind == "p":
                self.para(payload, size=size, lead=lead, space_after=3)
            elif kind == "b":
                self.bullets(payload, size=size, lead=lead, gap=3)
            elif kind == "n":
                self.numbered(payload, size=size, lead=lead, gap=3)
        self.ml, self.tw = save_ml, save_tw
        self.y = min(self.y, top - drawn_h)
        self.space(4)

    def scripts(self, items, label="Say it like this"):
        self.h3(label)
        size, lead = 9.5, 13.6
        for it in items:
            lines = wrap_runs(parse_runs(it, "I"), self.tw - 14, size)
            self.ensure(lead * min(2, len(lines)))
            block_top = self.y
            for ln in lines:
                if self.ensure(lead):
                    block_top = self.y
                self.y -= lead
                self.draw_line(self.ml + 14, self.y, ln, size, (0.20, 0.22, 0.24))
            self.line(self.ml + 3, self.y - 1, self.ml + 3, block_top - 2, ACCENT2, 1.4)
            self.space(6)

    def rule(self, space=8, color=RULE, lw=0.7, width=None):
        self.space(space)
        self.line(self.ml, self.y, self.ml + (width or self.tw), self.y, color, lw)
        self.space(space)

    def kv_table(self, rows, lw_col=112, size=9.4, lead=13.4):
        for k, v in rows:
            vlines = wrap_runs(parse_runs(v), self.tw - lw_col - 8, size)
            klines = wrap_runs(parse_runs(k, "B"), lw_col - 8, size)
            h = max(len(vlines), len(klines)) * lead + 6
            self.ensure(h)
            top = self.y
            y = top
            for ln in klines:
                y -= lead
                self.draw_line(self.ml, y, ln, size, ACCENT)
            y2 = top
            for ln in vlines:
                y2 -= lead
                self.draw_line(self.ml + lw_col, y2, ln, size, INK)
            self.y = min(y, y2) - 5
            self.line(self.ml, self.y, self.ml + self.tw, self.y, (0.90, 0.92, 0.93), 0.5)
            self.space(4)

    # -- finishing ---------------------------------------------------------
    def decorate(self, skip_pages=(), title="", running_from=0):
        """Add running heads and folios. Call once, after all content."""
        folio = 0
        for i, pg in enumerate(self.pages):
            folio += 1
            if i in skip_pages or not pg["folio"]:
                continue
            self._page = pg
            # folio
            n = str(folio)
            w = text_width(n, "R", 8.6)
            self.show((self.pw - w) / 2.0, self.mb - 30, n, "R", 8.6, MUTED)
            hdr = pg["header"]
            if hdr and i >= running_from:
                self.show(self.ml, self.ph - self.mt + 30, hdr.upper(), "B", 7.4,
                          MUTED, charspace=1.3)
                w2 = text_width(title.upper(), "R", 7.4) + 1.3 * len(title)
                self.show(self.pw - self.mr - w2, self.ph - self.mt + 30,
                          title.upper(), "R", 7.4, MUTED, charspace=1.3)
                self.line(self.ml, self.ph - self.mt + 22, self.pw - self.mr,
                          self.ph - self.mt + 22, RULE, 0.5)
