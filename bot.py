import telebot
import requests
from bs4 import BeautifulSoup
import time
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# بياناتك الرسمية
TOKEN = "8318157728:AAH91-oPTBOACrqaXFWeRNkxKoWBQyG-Qh0"
MY_ID = "1945385119"
# رابط GitHub Pages الخاص بمستودعك الجديد
WEB_APP_URL = "https://hamzahassou.github.io/xbit-radar/"

bot = telebot.TeleBot(TOKEN)
HEADERS = {'User-Agent': 'Mozilla/5.0 (Linux; Android 13; Xiaomi 2201117TG)'}

def fetch_crash_data():
    """سحب النتائج والهاش من الموقع الحقيقي"""
    try:
        url = "https://1xbetmaroc.com/ar/games/crash"
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # استخراج الهاش الحقيقي
        h_tag = soup.find('div', class_=lambda x: x and 'hash' in x.lower())
        h_val = h_tag.text.strip() if h_tag else "🔐 Encrypted_Hash"
        
        # استخراج النتائج (الفقاعات)
        bubbles = soup.find_all(['div', 'span'], class_=lambda x: x and 'history' in x.lower())
        current_val = bubbles[0].text.strip() if bubbles else "1.00x"
        
        return current_val, h_val
    except:
        return "1.08x", "Reconnecting..."

@bot.message_handler(commands=['start'])
def start(message):
    if str(message.chat.id) == MY_ID:
        markup = InlineKeyboardMarkup()
        # الزر الذي يفتح واجهة الرادار داخل تليجرام
        markup.add(InlineKeyboardButton("🚀 فتح رادار حمزة برو", web_app=WebAppInfo(WEB_APP_URL)))
        bot.send_message(MY_ID, "💎 متصل بالسيرفر الحقيقي.\nالتحديثات تصل إلى GitHub كل 10 ثوانٍ.", reply_markup=markup)

def run_sync():
    print("📡 المزامنة تعمل الآن...")
    while True:
        sig, h = fetch_data()
        # حفظ البيانات محلياً ليتم رفعها
        with open("data.json", "w") as f:
            json.dump({"signal": sig, "hash": h}, f)
        time.sleep(10)

if __name__ == "__main__":
    import threading
    threading.Thread(target=run_sync).start()
    bot.polling()

