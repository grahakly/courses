# Spoken English in 100 Days — source

Generator for `../Spoken_English_in_100_Days.pdf`: a 152-page A4 workbook teaching
spoken English to Indian learners, built around mother tongue influence, stress
and rhythm, the article system, Indianisms and speaking under pressure.

## Regenerate the PDF

```bash
python3 build.py ../Spoken_English_in_100_Days.pdf
```

No third-party packages. The PDF is written directly with the standard library.

## Check the output

```bash
python3 - <<'EOF'
import verify
verify.main("../Spoken_English_in_100_Days.pdf",
            pw=595.28, ph=841.89, ml=64, mr=58, mt=72, mb=64)
EOF
```

`verify.py` parses the generated file back: it validates the xref table, asserts
that every text run carries its own `Tc` (character spacing survives `ET`, so a
missing one silently corrupts a whole page), decompresses every stream, checks
that no two runs sharing a baseline overlap, and reports anything outside the
text block. Pass page numbers as extra arguments to dump their text.

## Layout

| File | Purpose |
| --- | --- |
| `pdfkit.py` | The PDF engine: base-14 font metrics, wrapping with inline `**bold**` / `*italic*`, headings, lists, boxes, tables, running heads, bookmarks, links. |
| `build.py` | Book assembly, front matter, day/stage/review renderers, appendix renderer, content lint. |
| `stage01.py` … `stage10.py` | Course content, one module per stage, each exporting a `STAGE` dict of ten days. |
| `appendices.py` | Sound drills, mother tongue tables, Indianisms, chunk bank, situation scripts, grammar reference, practice plan, sources. |
| `verify.py` | Post-build validation and text extraction. |

## Two constraints worth knowing before you edit

**No IPA, no arrows, no emoji.** The base-14 fonts are not embedded, so every
character must exist in WinAnsi (cp1252). `esc()` raises rather than substituting
`?`, and `build.py` runs a content lint over all strings before rendering. This is
why pronunciation uses a plain-letter respelling with CAPITALS for stress
(`imPORtant`, `uh-BOWT`) instead of phonetic symbols — which is also more usable
for most learners.

**Days fit their page automatically.** `render_day` trial-renders each day on a
throwaway document and reduces the leading in steps (1.0, 0.975, 0.95, 0.925,
0.90) until it fits one page. So you can write content freely without hand-tuning
lengths; only a very long day will be noticeably tighter than its neighbours.

## Day structure

```python
{
    "n": 11,
    "title": "*V* and *W*: Two Different Sounds",
    "focus": "One sentence naming the behaviour.",
    "why": "Why this costs the learner something now.",
    "learn": ["**Lead-in.** Detail.", ...],          # 3–4 items
    "fix": [("wrong version", "**right** version"), ...],   # optional table
    "minutes": 20,
    "drill": ["Step one.", ...],                     # 4–5 steps, done aloud
    "say": ["\u201cModel sentence.\u201d", ...],     # optional
    "trap": "How the learner's first language pulls them off target.",
    "journal": "One question, answered in English.",
}
```

Stage reviews use `summary`, `checklist`, `drill`, `score` and `struggle`.
