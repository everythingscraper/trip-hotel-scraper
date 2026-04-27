"""Trip.com Hotel Scraper — Apify Actor client example.

Loops over multiple destinations and prints the cheapest hotel found
in each city. Demonstrates calling the same Actor several times in
one script.

Actor: https://apify.com/hotels-scrapers/trip-hotel-scraper
"""

import os

from apify_client import ApifyClient

ACTOR = "hotels-scrapers/trip-hotel-scraper"

DESTINATIONS = [
    {"country": "GB", "searchWord": "London"},
    {"country": "FR", "searchWord": "Paris"},
    {"country": "JP", "searchWord": "Tokyo"},
]

STAY = {"checkIn": "2026-06-01", "checkOut": "2026-06-03", "adults": 2, "rooms": 1, "totalLimit": 25}


def cheapest_price(items: list[dict]) -> dict | None:
    priced = [i for i in items if isinstance(i.get("current_price"), (int, float))]
    return min(priced, key=lambda i: i["current_price"]) if priced else None


def main() -> None:
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_TOKEN (https://console.apify.com/settings/integrations)")

    client = ApifyClient(token)
    actor_client = client.actor(ACTOR)

    print(f"{'destination':<20}  {'best deal':<40}  {'★':<3}  {'price':>10}\n" + "-" * 80)

    for dest in DESTINATIONS:
        run_input = {**dest, **STAY}
        run = actor_client.call(run_input=run_input)
        items = client.dataset(run["defaultDatasetId"]).list_items().items
        deal = cheapest_price(items)
        if deal:
            print(
                f"{dest['searchWord']:<20}  "
                f"{str(deal.get('name', '—'))[:40]:<40}  "
                f"{deal.get('star_rating', '—')!s:<3}  "
                f"{deal['current_price']:>10}"
            )
        else:
            print(f"{dest['searchWord']:<20}  (no priced results)")


if __name__ == "__main__":
    main()
