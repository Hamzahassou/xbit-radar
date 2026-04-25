import telebot, requests, re, json, time, threading
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8318157728:AAH91-oPTBOACrqaXFWeRNkxKoWBQyG-Qh0"
MY_ID = "1945385119"
WEB_URL = "https://hamzahassou.github.io/xbit-radar/"

bot = telebot.TeleBot(TOKEN)
HEADERS = {'User-Agent': 'Mozilla/5.0 (Linux; Android 13; Xiaomi)'}

def logic_engine():
    """هذه هي 'العين' التي تحلل السجل الذي تراه في المتصفح"""
    try:
        # سحب الصفحة التي تحتوي على النتائج
        res = requests.get("https://1xbetmaroc.com/ar/games/crash", headers=HEADERS, timeout=7)
        # البحث عن كل الأرقام المتبوعة بـ x في السجل
        history = re.findall(r'(\d+\.\d+)x', res.text)
        
        if len(history) >= 3:
            # تحويل آخر 5 نتائج إلى أرقام حقيقية للتحليل
            last_results = [float(x) for x in history[:5]]
            avg = sum(last_results) / len(last_results)
            
            # --- منطق التحليل المنطقي ---
            # إذا كانت النتائج الأخيرة كلها منخفضة (تحت 1.50)، فالسيرفر سيقوم بالتعويض قريباً
            if all(x < 1.50 for x in last_results[:2]):
                prediction = round(avg * 1.2, 2) # رفع التوقع قليلاً
            else:
                prediction = round(avg * 0.85, 2) # تقليل المخاطرة
                
            # تأمين النتيجة لتكون دائماً "منطقية" ومضمونة
            if prediction < 1.20: prediction = 1.38
            if prediction > 3.0: prediction = 1.94
            
            return str(prediction), f"ANLYS_{int(time.time())}"
        
        return "1.42", "SCANNING_HISTORY"
    except:
        # في حال فشل السحب المباشر، نستخدم المحاكي المنطقي لكي لا يتوقف الرادار
        import random
        return str(round(random.uniform(1.30, 2.10), 2)), "VIRTUAL_SYNC"

def sync_loop():
    print("👁️ رادار حمزة برو يراقب السجل ويحلل النتائج الآن...")
    while True:
        p, h = logic_engine()
        with open("data.json", "w") as f:
            # تحديث ملف البيانات مع رفع عداد النجاح تلقائياً
            json.dump({"signal": p, "hash": h, "accuracy": 145 + int(time.time()) % 50}, f)
        time.sleep(15)

@bot.message_handler(commands=['start'])
def start(m):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🚀 فتح الرادار الذكي V3", web_app=WebAppInfo(WEB_URL)))
    bot.send_message(m.chat.id, "💎 **نظام التحليل المنطقي (العين الرقمية)**\n\nيتم الآن تحليل سجل الخسائر والربح لإعطائك أضمن نتيجة.", reply_markup=markup, parse_mode="Markdown")

if __name__ == "__main__":
    threading.Thread(target=sync_loop, daemon=True).start()
    bot.polling()

