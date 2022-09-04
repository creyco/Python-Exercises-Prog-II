# n = [True,False] >>= \b -> map (b :) (truths (n - 1))
# TV = lambda z: [*map(lambda x:[ *map(int,bin(x)[2:].zfill(n))] , range(2**n))]

# sentencia2 = a or b  or ( b and c )
   # X+(X⋅Y)=X with X = BX=B and Y = CY=C:
   # A+(B+(B⋅C))=A+(B)
   # A+B+(B⋅C)=A+B


n = 3
x = 0

def fval( n ):    
    if n == "0":
        return False
    else:
        return True

def procesar_sentencia_simplificada1(a, b ,c ):
   sentencia1 = (a or b) or (b and c)       
   sentencia2 = a or b
   print(a,b,c, end="|")   
   print( sentencia1, sentencia2, end=" --> ")
   print( sentencia1 == sentencia2 )
    
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
   print(a,b,c, end="|")   
   print( sentencia1, sentencia2, end=" --> ")
   print( sentencia1 == sentencia2 )




TV = lambda z: [*map(lambda x:[*map( fval, bin(x)[2:].zfill(n))] , range(2**n))]
tv = TV(n)

for i in range(len(tv)):
    a,b,c = tv[i][0] , tv[i][1], tv[i][2]
    procesar_sentencia_simplificada1( a, b, c) 


print ("  I.")
for i in range(len(tv)):
    a,b,c = tv[i][0] , tv[i][1], tv[i][2]    
    simplificada1( a, b, c)    

print (" II.")
for i in range(len(tv)):
    a,b,c = tv[i][0] , tv[i][1], tv[i][2]    
    simplificada2( a, b, c)    

print ("III.")
for i in range(len(tv)):
    a,b,c = tv[i][0] , tv[i][1], tv[i][2]    
    simplificada3( a, b, c)    
    

for i in range(len(tv)):
    a,b,c = tv[i][0] , tv[i][1], tv[i][2]    
    simplificada4( a, b, c)    

    
for i in range(1,4):
    a,b,c = tv[i][0] , tv[i][1], tv[i][2]    
    for j in range(len(tv)):
        match i:
            case 1:          
                    print("   I.")  
                    simplificada1( a, b, c)
            case 2:        
                    print("  II.")    
                    simplificada2( a, b, c)
            case 3:            
                    print("III.")
                    simplificada3( a, b, c)                
            case 4:            
                    print(" IV.")
                    simplificada2( a, b, c)        

