"""Run the Trip.com Hotel Scraper Apify Actor and print results.

Get your Apify API token: https://console.apify.com/settings/integrations
Actor page: https://apify.com/hotels-scrapers/trip-hotel-scraper

Install:
    pip install -r requirements.txt

Run:
    APIFY_TOKEN=your_token python main.py
"""

import os

from apify_client import ApifyClient

ACTOR_ID = "hotels-scrapers/trip-hotel-scraper"


def main() -> None:
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_TOKEN env var. Get one at https://console.apify.com/settings/integrations")

    client = ApifyClient(token)

    run_input = {
        "country": "GB",
        "searchWord": "London",
        "checkIn": "2026-06-01",
        "checkOut": "2026-06-03",
        "adults": 2,
        "rooms": 1,
        "totalLimit": 25,
    }

    print(f"Starting actor {ACTOR_ID} ...")
    run = client.actor(ACTOR_ID).call(run_input=run_input)

    print(f"Run finished: {run['status']}  (run id: {run['id']})")
    print(f"Console: https://console.apify.com/actors/runs/{run['id']}\n")

    dataset = client.dataset(run["defaultDatasetId"])
    items = dataset.list_items().items
    print(f"Got {len(items)} hotels.\n")

    for item in items[:5]:
        print(
            f"- {str(item.get('name', '?'))[:50]:50}  "
            f"stars={item.get('star_rating', '?')}  "
            f"rating={item.get('rating', '?')}"
        )

    print(f"\nFull dataset: https://api.apify.com/v2/datasets/{run['defaultDatasetId']}/items?format=json")


if __name__ == "__main__":
    main()
