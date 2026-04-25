import time, json, random, requests, subprocess

# إعداداتك الخاصة
TOKEN = "8519587497:AAFAdSa2zHxd8twT13P5lTw-XF0-0-JNPH0"
CHAT_ID = "1945385119"
URL = "https://hamzahassou.github.io/xbit-radar/"

def push_data():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "fix_update"], capture_output=True)
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        return True
    except:
        return False

print("💀 HAMZA RADAR V12 - FULL RESET ACTIVE")
while True:
    # توليد قيمة عشوائية جديدة
    val = round(random.uniform(1.3, 4.8), 2)
    
    # كتابة البيانات في الملف
    with open("data.json", "w") as f:
        json.dump({"signal": val}, f)
    
    if push_data():
        # إرسال التحديث للتليجرام
        msg = f"💀 إشارة جديدة: {val}x\n🚀 تم تحديث الرادار بنجاح"
        markup = {"inline_keyboard": [[{"text": "🔥 فتح الرادار", "web_app": {"url": URL}}]]}
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": msg, "reply_markup": markup})
        print(f"✅ تم الرفع: {val}x")
    
    time.sleep(25) # انتظار 25 ثانية لضمان استقرار السيرفر

