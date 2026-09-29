---
name: product-market-fit
description: Run PMF analysis for a product and audience. Use for product-market fit, ICP, offer validation, buyer fit, PMF score, or sales offer work.
---

# Product-Market Fit Skill

Run a product-market fit analysis from a product, target audience, and proof status.

Core flow:
1. Collect only the missing intake details.
2. Build the ICP internally.
3. Score PMF across four dimensions.
4. Show the PMF score and ask whether the user wants an offer document, PMF report, or both.

Do not write files unless the user asks for files.

## Critical Output Rule

The ICP and dimension scoring are internal work.

Never print:
- "Now I have everything I need."
- "Let me run the full analysis."
- "Phase 1"
- "Phase 2"
- ICP notes.
- Dimension-by-dimension scoring.
- Score math.
- Internal reasoning.

The first response after intake must be only the short score response in the First Response Format section.

If the user asks how you got the score, then show the PMF report. Do not show internal phase notes.

## Intake

Check what the user already provided.

Required:
- Product or service: what it does and who it is for.
- Target audience: job title, industry, and company size or stage.
- Proof status: existing customers, results, testimonials, pilots, or no proof yet.

If any detail is missing, ask only for the missing details. Ask no more than three questions at once.

Use these questions when needed:
1. "What is your product or service? One sentence: what it does and who it is for."
2. "Who is your target audience? Job title, industry, and company size or stage."
3. "Do you have customers, pilots, testimonials, or results yet? If not, say no proof yet."

Do not proceed without the product and audience. If the user has no proof yet, proceed and mark proof gaps clearly.

## Phase 1: ICP

Read [references/01-icp-engine.md](references/01-icp-engine.md).

Use the intake answers to create the ICP internally. Do not show the ICP after this phase unless the user asks for the ICP.

Ground every claim in the intake. When you estimate, label it as an estimate. Do not invent exact facts, quotes, prices, past attempts, or numbers as confirmed truth.

## Phase 2: PMF Score

Read [references/03-pmf-synthesis.md](references/03-pmf-synthesis.md).

Score the product against the ICP across all four dimensions:
- Problem-Solution Fit
- Desire-Outcome Fit
- Identity-Positioning Fit
- Fear-Objection Fit

Use this scoring:
- Strong Fit = 2.5 points
- Partial Fit = 1.25 points
- Gap = 0 points

Add the four dimension scores. Round to the nearest 0.5 when useful.

Labels:
- 8.5-10: Ready
- 6-8: Mostly Ready
- 3-5.5: Needs Work
- 0-2.5: Misaligned

## First Response Format

After Phase 2, send only this:

> **PMF Score: [X]/10 - [Ready / Mostly Ready / Needs Work / Misaligned]**
>
> [One sentence naming the strongest dimension.]
> [One sentence naming the most important gap.]
>
> Want to go deeper?
>
> - **Offer document** - Rebuilds the offer based on the PMF gaps. Includes a short version, promise, and three simple ways to buy.
> - **PMF report** - Shows the plain-English diagnosis and the top fixes.
>
> Which one do you want?

Do not add anything before or after this format.

## Follow-Up Requests

If the user asks for the offer document:
- Read [references/02-offer-execution-engine.md](references/02-offer-execution-engine.md).
- Build the offer from the intake, ICP, and PMF score.
- Print the offer document in the simplified offer format from that reference.
- Do not write a file unless the user asks.

If the user asks for the PMF report:
- Print the full report using the simplified PMF report format in [references/03-pmf-synthesis.md](references/03-pmf-synthesis.md).
- Do not write a file unless the user asks.

If the user asks for both:
- Print the offer document first.
- Print the PMF report second.
- Do not write a file unless the user asks.

If the user asks for the ICP:
- Print the ICP from Phase 1.

## Output Style

Write for a busy founder who wants the shortcut.

Assume the reader will skim. Make the answer obvious even if they know nothing about marketing, PMF, ICPs, positioning, or offers.

Use:
- Simple words.
- Short sentences.
- Clear labels.
- Direct answers.
- Concrete examples.
- "Do this next" advice.

Do not make the reader decode the answer.

Every important section should answer:
- What does this mean?
- Why does it matter?
- What should they do next?

Use specific facts from the user's inputs.

Avoid these words unless the user used them first or they are needed in a quoted title:
- leverage
- synergy
- solutions
- optimize
- align
- empower
- streamline
- facilitate
- holistic
- comprehensive
- end-to-end
- elevate
- transform
- unlock
- impact without a number
- visibility without saying who sees what
- growth without a number
- brand awareness
- brand presence
- brand building

Rules:
- No generic filler.
- No inferred facts presented as confirmed.
- Label estimates as "(estimate)".
- Use headers for long outputs.
- Use tables for comparisons and objections.
- Keep paragraphs under three lines.
- Put the plain-English answer before the detailed reasoning.
- Use "Good / Bad / Fix" wording when it makes the answer faster to understand.
- Explain any business term the first time you use it, or avoid the term.
- End long reports with a short "Do this first" section.
