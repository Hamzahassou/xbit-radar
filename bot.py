import time, json, random, requests, subprocess

TOKEN = "8519587497:AAFAdSa2zHxd8twT13P5lTw-XF0-0-JNPH0"
CHAT_ID = "1945385119"
WEB_APP_URL = "https://hamzahassou.github.io/xbit-radar/"

def push_to_github():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Update"], capture_output=True)
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        return True
    except: return False

def send_telegram(signal):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"🚀 إشارة جديدة: {signal}x",
        "reply_markup": {"inline_keyboard": [[{"text": "🚀 فتح الرادار المباشر", "web_app": {"url": WEB_APP_URL}}]]}
    }
    requests.post(url, json=payload)

print("💎 HAMZA RADAR STARTING...")
while True:
    val = round(random.uniform(1.2, 5.0), 2)
    with open("data.json", "w") as f: json.dump({"signal": val}, f)
    if push_to_github():
        send_telegram(val)
        print(f"✅ تم الرفع والإرسال: {val}x")
    time.sleep(20)

