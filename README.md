# Trip.com Hotel Scraper — 51-Country Hotel Pricing (Apify Actor)

A global hotel-data feed without the GDS contract. Scrape **[Trip.com](https://www.trip.com)** hotels in **51 countries** — including the UK, US, China, Japan, all major EU markets, and most of APAC — for nightly rates, star ratings, review scores, addresses, amenities, and photos.

Run it as-a-service on Apify: 👉 **https://apify.com/hotels-scrapers/trip-hotel-scraper**

This repository is a **Python integration example**: `main.py` loops over a list of destinations, calls the Actor for each, and prints the cheapest hotel found in every city. Drop your own list and you have a multi-city travel-comparison feed.

## Country coverage

🇺🇸 🇬🇧 🇩🇪 🇫🇷 🇮🇹 🇪🇸 🇵🇹 🇳🇱 🇧🇪 🇸🇪 🇩🇰 🇫🇮 🇮🇪 🇵🇱 🇨🇿 🇭🇺 🇬🇷 🇹🇷 🇪🇪 🇷🇺 🇨🇳 🇭🇰 🇹🇼 🇲🇴 🇯🇵 🇰🇷 🇹🇭 🇻🇳 🇲🇾 🇸🇬 🇮🇩 🇵🇭 🇮🇳 🇳🇵 🇰🇭 🇱🇦 🇺🇿 🇦🇲 🇦🇪 🇸🇦 🇮🇱 🇪🇬 🇦🇺 🇳🇿 🇫🇯 🇨🇦 🇲🇽 🇧🇷 🇩🇴 🇹🇿 🇸🇰

51 countries. Full list of country IDs in the Actor's input schema.

## Output fields

| Field | Description |
|---|---|
| `name` | Hotel name |
| `hotel_id` | Trip.com internal ID |
| `star_rating` | Official star count (1–5) |
| `rating` | Guest review score (0–10) |
| `current_price` | Lowest visible nightly rate |
| `currency` | Pricing currency (varies by market) |
| `address`, `city`, `country` | Location |
| `amenities` | List of amenity tags |
| `images` | Photo URLs |
| `url` | Canonical hotel URL on Trip.com |

## Quick start

```bash
git clone https://github.com/everythingscraper/trip-hotel-scraper.git
cd trip-hotel-scraper
pip install -r requirements.txt
APIFY_TOKEN=your_token python main.py
```

The script queries London, Paris, and Tokyo and prints the cheapest hotel per city.

## Three ways to pick a destination

1. **Country + city name** — set `country` (e.g. `GB`) and `searchWord` (`London`). Easiest.
2. **Trip.com city ID** — set `cityId` directly (London=338, Tokyo=228, Paris=192, NYC=633). Most reliable.
3. **Full URL override** — paste any Trip.com search URL into the advanced section. Supports custom filters.

Plus the usual stay parameters: `checkIn`, `checkOut`, `adults`, `rooms`, `totalLimit`, optional `proxyConfiguration`.

Schema: **[Input tab on Apify](https://apify.com/hotels-scrapers/trip-hotel-scraper/input-schema)**.

## Sample dataset row

```json
{
  "name": "The Savoy",
  "hotel_id": "748291",
  "star_rating": 5,
  "rating": 9.2,
  "current_price": 612.00,
  "currency": "GBP",
  "address": "Strand, London WC2R 0EU",
  "city": "London",
  "country": "United Kingdom",
  "url": "https://www.trip.com/hotels/london-hotel-detail-748291/the-savoy/",
  "scrapedAt": "2026-04-27T10:00:00Z"
}
```

Apify Storage exports as **JSON · CSV · Excel · HTML · XML**.

## Pricing

Apify CU-based. A typical 1,000-hotel single-city run fits inside the **Free plan's $5 credit**. Cost scales linearly with `totalLimit` and number of cities. Live pricing on the **[Apify Actor page](https://apify.com/hotels-scrapers/trip-hotel-scraper)**.

## FAQ

**Is there a Trip.com hotels API?** Affiliates only. For independent developers, scraping is the path.

**Where do I find the Trip.com `cityId`?** Open any Trip.com search URL in your browser — `city=<id>` is the parameter you want.

**Why three input modes?** Different teams have different starting points. URLs are great if you've already built the search in the UI; `cityId` is great for programmatic catalogs; country+name is great for ad-hoc queries.

**Does pricing currency follow the user or the hotel?** It follows the hotel's market. Pin a country to control it.

**Can I run multiple cities concurrently?** Yes — kick off several runs in parallel via the Apify API or use the Actor's task feature.

**Need room-type breakdown or rate plans (refundable / breakfast included)?** Open an issue — that's an extension on the roadmap.

## Other Apify Actors

- 🏖️ [Traveloka Hotel Scraper](https://github.com/everythingscraper/traveloka-hotel-scraper) — Southeast Asia
- 🏠 [Airbnb Scraper](https://github.com/everythingscraper/airbnb-scraper) — STR metrics
- 🏢 [LoopNet Scraper](https://github.com/everythingscraper/loopnet-scraper) — CRE listings
- 📊 [Moz Domain Authority Checker](https://github.com/everythingscraper/moz-domain-authority-checker)
- 🧑‍💼 [Booksy Leads Scraper](https://github.com/everythingscraper/booksy-leads-scraper)

## Legality

Only publicly displayed Trip.com hotel listings are extracted. No logins are bypassed and no private user data is harvested. Hotel and pricing data may still be subject to Trip.com's Terms of Service and the laws of your jurisdiction — consult counsel if unsure.

## License

MIT — see [LICENSE](./LICENSE).
