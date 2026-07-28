# -*- coding: utf-8 -*-
"""Back matter: reference appendices."""

APPENDICES = [
    # ---------------------------------------------------------------- A
    {
        "letter": "A",
        "key": "phrases",
        "title": "The Phrase Bank",
        "intro": "Language you can borrow verbatim until your own version "
                 "arrives. Say these aloud a few times before you need them "
                 "\u2014 a phrase you have never spoken will not come out under "
                 "pressure. Adapt the wording to your own voice; keep the "
                 "structure.",
        "blocks": [
            ("h", "Buying time to think"),
            ("s", ["\u201cThat is a good question. Give me a second.\u201d",
                   "\u201cI want to give you a proper answer rather than a fast one.\u201d",
                   "\u201cLet me put that in order before I answer.\u201d",
                   "\u201cCan I come back to you on that this afternoon? I would rather check than guess.\u201d"], "Use these instead of filler"),
            ("h", "Checking you understood"),
            ("s", ["\u201cSo what I am hearing is \u2026 have I got that right?\u201d",
                   "\u201cLet me play that back: \u2026\u201d",
                   "\u201cThe part I want to be sure about is \u2026\u201d",
                   "\u201cIs the real issue the cost, or the fact that nobody asked you?\u201d"]),
            ("h", "Opening a conversation with a stranger"),
            ("s", ["\u201cLonger queue than I expected \u2014 have you been to one of these before?\u201d",
                   "\u201cI do not know anybody here yet. Mind if I join you?\u201d",
                   "\u201cWhat brought you along to this one?\u201d",
                   "\u201cI came mostly for the second talk. What about you?\u201d"]),
            ("h", "Going one layer deeper"),
            ("s", ["\u201cHow did you end up doing that?\u201d",
                   "\u201cWhat is the hardest part of it?\u201d",
                   "\u201cYou said it was *mostly* fine \u2014 what was the part that was not?\u201d",
                   "\u201cWhat would you do if it were entirely your call?\u201d",
                   "\u201cWhat are you hoping to do next year that you have not managed yet?\u201d"]),
            ("h", "Leaving a conversation"),
            ("s", ["\u201cI am glad we talked \u2014 the point about pricing will stay with me. I am going to find the coffee.\u201d",
                   "\u201cI need to let you go. Before I do: who else here should I be talking to?\u201d",
                   "\u201cCan I message you about that next week?\u201d"]),
            ("np",),
            ("h", "Recovering a forgotten name"),
            ("s", ["\u201cSorry, I did not catch your name.\u201d",
                   "\u201cSay it again for me? I want to get it right.\u201d",
                   "\u201cI have completely lost your name and I would rather ask than guess.\u201d"]),
            ("h", "Saying no, and the conditional yes"),
            ("s", ["\u201cI cannot take that on this month without dropping something else.\u201d",
                   "\u201cNo to Thursday, but yes to the following week if that still helps.\u201d",
                   "\u201cYes, if the report moves to the twentieth. Otherwise I cannot do both properly.\u201d",
                   "\u201cIf it is more important than the audit, I will swap them \u2014 your call.\u201d",
                   "\u201cI am not able to. I can suggest someone who might be.\u201d"]),
            ("h", "Interrupting, and being interrupted"),
            ("s", ["\u201cLet me pause you there \u2014 I want Ana's view before we run out of time.\u201d",
                   "\u201cCan I jump in? One thing before we move on.\u201d",
                   "\u201cI would like to finish the thought, then I want to hear yours.\u201d",
                   "\u201cI was not quite done \u2014 thirty seconds and it is yours.\u201d"]),
            ("h", "Raising a problem"),
            ("s", ["\u201cCan we talk about the handover? I want it to work well, and at the moment it is causing problems downstream.\u201d",
                   "\u201cThe last three reports arrived after the deadline. I have been rewriting them at night, and I am frustrated. I need them by Thursday midday.\u201d",
                   "\u201cWhen I did not hear back for three days I assumed it was not a priority. Was that right?\u201d",
                   "\u201cFlagging early: this is not a problem yet, but I want you to know now rather than in two weeks.\u201d"]),
            ("h", "Disagreeing"),
            ("s", ["\u201cI can see why that is attractive, and I disagree \u2014 here is where I think it breaks.\u201d",
                   "\u201cIf we optimise for the launch date, A wins. If for support cost, B wins. Which are we optimising for?\u201d",
                   "\u201cI would change my mind if we could get written confirmation by Friday. Can we?\u201d",
                   "\u201cWhat am I missing?\u201d"]),
            ("np",),
            ("h", "When you are provoked"),
            ("s", ["\u201cI want to think before I answer.\u201d",
                   "\u201cI am finding this difficult and I would rather not say something I regret. Can we pick it up after lunch?\u201d",
                   "\u201cI need twenty minutes. I will come back at three.\u201d",
                   "\u201cHelp me understand what is behind that.\u201d"]),
            ("h", "Apologising"),
            ("s", ["\u201cI got that wrong. I committed you to a date without checking, and you worked the weekend because of it.\u201d",
                   "\u201cThat was not fair, and it was mine. From now on I will confirm with you first.\u201d",
                   "\u201cNo excuse \u2014 I should have told you on Monday.\u201d"]),
            ("h", "Giving feedback"),
            ("s", ["\u201cCan I give you one thing from yesterday? It is small and specific.\u201d",
                   "\u201cIn the call you answered twice before Ana had finished. She stopped contributing. Next time, hold your answer until she is done.\u201d",
                   "\u201cHow do you think that went? \u2026 And what would you do differently?\u201d"]),
            ("h", "Receiving feedback"),
            ("s", ["\u201cCan you give me an example so I know what to watch for?\u201d",
                   "\u201cThat is hard to hear and I think it is fair.\u201d",
                   "\u201cThank you for telling me. I want to think about it properly rather than react now.\u201d"]),
            ("h", "Hard questions and objections"),
            ("s", ["\u201cFair challenge. Short answer: we tested at half that volume and it held. Above that, we do not know.\u201d",
                   "\u201cI do not know. I would rather tell you that than guess. I will have an answer by Thursday.\u201d",
                   "\u201cDoes that answer it, or do you want the detail?\u201d",
                   "\u201cThat is a bigger discussion than we have time for \u2014 can we take it after?\u201d"]),
            ("h", "Negotiating"),
            ("s", ["\u201cWhat is driving that date? If I understand the constraint I can probably work with it.\u201d",
                   "\u201cI can do the earlier date if we drop the second review. Which would you prefer?\u201d",
                   "\u201cThat does not work for me. Here is what would.\u201d"]),
        ],
    },
    # ---------------------------------------------------------------- B
    {
        "letter": "B",
        "key": "starters",
        "title": "Sixty Conversation Starters",
        "intro": "Grouped by setting. None of them are clever, and that is the "
                 "point \u2014 a good opener is easy to answer. Pick five, learn "
                 "them, and use them until they are automatic.",
        "blocks": [
            ("h", "At work, with someone you barely know"),
            ("b", ["What are you working on at the moment?",
                   "How long have you been here?",
                   "What did you do before this?",
                   "Which part of your job would surprise people?",
                   "Who should I be talking to about this?",
                   "What is the busiest time of year for your team?",
                   "How did you end up in this field?",
                   "What is the thing everyone gets wrong about your work?",
                   "What would you fix first if it were up to you?",
                   "Is it always this busy, or have I picked a bad week?"]),
            ("h", "At an event or conference"),
            ("b", ["What brought you along to this one?",
                   "Have you been to one of these before?",
                   "Which session are you most looking forward to?",
                   "Anything worth catching that I have missed?",
                   "How far did you have to travel?",
                   "Do you know many people here?",
                   "What are you hoping to get out of today?",
                   "Was the morning session any good?",
                   "Who else here should I meet?",
                   "What made you pick this over the other track?"]),
            ("h", "With a colleague you know slightly"),
            ("b", ["How was your weekend \u2014 anything good?",
                   "What are you working on that you actually enjoy?",
                   "Have you got anything planned for the summer?",
                   "How is the new system treating you?",
                   "What is taking up most of your week?",
                   "Did you get anywhere with that problem from last month?",
                   "Are you still doing the running thing?",
                   "What is the best thing you have read lately?",
                   "How is the team looking after the changes?",
                   "Do you actually get a lunch break in your role?"]),
            ("np",),
            ("h", "Socially, with a stranger"),
            ("b", ["How do you know the host?",
                   "Have you tried the food yet \u2014 what is worth having?",
                   "Are you local, or did you travel in?",
                   "What do you do when you are not doing this?",
                   "How long have you lived around here?",
                   "What is the best thing about this neighbourhood?",
                   "Any recommendations for someone new to the area?",
                   "What have you got coming up that you are looking forward to?",
                   "Did you grow up nearby?",
                   "What would you be doing tonight if you were not here?"]),
            ("h", "Going deeper, once it is warm"),
            ("b", ["What is the best decision you made in the last year?",
                   "What are you learning at the moment?",
                   "What would you do differently if you started again?",
                   "What is something you have changed your mind about?",
                   "What is the part of your job you would keep if you left?",
                   "Who taught you the most, and what did they teach you?",
                   "What is the thing you keep meaning to start?",
                   "What is worth spending money on that most people would not?",
                   "What did you want to be doing at twenty?",
                   "What is the hardest thing you have learned to do?"]),
            ("h", "Reviving a dormant contact"),
            ("b", ["We talked about the tender process last year \u2014 how did that turn out?",
                   "This made me think of you.",
                   "Are you still at the same place?",
                   "I owe you a reply from about a year ago. How are things?",
                   "You mentioned you were learning to sail \u2014 how is that going?",
                   "I am working on something you would have an opinion about.",
                   "No agenda \u2014 just realised it had been a year.",
                   "Did you ever get that project off the ground?",
                   "Are you going to be at the conference this year?",
                   "Can I pick your brain about something for twenty minutes?"]),
        ],
    },
    # ---------------------------------------------------------------- C
    {
        "letter": "C",
        "key": "templates",
        "title": "Written Templates",
        "intro": "Skeletons for the messages you send most often. Replace the "
                 "square brackets, delete anything you do not need, and read it "
                 "aloud once before sending.",
        "blocks": [
            ("h", "Request with a decision needed"),
            ("box", "Template", [
                ("p", "**Subject:** Decision needed: [thing] by [date]"),
                ("p", "Hi [name] \u2014 I need one decision from you: [option A] or "
                      "[option B]."),
                ("p", "Context in three lines: [what changed]. [why it matters]. "
                      "[what happens if we do nothing]."),
                ("p", "My recommendation is [A], because [one reason]. A one-word "
                      "reply is fine. I need it by [date] because [real "
                      "constraint]."),
            ]),
            ("h", "Weekly status update"),
            ("box", "Template", [
                ("p", "**Status:** [on track / at risk / blocked / done]"),
                ("p", "**Progress:** [two outcomes that are now true and were not "
                      "last week]"),
                ("p", "**Next:** [the two things happening this week]"),
                ("p", "**Blockers:** [what is stopping progress, and who can "
                      "clear it]"),
                ("p", "**Ask:** [one specific request, or \u201cnothing needed\u201d]"),
            ]),
            ("h", "Meeting recap"),
            ("box", "Template", [
                ("p", "**Decisions:** [what was decided]"),
                ("p", "**Actions:** [name] does [thing] by [date]. [name] does "
                      "[thing] by [date]."),
                ("p", "**Open:** [what was not resolved, and who will pick it up]"),
                ("p", "Corrections to me by [time tomorrow], otherwise I will "
                      "assume this is right."),
            ]),
            ("np",),
            ("h", "Following up after meeting someone"),
            ("box", "Template", [
                ("p", "Hi [name] \u2014 we talked at [event] about [specific "
                      "topic]. You mentioned [the specific thing they said]; "
                      "[the thing you are sending] is what I was trying to "
                      "remember."),
                ("p", "No need to reply \u2014 just thought it might be useful. If "
                      "you ever want to compare notes on [shared topic], I am "
                      "always up for it."),
            ]),
            ("h", "Chasing something, without friction"),
            ("box", "Template", [
                ("p", "Hi [name] \u2014 nudging this one, and I know you have had a "
                      "busy week. I need [specific thing] to [consequence]. If it "
                      "is not going to happen by [date], tell me and I will "
                      "[alternative]."),
            ]),
            ("h", "Declining"),
            ("box", "Template", [
                ("p", "Thanks for asking me \u2014 I can see why it matters. I "
                      "cannot take it on [timeframe]; I have [honest reason, one "
                      "line]."),
                ("p", "What I can do is [smaller offer], or [person] may have "
                      "capacity. If this is more important than [current "
                      "priority], tell me and I will swap them."),
            ]),
            ("h", "Apology"),
            ("box", "Template", [
                ("p", "I got this wrong: [exactly what you did]. That meant [the "
                      "effect on them, in their terms]."),
                ("p", "No excuse. From now on I will [specific change]. If there "
                      "is anything I can do to put it right, tell me."),
            ]),
            ("h", "Asking for feedback"),
            ("box", "Template", [
                ("p", "Can I ask you something specific? What is one thing I "
                      "could do better in [meetings / my updates / how I run "
                      "this]? I am not fishing for reassurance \u2014 one concrete "
                      "example is more useful to me than a general answer."),
            ]),
        ],
    },
    # ---------------------------------------------------------------- D
    {
        "letter": "D",
        "key": "meetings",
        "title": "Meeting Language Toolkit",
        "intro": "The sentences that make meetings work, sorted by what you are "
                 "trying to do. Most of them belong to whoever is willing to say "
                 "them, not to whoever is chairing.",
        "blocks": [
            ("kv", [
                ("Open with purpose", "\u201cPurpose: we need to choose between the two suppliers. Twenty minutes: ten on trade-offs, five on the decision, five on next steps.\u201d"),
                ("Get in early", "\u201cCan I check one thing before we move on \u2014 are we assuming the budget is confirmed?\u201d"),
                ("Build on someone", "\u201cAdding to what Sam said \u2014 the same applies to renewals.\u201d"),
                ("Bring in a quiet person", "\u201cPriya, you have done this before. What are we missing?\u201d"),
                ("Slow a dominant voice", "\u201cLet me pause you there \u2014 I want to hear Ana before we run out of time.\u201d"),
                ("Name the confusion", "\u201cI think we are talking about two different problems. Can we separate them?\u201d"),
                ("Surface the assumption", "\u201cWhat are we assuming here that we have not verified?\u201d"),
                ("Force the decision", "\u201cWhat would we need to know to decide this today?\u201d"),
                ("Park it honestly", "\u201cWe are not going to resolve this now. I will take it offline with Jon and come back Thursday.\u201d"),
                ("Protect the quiet dissenter", "\u201cBefore we agree \u2014 is anyone uneasy about this? I would rather hear it now.\u201d"),
                ("Define done", "\u201cWhat does *done* look like for this, and who decides?\u201d"),
                ("Assign clearly", "\u201cWho owns that, and by when?\u201d"),
                ("Close it", "\u201cSo: we decided X. Ana does Y by Friday, I do Z by Monday. Still open: the training question. Anything I have missed?\u201d"),
                ("Handle the overrun", "\u201cWe have five minutes and two topics. I suggest we do the decision and move the update to email.\u201d"),
                ("Decline the meeting", "\u201cI do not think I am needed for this one \u2014 send me the notes and pull me in if the scope changes.\u201d"),
            ], 120),
            ("np",),
            ("h", "Running a meeting: the four-minute preparation"),
            ("n", ["Write the purpose in one sentence, and the decision needed.",
                   "Write the time plan: how many minutes on what.",
                   "List who must be there and why. Everyone else gets the notes.",
                   "Send purpose, decision and time plan in advance \u2014 two lines is enough.",
                   "Reserve the last two minutes for the closing summary, and protect them."]),
            ("h", "The five sentences that fix most meetings"),
            ("b", ["**\u201cWhat decision do we need by the end of this?\u201d** Asked at the start, it saves half the meeting.",
                   "**\u201cWho owns that, and by when?\u201d** The difference between a discussion and a plan.",
                   "**\u201cWhat are we assuming?\u201d** Surfaces the thing that later goes wrong.",
                   "**\u201cIs anyone uneasy about this?\u201d** Buys you the objection now rather than the failure later.",
                   "**\u201cLet me summarise where we are.\u201d** Available to anyone, and it makes you the most useful person in the room."]),
            ("h", "If you are the most junior person present"),
            ("b", ["Ask a clarifying question in the first ten minutes. It is low risk and it establishes that you speak.",
                   "Offer to take the notes and send the recap. It gives you a legitimate voice in what was agreed.",
                   "Bring one prepared point. Preparation, not seniority, is what makes a contribution land.",
                   "If you are talked over, return once: \u201cI would like to finish the thought.\u201d Once is enough to change the pattern."]),
            ("h", "Virtual meeting specifics"),
            ("b", ["Signpost more than feels necessary; you cannot read the room.",
                   "Stop every five minutes and ask a direct question to a named person.",
                   "Use the chat deliberately for links, decisions and names \u2014 not for a parallel conversation.",
                   "Say who you are handing to: \u201cThat is me. Ana, over to you.\u201d Turn-taking online has no body language to rely on."]),
        ],
    },
    # ---------------------------------------------------------------- E
    {
        "letter": "E",
        "key": "frameworks",
        "title": "The Frameworks at a Glance",
        "intro": "Every structure used in this course, on two pages, for when you "
                 "need one in a hurry.",
        "blocks": [
            ("kv", [
                ("Intent sentence", "*After this, [person] knows / feels / does [what].* Write it before you speak. Day 2."),
                ("Four message layers", "Content, self-disclosure, relationship, appeal. When a message misfires, it is rarely the content. Day 3."),
                ("Four levels of listening", "Ignoring, waiting, understanding, empathic. Ask which level you are on. Day 12."),
                ("Paraphrase", "\u201cSo what I am hearing is \u2026 have I got that right?\u201d Before you disagree. Day 13."),
                ("FORD", "Family, Occupation, Recreation, Dreams. Small-talk territories. Day 52."),
                ("Headline first (BLUF)", "Conclusion in sentence one, then reasons in descending order. Day 41."),
                ("PREP", "Point, Reason, Example, Point. Any answer in sixty seconds. Day 42."),
                ("Rule of three", "Announce three, deliver three. Day 43."),
                ("Signposting", "Map, transitions, importance flags, closing loop. Day 46."),
                ("STAR", "Situation, Task, Action, Result. Behavioural stories in ninety seconds. Day 49."),
                ("Thirty-second version", "Who it is for, what problem, what you are doing, where it is now. Day 50."),
                ("Status update", "Status word, progress, next, blockers, ask. Day 66."),
                ("Recap", "Decisions, actions with owners and dates, open questions. Day 67."),
                ("Feedback", "Behaviour, effect, request. Observable, recent, forward-looking. Day 75."),
                ("Receiving feedback", "Pause, ask for an example, thank them, decide later. Day 76."),
                ("Saying no", "Acknowledge, decline, offer. Or the conditional yes. Day 77."),
                ("Escalation", "Issue, impact, two options, recommendation, what you need. Day 78."),
                ("Assertive frame", "\u201cI need X. I can do Y. I cannot do Z.\u201d Day 81."),
                ("Difficult opening", "Request the conversation, state intention, describe facts, ask a question. Day 82."),
                ("DESC", "Describe, Express, Specify, Consequences. Day 83."),
                ("Observation vs judgement", "What a camera recorded, versus what you concluded. Day 84."),
                ("Three appeals", "Credibility, logic, feeling. Add the one you neglect. Day 88."),
                ("Objection handling", "Acknowledge, answer briefly, check it landed. Day 89."),
                ("Negotiation prep", "Ideal, minimum, alternative. Trade, do not concede. Day 90."),
                ("Talk design", "One message, three points, designed open and close. Day 91."),
                ("Impromptu", "PREP, or Past-Present-Future, or Problem-Solution-Benefit. Day 97."),
            ], 132),
        ],
    },
    # ---------------------------------------------------------------- F
    {
        "letter": "F",
        "key": "assessment",
        "title": "Self-Assessment: Day 1 and Day 100",
        "intro": "Score yourself out of ten in each area on Day 1, and again on "
                 "Day 100. Do not look at your first scores before writing the "
                 "second set. The gap is the course; the remaining low scores are "
                 "your next hundred days.",
        "blocks": [
            ("h", "The eight areas"),
            ("kv", [
                ("Listening", "I hold my response, paraphrase, and go past the first answer."),
                ("Clarity", "People understand me the first time, without asking me to repeat."),
                ("Brevity", "I answer in one breath and stop, without over-explaining."),
                ("Voice", "My pace, volume, pitch and endings support what I am saying."),
                ("Body language", "My posture, face and hands match my message."),
                ("Small talk", "I can start, sustain and leave a conversation with a stranger."),
                ("Writing", "My messages lead with the point and make the ask explicit."),
                ("Difficult conversations", "I can raise problems and disagree without damage."),
            ], 128),
            ("h", "Score sheet"),
            ("p", "Write the date, then a number out of ten for each area."),
            ("kv", [
                ("Date", "________________          Day 1  /  Day 100  (circle one)"),
                ("Listening", "____ / 10          Clarity  ____ / 10"),
                ("Brevity", "____ / 10          Voice  ____ / 10"),
                ("Body language", "____ / 10          Small talk  ____ / 10"),
                ("Writing", "____ / 10          Difficult conversations  ____ / 10"),
                ("Total", "____ / 80"),
            ], 128),
            ("h", "The recording comparison"),
            ("p", "Record sixty seconds answering *\u201cWhat do you do, and what "
                  "are you working on right now?\u201d* on Day 1 and again on Day "
                  "100. Listen to them back to back, and write what you hear."),
            ("kv", [
                ("Pace", "Day 1: __________________  Day 100: __________________"),
                ("Fillers per minute", "Day 1: __________________  Day 100: __________________"),
                ("Longest sentence", "Day 1: __________________  Day 100: __________________"),
                ("Clear point?", "Day 1: __________________  Day 100: __________________"),
                ("Ending", "Day 1: __________________  Day 100: __________________"),
            ], 128),
            ("h", "Three audible differences"),
            ("p", "Not “I sounded better.” Write three things a stranger "
                  "could verify by listening to both recordings."),
            ("lines", 4),
            ("h", "My next two skills, and the weekly drill for each"),
            ("p", "Choose by cost to you, not by interest. Name the drill and the "
                  "day of the week you will do it."),
            ("lines", 5),
            ("h", "The date I will re-measure"),
            ("p", "Put it in your calendar now, not later. Ninety days from "
                  "today is the usual choice."),
            ("lines", 2),
        ],
    },
    # ---------------------------------------------------------------- G
    {
        "letter": "G",
        "key": "drills",
        "title": "Drill Library and Practice Partners",
        "intro": "Reusable drills for after Day 100, and instructions you can hand "
                 "to a practice partner who has not read the book.",
        "blocks": [
            ("h", "Solo drills, five to ten minutes"),
            ("b", ["**Read aloud.** Three hundred words of good prose. Rotate the focus: breath at punctuation, final consonants, one stressed word per sentence, pace variation.",
                   "**The one-minute answer.** Pick a random question, take two seconds, answer in PREP for sixty seconds. Record one in five.",
                   "**Filler count.** Two minutes explaining anything. Count the fillers. Repeat once, replacing each with a pause.",
                   "**Headline drill.** Take five emails in your sent folder and rewrite the first line of each as a headline.",
                   "**Half-length edit.** Take a paragraph you wrote and cut it by fifty percent without losing meaning.",
                   "**Mirror greeting.** Eyebrow raise, eye contact, genuine smile, opening line. Ten repetitions.",
                   "**Impromptu five.** Five random topics, ninety seconds each, one of the three structures. Recorded.",
                   "**Voice warm-up.** Breath, body, hum, tongue twisters. Five minutes before anything that matters."]),
            ("h", "Real-world drills, no extra time required"),
            ("b", ["**Two strangers a day.** Thirty seconds each. Shop, lift, queue, corridor.",
                   "**One paraphrase per meeting.** Before you add your own view.",
                   "**Three-second gaps.** Leave three seconds after the other person stops, five times a day.",
                   "**One recap.** After every meeting that had actions in it.",
                   "**One question you were avoiding.** Weekly.",
                   "**One assertive sentence.** Daily, however small.",
                   "**Speak in the first ten minutes.** Every meeting, no exceptions."]),
            ("np",),
            ("h", "For your practice partner"),
            ("p", "Hand this section to whoever is helping you. Ten minutes a week "
                  "is enough."),
            ("n", ["**Two-minute listening test.** Talk to them about a real problem for two minutes. They may only nod. Afterwards they tell you the three main points they heard. You check their accuracy \u2014 this trains them and tests you.",
                   "**Question interview.** They ask you five questions about your work. You answer each in under sixty seconds, in PREP. They tell you which answer was longest and which was clearest.",
                   "**Hostile questioner.** They pick your five hardest questions and ask them rapidly, in a slightly cold tone. You practise acknowledge, answer briefly, check.",
                   "**Difficult conversation role-play.** You have prepared a DESC script. They play the other person and push back once, then agree. You practise not abandoning the request.",
                   "**One honest observation.** At the end, they give you one thing they noticed: filler words, pace, eye contact, hedging, length. One thing only \u2014 not a list."]),
            ("h", "The three habits to keep forever"),
            ("b", ["**The two-second pause** before answering anything important. It buys thinking time and reads as composure.",
                   "**The one-sentence intent** before anything that matters. Eight seconds of thought that removes most rambling.",
                   "**The weekly sixty-second recording.** The only honest feedback available for free, and the only reliable defence against quiet decay."]),
            ("h", "A note on what this course does not cover"),
            ("p", "Communication skills will not fix a bullying manager, an unsafe "
                  "workplace, a discriminatory process or a relationship in "
                  "crisis. If you are in one of those situations, the right tools "
                  "are HR, a union representative, a lawyer, a doctor or a "
                  "therapist \u2014 not a better script. Being able to speak "
                  "clearly helps you use those channels, but it is not a "
                  "substitute for them."),
        ],
    },
]

APPENDIX_INDEX = [(a["key"], "%s. %s" % (a["letter"], a["title"])) for a in APPENDICES]
