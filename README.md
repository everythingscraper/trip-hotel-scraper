# Trip.com Hotel Scraper — Prices, Ratings & Room Data (Apify Actor)

Scrape **[Trip.com](https://www.trip.com)** hotels in **51 countries** at scale: room prices, star ratings, review scores, hotel IDs, addresses, amenities, and photo URLs. Search by country + city, by Trip.com city ID, by free-text destination, or by full Trip.com URL — whichever you have.

> 👉 Run it on Apify (no install): **[apify.com/hotels-scrapers/trip-hotel-scraper](https://apify.com/hotels-scrapers/trip-hotel-scraper)**

This repository contains a minimal **Python example** that runs the deployed Actor via the Apify API and prints results.

## What this Trip.com scraper extracts

| Field | Description |
|---|---|
| `name` | Hotel name |
| `hotel_id` | Trip.com internal hotel ID |
| `star_rating` | Official star count (1–5) |
| `rating` | Guest review score |
| `current_price` | Lowest visible nightly rate |
| `currency` | Pricing currency |
| `address` / `city` / `country` | Location |
| `amenities` | List of amenity tags |
| `images` | Photo URLs |
| `url` | Canonical Trip.com hotel URL |

## Quick start — Python example

```bash
git clone https://github.com/everythingscraper/trip-hotel-scraper.git
cd trip-hotel-scraper
pip install -r requirements.txt
export APIFY_TOKEN=your_apify_token   # https://console.apify.com/settings/integrations
python main.py
```

`main.py` runs a 25-hotel London search and prints the first 5 results plus the dataset link.

## How to scrape Trip.com — input options

Three ways to pick a destination:

1. **By country + city** — set `country` (e.g. `GB`) and `searchWord` (e.g. `London`).
2. **By Trip.com city ID** — set `cityId` directly (e.g. `338` = London, `228` = Tokyo, `192` = Paris, `633` = New York).
3. **By URL** — paste a full Trip.com search URL into the advanced override.

Plus stay parameters: `checkIn`, `checkOut` (`YYYY-MM-DD`), `adults`, `rooms`, `totalLimit`, optional `proxyConfiguration`.

Full input schema: **[Input tab on Apify](https://apify.com/hotels-scrapers/trip-hotel-scraper/input-schema)**.

## Sample output

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

Datasets export as **JSON, CSV, Excel, HTML, or XML**.

## How much does it cost to scrape Trip.com?

Apify CU-based pricing. A typical run scraping ~1,000 Trip.com hotels fits inside the **Apify Free plan ($5 platform credit)**. Costs scale linearly with `totalLimit` and the number of destinations. See the [Apify Actor page](https://apify.com/hotels-scrapers/trip-hotel-scraper) for current pricing.

## FAQ

**Does Trip.com have an official hotels API?**
There is no public Trip.com hotels search API for non-affiliate developers. This Actor is the practical route for hotel pricing intelligence on Trip.com.

**Which countries are supported?**
51 countries including the US, UK, all major EU markets, China Mainland, Hong Kong, Taiwan, Japan, South Korea, Thailand, Vietnam, Malaysia, Singapore, Indonesia, India, UAE, Saudi Arabia, Australia, Canada, Mexico, Brazil. Full list in the input schema.

**Where do I find a Trip.com `cityId`?**
Open any Trip.com search URL — the `city=<id>` query parameter is the city ID.

**Do prices reflect the user's currency?**
Prices are returned in Trip.com's currency for the chosen market. Pin a country to control this.

**Need custom Trip.com data, room-type granularity, or rate breakdowns?**
Open an issue or contact us via the [Apify Actor page](https://apify.com/hotels-scrapers/trip-hotel-scraper).

## Other Apify Actors by everythingscraper

- 🏖️ **[Traveloka Hotel Scraper](https://github.com/everythingscraper/traveloka-hotel-scraper)** — Southeast Asia hotel data
- 🏠 **[Airbnb Scraper](https://github.com/everythingscraper/airbnb-scraper)** — STR metrics, ADR, RevPAR
- 🏢 **[LoopNet Scraper](https://github.com/everythingscraper/loopnet-scraper)** — commercial real estate listings

## Is it legal to scrape Trip.com?

This Actor extracts only publicly displayed Trip.com hotel listings. It does not bypass logins or harvest private user data. Hotel and pricing data may be subject to Trip.com's Terms of Service. Use legitimately (price intelligence, market research) and consult your lawyers if unsure.

## License

MIT — see [LICENSE](./LICENSE).
