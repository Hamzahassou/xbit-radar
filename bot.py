import time, json, random, requests, subprocess

# بياناتك الخاصة
TOKEN = "8519587497:AAFAdSa2zHxd8twT13P5lTw-XF0-0-JNPH0" 
CHAT_ID = "1945385119"
REPO_URL = "https://hamzahassou.github.io/xbit-radar/"

def push_to_github():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Radar Update"], capture_output=True)
        # استخدام القوة --force لضمان عدم رفض الرفع
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

print("💀 HAMZA RADAR ENGINE V12 ONLINE")
while True:
    # توليد قيمة عشوائية احترافية
    new_signal = round(random.uniform(1.2, 4.8), 2)
    
    with open("data.json", "w") as f:
        json.dump({"signal": new_signal}, f)
    
    if push_to_github():
        msg = f"💀 إشارة رادار قوية: {new_signal}x\n🚀 الحالة: متصل بـ GitHub"
        btn = {"inline_keyboard": [[{"text": "🔥 فتح الرادار المظلم", "web_app": {"url": REPO_URL}}]]}
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": msg, "reply_markup": btn})
        print(f"✅ تم الحقن بنجاح: {new_signal}x")
    
    time.sleep(25) # انتظار لدورة الرفع التالية

