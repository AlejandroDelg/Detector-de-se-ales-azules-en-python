import json

# cargar el archivo JSON
with open('anotaciones/Anotaciones.json', 'r') as f:
    data = json.load(f)


# Iterar sobre las imágenes
for imagen_id, imagen_data in data.items():
    print(f'Imagen: {imagen_data["filename"]}')

    # Iterar sobre las regiones
    for region in imagen_data['regions']:
        shape_attributes = region['shape_attributes']
        print(f'Posición x: {shape_attributes["x"]}')
        print(f'Posición y: {shape_attributes["y"]}')
        print(f'height : {shape_attributes["height"]}')
        print(f'width : {shape_attributes["width"]}')