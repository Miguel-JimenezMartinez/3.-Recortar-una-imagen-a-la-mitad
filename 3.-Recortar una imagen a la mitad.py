from PIL import Image
import cv2


img = cv2.imread('panda.jpg')      #Abro la imagen con Opencv

img2= Image.open("panda.jpg")      #Abro la imagen con Pillow

ancho = img.shape[1]               #Extraigo el ancho de la imagen, por eso es necesario abrir la imagen con Open cv

alto = img.shape[0]                #Extraigo el alto de la imagen, " " 

print(ancho)                       #solo verifico las dimensiones

print(alto)                        #solo verifico las dimensiones

region=(0,0,ancho,alto/2)          #delimito lo que voy a recortar con esta forma (corte izquierda+,corte arriba+, ancho-, alto-) 

imagen_recortada=img2.crop(region) #Recorte

imagen_recortada.show()            #muestro la foto recortada(opcional)

imagen_recortada.save("imagen_recortada.jpg") #Guardo la imagen en .jpg