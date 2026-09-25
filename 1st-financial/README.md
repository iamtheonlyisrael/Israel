# 1st Financial Credit Repair website

Two static pages. No build step, no dependencies.

| File | What it is |
|---|---|
| `index.html` | Sales page: ticker, departure board, bad-credit-tax calculator, 3-month ($75) and 6-month ($150) boarding passes, upgrade pop-up, FAQ, sticky "Book my seat" bar. |
| `thank-you.html` | After-purchase page: monitoring enrollment and intake form steps. |

## Before going live

1. **Checkout links.** In `index.html`, find `FFC_LINKS` near the bottom and paste the two GHL order-form URLs:
   ```js
   threeMonth: "PASTE-3-MONTH-CHECKOUT-URL",   // $75
   sixMonth:   "PASTE-6-MONTH-CHECKOUT-URL"    // $150
   ```
   The matching GHL products already exist in the Major Wealth Group sub-account:
   "1st Financial Credit Repair - 3 Months (Coach)" and "- 6 Months (First Class)".
2. **Logo.** Replace `PASTE-YOUR-LOGO-URL-HERE` in both files. Until then a text logo is shown.
3. **Thank-you redirect.** Point each GHL order form's success redirect to `thank-you.html`.
   Optional personalisation: `thank-you.html?first_name={{contact.first_name}}&plan=3` (or `plan=6`).
4. **Confirm links with the client:** monitoring enrollment (`myfreescorenow.com/enroll/B02C2516`),
   intake form (`bossupthemajorway.com/credit-intake-form`) and phone `(864) 536-0006`.

## Publishing

- **GHL funnel:** paste the part of `index.html` between `<body>` and `</body>` into a Custom Code element.
- **Any static host** (Netlify, Vercel, GitHub Pages, cPanel): upload this folder as-is.
