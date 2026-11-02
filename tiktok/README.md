# TikTok video pipeline (Linen & Form)

Vertical 1080x1920 product videos built from the real Amazon listing photos. Three layouts in `gen3.py`:
- `spot`: one product, full-bleed photos, hook text + feature pills, end card
- `list`: numbered roundup on a solid color (pal = background, text, accent)
- `check`: notes-app checklist with a photo for each item

`videos.py` holds the video specs (dict `V`), `captions.json` the TikTok captions (every caption ends with `#ad As an Amazon Associate I earn from qualifying purchases.`).
`products.txt`: `ASIN price KEY imageIds` (image IDs from the listing's hiRes images). Download with
`curl -o img/KEY_i.jpg https://m.media-amazon.com/images/I/<id>._AC_SL1500_.jpg` (escape `+` as `%2B`).

Run: `TT_DIR=/path/to/workdir/ python3 videos.py <name> [preview seconds,comma,separated]`. Preview first, look at the frames, then render.
Fonts: Cormorant Garamond + Jost variable TTFs (paths at top of gen3.py).

Rules that matter:
- End cards point to Pinterest ("Shop it on Pinterest: Linen & Form"): the TikTok has no bio link (needs 1,000 followers or a business account).
- Crop away the brand's text overlays on listing photos with `z` (zoom) + `fx`/`fy` (focus 0-1).
- Only claims that are on the listing. Prices as "Under $X" from the current price.
- Upload via Buffer (channel linenandform0) from a path under the repo, one per day at 12:00 PM PT. Free plan: 10 queued posts max.

## Batch log
- 2026-11-02: 01-moffe-lamp … 10-small-space (public/videos/tt/), queued Nov 2–11.
