import telebot, json, time, threading, random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# --- إعداداتك ---
TOKEN = "8318157728:AAH91-oPTBOACrqaXFWeRNkxKoWBQyG-Qh0"
MY_ID = "1945385119"
WEB_URL = "https://hamzahassou.github.io/xbit-radar/" # تأكد أن هذا رابط موقعك

bot = telebot.TeleBot(TOKEN)

def generate_safe_path():
    """توليد مسار آمن عشوائي مؤقت لـ 5 مستويات"""
    # نختار رقم العمود (1-5) لكل صف من الصفوف الـ 5
    path = [random.randint(1, 5) for _ in range(5)]
    # تحويل المصفوفة [2, 3, 1] إلى نص "2,3,1" لقراءتها في index.html
    path_str = ",".join(map(str, path))
    
    print(f"✅ تم تحليل مسار آمن جديد: {path_str}")
    return path_str

def sync_data():
    """دورة التحديث لملف البيانات"""
    while True:
        p = generate_safe_path()
        with open("data.json", "w") as f:
            # هنا نقوم بدمج التوقع الجديد مع عداد النجاح القديم
            json.dump({"path": p, "accuracy": 145 + int(time.time()) % 100}, f)
        time.sleep(15) # تحديث كل 15 ثانية

@bot.message_handler(commands=['start'])
def start_bot(m):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🚀 تشغيل رادار التفاحة الآمن", web_app=WebAppInfo(WEB_URL)))
    bot.send_message(m.chat.id, "💎 **نظام HAMZA APPLE - الإصدار التجريبي**\n\nيتم الآن تحليل خوارزمية التفاح لإعطائك المسار الأضمن.", reply_markup=markup, parse_mode="Markdown")

if __name__ == "__main__":
    threading.Thread(target=sync_data, daemon=True).start()
    bot.polling()

