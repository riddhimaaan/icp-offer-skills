---
name: beginner-icp-offer-finder
description: Turns a beginner's vague skills and generic offer into a sharp ICP, a specific offer, buying triggers, and exactly where to find those triggers. Built for freelancers, new agency owners, and career switchers who say things like "I help businesses grow with AI" or "I don't know who to target". Use this skill whenever someone shares what they can do, their bio, resume, Upwork profile, or a brain dump and wants to know who to sell to, what to offer, how to niche down, how to fix a generic offer, or who to cold email. Trigger even if they never say "ICP" or "offer", for example "I know n8n, who should I sell to?", "nobody replies to my outreach", "help me pick a niche", or "what service should I sell".
---

# Beginner ICP + Offer Finder

Beginners don't have case studies, closed deals, or a clear market. They have a skill, some life history, and an offer that sounds like everyone else's. This skill finds the specific edge hidden in their history, picks one niche that pays for their skill, builds an offer they can sell with zero results, and then gives triggers that show who needs it right now.

The final output has exactly four sections: **ICP, Offer, Triggers, Where to find them.** Nothing else.

## Hard rules

1. **Never ask questions.** Work with whatever the user gave. Fill gaps with research and sensible picks. Beginners stall when they get a questionnaire back.
2. **Never invent proof.** No made-up results, client names, or stats. If they have no results, the offer leans on experience and a low-risk first deal.
3. **Plain words.** No "ICP", "value prop", "leverage", "synergy" in the output itself beyond the section title. Write so a 12-year-old could explain the offer back.
4. **One niche, one offer.** Beginners need a single clear bet, not a menu.
5. **Everything must be findable.** If a trigger can't be found with a named source and a named search or filter, cut it.
6. **No em dashes** in the output. Short sentences.

## Workflow

Do stages 1 to 6 silently. Only the final four sections are shown to the user.

### Stage 1: Read the input
Read `references/input-handling.md`. The only thing that matters is what they can do. Everything else is a bonus. If they shared links (LinkedIn, Upwork, website, portfolio), fetch them first and pull out past jobs, industries, results, and how they describe themselves.

### Stage 2: Mine their edge
Read `references/advantage-mining.md`. Find what makes this person more believable to one group of buyers than a random freelancer: past jobs, industries they know from inside, language, location, deep tool knowledge, small wins. Label each as proof, experience, or skill. This is the most important stage. Beginners think they have nothing. Their history almost always holds one usable edge.

### Stage 3: Pick the niche
Read `references/niche-selection.md`. Build 3 niche candidates from the edge. Use web search to check that people already pay for this problem in each niche. Score them and pick one. Don't show the losers.

### Stage 4: Build the offer
Read `references/offer-rules.md`. One outcome, one buyer, one deliverable, a price, a low-risk way to start, and a "why trust me" line from Stage 2.

### Stage 5: Find triggers and sources
Read `references/trigger-rules.md`. Find 3 to 5 moments when the ICP feels the problem the offer solves. For each one, give the exact source and the exact search, filter, or tool to find those companies.

### Stage 6: Run the gate
Read `references/anti-generic-gate.md`. Test every section. Rewrite anything that fails. If you have Python available, run `scripts/gate_check.py` on the draft for the mechanical checks (banned phrases, em dashes, section headers, trigger count).

### Stage 7: Output
Use the exact format below. See `references/examples.md` for two full worked examples at the right level of detail.

## Output format

```
# ICP

**Who:** [one sentence: the specific type of business and the person who buys]

**Filters to build the list:**
- Industry: ...
- Size: ...
- Location: ...
- Buyer title: ...
- Must have: [an observable condition, like "runs Meta ads" or "uses Shopify"]

**Skip if:** [2 to 3 disqualifiers]

# Offer

**The offer:** [one sentence a buyer understands in 5 seconds]

**What they get:** [the concrete deliverable, 2 to 4 short lines]

**Price:** [a number or range, plus the first-deal structure]

**Why trust you:** [one line built only from their true history]

# Triggers

1. **[Trigger name]:** [what happened and why it means they need this now]
2. ...
(3 to 5 total)

# Where to find them

1. **[Trigger name]:** [source] → [exact search, filter, or query] → [tool to pull the list]
2. ...
(same order and count as Triggers)
```

No intro line, no summary, no next steps, no extra sections.
