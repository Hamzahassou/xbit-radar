import time, json, random, requests, subprocess

TOKEN = "8519587497:AAFAdSa2zHxd8twT13P5lTw-XF0-0-JNPH0"
CHAT_ID = "1945385119"
URL = "https://hamzahassou.github.io/xbit-radar/"

def sync_to_github():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "update"], capture_output=True)
        # الرفع الإجباري لمسح أي ملفات قديمة معلقة
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

print("🚀 HAMZA RADAR ENGINE STARTING...")
while True:
    # توليد الرقم
    new_val = round(random.uniform(1.2, 4.8), 2)
    
    # تحديث الملف المحلي
    with open("data.json", "w") as f:
        json.dump({"signal": new_val}, f)
    
    # الرفع لـ GitHub
    if sync_to_github():
        # إرسال الرسالة للتليجرام
        payload = {
            "chat_id": CHAT_ID,
            "text": f"💀 إشارة رادار جديدة: {new_val}x",
            "reply_markup": {"inline_keyboard": [[{"text": "🔥 فتح الرادار", "web_app": {"url": URL}}]]}
        }
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json=payload)
        print(f"✅ SIGNAL DEPLOYED: {new_val}x")
    
    time.sleep(25) # وقت كافي لضمان استقرار السيرفر

