import time
import json
import random
import requests
import subprocess
import os

# --- البيانات التي أرسلتها يا حمزة ---
TOKEN = "8519587497:AAFAdSa2zHxd8twT13P5lTw-XF0-0-JNPH0"
CHAT_ID = "1945385119"
WEB_APP_URL = "https://hamzahassou.github.io/xbit-radar/"

def update_data_file(signal):
    """تحديث ملف البيانات للموقع"""
    try:
        data = {"signal": signal, "timestamp": time.time()}
        with open("data.json", "w") as f:
            json.dump(data, f)
        return True
    except:
        return False

def push_to_github():
    """رفع التحديث لـ GitHub وتجاوز الأخطاء بالقوة"""
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Radar Update"], capture_output=True)
        # استخدام force لضمان عدم حدوث تعارض Rejected
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        return True
    except:
        return False

def send_telegram_signal(signal):
    """إرسال الرسالة مع زر فتح الموقع المباشر"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    text = (
        f"🚀 **إشارة رادار حمزة الجديدة**\n\n"
        f"🎯 الهدف القادم: `{signal}x`\n"
        f"✅ تم تحديث البيانات في الموقع المباشر"
    )
    
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [[
                {
                    "text": "🚀 فتح الرادار المباشر",
                    "web_app": {"url": WEB_APP_URL}
                }
            ]]
        }
    }
    
    try:
        requests.post(url, json=payload)
    except:
        print("❌ فشل في إرسال رسالة التليجرام")

def main():
    os.system('clear')
    print("💎 HAMZA RADAR ENGINE V12.0 💎")
    print("CONNECTED TO TOKEN: 85195...JNPH0")
    
    while True:
        # توليد رقم عشوائي أو قيمة الرادار
        val = round(random.uniform(1.25, 4.90), 2)
        
        print(f"📡 جلب إشارة: {val}x")
        
        # 1. تحديث الملف
        update_data_file(val)
        
        # 2. الرفع للموقع
        if push_to_github():
            print(f"✅ تم الرفع للموقع بنجاح")
            # 3. إرسال الزر للتليجرام
            send_telegram_signal(val)
        else:
            print("❌ فشل الرفع لـ GitHub")

        # انتظر 20 ثانية للإشارة التالية
        time.sleep(20)

if __name__ == "__main__":
    main()

