# from telegram import Bot
# import random

# def send_otp_to_telegram(chat_id, token):
#     # تولید یک OTP تصادفی
#     otp = random.randint(100000, 999999)
    
#     # ایجاد یک شیء Bot
#     bot = Bot(token=token)
    
#     # ارسال OTP به کاربر
#     message = f"کد OTP شما: {otp}"
#     bot.send_message(chat_id=chat_id, text=message)
    
#     return otp  # برگرداندن OTP برای استفاده‌های بعدی

# # توکن بوت تلگرام
# TOKEN = '7886898703:AAHQux9NpZv7ON5sNTW09eL0qtD-lAoPR1M'
# # شناسه چت کاربر (مثلاً می‌توانید از @user_id استفاده کنید)
# CHAT_ID = '@hassan_pv'

# otp = send_otp_to_telegram(CHAT_ID, TOKEN)
# print(f"OTP send {otp}")
import asyncio
from telegram import Bot
import random

async def send_otp_to_telegram(chat_id, token):
    # تولید یک OTP تصادفی
    otp = random.randint(100000, 999999)
    
    # ایجاد یک شیء Bot
    bot = Bot(token=token)
    
    # ارسال OTP به کاربر
    message = f"کد OTP شما: {otp}"
    await bot.send_message(chat_id=chat_id, text=message)
    
    return otp  # برگرداندن OTP برای استفاده‌های بعدی

# تابع اصلی برای فراخوانی تابع غیرهمزمان
def main():
    # توکن بوت تلگرام
    TOKEN = '7886898703:AAHQux9NpZv7ON5sNTW09eL0qtD-lAoPR1M'
    # شناسه چت کاربر
    CHAT_ID = 'Hassan_pv'
    
    # اجرای تابع غیرهمزمان
    otp = asyncio.run(send_otp_to_telegram(CHAT_ID, TOKEN))
    print(f"OTP ارسال شد: {otp}")

if __name__ == "__main__":
    main()
