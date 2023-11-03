import cv2
import numpy as np

# Seleccionamos la imagen
imagen = cv2.imread('informe-fotos/tuna1.jpg')
cv2.imshow('imagen original',imagen)
#redimensionar imagen para un mejor manejo 
imagen_redimensionado = cv2.resize(imagen, (600, 400), interpolation=cv2.INTER_AREA)



# Definición de rango de colores
#gris_low = np.array([0, 0, 128], dtype=np.uint8)
#gris_high = np.array([179, 64, 192], dtype=np.uint8)

# rangos de colores en hsv
red_low = np.array([20, 100, 100], dtype=np.uint8)
red_high = np.array([50, 200, 255], dtype=np.uint8)






# Aplicamos una máscara para identificar los objetos de interés por color
imagen_hsv = cv2.cvtColor(imagen_redimensionado, cv2.COLOR_BGR2HSV)
# mostrar la imagen HSV
cv2.imshow('imagen HSV ', imagen_hsv)

mask = cv2.inRange(imagen_hsv, red_low, red_high)
cv2.imshow('mask', mask)


# Encontramos los contornos de la imagen hsv
contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_contornos = cv2.drawContours(mask,contornos,-1,(0,0,255),1)
cv2.imshow('Imagen con contornos',img_contornos)

#Dibujar un rectángulo para cada objeto identificado
cont = 0
for contorno in contornos:
    area = cv2.contourArea(contorno)
    if area > 100 : 
        cont = cont + 1
        # Ajustar el valor mínimo y maximos de los pixeles permitidos
        x, y, w, h = cv2.boundingRect(contorno)
        ajust =5
        x-= ajust
        y-= ajust
        w+= 2*ajust
        h+= 2*ajust
        cv2.rectangle(imagen_redimensionado, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.putText(imagen_redimensionado,str(cont),(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255),1)

# mostrar los insectos a identficar a las mosca blanca
cv2.imshow("Objetos identificados", imagen_redimensionado)

cv2.waitKey(0)
cv2.destroyAllWindows()
