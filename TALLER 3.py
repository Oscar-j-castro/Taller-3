from os import listdir
import os

Ruta = 'E:\TRIMESTRE VI\AUTOMATIZACION DE REDES\TALLER 3\Castro Roncancio'

contenido = os.listdir(Ruta)
archivos = []
for archivo in contenido:
     if archivo.startswith('P'):
      print("El nombre del archivo es:",archivo, "la extencion es:", archivo[12:16], "y la ruta es:", Ruta)
from os import listdir
import os

Ruta = 'E:\TRIMESTRE VI\AUTOMATIZACION DE REDES\TALLER 3\Castro Roncancio'

contenido = os.listdir(Ruta)
archivos = []
for archivo in contenido:
     if archivo.startswith('P'):
      print("El nombre del archivo es:",archivo, "la extencion es:", archivo[12:16], "y la ruta es:", Ruta)
      
     if archivo.startswith('S'):
      print("El nombre del archivo es:",archivo, "la extencion es:", archivo[9:14], "y la ruta es:", Ruta)

     if archivo.startswith('u'):
      print("El nombre del archivo es:",archivo, "la extencion es:", archivo[8:12], "y la ruta es:", Ruta)
else:
      print("no existen mas archivos")

with open("E:\TRIMESTRE VI\AUTOMATIZACION DE REDES\TALLER 3\Castro Roncancio/Usuarios.csv","r") as archivo:

     print("\nEl contenido del archivo usuarios.csv es:")
     for linea in archivo:
        print("\n",linea)

import csv
with open("E:\TRIMESTRE VI\AUTOMATIZACION DE REDES\TALLER 3\Castro Roncancio/Usuarios.csv") as file:
    reader = list(file)
    for row in reader:
        print (row)