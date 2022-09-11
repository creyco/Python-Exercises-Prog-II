# e. Escribir un procedimiento numeros_par_impar(entrada) que, dada
# una lista de números, eleve cada elemento impar en ella al cuadrado 
# y los mueva a otra lista e imprima ambas. 
# La lista de números la ingresa el usuario en forma de números
# separados por coma. 
# Suponiendo que el usuario ingresa la siguiente lista:1,2,3,4,5,6,7,8,9
# Entonces, la salida del programa debería ser:
# 2,4,6,8
# 1,9,25,49,81

pares=[]
impares=[]

def numeros_par_impar(entrada):
    for i in entrada:        
        
        if i % 2 == 0:           
            pares.append(i)    
        else:            
            impares.append(i**2)
            
####################################################
# ACCESO MANUAL COMENTADO SE USA UNA LISTA CARGADA
#---------------------------------------------------
# num = input("Ingrese secuencia de numeros separados por coma: ")
# lisnum = num.split(sep=",")
# for m in range(len(lisnum)):
#     lisnum[m] = int(lisnum[m])
# print(lisnum)
# input("aki...")

lisnum =  [1,2,3,4,5,6,7,8,9]
numeros_par_impar(lisnum)

print("\x1b[1;33m")
print(lisnum,"\x1b[0;m") 
print("Pares: ", pares)
print("Impares" , impares)    


