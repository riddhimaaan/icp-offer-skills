# Worked Examples

These show the level of detail expected. The inputs are sample beginners. Prices here are placeholders; in a live run, prices come from the market check in niche-selection.

---

## Example 1: Generic AI automation beginner with a hidden edge

**Input:**
"I help businesses with AI automation. I know n8n and Make. Before this I worked 2 years at the front desk of a physio clinic in Manchester. No clients yet."

**Edge found:** 2 years inside a physio clinic front desk (experience). Knows missed calls and no shows firsthand.

**Output:**

# ICP

**Who:** Independent physiotherapy clinics in the UK with 2 to 10 practitioners, where the clinic owner handles bookings and admin.

**Filters to build the list:**
- Industry: Physiotherapy clinics
- Size: 2 to 10 practitioners
- Location: United Kingdom
- Buyer title: Clinic owner, clinic director, practice manager
- Must have: Phone number as the main booking method on Google Maps

**Skip if:** Part of a chain or franchise. Already uses an online booking tool with automated reminders. NHS only clinics.

# Offer

**The offer:** I set up an automatic text back for missed calls, so every caller you miss gets your booking link within 60 seconds. You pay once it's live and catching calls.

**What they get:**
- Missed call text back with the clinic's booking link
- Reminder text 24 hours before each appointment
- Weekly count of calls caught

**Price:** Setup fee plus a small monthly fee for running it. First clinic pays nothing until it's live.

**Why trust you:** I worked 2 years on a physio clinic front desk, so I've seen how many bookings get lost to voicemail.

# Triggers

1. **Reviews about not getting through:** Google reviews mention "couldn't get through", "no one picked up", or "never called back". The clinic is losing patients to missed calls right now.
2. **Hiring a receptionist:** They posted a receptionist or admin job. Calls are piling up and they're trying to fix it with a hire.
3. **Running ads to a phone number:** Active Meta ads that push people to call. Every missed call is paid traffic wasted.
4. **New practitioner joined:** More appointment slots to fill, same front desk.

# Where to find them

1. **Reviews about not getting through:** Google Maps → "physiotherapy clinic" in each UK city, rating 3.5 to 4.5, reviews containing "no answer", "couldn't get through" → Apify Google Maps Scraper with review export, then filter by keyword.
2. **Hiring a receptionist:** Indeed and LinkedIn Jobs → "physiotherapy receptionist", UK, past 30 days → Apify Indeed scraper, then Prospeo for the owner's email.
3. **Running ads to a phone number:** Meta Ad Library → country UK, keyword "physio", active ads → Apify Facebook Ads Library scraper, keep ads with "call us" in the text.
4. **New practitioner joined:** LinkedIn → search "physiotherapist" + "started a new position" + UK, company size 2 to 10 → Sales Navigator, then Apollo for the owner.

---

## Example 2: One line input, no edge, no results

**Input:**
"I edit short videos. From India. Want to earn in dollars."

**Edge found:** Skill only. Location gives a price advantage and time zone overlap with Australia. No proof. The offer carries trust through a small paid first project.

**Output:**

# ICP

**Who:** Independent Shopify skincare brands in Australia doing organic Instagram content, where the founder still makes the videos.

**Filters to build the list:**
- Industry: Skincare and beauty ecommerce
- Size: 1 to 15 employees
- Location: Australia
- Buyer title: Founder, owner, head of marketing
- Must have: Shopify store and an Instagram account posting Reels at least weekly

**Skip if:** Has an in-house content team. Posts under once a week (not invested in video). Sells only on Amazon.

# Offer

**The offer:** I turn the raw product clips you already film into 8 ready to post Reels a month, delivered while you sleep. First batch of 2 Reels is a small fixed price.

**What they get:**
- 8 edited Reels a month with captions and hooks
- Cuts from footage they already have
- Delivered overnight Australian time

**Price:** Monthly fee in USD. First 2 Reels at a small fixed price so they can judge the quality.

**Why trust you:** Skip the claim. The paid 2 Reel trial carries the trust.

# Triggers

1. **Founder posting raw, unedited Reels:** They already believe in video but have no editor.
2. **Launched a new product:** Needs content fast for the launch.
3. **Running Meta ads with static images only:** Video ads are missing from their mix.
4. **Posted a job for a content creator or video editor:** They know they need help and are looking now.

# Where to find them

1. **Founder posting raw Reels:** Store Leads → Shopify, Australia, category "Beauty" → export store list, then check Instagram links for Reels with no captions or cuts → manual review of the top 200.
2. **Launched a new product:** Instagram and Shopify stores from the list → posts with "new launch", "just dropped" in the past 30 days → Apify Instagram scraper on the exported handles.
3. **Static only Meta ads:** Meta Ad Library → country Australia, keyword "skincare", active ads, filter media type image → Apify Facebook Ads Library scraper.
4. **Hiring a video editor:** LinkedIn Jobs, Upwork → "video editor skincare", "UGC editor", Australia or remote → Apify LinkedIn Jobs scraper, then Prospeo for the founder's email.
