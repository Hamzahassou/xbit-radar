import time, json, random, subprocess, os

def update_system(val):
    try:
        # تحديث البيانات
        with open('data.json', 'w') as f:
            json.dump({"signal": val, "timestamp": time.time()}, f)
        
        # تنظيف أي تعارض بالقوة
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Auto Update"], capture_output=True)
        # استخدام force لضمان الرفع وتجاوز خطأ Rejected
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        return True
    except Exception as e:
        print(f"⚠️ خطأ: {e}")
        return False

def main():
    os.system('clear')
    print("💎 HAMZA AMKOM RADAR - POWER MODE 💎")
    while True:
        signal = round(random.uniform(1.15, 4.80), 2)
        if update_system(signal):
            print(f"✅ تم التحديث بنجاح: {signal}x")
        else:
            print("❌ فشل في المزامنة.. جارٍ إعادة المحاولة")
        time.sleep(20)

if __name__ == "__main__":
    main()

