#!/usr/bin/env python3
"""
Pure-Python PDF generator for the interview questions book.

No external dependencies (the build sandbox has no network access, so pandoc /
reportlab / weasyprint are unavailable). Writes a PDF 1.4 file directly.

Improvements over the original generate_pdf.py in this repo:
  * Page tree /Kids references are computed correctly (the original emitted
    consecutive object numbers while page objects are allocated two apart,
    producing a malformed page tree).
  * Code blocks render in Courier and are never re-wrapped or markdown-stripped.
  * Markdown tables are buffered and rendered as aligned monospace columns.
  * Width-aware word wrapping instead of a single hard-coded character count.
  * Footer with page numbers; headings avoid becoming orphans at a page break.

Usage:
    python3 generate_interview_pdf.py [input.md] [output.pdf]
"""

import re
import sys
import os

# ----------------------------------------------------------------------------
# Layout constants (US Letter, points)
# ----------------------------------------------------------------------------
PAGE_W, PAGE_H = 612, 792
MARGIN_L, MARGIN_R = 54, 54
MARGIN_T, MARGIN_B = 64, 58
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R

# Average glyph width as a fraction of font size.
# Courier is exactly 0.6 (monospace); Helvetica averages ~0.52 for mixed text.
COURIER_RATIO = 0.600
HELV_RATIO = 0.520

FONT_BODY = "/F1"      # Helvetica
FONT_BOLD = "/F2"      # Helvetica-Bold
FONT_MONO = "/F3"      # Courier


def helv_width(text, size):
    return len(text) * size * HELV_RATIO


def mono_max_chars(size):
    return int(CONTENT_W / (size * COURIER_RATIO))


class PDFBuilder:
    def __init__(self):
        self.pages = []              # list of list-of-content-stream-operators
        self.cur = []
        self.y = PAGE_H - MARGIN_T

    # ---------------- low level ----------------
    @staticmethod
    def _esc(text):
        """Escape for a PDF literal string and drop non-Latin-1 glyphs."""
        text = text.replace("\\", r"\\").replace("(", r"\(").replace(")", r"\)")
        # PDF base-14 fonts are Latin-1; replace anything outside it
        return text.encode("latin-1", errors="replace").decode("latin-1")

    def _space_left(self):
        return self.y - MARGIN_B

    def new_page(self):
        if self.cur:
            self.pages.append(self.cur)
        self.cur = []
        self.y = PAGE_H - MARGIN_T

    def _need(self, points):
        """Break the page if fewer than `points` vertical space remain."""
        if self._space_left() < points:
            self.new_page()

    def _line(self, text, size=10, font=FONT_BODY, indent=0, leading=None):
        leading = leading if leading is not None else size * 1.35
        self._need(leading)
        x = MARGIN_L + indent
        self.cur.append(
            f"BT {font} {size} Tf 1 0 0 1 {x} {self.y:.1f} Tm ({self._esc(text)}) Tj ET"
        )
        self.y -= leading

    def vspace(self, points):
        self.y -= points

    # ---------------- block level ----------------
    def wrapped(self, text, size=10, font=FONT_BODY, indent=0, hanging=0):
        """Word-wrap `text` to the content width and emit it."""
        if not text.strip():
            self.vspace(size * 0.5)
            return
        avail = CONTENT_W - indent
        words, line, first = text.split(), "", True
        for w in words:
            probe = w if not line else line + " " + w
            if helv_width(probe, size) > avail and line:
                self._line(line, size, font, indent if first else indent + hanging)
                first, line = False, w
            else:
                line = probe
        if line:
            self._line(line, size, font, indent if first else indent + hanging)

    def title(self, text):
        # Titles start a fresh page so each major part begins cleanly.
        if self.cur:
            self.new_page()
        self.vspace(120)
        self.wrapped(text, size=22, font=FONT_BOLD)
        self.vspace(14)

    def h1(self, text):
        self._need(70)
        self.vspace(16)
        self.wrapped(text, size=15, font=FONT_BOLD)
        self.vspace(7)

    def h2(self, text):
        self._need(56)
        self.vspace(11)
        self.wrapped(text, size=12, font=FONT_BOLD)
        self.vspace(4)

    def h3(self, text):
        self._need(46)
        self.vspace(8)
        self.wrapped(text, size=10.5, font=FONT_BOLD)
        self.vspace(3)

    def code_block(self, lines):
        size = 8.2
        limit = mono_max_chars(size)
        self.vspace(5)
        for raw in lines:
            raw = raw.replace("\t", "    ")
            if not raw.strip():
                self.vspace(size * 0.9)
                continue
            # Hard-split over-long code lines rather than reflowing words.
            while len(raw) > limit:
                cut = raw.rfind(" ", 0, limit)
                cut = cut if cut > limit * 0.6 else limit
                self._line(raw[:cut], size, FONT_MONO, indent=8, leading=size * 1.22)
                raw = "    " + raw[cut:].lstrip()
            self._line(raw, size, FONT_MONO, indent=8, leading=size * 1.22)
        self.vspace(6)

    def table(self, rows):
        """rows: list of list-of-cell-strings. Rendered as aligned monospace."""
        if not rows:
            return
        ncols = max(len(r) for r in rows)
        rows = [r + [""] * (ncols - len(r)) for r in rows]
        widths = [max(len(r[c]) for r in rows) for c in range(ncols)]

        size = 8.2
        limit = mono_max_chars(size)
        # Shrink the widest columns until the row fits the page width.
        while sum(widths) + 3 * (ncols - 1) > limit:
            widest = widths.index(max(widths))
            if widths[widest] <= 6:
                break
            widths[widest] -= 1

        def fmt(row):
            cells = []
            for c in range(ncols):
                cell = row[c]
                if len(cell) > widths[c]:
                    cell = cell[: max(1, widths[c] - 1)] + "~"
                cells.append(cell.ljust(widths[c]))
            return "  ".join(cells).rstrip()

        self.vspace(5)
        self._need(len(rows) * size * 1.25 + 10)
        header = fmt(rows[0])
        self._line(header, size, FONT_MONO, indent=6, leading=size * 1.25)
        self._line("-" * min(len(header), limit), size, FONT_MONO,
                   indent=6, leading=size * 1.25)
        for row in rows[1:]:
            self._line(fmt(row), size, FONT_MONO, indent=6, leading=size * 1.25)
        self.vspace(7)

    def rule(self):
        self._need(20)
        self.vspace(6)
        self.cur.append(
            f"0.6 w 0.65 G {MARGIN_L} {self.y:.1f} m {PAGE_W - MARGIN_R} {self.y:.1f} l S 0 G"
        )
        self.vspace(11)


# ----------------------------------------------------------------------------
# Markdown -> PDF
# ----------------------------------------------------------------------------
INLINE_PATTERNS = [
    (re.compile(r"\*\*(.+?)\*\*"), r"\1"),          # bold
    (re.compile(r"(?<!\w)__(.+?)__(?!\w)"), r"\1"), # bold alt
    (re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)"), r"\1"),  # italic
    (re.compile(r"`(.+?)`"), r"\1"),                # inline code
    (re.compile(r"\[(.+?)\]\((.+?)\)"), r"\1 (\2)"),# links
]

TABLE_DIVIDER = re.compile(r"^[\s|:\-]+$")


def strip_inline(text):
    for pattern, repl in INLINE_PATTERNS:
        text = pattern.sub(repl, text)
    return text


def split_table_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [strip_inline(c.strip()) for c in line.split("|")]


def render(md_text, pdf):
    lines = md_text.split("\n")
    i, n = 0, len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # ---- fenced code block: consume verbatim to the closing fence ----
        if stripped.startswith("```"):
            i += 1
            block = []
            while i < n and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1                      # skip closing fence
            pdf.code_block(block)
            continue

        # ---- markdown table: buffer contiguous pipe rows ----
        if stripped.startswith("|") and "|" in stripped[1:]:
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                if not TABLE_DIVIDER.match(lines[i].strip()):
                    rows.append(split_table_row(lines[i]))
                i += 1
            pdf.table(rows)
            continue

        # ---- horizontal rule ----
        if stripped in ("---", "***", "___"):
            pdf.rule()
            i += 1
            continue

        # ---- headings ----
        if stripped.startswith("#"):
            level = len(stripped) - len(stripped.lstrip("#"))
            text = strip_inline(stripped[level:].strip())
            if level == 1:
                pdf.title(text)
            elif level == 2:
                pdf.h1(text)
            elif level == 3:
                pdf.h2(text)
            else:
                pdf.h3(text)
            i += 1
            continue

        # ---- blockquote ----
        if stripped.startswith(">"):
            pdf.wrapped("  " + strip_inline(stripped[1:].strip()),
                        size=9.5, indent=10)
            i += 1
            continue

        # ---- bullet list ----
        m = re.match(r"^(\s*)[-*+]\s+(.*)$", line)
        if m:
            depth = len(m.group(1)) // 2
            pdf.wrapped("- " + strip_inline(m.group(2)),
                        size=9.7, indent=12 + depth * 14, hanging=10)
            i += 1
            continue

        # ---- ordered list ----
        m = re.match(r"^(\s*)(\d+)\.\s+(.*)$", line)
        if m:
            depth = len(m.group(1)) // 2
            pdf.wrapped(f"{m.group(2)}. " + strip_inline(m.group(3)),
                        size=9.7, indent=12 + depth * 14, hanging=12)
            i += 1
            continue

        # ---- blank / paragraph ----
        if not stripped:
            pdf.vspace(5)
        else:
            pdf.wrapped(strip_inline(stripped), size=10)
        i += 1


# ----------------------------------------------------------------------------
# PDF assembly
# ----------------------------------------------------------------------------
def add_footers(pages):
    """Stamp 'Page n of N' centred at the bottom of every page."""
    total = len(pages)
    for idx, content in enumerate(pages, start=1):
        label = f"Page {idx} of {total}"
        width = len(label) * 8 * HELV_RATIO
        x = (PAGE_W - width) / 2
        content.append(
            f"BT {FONT_BODY} 8 Tf 1 0 0 1 {x:.1f} {MARGIN_B - 26} Tm 0.45 g "
            f"({label}) Tj ET 0 g"
        )
    return pages


def build_pdf(pages):
    objects = []          # list of byte strings, index 0 -> object 1

    n_pages = len(pages)
    # Object layout: 1 catalog, 2 pages, 3 resources, then per page: page, content
    kids = " ".join(f"{4 + 2 * i} 0 R" for i in range(n_pages))

    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    objects.append(
        f"<< /Type /Pages /Kids [{kids}] /Count {n_pages} >>".encode("latin-1")
    )
    objects.append(
        b"<< /Font << "
        b"/F1 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica "
        b"/Encoding /WinAnsiEncoding >> "
        b"/F2 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold "
        b"/Encoding /WinAnsiEncoding >> "
        b"/F3 << /Type /Font /Subtype /Type1 /BaseFont /Courier "
        b"/Encoding /WinAnsiEncoding >> "
        b">> >>"
    )

    for content in pages:
        stream = "\n".join(content).encode("latin-1", errors="replace")
        page_obj = (
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PAGE_W} {PAGE_H}] "
            f"/Contents {len(objects) + 2} 0 R /Resources 3 0 R >>"
        ).encode("latin-1")
        objects.append(page_obj)
        objects.append(
            b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n"
            + stream + b"\nendstream"
        )

    out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = []
    for num, body in enumerate(objects, start=1):
        offsets.append(len(out))
        out += f"{num} 0 obj\n".encode("latin-1") + body + b"\nendobj\n"

    xref_at = len(out)
    out += f"xref\n0 {len(objects) + 1}\n".encode("latin-1")
    out += b"0000000000 65535 f \n"
    for off in offsets:
        out += f"{off:010d} 00000 n \n".encode("latin-1")
    out += (
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
        f"startxref\n{xref_at}\n%%EOF\n"
    ).encode("latin-1")
    return bytes(out)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        here, "interview-1000-questions.md")
    dst = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
        here, "Interview_1000_Questions.pdf")

    with open(src, encoding="utf-8") as fh:
        md = fh.read()

    print(f"Source   : {src}")
    print(f"Markdown : {len(md):,} chars, {md.count(chr(10)):,} lines")

    pdf = PDFBuilder()
    render(md, pdf)
    pdf.new_page()                       # flush the final page
    pages = add_footers(pdf.pages)
    data = build_pdf(pages)

    with open(dst, "wb") as fh:
        fh.write(data)

    # Question headings are section-prefixed: "## Question 1", "## MERN Q3", "## JS Q7", ...
    questions = len(re.findall(r"^## (?:Question|[A-Z]{2,4} Q)\s*\d+", md, re.M))
    print(f"Output   : {dst}")
    print(f"Size     : {len(data) / 1024:.1f} KB")
    print(f"Pages    : {len(pages)}")
    print(f"Questions: {questions}")


if __name__ == "__main__":
    main()
