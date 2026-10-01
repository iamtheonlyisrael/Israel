# Luxon Digital website: revision guide

Brand: navy `#0B1F3A`, gold `#D4AF37`, white `#FFFFFF`, charcoal `#1F2933`.
Fonts: Montserrat (headings), Inter (body).
Dark gold for small text on white: `#7A6210`. Brand gold on white is too light to read.

## About page

| # | Section | Build | Notes |
|---|---|---|---|
| 1 | Top bar | Native | Navy `#0B1F3A` background, white 12px Montserrat, letter-spacing 2px (currently black on white) |
| 2 | Header | Native | Same as every page: add a gold **Book Your AI Demo** button, nav text `#1F2933` |
| 3 | Hero | **Custom code** | `about/01-hero.html` replaces the plain white "AI Automation That Keeps Business Moving." block |
| 4 | Mission + Vision + Five principles | **Custom code** | `about/02-mission-values.html` replaces both sections. It fixes the duplicate "Simplicity" (5th is now **Partnership**), removes the empty 6th cell, and replaces the black borders and gray side strips with brand cards |
| 5 | Why transportation-specific | **Custom code** | `about/03-why-transportation.html` keeps your copy and adds a Generic vs Luxon comparison and the "why operators choose Luxon" row |
| 6 | CTA band | Native | Keep the navy box. Turn "BOOK YOUR AI DEMO" into a real gold button (gold `#D4AF37` background, navy text, 8px radius, about 54px tall) and add an outline button "See Luxon Limo AI in Action" |
| 7 | Footer | Native | Navy background, white logo version, page links, contact and social icons |

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
