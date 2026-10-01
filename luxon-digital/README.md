# Luxon Digital website: revision guide

Brand: navy `#0B1F3A`, gold `#D4AF37`, white `#FFFFFF`, charcoal `#1F2933`.
Fonts: Montserrat (headings), Inter (body).
Dark gold for small text on white: `#7A6210`. Brand gold on white is too light to read.

## Shared blocks (every page)

| File | What it is |
|---|---|
| `shared/header.html` | Navy top bar + white header: logo, menu with a **Luxon Limo AI** dropdown (the 4 feature pages), gold **Book Your AI Demo** button. Turns into a ☰ menu on phones |
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

`mockups/about.html` is the full About page (header, all sections, footer) in one file. Open it in any browser.
Run `./build-mockups.sh` to rebuild it after editing a block.

## About page

| # | Section | Build | Notes |
|---|---|---|---|
| 1–2 | Top bar + header | **Custom code** | `shared/header.html` |
| 3 | Hero | **Custom code** | `about/01-hero.html` replaces the plain white hero. Includes an animated tri-vision billboard (flipping slats, marquee lights, spotlights, headlight streaks). Edit the 3 billboard messages in the `MESSAGES` list at the bottom of the file |
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

Most sections are built with native GHL elements so the client can edit them.
Only two sections use a Custom Code element.

| # | Section | Build | Notes |
|---|---|---|---|
| 1 | Top bar | Native | Navy background, white 12px Montserrat text, letter-spacing 2px: "AI AUTOMATION THAT KEEPS BUSINESS MOVING" |
| 2 | Header | Native | Add a gold button on the right: **Book Your AI Demo** (navy text, 8px radius) |
| 3 | Hero | **Custom code** | `home/01-hero.html` |
| 4 | Missed call vs. Luxon | **Custom code** | `home/02-missed-call.html` |
| 5 | How it works | Native | Light gray `#F6F7F9` section, 4 columns: 01 Answers · 02 Captures the trip · 03 Follows up · 04 Helps convert. Big gold numbers, white cards; make the 4th card navy |
| 6 | Features | Native | White section, 2×2 cards linking to AI Receptionist, Lead Follow-Up, Review Automation, Lead Management. Navy square icon tile with gold icon. Light gray border `#E4E7EB`, 20px radius, no black borders |
| 7 | Who it's for | Native | Navy section, 3 cards (`#0F2647`, thin gold border): Owner-Operator · Growing Fleet Owner · Operations Manager |
| 8 | Why transportation-specific | Native | Keep the existing copy. Put it in 2 columns with a photo on the right (black car / chauffeur) |
| 9 | Guardrails | Native | "It never guesses. It hands off." plus 4 small cards: Never invents prices · A person when it matters · You approve it first · Tested before go-live |
| 10 | CTA band | Native | Keep it. Make "Book Your AI Demo" a real gold button and add a second outline button "See Luxon Limo AI in Action" |
| 11 | Footer | Native | Add columns: Luxon Limo AI pages · Company pages · contact + social icons. Navy background |

Move **Our Mission / Our Vision** and the **values** grid to the About page.
On the values grid, the 5th card repeats "Simplicity". It should be **Partnership**:
"Work alongside clients and support their long-term growth." Use 5 equal columns, or 3 + 2 centered, so there's no empty cell.

## Pasting a custom code block

1. In the GHL builder, add a full-width section with 0 padding.
2. Add a **Custom Code** (Custom JS/HTML) element and paste the whole file.
3. The buttons link to `/contact` and `/demo`. Change these if your page paths are different.
