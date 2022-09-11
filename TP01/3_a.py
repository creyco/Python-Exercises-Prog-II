#3_a

def suma(numero):
    sumatoria = 0
    i = 1
    while i <= numero:
        sumatoria += i
        i += 1        
    return sumatoria

def suma2(numero):
    sumatoria = 0
    for i in range(1, numero + 1):
        sumatoria += i
    return sumatoria 

def suma_rec(numero):
    if numero == 1:
        return 1
    else:
        return numero + suma_rec(numero - 1)

n=0
while True:
    print("\x1b[1;33m")    
    n = int(input("Ingrese un Nº, [0=Fin]: "))
    print("\x1b[0;m") 
       
    if n <= 0:
        print("Fin...")
        break
    else:    
        print("Funcion  / while     - /suma()   = ",suma(n))
        print("Funcion  / for       - /suma2()  = ",suma2(n))
        print("Funcion  / Recursiva - /sumarec()= ",suma_rec(n))
  