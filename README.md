# Proyecto de Análisis de Imágenes

Este proyecto analiza imágenes en un directorio específico y envía notificaciones a un número de Telegram si se cumple una condición predeterminada. La condición en este caso es que el color predominante en una parte de la imagen sea verde. Si la condición se cumple, el programa enviará un mensaje con la captura de la imagen resaltando la parte donde se cumple la condición. Si el color predominante no es verde, también se enviará un mensaje con la captura de la imagen indicando que la condición no se ha cumplido.

## Configuración

### 1. Clonar el Repositorio

Clona el repositorio en tu máquina local:


git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
2. Crear y Activar un Entorno Virtual
Es recomendable crear un entorno virtual para manejar las dependencias del proyecto:

sh
Copiar código
python -m venv .venv
source .venv/bin/activate  # En Windows usa `.venv\Scripts\activate`
3. Instalar las Dependencias
Instala las dependencias necesarias usando el archivo requirements.txt:

sh
Copiar código
pip install -r requirements.txt
4. Configurar tus Credenciales y Rutas
Edita el archivo config.py para configurar tus credenciales de Telegram y la ruta de las imágenes:

python
Copiar código
# config.py

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = '7331837186:AAHPnnzoQadXS_cmvvXQz7-3uFiFK1eUFm0'
CHAT_ID = '5106263363'

# Uso
Ejecutar el Script Principal
Ejecuta el script principal para comenzar a analizar las imágenes y enviar notificaciones a Telegram:

Copiar código
### python main.py
