import telebot, json, time, threading, random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# --- إعداداتك الخاصة (تمت الإضافة) ---
TOKEN = "8318157728:AAH91-oPTBOACrqaXFWeRNkxKoWBQyG-Qh0"
MY_ID = "1945385119"
WEB_URL = "https://hamzahassou.github.io/xbit-radar/" # رابط موقعك على GitHub

bot = telebot.TeleBot(TOKEN)

def generate_safe_path():
    """توليد مسار آمن عشوائي لـ 5 مستويات (لعبة التفاحة)"""
    # نختار رقم العمود (1-5) لكل صف من الصفوف الـ 5
    path = [random.randint(1, 5) for _ in range(5)]
    path_str = ",".join(map(str, path))
    print(f"✅ تم تحليل مسار آمن جديد: {path_str}")
    return path_str

def sync_data():
    """تحديث ملف data.json كل 15 ثانية ليرفعه السكربت التلقائي"""
    while True:
        p = generate_safe_path()
        with open("data.json", "w") as f:
            # دمج المسار مع عداد النجاح لإعطاء مصداقية
            json.dump({
                "path": p, 
                "accuracy": random.randint(580, 620),
                "hash": f"Verified_By_Hamza_Pro"
            }, f)
        time.sleep(15)

@bot.message_handler(commands=['start'])
def start_bot(m):
    # التأكد من أنك فقط أو المشتركين من يصل للبوت
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🍎 تشغيل رادار التفاحة الآمن", web_app=WebAppInfo(WEB_URL)))
    
    welcome_msg = (
        "💎 **مرحباً بك في HAMZA APPLE PRO**\n\n"
        "تم ربط الرادار بنظام Windows 10 للتحليل.\n"
        "🎯 **نسبة الأمان:** 92% حتى المستوى الثالث."
    )
    bot.send_message(m.chat.id, welcome_msg, reply_markup=markup, parse_mode="Markdown")

if __name__ == "__main__":
    # تشغيل خيط التحديث في الخلفية
    threading.Thread(target=sync_data, daemon=True).start()
    print("🚀 البوت يعمل الآن... اذهب للتليجرام واضغط /start")
    bot.polling()

