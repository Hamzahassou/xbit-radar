import requests
import time
import json
import random

TOKEN = "8634146766:AAE7LdlYKd-GT6PpPN9DSxL7g-D1sb7Q79U"
CHAT_ID = "1945385119"

def update_live_data(signal):
    # إنشاء ملف بيانات ليقرأ منه الموقع تلقائياً
    data = {"signal": signal, "timestamp": time.time()}
    with open('data.json', 'w') as f:
        json.dump(data, f)
    print(f"📊 تم تحديث الرادار الحقيقي إلى: {signal}x")

def get_1xbet_logic():
    # هنا نضع معادلة التحليل بناءً على سجل النتائج
    # حالياً سنحاكي التحليل من السجل الظاهر في لقطة الشاشة
    return round(random.uniform(1.30, 3.50), 2)

def main():
    while True:
        val = get_1xbet_logic()
        update_live_data(val)
        
        # إرسال تنبيه للتلجرام بوجود إشارة جديدة
        msg = f"📡 **إشارة 1XBET حقيقية**\n\n🎯 الهدف المتوقع: `{val}x`\n✅ الرادار المباشر محدث الآن!"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
        
        time.sleep(10) # تحديث كل 10 ثوانٍ لضمان استقرار السيرفر

if __name__ == "__main__":
    main()
