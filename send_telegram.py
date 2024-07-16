import requests

def send_telegram_message(message, chat_id):
    bot_token = '7331837186:AAHPnnzoQadXS_cmvvXQz7-3uFiFK1eUFm0'  # Token de acceso proporcionado
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

def send_telegram_photo(photo_path, caption, chat_id):
    bot_token = '7331837186:AAHPnnzoQadXS_cmvvXQz7-3uFiFK1eUFm0'  # Token de acceso proporcionado
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    files = {'photo': open(photo_path, 'rb')}
    payload = {
        'chat_id': chat_id,
        'caption': caption
    }
    response = requests.post(url, files=files, data=payload)
    return response.json()

if __name__ == "__main__":
    message = "El archivo ha sido procesado correctamente."
    chat_id = "5106263363"  # Reemplaza con tu chat ID
    send_telegram_message(message, chat_id)
