# a. Se elimine la sentencia if / else de la función anio_bisiesto.
# b. Las múltiples sentencias if la función dia_mes utilicen la cláusula in en lugar de varias cláusulas or.
# c. Se agregue una sentencia que valide que la edad ingresada por el usuario es numérica.
# d. Se agregue una función que encapsule el cálculo del equivalente de la edad en 
#    días y que tome como parámetros las variables hora_local, anio_comienzo y anio_fin.
# e. Todas las funciones sean transportadas a un archivo auxiliar de funciones 
#    llamado funciones.py, y este sea importado desde el programa principal.

import time
from calendar import isleap

# DEFINIR VARIABLES
hora_local = time.localtime(time.time())
anios = 0
anio_comienzo = 0
anio_fin = 0
meses = 0
dias = 0

# calcular si es un año bisiesto
def anio_bisiesto(anio): 
    return isleap(anio)

# calcular el numero de dias de cada mes
def calcular_dias_mes(mes, anio_bisiesto):
    dias_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if anio_bisiesto:
        dias_mes[2] = 29
    return (dias_mes[mes])      

# calcular los dias
 

###################################################
def calc_edad(nombre,edad):
    # seteo inicial de variables
    hora_local = time.localtime(time.time())
    anios = int(edad)
    anio_comienzo = int(hora_local.tm_year) - anios
    anio_fin = anio_comienzo + anios
    meses = anios * 12 + hora_local.tm_mon
    dias = 0
    ############
    # llamar funciones y retornar
    for a in range(anio_comienzo, anio_fin):
        if (anio_bisiesto(a)): 
            dias = dias + 366
        else: 
            dias = dias + 365
    
    # agregar los días transcurridos en este año
    for m in range(1, hora_local.tm_mon):
        dias = dias + calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))

    # agregar los días transcurridos en este mes
    dias = dias + hora_local.tm_mday

    # imprimir la edad del usuario y volver
    ###########################################
    print("\x1b[1;33m")
    print("La edad de %s es %d años o " % (nombre, anios), end="")
    print("%d meses o %d días" % (meses, dias))
    print("\x1b[0;m")
#<eof>