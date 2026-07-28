# Practical Communication Skills in 100 Days — source

Generator for `../Practical_Communication_Skills_in_100_Days.pdf`: a 145-page A4
workbook with 100 daily lessons, 10 part reviews and 7 appendices.

## Regenerate the PDF

```bash
python3 build.py ../Practical_Communication_Skills_in_100_Days.pdf
```

No third-party packages are needed — the PDF is written directly with the Python
standard library (`zlib` only).

## Check the output

```bash
python3 - <<'EOF'
import verify
verify.main("../Practical_Communication_Skills_in_100_Days.pdf",
            pw=595.28, ph=841.89, ml=64, mr=58, mt=72, mb=64)
EOF
```

`verify.py` parses the generated file back: it validates the xref table and
object offsets, decompresses every content stream, extracts the positioned text
runs, and reports anything that overflows the text block. Pass page numbers as
extra arguments to dump the text of specific pages.

## Layout

| File | Purpose |
| --- | --- |
| `pdfkit.py` | The PDF engine: base-14 font metrics, word wrapping with inline `**bold**` / `*italic*` markup, headings, lists, call-out boxes, tables, running heads, folios, bookmarks and internal links. |
| `build.py` | Book assembly: cover, front matter, contents, tracker, part and day rendering, appendices. Runs the layout twice so contents page numbers and links resolve. |
| `part01.py` … `part10.py` | Course content. One module per part, each exporting a `PART` dict of ten days. |
| `appendices.py` | Back matter: phrase bank, conversation starters, templates, meeting language, framework summary, assessment sheets, drill library. |
| `verify.py` | Post-build validation and text extraction. |

## Editing content

Each day is a dict:

```python
{
    "n": 1,
    "title": "Take Your Communication Baseline",
    "focus": "One sentence naming the behaviour of the day.",
    "why": "Two or three sentences of reasoning.",
    "learn": ["**Lead-in.** Supporting detail.", ...],   # 3–4 items
    "minutes": 20,
    "drill": ["Step one.", ...],                          # 4–5 numbered steps
    "say": ["\u201cBorrowable script.\u201d", ...],       # optional
    "watch": "The failure mode for this skill.",
    "journal": "One question to answer in two or three lines.",
}
```

Content is sized so that one day fills roughly one A4 page. If a day grows past
that it flows onto a second page rather than breaking — run `verify.py` and look
for sparse pages after editing. Use `**bold**` and `*italic*` inline; stay within
the WinAnsi (cp1252) character set, so no emoji or arrows.
