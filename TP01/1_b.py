# b. Escribir una función de nombre es_abc(palabra) la cual retorne
# True siempre y cuando las letras que componen dicha palabra estén
# en orden alfabético, y False en caso contrario.

def es_abc(palabra):
    palabra2 = "".join(sorted(palabra))

    if palabra == palabra2:
        return True
    else:
        return False

palabras = [
    "lo",
    "acción",
    "vocabulario",
    "gil",
    "jogging",
    "hijo",
    "ajo",
    "puño",
    "tu",
    "amor"]

for p in palabras:
    print("\x1b[1;33m {:>15} \x1b[0;m".format(p) , end=" ") 
    
    if es_abc(p):
        print(True)
    else:    
        print("      " , False)
