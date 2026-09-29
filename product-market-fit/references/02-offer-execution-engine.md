# Offer Execution Engine

Use this reference when the user asks for an offer document.

Write the offer so a buyer and a founder can understand it fast.

Rules:
- Say what is being sold.
- Say who should buy it.
- Say what problem it fixes.
- Say what changes after they buy.
- Show three simple offer options.
- Avoid clever names if a plain name is clearer.

Inputs:
- Intake answers.
- ICP document.
- PMF score and dimension ratings.
- PMF gaps and fixes from the PMF report.

Purpose:
- Do not repeat the original offer.
- Improve the offer based on the PMF gaps.
- Treat the PMF report as the diagnosis.
- Treat this offer document as the fixed prescription.

Do not run a separate discovery process unless a required offer detail is impossible to infer safely. Mark missing proof as `[NEEDS: proof point]`.

## Stage 0: PMF Gap Repair

Before writing the offer, identify the biggest PMF gap and use it to change the offer.

Use these rules:

- If Problem-Solution Fit is weak, change the offer around the buyer's sharpest problem.
- If Desire-Outcome Fit is weak, make the result more concrete, measurable, and tied to what the buyer already wants.
- If Identity-Positioning Fit is weak, make the buyer sound like the person they want to become.
- If Fear-Objection Fit is weak, add proof, a smaller starter offer, a guarantee, or mark `[NEEDS: proof point]`.

Every part of the offer must reflect at least one PMF fix.

Do not copy the product description into the offer. Rewrite it into a stronger buyer-facing offer.

## Stage 1: Cost of Inaction

Use the top ICP problem and the main desired outcome.

Name one financial cost and one non-financial cost.

Rules:
- Use numbers from the user when available.
- Label estimates as "(estimate)".
- Name the actual cost, not a broad category.

Output one sentence:

> Every month [specific prospect] delays solving [specific problem], they lose approximately [X] in [specific financial cost] and risk [specific non-financial cost].

## Stage 2: Buying Barrier

Find the most likely reason the buyer has not solved this yet.

Check:
- Risk: burned before, distrusts vendors, fears a failed rollout.
- Price: cannot see ROI, budget is tight.
- Effort: no bandwidth to implement.
- Time: no urgency right now.
- AI-era barrier: "We can just use AI for this," "This will be outdated soon," or "Everyone is doing this now."

Output one sentence:

> The primary barrier is [X]. The offer must lead with [Z].

## Stage 3: Multi-Option Stack

Build three simple options. Each option must be easy to understand in five seconds.

Do not add long explanations.
Each option must fix a different PMF weakness or buyer risk.

**Option 1: Starter**

- Smallest complete result.
- For a skeptical buyer who wants proof before a bigger buy.
- Use this to reduce fear when proof is weak.

**Option 2: Core**

- Main offer.
- Full result.
- Best default option for most buyers.
- Use this to deliver the main buyer outcome.

**Option 3: Premium**

- Fastest path.
- Least work for the buyer.
- Must be different from Core, not just more of the same.
- Use this to remove the buyer's biggest effort, risk, or delay.

## Stage 4: Outcome Sentence

Use this format:

> We help [specific prospect] achieve [specific outcome] in [timeframe] without [effort they hate most], guaranteed by [specific proof].

Rules:
- Prospect must be exact.
- Outcome must include a number, deliverable, or before/after state.
- Timeframe must be a real number.
- If no proof exists, write `[NEEDS: proof point]`.

## Simplified Offer Document Format

```markdown
# Offer: [Product Name]

## What Changed

[One sentence. Name the main PMF gap and how this offer fixes it.]

## Short Version

**Who should buy this:** [Exact buyer, sharpened from the ICP.]
**What they get:** [Specific result, improved from the PMF gaps.]
**How fast:** [Specific timeframe.]
**Price:** $[X]
**Best for:** [One sentence tied to the buyer's real pain.]

## The Promise

We help [buyer] get [result] in [timeframe] without [painful work].

## 3 Ways to Buy

### Option 1: Starter
- **For:** [Skeptical buyer or buyer with proof concerns]
- **Gets:** [Small complete win that lowers the biggest risk]
- **Time:** [X days]
- **Price:** $[X]

### Option 2: Core
- **For:** [Main buyer]
- **Gets:** [Full outcome that fixes the biggest PMF gap]
- **Time:** [X days or weeks]
- **Price:** $[X]

### Option 3: Premium
- **For:** [Buyer who wants speed and less work]
- **Gets:** [Full outcome with the biggest effort, risk, or delay removed]
- **Time:** [X days or weeks]
- **Price:** $[X]
```

## Anti-Patterns

- Do not describe a service and call it an offer.
- Do not write "proven process" without proof.
- Do not use generic prospect labels like "growing companies."
- Do not use abstract outcomes like "better positioning."
- Do not repeat the original offer without improving it from the PMF gaps.
- Do not add sections beyond What Changed, Short Version, The Promise, and 3 Ways to Buy unless the user asks.
