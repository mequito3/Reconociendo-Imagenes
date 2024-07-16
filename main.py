import os
import time
from analyze_image import get_dominant_color
from send_telegram import send_telegram_message, send_telegram_photo

# Directorio donde están las imágenes
images_directory = "C:/Users/ameri/OneDrive/Escritorio/ICSP/Automa_Intento_3/Automa_Intento_3/capturas_finales"
message_box = (1200, 50, 1400, 100)
chat_id = "5106263363"  # Reemplaza con tu chat ID

while True:
    # Iterar sobre todas las imágenes en el directorio
    for filename in os.listdir(images_directory):
        if filename.endswith(".png") or filename.endswith(".jpg"):  # Asegúrate de incluir todas las extensiones de tus imágenes
            image_path = os.path.join(images_directory, filename)
            dominant_color = get_dominant_color(image_path, message_box)
            print(f"El color predominante en {filename} es: {dominant_color}")

            # Verificar si el color es verde
            if dominant_color == (0, 255, 0):  # Ajusta este valor según el tono de verde que consideres
                message = f"El archivo {filename} ha sido procesado correctamente."
                send_telegram_message(message, chat_id)
            else:
                message = f"El archivo {filename} tiene un color diferente al verde."
                send_telegram_photo(image_path, message, chat_id)
                print(f"El mensaje para {filename} no es verde, se enviará la imagen y el nombre del archivo.")
    
    # Esperar 2 minutos antes de la siguiente iteración
    time.sleep(10)
