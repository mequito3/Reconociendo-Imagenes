from PIL import Image

def get_dominant_color(image_path, box):
    image = Image.open(image_path)
    region = image.crop(box)
    colors = region.getcolors(region.size[0] * region.size[1])
    return max(colors, key=lambda item: item[0])[1]

if __name__ == "__main__":
    image_path = "C:/Users/ameri/OneDrive/Escritorio/ICSP/Automa_Intento_3/Automa_Intento_3/capturas_finales/image.png"
    message_box = (1200, 50, 1400, 100)  # Ajustar según la posición real del mensaje
    dominant_color = get_dominant_color(image_path, message_box)
    print(f"El color predominante es: {dominant_color}")
