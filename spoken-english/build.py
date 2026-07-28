# -*- coding: utf-8 -*-
"""Build 'Spoken English in 100 Days: A Practical Course for Indian Learners'."""

import importlib
import sys

import pdfkit
from pdfkit import (Book, ACCENT, ACCENT2, INK, MUTED, RULE, TINT, TINT2,
                    text_width, wrap_runs, parse_runs)

TITLE = "Spoken English in 100 Days"
A4 = (595.28, 841.89)
STAGE_MODULES = ["stage%02d" % i for i in range(1, 11)]

WRONG = (0.60, 0.16, 0.12)
RIGHT = (0.08, 0.38, 0.22)


def load_stages():
    out = []
    for name in STAGE_MODULES:
        try:
            out.append(importlib.import_module(name).STAGE)
        except ImportError:
            continue
    return out


# ---------------------------------------------------------------------------
# content lint: every string must survive the WinAnsi encoding
# ---------------------------------------------------------------------------

def lint(obj, path="", bad=None):
    bad = {} if bad is None else bad
    if isinstance(obj, str):
        for ch in obj:
            try:
                ch.encode("cp1252")
            except UnicodeEncodeError:
                bad.setdefault(ch, []).append(path)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            lint(k, path, bad)
            lint(v, "%s.%s" % (path, k), bad)
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            lint(v, "%s[%d]" % (path, i), bad)
    return bad


# ---------------------------------------------------------------------------
# Front matter
# ---------------------------------------------------------------------------

def cover(b):
    b.add_page(header=None, folio=False)
    b.rect(0, 0, b.pw, b.ph, fill=ACCENT)
    b.rect(0, 0, b.pw, 26, fill=ACCENT2)
    b.show(b.ml, b.ph - 128, "FOR INDIAN LEARNERS", "B", 11, (0.72, 0.78, 0.92),
           charspace=4.4)
    b.show(b.ml, b.ph - 250, "SPOKEN", "B", 62, (1, 1, 1), charspace=1)
    b.show(b.ml, b.ph - 312, "ENGLISH", "B", 62, (1, 1, 1), charspace=1)
    b.show(b.ml, b.ph - 366, "IN 100 DAYS", "B", 40, (0.98, 0.70, 0.30), charspace=1)
    b.line(b.ml, b.ph - 400, b.ml + 130, b.ph - 400, ACCENT2, 4)
    y = b.ph - 448
    for line in ("From hesitation to clear, confident,",
                 "internationally understood English."):
        b.show(b.ml, y, line, "R", 14.5, (0.82, 0.86, 0.95))
        y -= 23
    y -= 16
    for line in ("Built around the problems Indian speakers actually have:",
                 "mother tongue influence, stress and rhythm, the article",
                 "system, Indianisms, and speaking under pressure."):
        b.show(b.ml, y, line, "R", 11.5, (0.70, 0.76, 0.90))
        y -= 18
    b.show(b.ml, 176, "A COMPLETE SELF-STUDY WORKBOOK", "B", 10.5, (1, 1, 1),
           charspace=2.2)
    b.show(b.ml, 156, "100 daily lessons  \u00b7  10 stage reviews  \u00b7  8 reference "
                      "appendices", "R", 10.5, (0.70, 0.76, 0.90))
    b.show(b.ml, 138, "Mother tongue trap tables for nine Indian languages",
           "R", 10.5, (0.70, 0.76, 0.90))
    b.line(b.ml, 112, b.pw - b.mr, 112, (0.28, 0.36, 0.58), 0.8)
    b.show(b.ml, 88, "Name", "B", 9.5, (0.66, 0.72, 0.88), charspace=1.2)
    b.line(b.ml + 38, 85, b.ml + 230, 85, (0.34, 0.42, 0.64), 0.8)
    b.show(b.ml + 250, 88, "Start date", "B", 9.5, (0.66, 0.72, 0.88), charspace=1.2)
    b.line(b.ml + 316, 85, b.pw - b.mr, 85, (0.34, 0.42, 0.64), 0.8)


def imprint(b):
    b.header = None
    b.start_page(folio=False)
    b.y = b.ph - 150
    b.para("**Spoken English in 100 Days**", size=16, lead=23)
    b.para("A practical, self-study speaking course for Indian learners.",
           size=10.8, lead=16, color=MUTED)
    b.space(26)
    b.rule()
    b.para("**The goal is clarity, not a foreign accent.** This book will not try "
           "to make you sound American or British, and you should be suspicious of "
           "anything that promises it. Indian English is a legitimate, "
           "fully-developed variety spoken by more people than live in most "
           "countries. What costs you opportunities is not having an Indian "
           "accent; it is being *hard to follow* \u2014 wrong syllable stressed, "
           "flat rhythm, words run together, endings dropped, sentences that "
           "wander. Every drill here targets intelligibility and confidence. Your "
           "accent stays yours.", size=10.4, lead=15.8)
    b.space(6)
    b.para("**Why a pronunciation respelling instead of phonetic symbols.** Most "
           "learners cannot read the International Phonetic Alphabet, and a book "
           "you cannot use is worthless. So sounds are written in plain letters "
           "(*thin* = tongue between the teeth, *ship* versus *sheep*) and the "
           "stressed syllable is written in CAPITALS: *phoTOgrapher*, *DEvelop*, "
           "*imPORtant*. The key is on page 5. If you already read phonetic "
           "symbols, you lose nothing \u2014 the sounds are the same sounds.",
           size=10.4, lead=15.8)
    b.space(6)
    b.para("**This is a workbook, not a reader.** Every day has a drill that must "
           "be done *out loud*. Reading about pronunciation silently produces no "
           "change whatsoever \u2014 your mouth learns by moving, and your ear "
           "learns by hearing you.", size=10.4, lead=15.8)
    b.space(6)
    b.para("**On sources.** The course structure follows the sequence used by "
           "established teaching institutions (sounds and stress before rhythm, "
           "rhythm before fluency, fluency before performance) and the mother "
           "tongue influence framing used across Indian training practice. "
           "Sources and further reading are listed in Appendix H.",
           size=10.4, lead=15.8)
    b.space(6)
    b.para("**Scope.** This book teaches speaking. It is not a stammering or "
           "speech-disorder treatment, and it is not an exam guide \u2014 though "
           "Stage 9 will help with the speaking sections of IELTS-style tests and "
           "with visa and placement interviews. If you have a suspected speech or "
           "hearing difficulty, see a speech-language pathologist alongside this "
           "practice.", size=10.4, lead=15.8)
    b.space(18)
    b.rule()
    b.para("Printable A4 workbook. Print double-sided at actual size.",
           size=9.4, lead=14, color=MUTED)


def how_to_use(b):
    b.header = "How to use this course"
    b.start_page()
    b.bookmark("How to Use This Course", 1)
    b.h2("How to Use This Course", space_before=0, size=22)
    b.space(6)
    b.para("You already know more English than you can speak. That gap \u2014 "
           "between what you understand and what comes out of your mouth \u2014 is "
           "not a knowledge problem, so more grammar study will not close it. It "
           "closes with mouth practice, ear practice, and speaking when you are "
           "slightly nervous. This course is built entirely around that.",
           size=10.6, lead=16)
    b.h3("The shape of a day")
    b.kv_table([
        ("Focus", "The single thing today changes about your speech."),
        ("Why it matters", "Two minutes of reading. Why this costs you something now."),
        ("Learn", "The rule or sound, with the detail you need to apply it."),
        ("Instead of / Say this", "Side-by-side correction of the specific mistake."),
        ("Practice today", "The drill. Out loud. Ten to twenty minutes."),
        ("Model sentences", "Sentences to copy exactly until they are automatic."),
        ("Mother tongue trap", "How your first language pulls you off target, and the fix."),
        ("Journal", "One line, in English, before you close the book."),
    ], lw_col=124, size=10.0, lead=14.6)
    b.h3("The five rules that decide whether this works")
    b.numbered([
        "**Speak every drill out loud.** Whispering and reading in your head train nothing. If you live somewhere you cannot speak freely, use a bathroom, a terrace, a bike ride, or a walk with earphones in so it looks like a call.",
        "**Record yourself every week.** Sixty seconds on your phone, same question every time. Your ear cannot hear your own mouth in real time \u2014 the recording is the only honest feedback you have, and it is free.",
        "**Use English with a human being every day.** One sentence counts. A shopkeeper, an auto driver, a colleague, a cousin. Ninety days of drills with no human contact produces a fluent reader, not a fluent speaker.",
        "**Do not translate from your mother tongue.** Translation is what makes you slow and makes your sentences sound wrong. Stage 6 trains you to build English from English chunks instead.",
        "**Repair, do not restart.** When you make a mistake mid-sentence, say the correct version and continue. Confident speakers correct and move on; hesitant speakers apologise and start again.",
    ], size=10.4, lead=15.4)
    b.h3("If you are short on time")
    b.para("Do the drill and skip the reading. Twelve minutes of speaking beats "
           "forty minutes of studying, every single day.", size=10.4, lead=15.4)


def key_page(b):
    b.header = "Pronunciation key"
    b.start_page()
    b.bookmark("The Pronunciation Key", 1)
    b.h2("The Pronunciation Key", space_before=0, size=20)
    b.para("Everything in this book uses ordinary letters. Learn these six "
           "conventions once and the whole course is readable.", size=10.6, lead=16)
    b.box("The six conventions", [
        ("n", [
            "**CAPITALS mark the stressed syllable.** *imPORtant*, *DEvelop*, "
            "*phoTOgrapher*, *hosPItal*. Stress is the single biggest cause of "
            "\u201cI could not follow him\u201d, so it appears on almost every page.",
            "**A sound is named by a common word.** The *ship* sound and the "
            "*sheep* sound. The *cot* sound and the *caught* sound. If you can say "
            "the word, you know the sound.",
            "**The weak sound is written *uh*.** English reduces most unstressed "
            "vowels to a lazy *uh*: *aBOUT* is *uh-BOWT*, *supPORT* is *suh-PORT*. "
            "This one habit does more for your rhythm than anything else.",
            "**Hyphens split syllables.** *com-FOR-tuh-bul*. Say each piece, then "
            "join them at speed.",
            "**Bold marks the part being drilled.** In *de**velop***, the bold is "
            "where your attention goes.",
            "**Nothing here is an accent instruction.** Keep your own voice; "
            "change only what stops people understanding you.",
        ]),
    ], fill=TINT, bar=ACCENT, size=10.0, lead=14.8)
    b.h3("The eight sounds Indian speakers most often need")
    b.kv_table([
        ("*v* and *w*", "**v**an / **w**ine. For *v*, top teeth touch bottom lip. For *w*, round the lips, teeth touch nothing."),
        ("the two *th*", "**th**in (air, no voice) and **th**is (voiced). Tongue tip lightly between the teeth, not behind them."),
        ("*t* and *d*", "**t**op, **d**og. Tongue on the ridge just behind the top teeth, not curled back on the roof of the mouth."),
        ("*p* and *f*", "**p**an / **f**an. For *f*, teeth on lip and let air hiss; no lip pop."),
        ("*s* and *sh*", "**s**ip / **sh**ip. *sh* is wider, with the tongue pulled back."),
        ("*z*", "**z**oo, ro**s**e, hi**s**. English uses *z* far more than the spelling suggests."),
        ("the *cat* sound", "c**a**t, b**a**d, m**a**n. Wider and flatter than the vowel in most Indian languages."),
        ("*uh*, the weak sound", "**a**bout, doct**o**r, suff**e**r. The most common vowel in spoken English."),
    ], lw_col=104, size=9.8, lead=14.2)
    b.para("*Every one of these gets a full day of its own in Stages Two and "
           "Three. This page is only so you can read the notation.*",
           size=9.6, lead=14, color=MUTED)


def placement(b):
    b.header = "Where you are now"
    b.start_page()
    b.bookmark("Where You Are Now", 1)
    b.h2("Where You Are Now", space_before=0, size=20)
    b.para("Tick every statement that is true today. Be honest \u2014 nobody sees "
           "this, and an inflated score just wastes your next hundred days.",
           size=10.6, lead=16)
    b.h3("Tick what is true")
    b.checkboxes([
        "I can introduce myself for a full minute without preparing.",
        "I can speak on the phone in English without dreading it.",
        "People rarely ask me to repeat myself.",
        "I can tell a story about my weekend for two minutes.",
        "I can disagree with someone in English without going silent.",
        "I know which syllable is stressed in words like *comfortable* and *photographer*.",
        "I can hear the difference between *ship* and *sheep* when someone else says them.",
        "I use *a*, *an* and *the* without thinking about it.",
        "I can speak in a meeting of ten people.",
        "I can take a job interview in English and expect to do well.",
        "I think in English for at least part of the day.",
        "I can explain my work to someone outside my field, in English, in one minute.",
    ], size=10.0, lead=14.6)
    b.h3("Read your score")
    b.kv_table([
        ("0 to 3 ticks", "**Start at Day 1 and do not skip.** Your foundation is the sound system and basic patterns. Expect Stages One to Four to feel slow and to matter enormously. Give yourself extra days when a sound will not come."),
        ("4 to 7 ticks", "**Start at Day 1 anyway,** but move faster through Stage One. Your gap is usually rhythm, articles and confidence under pressure \u2014 Stages Four, Five and Nine are where your score will change."),
        ("8 to 10 ticks", "**Skim Stages One to Three for the sounds you personally fail** (record yourself first, Day 1), then work properly from Stage Four. Your remaining accent is fine; your remaining problem is precision and performance."),
        ("11 or 12 ticks", "**You do not need a beginner book.** Work Stages Four, Six, Eight, Nine and Ten in full, use the appendices as reference, and put your effort into Stage Ten's shadowing programme."),
    ], lw_col=104, size=9.9, lead=14.4)
    b.para("Whatever your score, do Day 1 today. The recording you make is the "
           "only way you will ever be able to prove to yourself that this worked.",
           size=10.2, lead=15.2)


def routine_page(b):
    b.header = "The daily twenty minutes"
    b.start_page()
    b.h2("The Daily Twenty Minutes", space_before=0, size=20)
    b.para("A fixed routine removes the daily decision about what to do, which is "
           "where most self-study dies.", size=10.6, lead=16)
    b.box("The routine", [
        ("n", ["**Two minutes \u2014 warm up the mouth.** Say the day's sound ten "
               "times slowly, then ten times fast. Stretch your jaw, hum, and read "
               "one sentence aloud twice.",
               "**Four minutes \u2014 read the day.** Focus, why, learn. Say every "
               "example aloud as you read it; never read an example silently.",
               "**Ten minutes \u2014 do the drill.** Out loud, standing if you can. "
               "Record it whenever the day asks you to.",
               "**Two minutes \u2014 use it with a human.** One real sentence to a "
               "real person, today, using what you just practised.",
               "**Two minutes \u2014 journal in English.** One or two lines. Mistakes "
               "allowed and expected; this is practice, not an exam."]),
    ], fill=TINT2, bar=ACCENT2, size=10.2, lead=15.2)
    b.h3("What you need")
    b.bullets([
        "**A phone**, for recording your voice and for listening practice.",
        "**Earphones.** Real listening practice needs them; laptop speakers hide exactly the sounds you are trying to hear.",
        "**A notebook** for the journal and the written drills.",
        "**A mirror**, for the sound days. Watching your own lips and teeth is how *v* and *w* finally separate.",
        "**A speaking partner, if possible.** A friend, a sibling, a colleague, an online partner. About a third of the drills are better with one; all of them work alone.",
    ], size=10.4, lead=15.4)
    b.h3("Where to find listening material free")
    b.para("You need natural English audio with transcripts for the shadowing "
           "work. Public broadcaster learning services, TED talks with "
           "transcripts, and any podcast that publishes a transcript all work. "
           "Choose speakers you would be happy to sound like, and choose material "
           "you would listen to anyway \u2014 interest beats prestige, because you "
           "will actually finish it.", size=10.4, lead=15.4)
    b.h3("A word about feeling embarrassed")
    b.para("Practising sounds out loud feels ridiculous. Everyone who speaks "
           "excellent second-language English went through exactly this stage, "
           "usually alone in a room, feeling stupid. The embarrassment is not a "
           "sign that it is not working. It is the sign that it is.",
           size=10.4, lead=15.4)


def contents(b, stages, toc, locs, dests):
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

    for label, key in (("How to Use This Course", ("front", "how")),
                       ("The Pronunciation Key", ("front", "key")),
                       ("Where You Are Now", ("front", "placement")),
                       ("The Daily Twenty Minutes", ("front", "routine")),
                       ("Your 100-Day Tracker", ("front", "tracker"))):
        entry(label, key, "B", 10.6)
    b.space(8)
    for s in stages:
        b.ensure(70)
        b.space(7)
        entry("Stage %s \u00b7 %s" % (s["num"], s["title"]), ("stage", s["num"]),
              "B", 11.2, 0, ACCENT)
        b.space(3)
        for d in s["days"]:
            entry("Day %d \u00b7 %s" % (d["n"], d["title"]), ("day", d["n"]),
                  "R", 10.0, 14)
        entry("Stage %s Review" % s["num"], ("review", s["num"]), "I", 10.0, 14, MUTED)
    b.space(10)
    b.ensure(120)
    entry("Appendices", ("app", "top"), "B", 11.2, 0, ACCENT)
    b.space(3)
    for key, label in APPENDIX_INDEX:
        entry(label, ("app", key), "R", 10.0, 14)


def tracker(b):
    b.header = "Your 100-day tracker"
    b.start_page()
    b.h2("Your 100-Day Tracker", space_before=0, size=20)
    b.para("Write the date in each box as you finish. Each row is one stage of the "
           "course.", size=10.4, lead=15.4)
    b.space(8)
    cols, rows = 10, 10
    cw = b.tw / cols
    ch = 32.0
    top = b.y
    for r in range(rows):
        for c in range(cols):
            n = r * cols + c + 1
            x = b.ml + c * cw
            y = top - (r + 1) * ch
            b.rect(x, y, cw - 3, ch - 4, stroke=RULE, lw=0.6)
            b.show(x + 4, y + ch - 14, str(n), "B", 7.6, ACCENT2)
    b.y = top - rows * ch - 14
    b.h3("My weekly recording log")
    b.para("Record the same sixty seconds every week: *\u201cTell me about "
           "yourself and what you do.\u201d* Note the date and the one thing you "
           "hear that you want to fix.", size=9.8, lead=14.2, color=MUTED)
    for _ in range(7):
        b.space(19)
        b.line(b.ml, b.y, b.ml + b.tw, b.y, (0.88, 0.90, 0.91), 0.5)
    b.space(12)
    b.para("*Missing a day is normal. Missing three in a row is the point where "
           "people quit \u2014 if it happens, do a five-minute version of the next "
           "day rather than trying to catch up.*", size=9.8, lead=14.4, color=MUTED)


# ---------------------------------------------------------------------------
# Body
# ---------------------------------------------------------------------------

def fix_table(b, pairs, k=1.0):
    """Two-column 'instead of / say this' correction table."""
    size, lead = 9.5, 13.0 * k
    col = (b.tw - 14) / 2.0
    b.ensure(34)
    b.space(6)
    b.y -= 9.6
    b.show(b.ml, b.y, "INSTEAD OF", "B", 8.2, WRONG, charspace=1.4)
    b.show(b.ml + col + 14, b.y, "SAY THIS", "B", 8.2, RIGHT, charspace=1.4)
    b.space(4)
    b.line(b.ml, b.y, b.ml + b.tw, b.y, RULE, 0.6)
    b.space(3)
    for wrong, right in pairs:
        lw = wrap_runs(parse_runs(wrong, "I"), col - 6, size)
        rw = wrap_runs(parse_runs(right, "R"), col - 6, size)
        b.ensure(max(len(lw), len(rw)) * lead + 6)
        top = b.y
        y = top
        for ln in lw:
            y -= lead
            b.draw_line(b.ml, y, ln, size, WRONG)
        y2 = top
        for ln in rw:
            y2 -= lead
            b.draw_line(b.ml + col + 14, y2, ln, size, INK)
        b.y = min(y, y2) - 4
        b.line(b.ml, b.y, b.ml + b.tw, b.y, (0.91, 0.92, 0.93), 0.5)
        b.space(2)
    b.space(1)


def draw_day(b, d, k=1.0):
    """Draw one day. k scales the leading so a heavy day can be squeezed."""
    b.lead = 14.2 * k
    b.day_heading(d["n"], d["title"], d["focus"])
    b.para(d["why"])
    b.h3("Learn")
    b.bullets(d["learn"], lead=14.2 * k, gap=3 * k)
    if d.get("fix"):
        fix_table(b, d["fix"], k)
    b.box("Practice today \u2014 %d minutes" % d["minutes"],
          [("n", d["drill"])], fill=TINT2, bar=ACCENT2, lead=13.1 * k)
    if d.get("say"):
        b.scripts(d["say"], label="Model sentences \u2014 say each one five times",
                  lead=13.2 * k)
    b.h3("Mother tongue trap")
    b.para(d["trap"], size=9.6, lead=13.6 * k, color=(0.30, 0.32, 0.34))
    b.h3("Journal, in English")
    b.para("*" + d["journal"] + "*", size=9.6, lead=13.6 * k, color=MUTED)


def fits_on_one_page(d, k):
    """Trial-render a day on a throwaway document to see if it fits."""
    t = Book(pw=A4[0], ph=A4[1], ml=64, mr=58, mt=72, mb=64)
    t.body = 10.2
    t.header = "trial"
    t.start_page()
    draw_day(t, d, k)
    return len(t.pages) == 1


def render_day(b, d, stage_title, locs):
    k = 1.0
    for trial in (1.0, 0.975, 0.95, 0.925, 0.90):
        if fits_on_one_page(d, trial):
            k = trial
            break
        k = trial
    b.header = stage_title
    b.start_page()
    locs[("day", d["n"])] = (b.page_index, b.ph - 40)
    draw_day(b, d, k)
    b.lead = 14.2


def render_review(b, s, locs):
    b.header = "Stage %s review" % s["num"]
    b.start_page()
    locs[("review", s["num"])] = (b.page_index, b.ph - 40)
    r = s["review"]
    b.bookmark("Stage %s Review" % s["num"], 2)
    b.show(b.ml, b.y - 12, "CHECKPOINT", "B", 8.8, ACCENT2, charspace=2.0)
    b.y -= 30
    b.show(b.ml, b.y, "Stage %s Review" % s["num"], "B", 21, ACCENT)
    b.y -= 16
    b.rule(space=10)
    b.para(r["summary"], size=10.6, lead=16)
    b.h3("Say it out loud \u2014 tick only what you can actually do")
    b.checkboxes(r["checklist"], size=10.0, lead=14.6)
    b.box("Recording test", [("p", r["drill"])], fill=TINT, bar=ACCENT,
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
    b.h3("If it is not working yet")
    b.para(r["struggle"], size=10.0, lead=14.8, color=(0.30, 0.32, 0.34))


def render_stage(b, s, locs):
    b.part_opener(s["num"], s["title"], s["kicker"], s["blurb"], s["outcomes"])
    locs[("stage", s["num"])] = (b.page_index, b.ph - 20)
    short = "Stage %s \u00b7 %s" % (s["num"], s["title"])
    for d in s["days"]:
        render_day(b, d, short, locs)
    render_review(b, s, locs)


# ---------------------------------------------------------------------------
# Back matter
# ---------------------------------------------------------------------------

try:
    from appendices import APPENDICES, APPENDIX_INDEX
except ImportError:
    APPENDICES, APPENDIX_INDEX = [], []


def render_appendices(b, locs):
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
                b.ensure(74)
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
                           size=9.9, lead=14.2)
            elif kind == "fix":
                fix_table(b, block[1])
            elif kind == "box":
                b.box(block[1], [("p", block[2])] if isinstance(block[2], str)
                      else block[2], fill=TINT, bar=ACCENT, size=10.0, lead=14.8)
            elif kind == "np":
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
    b.y = b.ph - 250
    b.show(b.ml, b.y, "Day 101", "B", 34, (1, 1, 1))
    b.y -= 26
    b.line(b.ml, b.y, b.ml + 80, b.y, ACCENT2, 3)
    b.y -= 40
    save = b.tw
    b.tw = b.tw - 40
    for txt in ("You will not wake up on Day 101 speaking like a newsreader, and "
                "that was never the target. What you should have is different: "
                "people stop asking you to repeat yourself, you stop rehearsing "
                "sentences before you say them, and you stop avoiding the phone.",
                "Keep three habits and the rest maintains itself: the weekly "
                "sixty-second recording, ten minutes of shadowing, and one real "
                "conversation in English every day.",
                "And stop apologising for your English. Nobody who speaks three "
                "languages owes anybody an apology for their accent in the "
                "second one."):
        for ln in wrap_runs(parse_runs(txt), b.tw, 12.6):
            b.y -= 19
            b.draw_line(b.ml, b.y, ln, 12.6, (0.82, 0.86, 0.95))
        b.y -= 14
    b.tw = save


# ---------------------------------------------------------------------------

def build(toc=None, dests=None):
    stages = load_stages()
    b = Book(pw=A4[0], ph=A4[1], ml=64, mr=58, mt=72, mb=64)
    b.body, b.lead = 10.2, 14.2
    locs, toc, dests = {}, toc or {}, dests or {}
    cover(b)
    imprint(b)
    how_to_use(b)
    locs[("front", "how")] = (b.page_index, b.ph - 40)
    key_page(b)
    locs[("front", "key")] = (b.page_index, b.ph - 40)
    placement(b)
    locs[("front", "placement")] = (b.page_index, b.ph - 40)
    routine_page(b)
    locs[("front", "routine")] = (b.page_index, b.ph - 40)
    contents(b, stages, toc, locs, dests)
    tracker(b)
    locs[("front", "tracker")] = (b.page_index, b.ph - 40)
    for s in stages:
        render_stage(b, s, locs)
    render_appendices(b, locs)
    closing(b)
    b.decorate(title=TITLE, skip_pages=(0, 1))
    return b, locs


def main(out="Spoken_English_in_100_Days.pdf"):
    stages = load_stages()
    bad = lint(stages) or {}
    bad.update(lint(APPENDICES) or {})
    if bad:
        for ch, where in bad.items():
            print("UNENCODABLE U+%04X %r in %s" % (ord(ch), ch, where[:3]))
        raise SystemExit("content contains characters the base-14 fonts cannot show")
    print("content lint: ok (%d stages, %d days, %d appendices)"
          % (len(stages), sum(len(s["days"]) for s in stages), len(APPENDICES)))
    b1, locs1 = build()
    toc = {k: v[0] + 1 for k, v in locs1.items() if v}
    b2, locs2 = build(toc, locs1)
    toc2 = {k: v[0] + 1 for k, v in locs2.items() if v}
    if toc2 != toc:
        b2, locs2 = build(toc2, locs2)
    size = b2.output(out)
    print("wrote %s: %d pages, %.1f KB" % (out, len(b2.pages), size / 1024.0))
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
