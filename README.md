# Amy | Intuitive Readings

A complete responsive HTML, CSS, and vanilla JavaScript website based on the supplied Amy brief. The user's explicit request for HTML takes precedence over the brief's suggested React stack. No framework, package installation, or build step is needed to run the delivered site.

## Open the site locally

1. Extract this folder.
2. With Node.js installed, run `node server.mjs` from this folder.
3. Open `http://localhost:4173`.

Do not open the HTML files directly with `file://`. The site uses real URL paths, shared assets, browser storage, and a confirmation route fallback. The supplied server supports them. Static hosting can serve the `dist` directory. Configure `/booking/confirmed/*` to serve `/booking/confirmed/demo/index.html`, and unknown routes to serve `404.html` with status 404. A Cloudflare compatible `_redirects` file is included.

## Pages and features

72 page templates plus the standalone 404 response document. The site includes Home; Readings; Video, Chat, and Email reading details; Pricing; Booking; Checkout; Confirmation; How It Works; About; Daily Card; 22 individual tarot meaning pages; Horoscopes; 12 individual sign pages; Monthly Energy; Journal; six article pages; Gift Readings; Client Reflections; FAQ; Contact; Login; Signup; Reset Password; Account; Bookings; Email Readings; Settings; Privacy; Terms; Refund Policy; Disclaimer; Privacy Choices; and 404.

Interactive features include a reading match quiz, daily tarot pull that stays consistent for each visitor and date, sequential three card spread, reading and topic filters, duration selection, birthday sign finder, horoscope period and compatibility reflections, approximate moon calendar, journal filters and load more, searchable FAQs, scripted chat, validated forms, email question intake, and gift preview.

Booking includes saved progress, Central Time sample availability converted into the visitor's selected time zone, date and time selection, conflict checks, review, test checkout, confirmation, downloadable ICS, a Google Calendar link, and a video room preview. Email confirmations calculate delivery exactly 48 hours after the sample purchase. Gift checkout issues a local single use code matching the purchased reading type and duration.

## Demonstration behavior

This is a complete frontend demonstration, not a connected commerce service. Availability, accounts, payments, chat, gift codes, form delivery, and video rooms are simulated. No actual appointment is made, money collected, email sent, or video captured. Saved data stays in the visitor's browser. The shared demo login intentionally sees all demo bookings in that browser. Individual demo accounts filter bookings by email. This is not a production security boundary.

Use `Explore the demo account`, or sign in with `demo@amyreadings.com` and `demo1234`. Do not reuse real passwords or enter sensitive personal information.

Test checkout accepts `4242 4242 4242 4242` for success and `4000 0000 0000 0002` for decline, a future expiry, a three digit CVC, and a five digit ZIP. Other card numbers are rejected. Card values are never saved or transmitted. `AMY15` illustrates a promo state; final prices remain placeholders. Submit a form using `error@example.com` to exercise its error state.

## Files

* `dist/`: deployment ready HTML pages and assets.
* `dist/assets/tokens.css`: semantic colors, typography, and motion values.
* `dist/assets/styles.css`: responsive layout and component styling.
* `dist/assets/app.js`: page interactions, booking, checkout, and account UI.
* `dist/assets/services.js`: browser storage, availability, mock payments, mock forms, and demo account hashing.
* `dist/assets/data.js`: generated reading content and sample editorial data.
* `build.py`: dependency free Python page generator. Run `python3 build.py` only when editing shared content or templates. It rebuilds HTML, SVG artwork, and data; it leaves CSS, service adapters, fonts, and video files in place.
* `server.mjs`: zero dependency local server with deep route support and video byte ranges.
* `verify.py`: checks document metadata, duplicate IDs, heading structure, and local asset/link targets.
* `routes.json`: all generated routes.

## Content Amy must supply

Search for square brackets in `build.py` and `dist/assets/app.js` to find the editable slots. They include `[PRICE]`, `[EMAIL]`, `[PHONE]`, Amy's portrait, biography, reading approach, specialties, satisfaction promise, rescheduling policy, refund policy, monthly package, monthly letter, archive letters, response time, review text, client name and location, and every draft legal provision. No testimonials, credentials, awards, reading statistics, or experience claims have been invented.

The six journal articles, tarot meanings, and horoscope reflections are original sample editorial content for Amy's review. They are labeled as reflective material and do not make guaranteed predictions. All policy pages are explicitly marked for professional review.

Amy's actual photograph was not attached. The specified pastel arch with an `A` is used throughout the site instead of an invented portrait. When supplied, create natural color WebP and JPG versions at 400, 800, and 1200 pixels. Update `portrait()` and `avatar()` in `build.py` and the avatar markup in `app.js`, using `object-fit: cover; object-position: center 25%`. Preserve the initial fallback. Replace `social.png` with a 1200 by 630 image including her approved photograph.

## Production connections

1. Scheduling: replace `AmyServices.availability` with server calls to the selected scheduler. Read availability from Calendly or Acuity and create reservations server side, with webhooks for cancellations and rescheduling. Keep time values in UTC and display them through the existing time zone formatter.
2. Payments: confirm that the chosen processor accepts psychic services. Replace the mock card fields with the provider's hosted checkout or tokenized payment elements. Create payment sessions on a server, verify webhooks, enforce idempotency, validate prices server side, and only confirm bookings after verified payment. Never add secret API keys to browser JavaScript.
3. Video: generate Zoom or Google Meet links on the server after a confirmed booking, then show and email the actual link. Replace the explicitly labeled preview room.
4. Chat: replace the scripted assistant with an approved chat provider such as Crisp, Tidio, or Tawk.to, including truthful availability and response time indicators.
5. Email: connect contact, newsletter, receipt, gift, reset, and reading delivery workflows to server endpoints and an email provider. Implement consent records and unsubscribe handling before sending marketing email.
6. Accounts: replace browser local mock authentication with server backed accounts, secure sessions, verified email, access checks, rate limits, and appropriate retention. Never use the demo account logic to protect real data.
7. Gift codes: move code generation, redemption, expiry, and fulfillment to the server, with atomic single use redemption.
8. Content and launch: replace the placeholders, approve policies and delivery promises, set the final domain in metadata, and replace the intentional `noindex,nofollow` and robots disallow only when the site is ready for real visitors.

## Media and typography

The self hosted stock hero is Mixkit item 51082: https://mixkit.co/free-stock-video/a-mystical-altar-with-tarot-cards-a-dummy-hand-and-51082/ . The source page identifies it under the Mixkit Stock Video Free License: https://mixkit.co/license/#videoFree . The clip was trimmed with an end transition and exported as MP4 and WebM, with a smaller mobile MP4 and WebP poster. It is muted, pauses outside the viewport, and respects reduced motion. Desktop MP4 is under 1 MB and mobile MP4 under 300 KB.

Fraunces and Inter are self hosted WOFF fonts obtained through Google Fonts. Retain their SIL Open Font License notices. Original SVG illustrations and line icons are included in the source. Layout reference: https://www.californiapsychics.com/ . Motion reference: https://www.purplegarden.co/ . No reference site copy, photographs, logos, or commercial tarot artwork was reused.

## Verification

The document check passed for all 73 HTML files and 4,211 local links/assets. JavaScript syntax checks passed. Service tests verified Central Time conversion in winter and summer, selected time zone dates, closed days, booking conflicts, rescheduling exclusions, payment success and decline, and form error states.

Browser checks verified the homepage, video slot prefill, booking details and review, declined payment recovery, successful checkout, confirmation, protected account navigation, demo account entry, rescheduling, cancellation, tarot pull and spread, mobile navigation, and mobile/tablet horizontal overflow. A tablet tarot overflow issue and query string redirect issue were corrected. A later browser session was unavailable, so the email and gift flows were inspected in source but not fully exercised in that session. No Lighthouse score or formal WCAG certification is claimed.
