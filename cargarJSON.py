import json

# cargar el archivo JSON
with open('anotaciones/Anotaciones.json', 'r') as f:
    data = json.load(f)

imagenes = []
# Iterar sobre las imágenes
for imagen_id, imagen_data in data.items():
    #print(f'Imagen: {imagen_data["filename"]}')
    image_name = imagen_data["filename"]
    # Iterar sobre las regiones
    for region in imagen_data['regions']:
        if image_name == "00006.png":
            shape_attributes = region['shape_attributes']
            x1_img = shape_attributes["x"]
            y1_img = shape_attributes["y"]
            height = shape_attributes["height"]
            width = shape_attributes["width"]
            x2_img = x1_img + width
            y2_img = y1_img + height
            imagenes.append(x1_img)
            imagenes.append(x2_img)
            imagenes.append(y1_img)
            imagenes.append(y2_img)

print(imagenes)