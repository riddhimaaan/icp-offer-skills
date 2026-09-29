# Trigger Rules

A trigger is something you can see from outside that shows a business feels the exact problem the offer solves, right now. Once the ICP and offer are specific, triggers come from one question:

**"What would I see from outside when this business has this problem?"**

## How to derive triggers

For the chosen offer, walk through:

1. **The pain shows up:** what visible sign does the problem leave? (bad reviews mentioning it, slow site, no reply to inquiries, broken booking link)
2. **They try to fix it themselves:** job post for the role, Upwork post, asking in a Facebook group or subreddit
3. **Something makes the pain bigger:** new location, started running ads, new product launch, hiring more staff, seasonal rush coming
4. **They're missing what peers have:** competitors have it, they don't (no online booking, no reviews reply, no email flows)

Pick 3 to 5. Mix types. At least one should be "pain shows up" because it's the strongest.

## Three tiers

- **Universal** (raised funding, hiring, new leader): allowed only when tied to the offer with a specific condition. "Hiring" alone fails. "Posted a job for a receptionist in the last 30 days" passes for a call handling offer.
- **Niche:** specific to the industry. "Dental clinic running Invisalign ads on Meta."
- **Visible pain:** public data that shows the exact problem. "Google reviews mentioning 'couldn't get through' or 'no one answered'."

Prefer visible pain and niche triggers.

## Named example of the standard

Eric Nowoslawski's agency Growth Engine X ran a campaign for a Google reputation management client. They targeted businesses rated between 3.5 and 4.5 stars, pulled the specific negative reviews, and offered to remove them with payment only after removal. It got a positive reply on about 1 in 70 emails (source: The GTM Engineer podcast). The ICP, trigger, and offer were one idea. That's the bar.

## Trigger quality check

Each trigger must pass all four:

1. **Tied to the offer:** removing the offer makes the trigger pointless.
2. **Visible:** can be seen from outside without insider access.
3. **Fresh:** has a time window (last 30 days, currently running, upcoming season), or is an ongoing visible problem.
4. **Findable:** a named source plus a named search, filter, or tool pulls the list.

## Source map

Use exact searches in "Where to find them". Swap brackets for the ICP.

| What to find | Source | Exact search or filter | Tool to pull the list |
|---|---|---|---|
| Businesses with review complaints | Google Maps | Search "[business type] in [city]", filter rating 3.5 to 4.5, read reviews for keywords like "no answer", "slow", "rude", "waited" | Apify Google Maps Scraper (compass/crawler-google-places) with review export |
| Businesses running ads | Meta Ad Library (facebook.com/ads/library) | Country + keyword "[service or product]", active ads only | Apify Facebook Ads Library scraper |
| Job posts for the task | LinkedIn Jobs, Indeed | "[role] [industry]" posted past week or month, location filter | Apify LinkedIn Jobs or Indeed scraper, Apollo job postings filter |
| Upwork posts for the task | Upwork | "[task] [industry]" in the job feed | Manual or Apify Upwork scraper |
| Tech they use or lack | BuiltWith, Wappalyzer, Store Leads (for Shopify) | Tech filter such as "Shopify" without "Klaviyo", or "WordPress" without a booking plugin | BuiltWith lists, Store Leads export |
| Slow or broken websites | Google PageSpeed Insights | Run site URLs from the list, flag mobile score under 50 | Batch via Apify or a simple script |
| New locations or launches | Google News, LinkedIn company posts | "[business type] opens new location [city]", "now open" | Google Alerts, Apify Google Search scraper |
| Recently funded companies | Crunchbase | Industry + funding date last 90 days + employee count | Crunchbase export, Apify Crunchbase scraper |
| Asking for help publicly | Reddit, Facebook groups | Subreddit search "[problem] recommendation", group search | Apify Reddit scraper, manual for groups |
| Leadership or role change | LinkedIn Sales Navigator | Title + "changed jobs in past 90 days" + industry + headcount | Sales Navigator, then Prospeo or Apollo for emails |
| Hiring a lot (growth pain) | LinkedIn company page, Sales Navigator | "Headcount growth" filter, 10%+ in 6 months | Sales Navigator |
| Seasonal rush coming | Industry calendar | Tax season for accountants, summer for HVAC, wedding season for venues | Time the list pull 4 to 8 weeks before |
| Contact emails for any list | Company site, LinkedIn | Owner or buyer title from ICP filters | Prospeo, Apollo, Icypeas, Hunter |

## Writing "Where to find them"

One line per trigger, same order as Triggers:

`[Trigger name]: [source] → [exact search or filter] → [tool to pull the list]`

Bad: "Check LinkedIn for companies that are hiring."
Good: "Hiring a front desk role: LinkedIn Jobs → 'receptionist physiotherapy', UK, past 30 days → Apify LinkedIn Jobs scraper, then Prospeo for the clinic owner's email."
