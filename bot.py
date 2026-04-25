import time, json, random, requests, subprocess

TOKEN = "8519587497:AAFAdSa2zHxd8twT13P5lTw-XF0-0-JNPH0" #
CHAT_ID = "1945385119" #
URL = "https://hamzahassou.github.io/xbit-radar/"

def sync_github():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "update"], capture_output=True)
        # استخدام force لإصلاح مشاكل الـ Rejected السابقة
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        return True
    except: return False

print("💀 HAMZA ENGINE V12 ONLINE")
while True:
    val = round(random.uniform(1.2, 4.5), 2)
    with open("data.json", "w") as f:
        json.dump({"signal": val}, f)
    if sync_github():
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={
            "chat_id": CHAT_ID,
            "text": f"💀 إشارة رادار جديدة: {val}x",
            "reply_markup": {"inline_keyboard": [[{"text":"💀 فتح الرادار المظلم","web_app":{"url":URL}}]]}
        })
        print(f"✅ تم التحديث والإرسال: {val}x") #
    time.sleep(25)

