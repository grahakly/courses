# Courses

Self-study course books, generated as printable PDFs from source in this repo.

| Course | PDF | Source |
| --- | --- | --- |
| System Design in 100 Days | [`System_Design_in_100_Days.pdf`](System_Design_in_100_Days.pdf) | [`system-design-100-days.md`](system-design-100-days.md) + [`generate_pdf.py`](generate_pdf.py) |
| Practical Communication Skills in 100 Days | [`Practical_Communication_Skills_in_100_Days.pdf`](Practical_Communication_Skills_in_100_Days.pdf) | [`communication-skills/`](communication-skills/) |

Both PDFs are produced with the Python standard library only — no third-party
packages to install.

```bash
# System design
python3 generate_pdf.py

# Communication skills
cd communication-skills && python3 build.py ../Practical_Communication_Skills_in_100_Days.pdf
```
