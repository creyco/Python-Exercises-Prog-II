#import re

'''
LOGICA PROPOSICIONAL O LOGICA VALOR CERO

i. (a or b) or (b and c)
ii. b and c or False
iii. a and b or c or (b and a)
iv. a == False or b == False

      (a or b) es true 
      (b and c) es false, 
      true or false es true
# True / False = 2
# a, b, c = 3
# 2 ^ 3 = 8
# https://www.dcode.fr/boolean-expressions-calculator
'''
# DEFINICION DE FUNCIONES

def fval( n ):    # True or False
    if n == "0":
        return False
    else:
        return True

def procesar_sentencia(a, b ,c ):
    sentencia1 = (a and b) or (b and a)
    sentencia2 = a and b
    print( sentencia1, sentencia2, end=" ")
    print( sentencia1 ==  sentencia2 )
   
def simplificada1(a, b ,c ):
   sentencia1 = (a or b) or (b and c)       
   sentencia2 = a or b  
   print( sentencia1, sentencia2, end=" --> ")
   print( sentencia1 == sentencia2 )
    
def simplificada2(a, b ,c ):
   sentencia1 = b and c or False
   sentencia2 = b and c
   print( sentencia1, sentencia2, end=" --> ")
   print( sentencia1 == sentencia2 )

def simplificada3(a, b ,c ):
   sentencia1 = a and b or c or (b and a)
   sentencia2 = (a and b ) or c
   print( sentencia1, sentencia2, end=" --> ")
   print( sentencia1 == sentencia2 )

def simplificada4(a, b ,c ):
   sentencia1 = a == True or b == False
   sentencia2 = a or not b
   print( sentencia1, sentencia2, end=" --> ")
   print( sentencia1 == sentencia2 )

########################################################################### tabla de verdad
tabla_de_verdad = lambda z: [*map(lambda x:[*map( fval, bin(x)[2:].zfill(n))] , range(2**n))]
n=3
tv = tabla_de_verdad(n)    # Tabla de verdad

print("\x1b[1;33mPROCESAR_SENTECIA \x1b[0;m")
for i in range(len(tv)):
    a,b,c = tv[i][0] , tv[i][1], tv[i][2]
    procesar_sentencia( a, b, c) 

# EJECUTA LLAMADA A simplificadas

for i in range(1,5):    
    print("\x1b[1;33mSentencia nº: " , str(i) , "\x1b[0;m")
    a,b,c = tv[i][0] , tv[i][1], tv[i][2]    
    for j in range(len(tv)):
        match i:
            case 1:                         
                    simplificada1( a, b, c)
            case 2:                            
                    simplificada2( a, b, c)
            case 3:                                
                    simplificada3( a, b, c)                
            case 4:            
                    simplificada4( a, b, c)        



'''
000
001
010
011
100
101
110
111
'''