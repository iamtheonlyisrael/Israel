# DW Credit Restoration website (DW Tax Solution)

Static pages. No build step, no dependencies.

| File | What it is |
|---|---|
| `index.html` | Sales page: animated score gauge, before/after toggle, pricing (3 months $75 / 6 months $150), monitoring checkbox, 6-month upsell pop-up, FAQ. Logo is embedded. |
| `thank-you.html` | After-purchase page: activate monitoring and complete intake. |
| `logo.webp` | DW Tax Solution logo (used by `thank-you.html` and as the icon). |
| `ghl-paste-home.html` | The sales page as a single block for a GHL **Custom Code** element. |

## Before going live

1. **Checkout links:** in `index.html` (and `ghl-paste-home.html`), find `DW_LINKS` in the script and replace both `"#"` with the GHL order-form URLs.
   The GHL products already exist in the Major Wealth Group sub-account:
   "DW Credit Restoration - 3 Month Plan (Jump Start)" ($75) and "- 6 Month Plan (Full Transformation)" ($150).
   Buyer tags: `dw-credit-3mo-$75` and `dw-credit-6mo-$150`.
2. **Next-step links:** in `thank-you.html`, fill in `DW_NEXT.monitoring` and `DW_NEXT.intake`.
   Until then, the page says the links will be sent by text and email.
3. **Redirect:** point each order form's success redirect to `thank-you.html?first_name={{contact.first_name}}&plan=3` (or `plan=6`).

Buy buttons only work after the visitor ticks the "I understand monitoring must stay active" box. The 3-month button opens the 6-month upsell first.
