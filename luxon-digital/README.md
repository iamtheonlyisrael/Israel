# Luxon Digital website: revision guide

Brand: navy `#0B1F3A`, gold `#D4AF37`, white `#FFFFFF`, charcoal `#1F2933`.
Fonts: Montserrat (headings), Inter (body).
Dark gold for small text on white: `#7A6210`. Brand gold on white is too light to read.

## Updates from the Oct 1 client call

- **CTAs, site-wide:** only two labels: **Book Your AI Demo** (gold gradient button) and **Watch the Demo Here** (gold-outline button). Every code block now uses these. Change any native GHL buttons to match, including the CTA on the Automated Lead Follow-Up page.
- **Gold gradient button:** `linear-gradient(135deg, #B8922A 0%, #D4AF37 40%, #F5DC85 70%, #D4AF37 100%)`, navy text `#0B1F3A`. The shine slides across on hover.
- **No unrealistic numbers or promises:** the home hero badge now says "Missed call, answered automatically" (it was "Replied in under a minute"). Remove "6 missed callbacks" and similar stats from any native sections.
- **Home testimonials:** replace the empty testimonials section with `home/07-founder-story.html` (founder photo + story + 3 "behind the technology" cards). It needs the founder's name, photo and story.
- **Top bar:** "Founding Partner Spots Open" was replaced with "Done-For-You AI for Limo & Chauffeur Companies" (not a confirmed offer).

### Google Ads safety checklist (the client had a rejection before)
- [ ] Every code block was tested in a browser: no JavaScript errors, no failed requests, no sideways scrolling on phones.
- [ ] No placeholder images load until a real URL is pasted. The logo and founder photo `<img>` lines are commented out.
- [ ] Before publishing, replace or delete **every** `PASTE-...-URL` link (social icons). A placeholder link leads to a broken page.
- [ ] Fill in or remove `[Business email]`, `[Business phone]`, `[hours]`, `[Founder name]`, `[Founder story]`.
- [ ] Privacy Policy and Terms pages must be live and linked in the footer before running ads.
- [ ] Each button links to a page that exists (`/contact`, `/demo`, and so on).

## All other pages (one block per page)

Each page is **one Custom Code block** in `pages/`. Paste the whole file into a single Custom Code element, between the header and the "Let's talk" band. Contact and the two legal pages skip the band.

| Page | Paste file | Live graphic / effects |
|---|---|---|
| About Us | `pages/about.html` | Who-we-serve glass card; Five Principles (— WHAT WE VALUE eyebrow, gold, 14px/700/1px, 80px padding); Generic vs Luxon comparison; equation row |
| Luxon Limo AI | `pages/luxon-limo-ai.html` | Inquiries → glowing Luxon hub → results, with light sweeping each row; 4 feature panels with mini live demos |
| AI Receptionist | `pages/ai-receptionist.html` | Live call card: voice waveform, transcript bubbles appear one by one, trip details captured |
| Automated Lead Follow-Up | `pages/lead-follow-up.html` | Follow-up timeline lights up step by step (missed call → text → quote → booked). Fixes the CTA the client flagged |
| Review Automation | `pages/review-automation.html` | Review request with stars filling in; happy rider vs concern routing |
| Lead Management | `pages/lead-management.html` | Lead board with a trip card moving New → Quoted → Booked → Completed |
| Demo | `pages/demo.html` | Video area (paste the video embed), demo phone line card, **calendar embed spot** |
| Pricing | `pages/pricing.html` | 3 plans: Essentials $297/mo, Growth $397/mo (+ $1,500 setup), Custom |
| FAQ | `pages/faq.html` | Jump links + open/close questions (works without any script) |
| Contact / Book a Demo | `pages/contact.html` | **Calendar embed spot**, what to expect, contact details |
| Privacy Policy | `pages/privacy-policy.html` | Sticky table of contents. **Placeholder text: final legal copy needed** |
| Terms & Conditions | `pages/terms-and-conditions.html` | Same layout. **Placeholder text: final legal copy needed** |

**Where to paste embeds** (search the file for these comments):
- `<!-- CALENDAR: ...` in `demo.html` and `contact.html` → replace the dashed box with the GHL "Book Your AI Demo" calendar embed.
- `<!-- DEMO VIDEO: ...` in `demo.html` → replace with the video embed.
- `<!-- PRICES: ...` at the top of `pricing.html` → change the amounts if needed.

**SOP rules followed on every page:** brand voice from the brand kit (simple business language, no jargon). None of the "words we avoid" appear on any page: no "bot", "CRM", "guaranteed", "workflow", "integration" and so on. Only two CTA labels: "Book Your AI Demo" and "Watch the Demo Here". No invented stats; example graphics are labeled "Sample data" or "Example". AI safety messaging throughout: never invents prices, hands off to a person, approved and tested before launch.

**Editing:** change the page source in `pages/src/`, the shared style in `kit/kit.css`, then run `python3 build-pages.py`. This rebuilds `pages/` and `mockups/`.

## Shared blocks (every page)

| File | What it is |
|---|---|
| `shared/header.html` | Billboard-style top bar (flipping slats, chasing marquee lights, light sweep; links to /contact; edit its 3 messages in the `MESSAGES` list at the bottom) + white header: logo, menu with a **Luxon Limo AI** dropdown (the 4 feature pages), gold **Book Your AI Demo** button. Turns into a ☰ menu on phones |
| `shared/cta-band.html` | "Let's talk about your business." navy box with two real buttons |
| `shared/footer.html` | Navy footer: logo, tagline, social icons, product links, company links, contact, legal links |

**Before pasting, replace:**
- `PASTE-LOGO-URL` (header): the regular logo, from the GHL media library
- `PASTE-LIGHT-LOGO-URL` (footer): a **white/light** version of the logo, because the navy logo won't show on navy. Until then, a text logo appears
- `PASTE-FACEBOOK-URL`, `PASTE-INSTAGRAM-URL`, `PASTE-LINKEDIN-URL`, `PASTE-YOUTUBE-URL`: delete any icon the client doesn't use
- `[Business email]`, `[Business phone]`, `[hours]`
- Page links (`/about`, `/ai-receptionist`, ...): change them if your GHL page paths are different

In GHL, either paste the header and footer into each page's first and last section, or save them once as a **Global Section** so you only edit them in one place.

## Full-page mockups

`mockups/home.html` and `mockups/about.html` are full pages (header, all sections, footer) in one file. Open it in any browser.
Run `./build-mockups.sh` to rebuild it after editing a block.

## About page (older section blocks)

> Superseded by `pages/about.html` (one block, colorful style). The blocks below are kept because some may already be pasted in GHL.

| # | Section | Build | Notes |
|---|---|---|---|
| 1–2 | Top bar + header | **Custom code** | `shared/header.html` |
| 3 | Hero | **Custom code** | `about/01-hero.html` replaces the plain white "AI Automation That Keeps Business Moving." block |
| 4 | Mission + Vision + Five principles | **Custom code** | `about/02-mission-values.html` replaces both sections. It fixes the duplicate "Simplicity" (5th is now **Partnership**), removes the empty 6th cell, and replaces the black borders and gray side strips with brand cards |
| 5 | Why transportation-specific | **Custom code** | `about/03-why-transportation.html` keeps your copy and adds a Generic vs Luxon comparison and the "why operators choose Luxon" row |
| 6 | CTA band | **Custom code** | `shared/cta-band.html` |
| 7 | Footer | **Custom code** | `shared/footer.html` |

### Off-brand colors to fix on every page
- **Black `#000` headings** → navy `#0B1F3A`
- **Black 1px borders** around cards and grids → light gray `#E4E7EB` with 16–20px rounded corners, or no border
- **Blue-gray side strips** (`#C9D4E0`-style) → remove
- **Light gray body text** → `#3E4C59` (easier to read)
- **Gold eyebrow labels on white** (`#D4AF37`) → `#7A6210`. Keep `#D4AF37` for labels on navy only
- **Dark divider line** above the footer → remove, or use `#E4E7EB`
- **Fonts:** Poppins / Roboto → Montserrat (headings) and Inter (body)

## Home page

Every section is now a Custom Code block, so the whole page shares one colorful style. Paste them in this order:

| # | Section | File | Background / effect |
|---|---|---|---|
| 1 | Top bar + header | `shared/header.html` | Billboard top bar, gold gradient button |
| 2 | Hero | `home/01-hero.html` | Navy→blue gradient with drifting glows. Live dispatch board ("Tonight's inquiries"): new trips slide in as RINGING, flip to ANSWERED, then QUOTED and BOOKED; clock follows the newest inquiry; a car drives the lane below. Labeled "Sample data" |
| 3 | Missed call vs. Luxon | `home/02-missed-call.html` | Light blue→white→soft gold gradient |
| 4 | How it works | `home/03-how-it-works.html` | Dark gradient, dot grid, light running along the 4 steps, steps pulse in turn |
| 5 | What's included | `home/04-features.html` | Light gradient, gradient-border cards, pulsing icon rings |
| 6 | Who it's for | `home/05-who-its-for.html` | Blue/gold gradient, glass cards with moving gradient top bar |
| 7 | Guardrails | `home/06-guardrails.html` | Light gradient, shield with radar pulse |
| 8 | Founder story (replaces testimonials) | `home/07-founder-story.html` | Warm gold→white gradient |
| 9 | Let's talk band | `shared/cta-band.html` | Blue/gold gradient box with light sheen |
| 10 | Footer | `shared/footer.html` | |

All sections fade in on scroll. Visitors who have "reduce motion" turned on in their device settings see everything still.

**Colors used:** navy `#0B1F3A`, deep navy `#071528`, brand blue `#1E4FA8` / `#2F6FE4` / `#8DB4FF`, gold `#D4AF37` / `#F5DC85` / `#B8922A`.

## Pasting a custom code block

1. In the GHL builder, add a full-width section with 0 padding.
2. Add a **Custom Code** (Custom JS/HTML) element and paste the whole file.
3. The buttons link to `/contact` and `/demo`. Change these if your page paths are different.
