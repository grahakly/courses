# -*- coding: utf-8 -*-
"""Build the 100 Days of Practical Communication Skills course book."""

import importlib
import sys

from pdfkit import (Book, ACCENT, ACCENT2, INK, MUTED, RULE, TINT, TINT2,
                    text_width, wrap_runs, parse_runs)

TITLE = "100 Days of Practical Communication"
A4 = (595.28, 841.89)

PART_MODULES = ["part%02d" % i for i in range(1, 11)]


def load_parts():
    parts = []
    for name in PART_MODULES:
        try:
            mod = importlib.import_module(name)
        except ImportError:
            continue
        parts.append(mod.PART)
    return parts


# ---------------------------------------------------------------------------
# Front matter
# ---------------------------------------------------------------------------

def cover(b):
    b.add_page(header=None, folio=False)
    b.rect(0, 0, b.pw, b.ph, fill=ACCENT)
    b.rect(0, 0, b.pw, 26, fill=ACCENT2)
    b.show(b.ml, b.ph - 132, "A DAILY PRACTICE COURSE", "B", 11,
           (0.70, 0.85, 0.88), charspace=4.4)
    # numeral block
    b.show(b.ml, b.ph - 262, "100", "B", 128, (1, 1, 1))
    b.show(b.ml + 244, b.ph - 210, "DAYS", "B", 44, (0.98, 0.74, 0.44), charspace=2)
    b.show(b.ml + 246, b.ph - 240, "OF PRACTICE", "B", 13, (0.70, 0.85, 0.88),
           charspace=3.2)
    b.line(b.ml, b.ph - 292, b.ml + 130, b.ph - 292, ACCENT2, 4)
    y = b.ph - 348
    for line in ("Practical", "Communication", "Skills"):
        b.show(b.ml, y, line, "B", 38, (1, 1, 1))
        y -= 45
    y -= 22
    for line in ("Ten minutes of theory. Twenty minutes of practice.",
                 "One skill a day, for one hundred days."):
        b.show(b.ml, y, line, "R", 13.5, (0.80, 0.90, 0.92))
        y -= 22
    b.show(b.ml, 168, "A COMPLETE SELF-STUDY WORKBOOK", "B", 10.5, (1, 1, 1),
           charspace=2.2)
    b.show(b.ml, 148, "100 daily lessons  \u00b7  10 part reviews  \u00b7  7 appendices "
                      "of scripts and templates", "R", 10.5, (0.70, 0.85, 0.88))
    b.line(b.ml, 122, b.pw - b.mr, 122, (0.24, 0.48, 0.54), 0.8)
    b.show(b.ml, 96, "Name", "B", 9.5, (0.62, 0.80, 0.84), charspace=1.2)
    b.line(b.ml + 38, 93, b.ml + 230, 93, (0.30, 0.55, 0.60), 0.8)
    b.show(b.ml + 250, 96, "Start date", "B", 9.5, (0.62, 0.80, 0.84), charspace=1.2)
    b.line(b.ml + 316, 93, b.pw - b.mr, 93, (0.30, 0.55, 0.60), 0.8)


def imprint(b):
    b.header = None
    b.start_page(folio=False)
    b.y = b.ph - 200
    b.para("**100 Days of Practical Communication Skills**", size=15, lead=22)
    b.para("A self-study course book with daily lessons, drills, scripts and "
           "review checkpoints.", size=10.6, lead=16, color=MUTED)
    b.space(28)
    b.rule()
    b.para("**How this book is meant to be used.** This is a workbook, not a "
           "reader. Every day contains a short explanation and a practice task "
           "that must be done out loud, in writing, or with another person. "
           "Reading a day without doing the drill produces no measurable change.",
           size=10.4, lead=15.8)
    b.space(6)
    b.para("**A note on evidence and judgement.** The frameworks here (active "
           "listening, PREP, STAR, DESC, non-violent communication, the rhetorical "
           "appeals, BLUF) are long-established tools from teaching, negotiation "
           "and professional training practice. They are starting structures, not "
           "rules. Culture, hierarchy, industry and personality all change what "
           "lands well. Adapt the wording to your own voice and context; keep the "
           "underlying behaviour.", size=10.4, lead=15.8)
    b.space(6)
    b.para("**Scope.** This course covers everyday, professional and public "
           "communication. It is not therapy, and it is not a substitute for "
           "professional help with anxiety, trauma, a speech or language disorder, "
           "or a workplace situation involving harassment or safety. If any of "
           "those apply, seek the appropriate specialist alongside this practice.",
           size=10.4, lead=15.8)
    b.space(20)
    b.rule()
    b.para("Generated as a printable A4 workbook. Set your printer to "
           "double-sided, actual size.", size=9.4, lead=14, color=MUTED)


def how_to_use(b):
    b.header = "How to use this course"
    b.start_page()
    b.bookmark("How to Use This Course", 1)
    b.h2("How to Use This Course", space_before=0, size=22)
    b.space(6)
    b.para("The course is built on a single assumption: communication is a motor "
           "skill as much as an intellectual one. You already understand most of "
           "the ideas in this book. What you lack is repetition under mild "
           "pressure. So the structure is deliberately repetitive.", size=10.6,
           lead=16)
    b.h3("The shape of a day")
    b.kv_table([
        ("Focus", "One sentence naming the single behaviour of the day."),
        ("Why it matters", "The short version of the reasoning. Two minutes of reading."),
        ("Learn", "Two to four concepts, each with the detail you need to apply it."),
        ("Practice today", "The drill. Timed, specific, and mostly done out loud or in writing."),
        ("Say it like this", "Ready-made language you can borrow verbatim until your own version arrives."),
        ("Watch out", "The failure mode. This is where most people go wrong on this skill."),
        ("Journal", "One question to answer in two or three lines before you close the book."),
    ], lw_col=112, size=10.0, lead=14.6)
    b.h3("The rhythm")
    b.bullets([
        "**One day at a time, in order.** The parts build on each other: listening before persuasion, breath before public speaking.",
        "**Twenty to thirty minutes.** Ten minutes reading, fifteen to twenty minutes practising. If you only have ten, do the drill and skip the reading.",
        "**Missed a day? Do not double up.** Just continue. A hundred lessons spread over five months still works. Doubling up turns practice into reading.",
        "**After every tenth day, stop and review.** A part review sits after each block of ten days, with a self-check, a consolidation drill and a five-point score. It is not a lesson day \u2014 add it to the tenth day, or take an extra day for it.",
    ], size=10.4, lead=15.4)
    b.h3("Four rules that decide whether this works")
    b.numbered([
        "**Practise out loud.** Silent reading trains nothing. Your mouth, breath and nerves need the repetition, not your eyes.",
        "**Record yourself weekly.** Sixty seconds on your phone. It is the only honest feedback available for free.",
        "**Use one real situation per day.** Every drill is designed to be dropped into work or life the same day. That transfer is the whole point.",
        "**Keep a written log.** Two or three lines a day. On Day 100 you will read it back, and the change will be obvious in a way that memory cannot show you.",
    ], size=10.4, lead=15.4)


def routine_page(b):
    b.header = "How to use this course"
    b.start_page()
    b.h2("The Daily Twenty Minutes", space_before=0, size=18)
    b.para("If you want a fixed routine, use this one. It fits in a lunch break "
           "and needs no equipment beyond a phone.", size=10.6, lead=16)
    b.box("The routine", [
        ("n", ["**Two minutes \u2014 breathe and warm up.** Ten low breaths (four in, six out). "
               "Hum up and down your range. Say a tongue twister three times, slowly.",
               "**Five minutes \u2014 read the day.** Focus, why, learn. Underline one sentence.",
               "**Ten minutes \u2014 do the drill.** Out loud, standing if you can. Record it if the day asks you to.",
               "**Two minutes \u2014 plan the transfer.** Name the exact conversation today where you will use it, and the words you will use.",
               "**One minute \u2014 journal.** Answer the prompt in two or three lines. Date it."]),
    ], fill=TINT2, bar=ACCENT2, size=10.2, lead=15.2)
    b.h3("What you need")
    b.bullets([
        "**A phone** for audio and video recording.",
        "**A notebook** or a single running document for the journal and the drills that involve writing.",
        "**A practice partner, ideally.** A friend, partner or colleague who will spend ten minutes a week doing a role-play and giving you one honest observation. Roughly a quarter of the drills are better with a partner; all of them can be done alone.",
        "**A mirror or a laptop camera** for the body-language and delivery days.",
    ], size=10.4, lead=15.4)
    b.h3("If you are short on time")
    b.para("Do the drill and nothing else. Twelve minutes of practice beats "
           "thirty minutes of reading every time. The reading is scaffolding; the "
           "drill is the building.", size=10.4, lead=15.4)
    b.h3("If you are nervous about practising with real people")
    b.para("Start with the low-stakes half of every drill: read aloud, record "
           "yourself, rehearse in a mirror, write the script. Then use the "
           "language with a stranger you will never see again \u2014 a shop "
           "assistant, a barista, a neighbour. Strangers are the safest gym in the "
           "world, because there is no history to protect.", size=10.4, lead=15.4)


def contents(b, parts, toc, locs, dests):
    b.header = "Contents"
    b.start_page()
    b.bookmark("Contents", 1)
    b.h2("Contents", space_before=0, size=22)
    b.space(4)

    def entry(label, key, style="R", size=10.2, indent=0, color=None):
        lead = 13.8 if style == "R" else 15.4
        b.ensure(lead + 2)
        b.y -= lead
        x = b.ml + indent
        b.show(x, b.y, label, style, size, color or INK)
        num = toc.get(key)
        if num:
            s = str(num)
            w = text_width(s, style, size)
            b.show(b.ml + b.tw - w, b.y, s, style, size, color or MUTED)
            lw = text_width(label, style, size)
            b.line(x + lw + 6, b.y + 3, b.ml + b.tw - w - 6, b.y + 3,
                   (0.86, 0.88, 0.89), 0.5)
            dest = dests.get(key) or locs.get(key)
            if dest:
                b.link(x, b.y - 3, b.tw - indent, lead, dest[0], dest[1])

    entry("How to Use This Course", ("front", "how"), "B", 10.6)
    entry("The Daily Twenty Minutes", ("front", "routine"), "B", 10.6)
    entry("Your 100-Day Tracker", ("front", "tracker"), "B", 10.6)
    b.space(10)
    for p in parts:
        b.ensure(70)
        b.space(7)
        entry("Part %s \u00b7 %s" % (p["num"], p["title"]), ("part", p["num"]),
              "B", 11.2, 0, ACCENT)
        b.space(3)
        for d in p["days"]:
            entry("Day %d \u00b7 %s" % (d["n"], d["title"]), ("day", d["n"]),
                  "R", 10.0, 14)
        entry("Part %s Review" % p["num"], ("review", p["num"]), "I", 10.0, 14, MUTED)
    b.space(10)
    b.ensure(120)
    entry("Appendices", ("app", "top"), "B", 11.2, 0, ACCENT)
    b.space(3)
    for key, label in APPENDIX_INDEX:
        entry(label, ("app", key), "R", 10.0, 14)


def tracker(b):
    b.header = "Your 100-day tracker"
    b.start_page()
    b.h2("Your 100-Day Tracker", space_before=0, size=18)
    b.para("Fill in the date as you finish each day. Ten columns, ten rows: each "
           "row is one part of the course.", size=10.4, lead=15.4)
    b.space(10)
    cols, rows = 10, 10
    cw = b.tw / cols
    ch = 34.0
    top = b.y
    for r in range(rows):
        for c in range(cols):
            n = r * cols + c + 1
            x = b.ml + c * cw
            y = top - (r + 1) * ch
            b.rect(x, y, cw - 3, ch - 4, stroke=RULE, lw=0.6)
            b.show(x + 4, y + ch - 15, str(n), "B", 7.6, ACCENT2)
    b.y = top - rows * ch - 16
    b.h3("Streak notes")
    for _ in range(6):
        b.space(20)
        b.line(b.ml, b.y, b.ml + b.tw, b.y, (0.88, 0.90, 0.91), 0.5)
    b.space(14)
    b.para("*Three missed days in a row is the danger point. If it happens, "
           "restart with a five-minute version of the next day rather than trying "
           "to catch up.*", size=9.8, lead=14.4, color=MUTED)


# ---------------------------------------------------------------------------
# Body
# ---------------------------------------------------------------------------

def render_day(b, d, part_title, locs):
    b.header = part_title
    b.start_page()
    locs[("day", d["n"])] = (b.page_index, b.ph - 40)
    b.day_heading(d["n"], d["title"], d["focus"])
    b.para(d["why"])
    b.h3("Learn")
    b.bullets(d["learn"])
    b.box("Practice today \u2014 %d minutes" % d["minutes"],
          [("n", d["drill"])], fill=TINT2, bar=ACCENT2)
    if d.get("say"):
        b.scripts(d["say"])
    b.h3("Watch out")
    b.para(d["watch"], size=9.6, lead=14.0, color=(0.30, 0.32, 0.34))
    b.h3("Journal")
    b.para("*" + d["journal"] + "*", size=9.6, lead=14.0, color=MUTED)


def render_review(b, p, locs):
    b.header = "Part %s review" % p["num"]
    b.start_page()
    locs[("review", p["num"])] = (b.page_index, b.ph - 40)
    r = p["review"]
    b.bookmark("Part %s Review" % p["num"], 2)
    b.show(b.ml, b.y - 12, "CHECKPOINT", "B", 8.8, ACCENT2, charspace=2.0)
    b.y -= 30
    b.show(b.ml, b.y, "Part %s Review" % p["num"], "B", 21, ACCENT)
    b.y -= 16
    b.rule(space=10)
    b.para(r["summary"], size=10.6, lead=16)
    b.h3("Self-check \u2014 tick only what is true")
    b.checkboxes(r["checklist"], size=10.0, lead=14.6)
    b.box("Consolidation drill", [("p", r["drill"])], fill=TINT, bar=ACCENT,
          size=10.2, lead=15.2)
    b.h3("Score yourself 1-5")
    for label in r["score"]:
        b.ensure(20)
        b.y -= 18
        b.show(b.ml, b.y, label, "R", 10.0, INK)
        x = b.ml + b.tw - 5 * 22
        for k in range(5):
            b.rect(x + k * 22, b.y - 2.5, 13, 13, stroke=RULE, lw=0.6)
            b.show(x + k * 22 + 4.4, b.y + 0.6, str(k + 1), "R", 7.4, MUTED)
    b.space(14)
    b.h3("If you are still struggling")
    b.para(r["struggle"], size=10.0, lead=14.8, color=(0.30, 0.32, 0.34))


def render_part(b, p, locs):
    b.part_opener(p["num"], p["title"], p["kicker"], p["blurb"], p["outcomes"])
    locs[("part", p["num"])] = (b.page_index, b.ph - 20)
    short = "Part %s \u00b7 %s" % (p["num"], p["title"])
    if len(short) > 58:
        short = short[:56].rstrip() + "\u2026"
    for d in p["days"]:
        render_day(b, d, short, locs)
    render_review(b, p, locs)


# ---------------------------------------------------------------------------
# Back matter
# ---------------------------------------------------------------------------

try:
    from appendices import APPENDICES, APPENDIX_INDEX
except ImportError:
    APPENDICES, APPENDIX_INDEX = [], []


def render_appendices(b, locs):
    if not APPENDICES:
        return
    for a in APPENDICES:
        b.header = "Appendix %s \u00b7 %s" % (a["letter"], a["title"])
        b.start_page()
        locs[("app", a["key"])] = (b.page_index, b.ph - 40)
        if a is APPENDICES[0]:
            locs[("app", "top")] = (b.page_index, b.ph - 40)
            b.bookmark("Appendices", 1)
        b.bookmark("%s. %s" % (a["letter"], a["title"]), 2)
        b.show(b.ml, b.y - 12, "APPENDIX %s" % a["letter"], "B", 8.8, ACCENT2,
               charspace=2.0)
        b.y -= 32
        for ln in wrap_runs(parse_runs(a["title"], "B"), b.tw, 21):
            b.draw_line(b.ml, b.y, ln, 21, ACCENT)
            b.y -= 25
        b.y += 4
        b.rule(space=10)
        if a.get("intro"):
            b.para(a["intro"], size=10.4, lead=15.6, color=(0.28, 0.30, 0.32))
        for block in a["blocks"]:
            kind = block[0]
            if kind == "h":
                b.ensure(74)          # never orphan a heading at a page foot
                b.h2(block[1], space_before=14, space_after=4, size=13)
            elif kind == "sh":
                b.h3(block[1])
            elif kind == "p":
                b.para(block[1], size=10.2, lead=15.2)
            elif kind == "b":
                b.bullets(block[1], size=10.0, lead=14.3, gap=3)
            elif kind == "n":
                b.numbered(block[1], size=10.0, lead=14.3, gap=3)
            elif kind == "s":
                b.scripts(block[1], label=block[2] if len(block) > 2 else "Say it like this")
            elif kind == "kv":
                b.kv_table(block[1], lw_col=block[2] if len(block) > 2 else 130,
                           size=10.0, lead=14.6)
            elif kind == "box":
                b.box(block[1], [("p", block[2])] if isinstance(block[2], str)
                      else block[2], fill=TINT, bar=ACCENT, size=10.0, lead=14.8)
            elif kind == "np":
                # soft break: only if the current page is meaningfully used
                if b.y < b.ph - b.mt - 170:
                    b.start_page()
            elif kind == "lines":
                for _ in range(block[1]):
                    b.space(19)
                    b.line(b.ml, b.y, b.ml + b.tw, b.y, (0.88, 0.90, 0.91), 0.5)
                b.space(10)


def closing(b):
    b.header = None
    b.start_page(folio=True)
    b.rect(0, 0, b.pw, b.ph, fill=ACCENT)
    b.y = b.ph - 260
    b.show(b.ml, b.y, "Day 101", "B", 34, (1, 1, 1))
    b.y -= 26
    b.line(b.ml, b.y, b.ml + 80, b.y, ACCENT2, 3)
    b.y -= 40
    save = b.tw
    b.tw = b.tw - 40
    for txt in ("Nobody finishes learning this. The point of a hundred days is "
                "not mastery; it is a set of habits that keep improving on their "
                "own because you now notice what you are doing.",
                "Keep three things: the pause, the one-sentence intent, and the "
                "weekly recording. Those three will carry the rest.",
                "Then pick the two skills that still cost you the most, and give "
                "them the next hundred days."):
        for ln in wrap_runs(parse_runs(txt), b.tw, 12.6):
            b.y -= 19
            b.draw_line(b.ml, b.y, ln, 12.6, (0.86, 0.93, 0.94))
        b.y -= 14
    b.tw = save


# ---------------------------------------------------------------------------

def build(toc=None, dests=None):
    parts = load_parts()
    b = Book(pw=A4[0], ph=A4[1], ml=64, mr=58, mt=72, mb=64)
    b.body, b.lead = 10.2, 14.9
    locs = {}
    toc = toc or {}
    dests = dests or {}
    cover(b)
    imprint(b)
    locs[("front", "how")] = None
    how_to_use(b)
    locs[("front", "how")] = (b.page_index, b.ph - 40)
    routine_page(b)
    locs[("front", "routine")] = (b.page_index, b.ph - 40)
    contents(b, parts, toc, locs, dests)
    tracker(b)
    locs[("front", "tracker")] = (b.page_index, b.ph - 40)
    for p in parts:
        render_part(b, p, locs)
    render_appendices(b, locs)
    closing(b)
    b.decorate(title=TITLE, skip_pages=(0, 1))
    return b, locs


def main(out="100-Days-of-Practical-Communication-Skills.pdf"):
    # pass 1: discover where everything landed
    b1, locs1 = build()
    toc = {k: v[0] + 1 for k, v in locs1.items() if v}
    # pass 2: page numbers and working internal links
    b2, locs2 = build(toc, locs1)
    toc2 = {k: v[0] + 1 for k, v in locs2.items() if v}
    if toc2 != toc:
        # layout shifted; converge once more
        b2, locs2 = build(toc2, locs2)
    size = b2.output(out)
    print("wrote %s: %d pages, %.1f KB" % (out, len(b2.pages), size / 1024.0))
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
