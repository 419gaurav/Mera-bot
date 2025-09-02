import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": "✅ Test message from GitHub at run time"
}

response = requests.post(url, data=payload)

print("---- Telegram API Response ----")
print(response.text)
print("--------------------------------")
