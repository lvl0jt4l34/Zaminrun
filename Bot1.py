import requests
import schedule
import time
import jdatetime

TOKEN = "1342439526:crs6Nat6WZPJNBZVweFZlNZpF03Wyf1O1yQ"
GROUP_ID = "1608959784"

BASE_URL = f"https://tapi.bale.ai/bot{TOKEN}"


def send_message(text):

    requests.post(
        f"{BASE_URL}/sendMessage",
        json={
            "chat_id": GROUP_ID,
            "text": text
        }
    )


# پیام صبح
def morning_message():

    now = jdatetime.datetime.now()

    today = now.strftime("%Y/%m/%d")
    day = now.strftime("%A")

    text = f"""
🌞 سلام و صبح بخیر

شروع روز کاری پروژه

📅 تاریخ: {today}
🗓 {day}

موفق باشید 🌷
"""

    send_message(text)


# پیام عصر
def evening_message():

    now = jdatetime.datetime.now()

    today = now.strftime("%Y/%m/%d")

    text = f"""
🕔 پایان ساعت کاری

📅 تاریخ: {today}

لطفاً گزارش روزانه ثبت شود.
"""

    keyboard = {
        "inline_keyboard": [
            [
                {
                    "text": "📋 ثبت گزارش روزانه",
                    "callback_data": "daily_report"
                }
            ]
        ]
    }

    requests.post(
        f"{BASE_URL}/sendMessage",
        json={
            "chat_id": GROUP_ID,
            "text": text,
            "reply_markup": keyboard
        }
    )


# زمان بندی
schedule.every().day.at("08:00").do(morning_message)
schedule.every().day.at("17:00").do(evening_message)


print("BOT STARTED")


while True:

    schedule.run_pending()

    time.sleep(30)
