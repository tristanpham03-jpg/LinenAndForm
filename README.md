# Linen & Form

**Beautifully considered. Sensibly chosen.**

A deployable editorial affiliate site for affordable luxury home and apartment finds, built for readers arriving from Pinterest. Ten substantial buying guides, 30 product-category sections, a responsive homepage, guide collection, About, Contact, Privacy Policy, affiliate disclosure, and custom 404 page.

Contact: **collegelife3500@gmail.com** (retained as requested).

## Deploy to Vercel

1. Unzip the package and put the contents of the `linen-and-form` folder in a GitHub repository you control.
2. In Vercel, choose **Add New → Project**, then import the repository.
3. Select **Other** as the framework. Use the folder containing `package.json` as the root. The included configuration sets **Build Command: `npm run build`** and **Output Directory: `public`**.
4. Deploy. Make sure the production URL is publicly accessible without visitor authentication. Open the homepage, two guides, and Contact on desktop and mobile.
5. Set `url` in `site.json` to the final HTTPS address, then commit and redeploy. This fills in the canonical URLs, article-specific social image URLs, and `/sitemap.xml` entries.

Alternative: from the project folder, run `npx vercel --prod`, sign in, and follow the prompts. Vercel requires your account. No database, environment variables, API keys, or runtime packages are required.

Official deployment reference: https://vercel.com/docs/builds/configure-a-build

## Local preview

Requires Node.js 20 or newer; no package installation is needed.

```sh
npm run build
npm start
```

Visit **http://127.0.0.1:4173**. Stop the preview with Ctrl+C. Use HTTP rather than opening individual HTML files, because navigation and assets use root-relative URLs.

## Edit the site

- `articles.json`: guide titles, introductions, shopping criteria, product-category text, and product slot IDs.
- `site.json`: public URL, contact email, optional publisher name, and affiliate links.
- `build.mjs`: homepage, shared layouts, and About/Contact/Privacy/disclosure content.
- `public/assets/style.css`: desktop/mobile layout and visual theme.
- `public/assets/*.jpg`: three locally bundled, compressed room-inspiration images.
- `public/`: generated static website to deploy.

Run `npm run build` after changing content or configuration. Run `npm run check` to verify page structure, links, assets, anchors, branding, disclosures, article length, and the 30 unique shopping slots.

The site needs no JavaScript in the browser. Mobile navigation uses a native expandable menu. All content, jump links, email links, and navigation are static HTML.

## Add verified products and affiliate URLs

Every product section currently describes a **category**, not an invented Amazon item. It includes who it may suit, why it is useful, what to check, when to skip it, and a clearly labeled non-clickable affiliate placeholder.

1. Choose and verify the actual product on Amazon. Confirm that its dimensions and features support the adjacent text.
2. Update that entry in `articles.json` with the accurate product name and product-specific selection notes. Do not add a testing claim unless you actually tested it.
3. Create its real affiliate URL through your Amazon Associates account.
4. Add the URL to `site.json` under `affiliateLinks`, keyed by the product's `id` from `articles.json`.
5. Build, check, and redeploy.

Example structure only—replace the value with your real link:

```json
"affiliateLinks": {
  "sculptural-table-lamp": "PASTE_YOUR_REAL_HTTPS_AMAZON_AFFILIATE_URL_HERE"
}
```

Do not use this example value literally. The build rejects non-HTTPS and non-Amazon URLs. This US-program starter allows `amazon.com`, its subdomains, and `amzn.to`. Other marketplaces require an intentional update to validation.

Once configured, the slot becomes a prominent **View on Amazon (paid link)** CTA with `rel="sponsored nofollow noopener"`. The exact phrase **“As an Amazon Associate I earn from qualifying purchases.”** appears on every page and near article shopping sections.

No prices, ratings, customer reviews, inventory claims, fabricated product URLs, or false testing claims are included. The under-$100 article is explicitly a budget framework, not a verified live-price roundup. Check total price before selecting products for it. When product selections are finalized, update intro, category labels, and placeholder explanations accurately; the current copy deliberately describes the starter state.

## Content and Pinterest destinations

Link each Pin to its relevant article instead of sending all traffic to the homepage. Match the Pin's promise to the page and avoid depicting generated room objects as actual products for sale.

| Topic | Destination path |
| --- | --- |
| Expensive-looking home details | `/guides/amazon-home-finds-look-expensive/` |
| Affordable bedroom upgrades | `/guides/affordable-bedroom-upgrades/` |
| Designer-inspired furniture | `/guides/amazon-furniture-designer-style/` |
| Small-apartment organization | `/guides/small-apartment-organization/` |
| Useful kitchen upgrades | `/guides/kitchen-upgrades-worth-buying/` |
| Neutral living room essentials | `/guides/neutral-living-room-essentials/` |
| Affordable lighting | `/guides/affordable-high-end-lighting/` |
| Vanity and beauty organization | `/guides/vanity-beauty-organization/` |
| Under-$100 budget framework | `/guides/home-finds-under-100/` |
| Practical apartment essentials | `/guides/apartment-essentials-worth-it/` |

Use the final site domain plus the destination path when creating Pins. Review Pinterest and affiliate disclosure requirements for the Pin itself. The website's disclosure does not replace disclosure on other content.

Official Pinterest guidance: https://business.pinterest.com/blog/lower-funnel-creative-best-practices/

## Before publication and Amazon review

- Review and personalize the content to reflect your actual editorial judgment. Ten articles alone do not guarantee approval, traffic, or earnings.
- Confirm the public URL is under your control and add the correct address to your Amazon Associates site list.
- The requested Amazon disclosure is already included. Ensure it accurately reflects your participation when publishing or activating links.
- Add a publisher name in `site.json` if desired. Check the retained contact email.
- Review the Privacy Policy against your actual hosting and email practices. Update it before adding analytics, Pinterest conversion tracking, forms, newsletters, or advertising. Those features are not included in this starter.
- Check domain and brand availability before committing commercially. **Linen & Form has not been cleared for trademark or domain availability.**

Official Amazon references checked October 7, 2026:
- Application review: https://affiliate-program.amazon.com/help/node/topic/G8TW5AE9XL2VX9VM
- Required disclosure: https://affiliate-program.amazon.com/help/node/topic/GHQNZAU6669EZS98

## Brand direction

Five options were proposed: **Linen & Form** (recommended and implemented), The Collected Room, Everyday Heirloom, The Apartment Edit, and Soft Space Studio.

The implemented identity uses editorial serif headings, deep olive accents, warm neutral interiors, and practical buying guidance. It is aimed at adults seeking attainable home inspiration, including the requested Pinterest audience of women roughly 22–44, without restricting the site to that audience.

## Images, privacy, and validation

The three room images are AI-generated **style inspiration**, not product photography or evidence of product testing. Article captions, About, and the footer make this explicit. They are reused by relevant room category and served locally; no remote fonts or image requests are required.

There are no cookies, local-storage code, analytics, accounts, forms, or fake newsletter signups. Hosting may still process technical logs. Email is handled by Gmail.

Build and structural checks were completed. A live browser preview was not verified because permission to start the local preview server was declined. Before sharing the live site, check mobile/desktop layout, 200% zoom, keyboard navigation, the mobile menu, in-page links, contact email, 404 behavior, and any affiliate links you add.

The project is packaged for deployment; it has not been published to Vercel or any other host.
