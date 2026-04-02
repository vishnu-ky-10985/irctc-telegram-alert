# IRCTC Telegram Alert

A GitHub Actions-powered Python script that sends a daily Telegram message when IRCTC booking opens for a travel date 60 days away. It also highlights if the following day is a public holiday or a 2nd/4th Saturday — useful for planning long weekends.

## How It Works

1. **Travel date calculation** — Computes the date 60 days from today (the day IRCTC opens advance bookings).
2. **Holiday check** — Checks if the day after the travel date is:
   - A Central Government holiday (using the [`holidays`](https://pypi.org/project/holidays/) library).
   - A Tamil Nadu–specific holiday listed in the script.
   - A 2nd or 4th Saturday (bank/government holiday).
3. **Telegram alert** — Sends a formatted message to a Telegram chat via the Bot API.

## Setup

### 1. Create a Telegram Bot

1. Open Telegram and message [@BotFather](https://t.me/BotFather).
2. Use `/newbot` to create a bot and copy the **Bot Token**.
3. Add the bot to your target chat/group and retrieve the **Chat ID** (e.g., via `https://api.telegram.org/bot<TOKEN>/getUpdates`).

### 2. Add GitHub Secrets

In your repository, go to **Settings → Secrets and variables → Actions** and add:

| Secret name | Value |
|-------------|-------|
| `BOT_TOKEN` | Your Telegram bot token |
| `CHAT_ID`   | Your Telegram chat/group ID |

### 3. Schedule

The workflow (`.github/workflows/run.yml`) runs automatically every day at **02:30 UTC** via a cron schedule, and can also be triggered manually from the **Actions** tab.

## Running Locally

```bash
pip install requests holidays

BOT_TOKEN=<your_token> CHAT_ID=<your_chat_id> python irctc_alert.py
```

## Dependencies

- [`requests`](https://pypi.org/project/requests/) — HTTP calls to the Telegram Bot API.
- [`holidays`](https://pypi.org/project/holidays/) — Indian public holiday lookup.

## Customising Tamil Nadu Holidays

The script contains a small dictionary of Tamil Nadu–specific holidays that are not covered by the national calendar. Edit the `tamil_nadu_extra` dict in `irctc_alert.py` to add or update dates:

```python
tamil_nadu_extra = {
    "2026-01-14": "Pongal",
    "2026-04-14": "Tamil New Year",
    "2026-10-20": "Ayudha Pooja",
}
```
