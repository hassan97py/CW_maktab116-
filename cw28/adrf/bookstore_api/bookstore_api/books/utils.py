import requests
from django.conf import settings

def send_otp_to_telegram(chat_id, otp):
    bot_token = settings.TELEGRAM_BOT_TOKEN
    message = f'Your OTP is: {otp}'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error sending OTP to Telegram: {e}")
