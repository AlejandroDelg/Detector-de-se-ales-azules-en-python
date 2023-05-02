import cv2
import matplotlib.pyplot as plt
import numpy as np

# Cargar la imagen
img = cv2.imread('imgs/00004.png')

# Convertir la imagen a gris para que el azul se detecte mejor
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mser = cv2.MSER_create(1, 1500, 8000)

# Detectar regiones
(regions,_) = mser.detectRegions(gray)

# Crear una lista vacía para almacenar los sub-paneles detectados
subpanels = []

puntuacion = []
# Iterar sobre las regiones detectadas
for region in regions:
    # Obtener las coordenadas del rectángulo que rodea a la región
    x, y, w, h = cv2.boundingRect(region)
    # Calcular la relación de aspecto del rectángulo
    aspect_ratio = w / h
    x-= 30
    y-=30
    w += 30
    h += 30
    # Si la relación de aspecto es razonable, añadir la región a la lista de sub-paneles
    if  aspect_ratio <= 2.5 and  0.5 <= aspect_ratio:
        # Asegurarse de que los límites del rectángulo no sobrepasen los límites de la imagen
        x, y, w, h = max(x, 0), max(y, 0), min(w, img.shape[1] - x), min(h, img.shape[0] - y)
        # Recortar la ventana detectada y redimensionarla
        window = img[y:y+h, x:x+w]
        window_resized = cv2.resize(window, (200, 200))

        subpanel_hsv = cv2.cvtColor(window_resized, cv2.COLOR_BGR2HSV)

        mascara_hsv = np.zeros((200,200))

        for i in range(200):
            for j in range(200):
                pixel = subpanel_hsv[i,j]
                if (pixel[0] >=0 and pixel[0] <= 150 and pixel[1] >= 100  and pixel[2] >= 100):
                    mascara_hsv[i,j] = 1
        # Definir la máscara ideal de color azul saturado
        mascara_ideal = np.ones((200, 200))

        # Correlar M (multiplicar los elementos de la mascara ideal (todo unos) con nuestra mascara azul)
        correlation = np.sum(mascara_hsv * mascara_ideal)
        
        # Establecer un umbral y añadir el sub-panel a la lista de sub-paneles si la correlación es mayor que el umbral
        threshold = 0.6
        if correlation >= threshold:
            puntuacion.append(correlation / np.sum(mascara_ideal))
            subpanels.append(window_resized)


# Mostrar los sub-paneles detectados
for i in range (len(subpanels)):
    if(puntuacion[i] > .3):
        print("puntuacion:", puntuacion[i])
        plt.imshow(subpanels[i])
        
        plt.show()
        plt.plot()