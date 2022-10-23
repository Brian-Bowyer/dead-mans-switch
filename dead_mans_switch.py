# Python 3.10
import requests

from discord import SyncWebhook

OVERSEER_URL = ...
WEBHOOK_URL = ...


def main() -> None:
    webhook = SyncWebhook.from_url(WEBHOOK_URL)
    response = requests.get(OVERSEER_URL)
    if not response.ok:
        webhook.send(f"Media server is down with response code {response.status_code}")


if __name__ == "__main__":
    main()
