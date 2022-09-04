# a_e. Todas las funciones sean transportadas a un archivo auxiliar de funciones 
#    llamado funciones.py, y este sea importado desde el programa principal.

import time
from funciones import *
from calendar import isleap
   

while True:
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad o escriba [fin]:" )  

    try:
        edad=int(edad)
    except ValueError:
        if edad.lower() == "fin":
            break
    if edad <= 0: 
        print("Ingrese un nº > 0 ")    
        continue
    else:
        calc_edad(nombre , edad)

