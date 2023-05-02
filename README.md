# Detector de señales azules en python

Detector de señales en python, utlizando las librerias de openCv, matplotlib y numpy.

## Funcionamiento

El programa busca imagenes en la carpeta `imgs`, y mediante un `MSER` (Maximally stable extremal regions) detecta determinadas regiones con colores estables, en base a los argumentos que 
le pasemos a la hora de crear el MSER en la funcion `MSER_create`.

Itera sobre las regiones que ha detectado, las convierte a un tamaño estandar para que todas las imagenes finales tengan la misma cantidad de pixeles (`window_resized = cv2.resize(window, (200, 200))`)
 y por cada region, aplica el modelo de HSV. El modelo de HSV consiste en que mediante dos mascaras(una mascara ideal y una mascara con la cantidad de pixeles azules que tiene la foto)
 correlaciona ambas mascaras para detectar cuantos de los pixeles son azules, y en base a un `threshold` para determinar cuantos pixeles azules tiene, se acepta la imagen o no.
 
 Finalmente, se itera sobre todos los subpaneles y se imprime tanto la imagen como la puntuacion que ha obtenido
