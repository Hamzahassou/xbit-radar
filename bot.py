import time, json, random, requests, subprocess

TOKEN = "8519587497:AAFAdSa2zHxd8twT13P5lTw-XF0-0-JNPH0"
CHAT_ID = "1945385119"
URL = "https://hamzahassou.github.io/xbit-radar/"

def push():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "fix"], capture_output=True)
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        return True
    except: return False

print("💀 DARK RADAR ENGINE ONLINE")
while True:
    val = round(random.uniform(1.2, 5.0), 2)
    with open("data.json", "w") as f:
        json.dump({"signal": val}, f)
    if push():
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={
            "chat_id": CHAT_ID,
            "text": f"💀 إشارة مدمرة: {val}x",
            "reply_markup": {"inline_keyboard": [[{"text":"💀 فتح الرادار المظلم","web_app":{"url":URL}}]]}
        })
        print(f"✅ تم الحقن: {val}x")
    time.sleep(25)

