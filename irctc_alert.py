import requests
from datetime import datetime, timedelta

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

today = datetime.utcnow()
travel_date = today + timedelta(days=60)

message = f"""
🚆 IRCTC BOOKING ALERT 🚆

Today: {today.strftime('%d %B %Y')}
Booking Open For Travel Date:
{travel_date.strftime('%d %B %Y')}
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
