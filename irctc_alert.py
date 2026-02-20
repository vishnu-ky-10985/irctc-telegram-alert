import requests
import os
from datetime import datetime, timedelta

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

today = datetime.utcnow()
travel_date = today + timedelta(days=60)

message = f"""
🚆 IRCTC BOOKING ALERT 🚆

Today: {today.strftime('%d %B %Y')}
Booking Open For:
{travel_date.strftime('%d %B %Y')}
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
