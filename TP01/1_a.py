# a. Escribir una función de nombre:
# palabra_no_tiene_letras(palabra, letras_prohibidas)
# la cual retorne True si es que los caracteres que componen
# una palabra no se encuentran en una lista de caracteres prohibidos.'

#from timeit import timeit
import re

def palabra_no_tiene_letras(palabra, letras_prohibidas):
      
    if not any([ True if c in letras_prohibidas else False for c in palabra]) :    
       return True
    return False

def palabra_no_tiene_letras2(palabra, letras_prohibidas):

    for letra in palabra:
        if letra in letras_prohibidas:
            return False
    return True



prohibidas = ["^", "&", "!", "%", "~"]

palabras = [
    "apéndice",
    "l^sta",
    "espec^fica",
    "palabras",
    "ni~o",
    "b%sicas",
    "vocabulario",
    "general",
    "Sustantivos",
    "Gente",
    "humanidad",
    "humano",
    "persona",
    "gente"]


# print(type(palabras))
# print(type(prohibidas))

print("".join(prohibidas))


for p in palabras:
    print("\x1b[1;33m {:>15} \x1b[0;m".format(p) , end=" ") 
    if palabra_no_tiene_letras(p, prohibidas):
        print(True)
    else:
        print("    ",False)

input("aaki otro Metodo...")
for p in palabras:    
    print("\x1b[1;33m {:>15} \x1b[0;m".format(p) , end=" ") 
    if palabra_no_tiene_letras2(p,prohibidas):
       print(True)
    else:
        print("    ",False)

