import time, json, random, requests, subprocess

TOKEN = "8519587497:AAFAdSa2zHxd8twT13P5lTw-XF0-0-JNPH0"
CHAT_ID = "1945385119"
URL = "https://hamzahassou.github.io/xbit-radar/"

def sync():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "fix"], capture_output=True)
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        return True
    except: return False

print("💀 RADAR ENGINE STARTING...")
while True:
    val = round(random.uniform(1.2, 4.5), 2)
    with open("data.json", "w") as f:
        json.dump({"signal": val}, f)
    if sync():
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={
            "chat_id": CHAT_ID,
            "text": f"💀 إشارة جديدة: {val}x",
            "reply_markup": {"inline_keyboard": [[{"text":"🔥 فتح الرادار","web_app":{"url":URL}}]]}
        })
        print(f"✅ تم الرفع: {val}")
    time.sleep(25)

