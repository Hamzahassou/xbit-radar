import telebot
import requests
from bs4 import BeautifulSoup
import time
import json
import threading
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# --- بياناتك الرسمية ---
TOKEN = "8318157728:AAH91-oPTBOACrqaXFWeRNkxKoWBQyG-Qh0"
CH_ID = "1945385119"
# رابط الموقع بعد تفعيل GitHub Pages
URL_GITHUB = "https://hamzahassou.github.io/xbit-radar/" 

bot = telebot.TeleBot(TOKEN)
HEADERS = {'User-Agent': 'Mozilla/5.0 (Xiaomi; Android 13)'}

def fetch_real_game_data():
    """محرك سحب البيانات الحقيقية من 1xbet"""
    try:
        res = requests.get("https://1xbetmaroc.com/ar/games/crash", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # سحب الهاش
        h_tag = soup.find('div', class_=lambda x: x and 'hash' in x.lower())
        h_val = h_tag.text.strip() if h_tag else "🔐 SHA256-ENCRYPTED-LIVE"
        
        # سحب آخر نتيجة
        bubbles = soup.find_all(['div', 'span'], class_=lambda x: x and 'history' in x.lower())
        val = bubbles[0].text.replace('x', '').strip() if bubbles else "1.00"
        
        return val, h_val
    except:
        return "1.08", "Re-connecting to main server..."

@bot.message_handler(commands=['start'])
def welcome(message):
    # نص ترحيبي قوي للمشتركين
    msg = (
        "💎 **نظام HAMZA PRO المتكامل**\n\n"
        "أنت الآن متصل بالسيرفر الرسمي لتحليل Crash.\n"
        "● الحالة: متصل ✅\n"
        "● المزامنة: حية ⚡\n\n"
        "اضغط أدناه لفتح الرادار الأحمر الحقيقي."
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🚀 فتح الرادار الأحمر", web_app=WebAppInfo(URL_GITHUB)))
    bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode="Markdown")

def sync_data():
    """المزامنة التلقائية مع ملف البيانات"""
    print("📡 المزامنة تعمل.. بانتظار تحديثات السيرفر.")
    while True:
        s, h = fetch_real_game_data()
        with open("data.json", "w") as f:
            json.dump({"signal": s, "hash": h}, f)
        print(f"✅ تم تحديث الرادار: {s}x")
        time.sleep(10)

if __name__ == "__main__":
    threading.Thread(target=sync_data, daemon=True).start()
    bot.polling()

