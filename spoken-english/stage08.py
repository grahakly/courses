# -*- coding: utf-8 -*-
STAGE = {
    "num": "Eight",
    "title": "English at Work",
    "kicker": "Days 71-80",
    "blurb": "This is the stage that changes your salary. Indian professionals are "
             "often technically stronger than their communication makes them look, "
             "and the gap costs promotions, client trust and credit for their own "
             "work. Ten days on the specific situations that matter: dropping the "
             "Indianisms that mark you in global rooms, standups, client calls, "
             "speaking up in meetings, asking for help, feedback in both directions, "
             "pushing back, presenting, and talking to seniors across cultures.",
    "outcomes": [
        "Replace the office Indianisms with international equivalents.",
        "Give a sixty-second status update that a manager can act on.",
        "Speak up in a meeting within the first ten minutes.",
        "Ask for help and clarification in a way that raises your credibility.",
        "Push back on an unreasonable request without damaging the relationship.",
    ],
    "days": [
        {
            "n": 71,
            "title": "Drop the Office Indianisms",
            "focus": "Swap thirty phrases for their international equivalents.",
            "why": "Indian office English has its own well-established vocabulary "
                   "\u2014 *do the needful, revert, prepone, out of station, kindly, "
                   "the same* \u2014 which is perfectly correct within India and "
                   "unknown, archaic or brusque outside it. If you work with global "
                   "teams, or want to, this list is the single fastest change you can "
                   "make. It takes one day and it lasts forever.",
            "learn": [
                "**Most of these are old-fashioned rather than wrong.** *Do the needful* and *revert* were normal British business English a century ago and survived here. Outside India they sound either quaint or vague.",
                "**The replacement is always more specific.** *Do the needful* becomes an actual instruction: *\u201ccould you approve it and send it back?\u201d*",
                "**Keep them for Indian contexts if you like.** This is register-switching, not self-correction. Two vocabularies, chosen deliberately.",
            ],
            "fix": [
                ("*Please do the needful and revert.*", "*Could you approve it and let me know?*"),
                ("*Can we prepone the meeting?*", "*Could we move the meeting earlier?*"),
                ("*He is out of station.* / *on leave only*", "*He is out of town.* / *He is on leave.*"),
                ("*Kindly find the same attached.*", "*I have attached it.* / *The file is attached.*"),
            ],
            "minutes": 22,
            "drill": [
                "Learn these ten swaps and say each aloud five times: *do the needful -> take a look and confirm \u00b7 revert -> reply / get back to me \u00b7 prepone -> move earlier \u00b7 out of station -> out of town \u00b7 kindly -> please \u00b7 the same -> it \u00b7 intimate -> inform / let me know \u00b7 discuss about -> discuss \u00b7 cope up with -> cope with \u00b7 order for -> order.*",
                "Ten more: *myself Rajesh -> I'm Rajesh \u00b7 what is your good name -> what was your name \u00b7 pass out (of college) -> graduate \u00b7 doubt -> question \u00b7 today itself -> today \u00b7 yesterday only -> just yesterday \u00b7 like that only -> something like that \u00b7 tell me -> how can I help? \u00b7 no issues -> no problem \u00b7 same to same -> exactly the same.*",
                "Search your last twenty sent emails for these phrases. Count them; the number is usually a surprise.",
                "Rewrite three real messages with the replacements, then read both versions aloud.",
                "Pick your three most-used and ban them for a week.",
            ],
            "say": [
                "\u201cCould you review this and get back to me by Thursday?\u201d",
                "\u201cI have a question about the second requirement \u2014 could we go through it?\u201d",
            ],
            "trap": "*Doubt* is the one that causes real confusion: in Indian English "
                    "it means *question*, but internationally *\u201cI have a "
                    "doubt\u201d* suggests you distrust what you were told. Say *\u201cI "
                    "have a question\u201d*. Similarly *\u201cI passed out in "
                    "2019\u201d* means you fainted; say *graduated*.",
            "journal": "Which three Indianisms do I use most? Write the replacement for each.",
        },
        {
            "n": 72,
            "title": "The Standup and the Status Update",
            "focus": "Sixty seconds: status, progress, blockers, ask.",
            "why": "Daily standups and weekly updates are where most people are "
                   "quietly judged. Long, detailed accounts of effort read as poor "
                   "prioritisation; a crisp update reads as someone who understands "
                   "what matters. The same information, in a fixed order, changes how "
                   "senior people see your judgement.",
            "learn": [
                "**Lead with a status word:** *on track, at risk, blocked, done.* One word tells your manager whether to keep listening closely.",
                "**Report outcomes, not activity.** *\u201cPayment flow is live for ten per cent of users\u201d* rather than *\u201cI worked on payments.\u201d*",
                "**Name the blocker and who can clear it.** This is the entire reason the meeting exists.",
                "**Finish with your ask, or say there is none.** Both are useful; trailing off is not.",
            ],
            "fix": [
                ("*Yesterday I was doing the API work, then I was checking\u2026*", "*On track. The API is done and tested.*"),
                ("*There is some small issue but I will manage.*", "*Blocked: I need the test account from IT by Wednesday.*"),
                ("*I am trying my best, sir.*", "*It should be done by Thursday. I will flag it if that changes.*"),
                ("*Nothing to update.*", "*No change since yesterday \u2014 still on the migration, still on track.*"),
            ],
            "minutes": 20,
            "drill": [
                "Write your real update in four lines: status word, progress, next, blocker or ask.",
                "Say it aloud and time it. Cut until it is under sixty seconds.",
                "Rewrite every activity phrase as an outcome. *\u201cI was working on\u201d* becomes *\u201cX is now done / X is now live.\u201d*",
                "Practise the blocked version five times: *\u201cBlocked. I need X from Y by Wednesday, otherwise the date moves.\u201d*",
                "Deliver it for real tomorrow and note whether anyone asked for more detail \u2014 if they did, the length was right.",
            ],
            "say": [
                "\u201cOn track. Two of the three integrations are live and tested. Next: the third, then load testing. Nothing needed from anyone.\u201d",
                "\u201cAt risk. If I do not get sign-off by Thursday, the launch moves to the eighth. That is the whole update.\u201d",
            ],
            "trap": "Two habits to unlearn: describing how hard you worked, which "
                    "reads as justification rather than progress; and hiding a "
                    "problem to avoid looking bad. Flagging a risk early is the "
                    "single strongest credibility signal available to a junior "
                    "employee anywhere in the world.",
            "journal": "Write tomorrow's update in four lines.",
        },
        {
            "n": 73,
            "title": "Client Calls With Global Teams",
            "focus": "Be clear, be structured, and check understanding.",
            "why": "On an international client call you are dealing with three things "
                   "at once: a compressed audio channel, listeners who do not share "
                   "your context, and often several accents in one room. Structure "
                   "carries more weight here than vocabulary, and checking "
                   "understanding is not weakness \u2014 it is standard professional "
                   "practice on every call in every country.",
            "learn": [
                "**Open with the agenda and the time.** *\u201cThree things today, about twenty minutes: the delay, the two options, and what I need from you.\u201d*",
                "**Signpost each section.** *\u201cThat is the problem. Now the options.\u201d* Listeners on a call cannot see your structure.",
                "**Check in every few minutes:** *\u201cDoes that make sense so far?\u201d \u201cShall I go into the detail, or is the summary enough?\u201d*",
                "**Summarise and confirm at the end,** with owners and dates. Then send it in writing the same day.",
            ],
            "fix": [
                ("Starting with detail and no map", "*\u201cLet me give you the headline first, then the detail.\u201d*"),
                ("*Yes yes, ok ok* while not following", "*\u201cSorry, could I check one thing before we move on?\u201d*"),
                ("*I will revert with the same.*", "*\u201cI will send you the summary today.\u201d*"),
                ("Ending with no summary", "*\u201cSo: you confirm by Friday, I send the revised plan Monday.\u201d*"),
            ],
            "minutes": 22,
            "drill": [
                "Write the opening for your next real call: three items, total time, and the one decision you need.",
                "Say it aloud five times until it is smooth.",
                "Practise two signposting phrases and two check-in phrases, five times each.",
                "Practise the closing summary: two actions with names and dates, then *\u201canything I have missed?\u201d*",
                "On your next real call, use the opening, one check-in and the closing summary. Note what changed.",
            ],
            "say": [
                "\u201cBefore we start: three things, about twenty minutes, and I need one decision from you at the end.\u201d",
                "\u201cLet me pause there \u2014 does that match what you are seeing on your side?\u201d",
            ],
            "trap": "Saying *yes* to show respect while not following is common and "
                    "expensive, because you then act on the wrong information and the "
                    "client discovers it later. Asking a clarifying question mid-call "
                    "costs you nothing in international business culture and protects "
                    "the relationship.",
            "journal": "What is the opening line for my next client call?",
        },
        {
            "n": 74,
            "title": "Speaking Up in Meetings",
            "focus": "Say something in the first ten minutes.",
            "why": "In meetings, silence is read as having nothing to contribute, "
                   "whatever the real reason. The longer you wait, the higher the bar "
                   "becomes in your own head. Speaking early and briefly resets it, "
                   "and it is far easier than it sounds because your first "
                   "contribution does not need to be brilliant.",
            "learn": [
                "**Four low-risk entries:** ask a clarifying question; agree with a reason; build on what someone said; summarise where the discussion is.",
                "**Prepare two things beforehand.** One question and one point. Preparation is what makes people sound spontaneous.",
                "**Interrupt politely when you must:** *\u201cCan I add something here?\u201d \u201cSorry, can I jump in?\u201d \u201cBefore we move on \u2014 one thing.\u201d*",
                "**Say your point and stop.** Contributions over forty-five seconds get interrupted anyway.",
            ],
            "fix": [
                ("Staying silent through the whole meeting", "*\u201cCan I check one thing before we move on?\u201d*"),
                ("*Sorry sorry, excuse me, sorry\u2026*", "*\u201cCan I add something here?\u201d*"),
                ("*I also feel the same as him only.*", "*\u201cI agree with Sam, and I would add that \u2026\u201d*"),
                ("Speaking for three minutes when interrupted", "*\u201cShort point: \u2026 Happy to say more if useful.\u201d*"),
            ],
            "minutes": 20,
            "drill": [
                "Before your next three meetings, write one question and one point you could make.",
                "Say each aloud twice before the meeting. Rehearsal removes ninety per cent of the hesitation.",
                "Learn the four entries by heart: *\u201cCan I check \u2026\u201d \u201cI agree with X because \u2026\u201d \u201cAdding to what X said \u2026\u201d \u201cSo where we are is \u2026\u201d*",
                "Practise the polite interrupt five times aloud, in a normal voice.",
                "In your next meeting, speak within the first ten minutes, even if only to ask something.",
            ],
            "say": [
                "\u201cCan I check one thing \u2014 are we assuming the budget is already approved?\u201d",
                "\u201cAdding to what Ana said, the same issue applies to renewals.\u201d",
            ],
            "trap": "Many Indian workplaces genuinely discourage juniors from "
                    "speaking before seniors, so silence is often a learned "
                    "professional habit rather than a language problem. In "
                    "international teams the same silence is read as "
                    "disengagement or weak ownership. Know which room you are in.",
            "journal": "What did I not say in a meeting today? Write the sentence.",
        },
        {
            "n": 75,
            "title": "Asking for Help and Clarification",
            "focus": "Ask in a way that shows judgement, not ignorance.",
            "why": "Most people avoid asking questions at work because they fear "
                   "looking incapable, and instead spend hours guessing. A "
                   "well-framed question does the opposite of exposing you: it shows "
                   "you have thought about the problem, and it surfaces the wrong "
                   "assumption before it becomes an expensive mistake.",
            "learn": [
                "**Show your work first.** *\u201cI have read the spec and tried two approaches. What I cannot work out is \u2026\u201d* This converts a question into evidence of effort.",
                "**Ask about assumptions:** *\u201cWhat are we assuming about the client's timeline?\u201d* Often the highest-value question in the room.",
                "**Define done:** *\u201cWhat does finished look like for this, and who signs it off?\u201d* Ask this at the start of every task.",
                "**Ask the obvious question when nobody else will.** Frequently three other people also did not understand.",
            ],
            "fix": [
                ("*Sir, I have a doubt.*", "*I have a question about the second requirement.*"),
                ("*I am not able to do it.*", "*I have tried X and Y. I am stuck on Z \u2014 could you point me to the right person?*"),
                ("*Please explain again.* (no context)", "*I followed the first part. Could you go over the data flow again?*"),
                ("Guessing and delivering the wrong thing", "*Before I start: what does done look like here?*"),
            ],
            "minutes": 20,
            "drill": [
                "Write the three questions you have been avoiding at work. For each, add the line *\u201cwhat I have already tried is \u2026\u201d*",
                "Say each aloud three times, then ask one of them today.",
                "Practise the assumption question and the define-done question five times each.",
                "Practise the partial-understanding request: *\u201cI followed up to the point where \u2026 could you take it from there again?\u201d*",
                "Write down what happened when you asked. It is almost never as bad as expected.",
            ],
            "say": [
                "\u201cI have read the brief twice and tried two approaches. I am stuck on how the two systems share the customer record \u2014 who would know?\u201d",
                "\u201cBefore we commit: what are we assuming here that we have not verified?\u201d",
            ],
            "trap": "Asking questions you could answer with five minutes of reading "
                    "is a genuine cost to colleagues; asking the question that "
                    "reading exposed is a genuine contribution. And replace *doubt* "
                    "with *question* \u2014 in international English, *\u201cI have a "
                    "doubt\u201d* implies suspicion.",
            "journal": "What question have I been avoiding? What is the cost of not asking it?",
        },
        {
            "n": 76,
            "title": "Feedback, Both Directions",
            "focus": "Give it specifically; take it without defending.",
            "why": "Feedback conversations are where careers are shaped and "
                   "relationships are damaged. Two skills cover most of it: "
                   "describing a specific behaviour rather than judging a person, "
                   "and receiving criticism without explaining, which is what makes "
                   "people willing to tell you things in future.",
            "learn": [
                "**Give it as behaviour, effect, request.** *\u201cIn the client call you answered before Ana finished, twice. She stopped contributing. Next time, let her finish.\u201d*",
                "**Never use character words:** *lazy, careless, negative, disorganised.* Describe what a camera would have recorded.",
                "**Receiving: pause, ask for an example, thank them, decide later.** *\u201cCan you give me an example so I know what to watch for?\u201d*",
                "**Do not explain in the moment.** *\u201cLet me think about that and come back to you\u201d* is a complete, strong response.",
            ],
            "fix": [
                ("*You are always careless with the numbers.*", "*Two of the figures in Friday's report were wrong. Could you double-check before sending?*"),
                ("*Sir, it was not my mistake, actually the data\u2026*", "*Thank you \u2014 can you give me an example so I know what to look for?*"),
                ("*Your English is bad.* (as feedback you receive)", "*Which part was unclear? I would rather know.*"),
                ("*Sorry sorry, I will never do it again.*", "*Understood. I will add a check before sending.*"),
            ],
            "minutes": 20,
            "drill": [
                "Write one piece of real feedback you owe someone, in behaviour-effect-request form. Remove every judgement word.",
                "Say it aloud three times, then deliver it this week.",
                "Write your own defensive reflex \u2014 explaining, blaming the data, going silent, over-apologising. Everyone has one.",
                "Rehearse the four-step receiving response aloud until automatic: pause, example, thanks, think about it.",
                "Ask one person today: *\u201cWhat is one thing I could do better in our meetings?\u201d* Then run the four steps.",
            ],
            "say": [
                "\u201cCan I give you one thing from yesterday's call? It is small and specific.\u201d",
                "\u201cThat is useful, and it is fair. Can you give me one more example?\u201d",
            ],
            "trap": "In many Indian workplaces feedback arrives as blunt criticism, "
                    "often publicly, so the learned response is either to apologise "
                    "heavily or to defend. Both damage you in international settings. "
                    "The neutral, curious response \u2014 asking for an example "
                    "\u2014 reads as confidence everywhere.",
            "journal": "What feedback do I owe someone? Write the behaviour-effect-request version.",
        },
        {
            "n": 77,
            "title": "Saying No and Pushing Back",
            "focus": "Decline or renegotiate without damaging the relationship.",
            "why": "Saying yes to everything makes you unreliable, because you then "
                   "miss things quietly. A clear no given early protects your "
                   "reputation far better than a reluctant yes followed by a late "
                   "delivery. This is harder in hierarchical workplaces, which is "
                   "exactly why the conditional yes is the most useful tool here.",
            "learn": [
                "**Acknowledge, decline, offer:** *\u201cI can see why this matters. I cannot take it on this week. What I can do is review the draft.\u201d*",
                "**The conditional yes is usually the best answer:** *\u201cYes, if the report moves to the twentieth\u201d* or *\u201cyes, if we drop the newsletter.\u201d* It makes the trade-off visible instead of hidden.",
                "**Give a short, real reason.** One line. Long justifications invite negotiation.",
                "**Do not over-apologise.** One acknowledgement is enough; repeated apology invites them to reopen the request.",
            ],
            "fix": [
                ("*Yes sir, no problem.* (when it is impossible)", "*I can do it by Wednesday, not by Monday. Which matters more?*"),
                ("*I will try.* (meaning no)", "*I do not think I can. Here is what I can do instead.*"),
                ("*Sorry sorry, I am very sorry, actually I have\u2026*", "*I am at capacity this week. Could we look at next week?*"),
                ("*That is not my work.*", "*That sits with the platform team \u2014 shall I introduce you?*"),
            ],
            "minutes": 20,
            "drill": [
                "List three things you said yes to recently that you should have renegotiated.",
                "Write the acknowledge-decline-offer version of each and say it aloud three times.",
                "Write two conditional-yes sentences for requests you expect this week.",
                "Practise the trade-off question five times: *\u201cIf I take this on, which of the other two moves?\u201d*",
                "Say no, or a conditional yes, to one real thing this week. Note what actually happened \u2014 usually nothing.",
            ],
            "say": [
                "\u201cI can take it on if the audit moves to next week. Otherwise I will not do either properly \u2014 your call.\u201d",
                "\u201cI cannot make Monday. Wednesday is realistic, and I will send a draft on Tuesday.\u201d",
            ],
            "trap": "*\u201cI will try\u201d* used to mean *no* is common in Indian "
                    "workplaces and is understood locally. International managers "
                    "hear it as *yes, probably*, and plan accordingly \u2014 then the "
                    "deadline is missed and you are blamed for something you thought "
                    "you had declined. Say the real answer.",
            "journal": "What should I have said no to this week? Write the sentence.",
        },
        {
            "n": 78,
            "title": "Presenting to a Room",
            "focus": "One message, three points, a designed opening and close.",
            "why": "Presentations are where technical people are judged as leaders. "
                   "Most bad presentations are not delivery failures; they are "
                   "structure failures \u2014 no clear message, too many points, and "
                   "slides read aloud. Fixing the structure improves the delivery "
                   "automatically, because you are no longer trying to remember what "
                   "comes next.",
            "learn": [
                "**Write the one-sentence message first:** *\u201cIf they remember one thing, it should be \u2026\u201d* Everything that does not serve it comes out.",
                "**Three points, each with one example.** Announce the number at the start so listeners know how long to concentrate.",
                "**Never read your slides.** Six words or an image per slide; the words come from your mouth.",
                "**Rehearse aloud, standing, three times.** The first is a mess, the second finds the structure, the third is close to real.",
            ],
            "fix": [
                ("Reading every word on the slide", "Slide says *\u201cRefunds: 11 days\u201d*; you explain why"),
                ("*Today I am going to talk about\u2026*", "*\u201cLast month a customer waited eleven days for a four-rupee refund.\u201d*"),
                ("*So, yeah, that is all. Any questions?*", "*\u201cSo: fix the help page before we hire. That is what I am asking for.\u201d*"),
                ("*Sorry, I am not a good speaker.*", "Say nothing about yourself; start with the content"),
            ],
            "minutes": 25,
            "drill": [
                "Take a real presentation you must give. Write the one-sentence message. Rewrite it until it is under twenty words.",
                "Write three points, each with one example, on a single page. No slides yet.",
                "Write and memorise the first thirty seconds and the last thirty seconds. These two are worth learning almost word for word.",
                "Rehearse the whole thing aloud, standing, three times, timing each run.",
                "Record the third run. Watch it once on mute for your body, once with eyes closed for your voice.",
            ],
            "say": [
                "\u201cThree things, twelve minutes, and one decision I will ask you for at the end.\u201d",
                "\u201cLet me finish with this: sixty per cent of our tickets are three questions we already know the answers to.\u201d",
            ],
            "trap": "Reading slides word for word is the most common presentation "
                    "habit in Indian corporate settings, and it is the fastest way to "
                    "lose a room anywhere. If you need the words for safety, put them "
                    "in your notes, not on the audience's screen.",
            "journal": "What is the one sentence I want my audience to remember?",
        },
        {
            "n": 79,
            "title": "Speech Versus Writing",
            "focus": "Say it simply; write it clearly. They are different jobs.",
            "why": "Indian professional writing tends to be more formal than "
                   "international writing, while Indian speech is often more direct. "
                   "Both mismatches cost you. Written English should be plainer than "
                   "you think, and it must state the ask; spoken English should be "
                   "softer than you think.",
            "learn": [
                "**Write the way you would speak, then cut a third.** If you would never say a sentence aloud, do not write it.",
                "**Put the ask in the first line, with a deadline.** *\u201cI need one decision from you: A or B, by Thursday.\u201d*",
                "**Drop the formal shell:** *respected sir, please be advised, kindly find the same, awaiting your revert.* All can be deleted.",
                "**In writing, add warmth deliberately.** Text carries no tone, so readers supply their own, and under pressure they supply a negative one.",
            ],
            "fix": [
                ("*Respected Sir, Please be advised that\u2026*", "*Hi Anil \u2014 quick update on the invoice.*"),
                ("*Kindly find the same attached for your perusal.*", "*I have attached the file.*"),
                ("*Awaiting your revert at the earliest.*", "*Could you reply by Thursday? I need it for the client call.*"),
                ("*Thanking you in anticipation.*", "*Thanks \u2014 much appreciated.*"),
            ],
            "minutes": 20,
            "drill": [
                "Take an email you sent recently. Read it aloud. Mark every sentence you would not say to the person's face.",
                "Rewrite it: ask in the first line, deadline stated, formal shell deleted, one line of warmth added.",
                "List your five most-used stock phrases and write the plain replacement for each.",
                "Practise the two-line message aloud five times: purpose, then ask with a date.",
                "Send one rewritten message today and compare the reply speed with your usual.",
            ],
            "say": [
                "\u201cHi Meera \u2014 one decision needed: supplier A or B. Both costed below. Thursday would help, because the price expires Friday.\u201d",
                "\u201cHope the launch went well. Quick one: has the invoice gone out?\u201d",
            ],
            "trap": "The formal Indian business register signals respect here and "
                    "reads as either archaic or evasive elsewhere. It is not a "
                    "mistake \u2014 it is a different convention. Keep it for "
                    "government and traditional Indian correspondence; use plain "
                    "English with international colleagues.",
            "journal": "Rewrite one email opening from today in plain English.",
        },
        {
            "n": 80,
            "title": "Talking to Seniors and Across Cultures",
            "focus": "Adjust your directness deliberately, in both directions.",
            "why": "Indian professional culture is generally more hierarchical and "
                   "more indirect with seniors; American culture is more direct and "
                   "flatter; British is indirect but informal; German and Dutch are "
                   "very direct. Reading these differences is a genuine professional "
                   "skill, and misreading them gets you labelled unfairly \u2014 as "
                   "either aggressive or as lacking ownership.",
            "learn": [
                "**With flat, direct cultures:** give your opinion without being asked, disagree openly with reasons, use first names, skip the honorifics. Silence is read as not caring.",
                "**With indirect cultures:** soften with modals, offer options rather than verdicts, read what is *not* said.",
                "**With seniors anywhere:** bring options and a recommendation rather than a problem. That works in every culture.",
                "**Ask about the norms directly.** *\u201cHow do you prefer to get updates \u2014 in writing or on a call?\u201d* Nobody minds being asked.",
            ],
            "fix": [
                ("*Sir, whatever you decide is fine.*", "*I would recommend B, mainly because of the timeline. Happy to go with A if you prefer.*"),
                ("*As per your kind instruction, I have done\u2026*", "*Done \u2014 here is what changed.*"),
                ("Waiting to be asked for your view", "*Can I offer a view on this?*"),
                ("*You are wrong.* (with a direct culture, still)", "*I see it differently \u2014 here is my concern.*"),
            ],
            "minutes": 20,
            "drill": [
                "Write down the three cultures you work with most, and one sentence about how direct each is.",
                "Practise the recommendation form five times: *\u201cI would recommend X, because Y. Happy to discuss.\u201d*",
                "Practise volunteering an opinion unasked, five times: *\u201cCan I offer a view on this?\u201d*",
                "Ask one senior colleague how they prefer to receive updates.",
                "In one meeting this week, give an unrequested recommendation with a reason.",
            ],
            "say": [
                "\u201cI would recommend option B, mainly because it protects the launch date. I am comfortable with A if you would rather.\u201d",
                "\u201cCan I offer a different view? I think the risk sits in the handover.\u201d",
            ],
            "trap": "The most common unfair label for Indian professionals in global "
                    "teams is *\u201cdoes not take ownership\u201d* \u2014 and it "
                    "usually comes from deference that reads as passivity, not from "
                    "any lack of capability. Stating a recommendation instead of "
                    "waiting to be asked fixes most of it.",
            "journal": "Where did I defer today when I should have recommended?",
        },
    ],
    "review": {
        "summary": "You have replaced the office Indianisms, tightened your status "
                   "updates, structured your client calls, learned to speak up early, "
                   "to ask questions that build credibility, to give and take "
                   "feedback, to say no, to present, to write plainly and to adjust "
                   "your directness across cultures. This is the stage that shows up "
                   "in your career.",
        "checklist": [
            "I have replaced *do the needful*, *revert*, *prepone* and *doubt*.",
            "My status update is under sixty seconds and starts with a status word.",
            "I open client calls with an agenda and close with a summary.",
            "I speak within the first ten minutes of a meeting.",
            "I show what I have already tried when I ask for help.",
            "I can receive criticism without explaining or over-apologising.",
            "I have said a clear no, or a conditional yes, this stage.",
            "I have a one-sentence message and three points for my next presentation.",
            "My emails put the ask in the first line with a deadline.",
            "I give a recommendation instead of waiting to be asked.",
        ],
        "drill": "Record a three-minute mock client update: the opening with an "
                 "agenda, a status report on a real project, one problem with two "
                 "options and a recommendation, and a closing summary with owners and "
                 "dates. Then listen for four things: Indianisms, status word "
                 "present, whether you gave a recommendation, and whether your "
                 "closing summary had names and dates in it.",
        "score": [
            "Dropping Indianisms",
            "Status updates",
            "Speaking up in meetings",
            "Feedback in both directions",
            "Boundaries and recommendations",
        ],
        "struggle": "If speaking up is still the hard part, the obstacle is usually a "
                    "specific person rather than the language. Prepare one sentence "
                    "for that specific meeting each week and say it in the first ten "
                    "minutes. Preparation beats confidence, and confidence follows "
                    "afterwards \u2014 never the other way round.",
    },
}
