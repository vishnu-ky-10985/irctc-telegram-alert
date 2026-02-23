import requests
import os
from datetime import datetime, timedelta
import holidays

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

today = datetime.utcnow()
travel_date = today + timedelta(days=60)
next_day = travel_date + timedelta(days=1)

# --- Central Govt Holidays ---
india_holidays = holidays.country_holidays('IN')

holiday_name = None

if next_day.date() in india_holidays:
    holiday_name = india_holidays.get(next_day.date())

# --- Tamil Nadu specific holidays (add important ones manually if needed) ---
tamil_nadu_extra = {
    "2026-01-14": "Pongal",
    "2026-04-14": "Tamil New Year",
    "2026-10-20": "Ayudha Pooja",
}

if next_day.strftime("%Y-%m-%d") in tamil_nadu_extra:
    holiday_name = tamil_nadu_extra[next_day.strftime("%Y-%m-%d")]

# --- 2nd / 4th Saturday Check ---
week_number = (next_day.day - 1) // 7 + 1
is_special_saturday = (
    next_day.weekday() == 5 and (week_number == 2 or week_number == 4)
)

club_message = ""

if holiday_name:
    club_message = f"\n🔥 Club Opportunity:\n{next_day.strftime('%d %B %Y')} is {holiday_name}"

elif is_special_saturday:
    club_message = f"\n🔥 Club Opportunity:\n{next_day.strftime('%d %B %Y')} is {week_number}th Saturday"

message = f"""
🚆 IRCTC BOOKING ALERT 🚆

Booking Open For:
{travel_date.strftime('%d %B %Y')}

{club_message}
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
