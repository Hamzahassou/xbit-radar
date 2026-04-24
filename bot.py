import requests

# إعدادات حمزة
TOKEN = "8634146766:AAE7LdlYKd-GT6PpPN9DSxL7g-D1sb7Q79U"
CHAT_ID = "1945385119"
# الرابط الذي استخرجناه للتو
URL = "https://hamzahassou.github.io/xbit-radar/"

def launch_web_app():
    api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": """
🔱 **HAMZA-FF WEB-APP ENGINE v9.0** 🔱
━━━━━━━━━━━━━━━━━━━━
نظام الرادار السحابي متصل الآن.
اضغط على الزر أدناه لفتح واجهة القناص.
━━━━━━━━━━━━━━━━━━━━
🔵🔴 *VISCA EL BARÇA*
""",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "🚀 إطلاق واجهة الصاروخ",
                        "web_app": {"url": URL}
                    }
                ]
            ]
        },
        "parse_mode": "Markdown"
    }
    r = requests.post(api_url, json=payload)
    if r.status_code == 200:
        print("✅ تم الإرسال بنجاح! افتح تلجرام الآن.")
    else:
        print("❌ فشل الإرسال، تأكد من الـ Token.")

if __name__ == "__main__":
    launch_web_app()

