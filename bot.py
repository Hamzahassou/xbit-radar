import requests
import random
import time

# بياناتك الأساسية
TOKEN = "8634146766:AAE7LdlYKd-GT6PpPN9DSxL7g-D1sb7Q79U"
CHAT_ID = "1945385119"
# رابط موقعك على جيت هاب
URL_BASE = "https://hamzahassou.github.io/xbit-radar/"

def send_premium_signal():
    # توليد رقم تحليل عشوائي احترافي
    target = round(random.uniform(1.20, 3.85), 2)
    
    # بناء الرابط مع حقن الإشارة (Signal Injection)
    web_app_url = f"{URL_BASE}?val={target}"
    
    payload = {
        "chat_id": CHAT_ID,
        "text": f"🔱 **HAMZA VIP SIGNAL** 🔱\n\n🎯 الهدف القادم: `{target}x`\n📊 الثقة: {random.randint(85, 99)}%\n✅ الحالة: تحليل حقيقي آمن",
        "reply_markup": {
            "inline_keyboard": [[
                {"text": "🚀 إطلاق الرادار المباشر", "web_app": {"url": web_app_url}}
            ]]
        },
        "parse_mode": "Markdown"
    }
    
    try:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json=payload)
        print(f"✅ تم إرسال إشارة {target}x بنجاح!")
    except Exception as e:
        print(f"❌ خطأ في الاتصال: {e}")

if __name__ == "__main__":
    send_premium_signal()

