# 3_b
# 1, 2, 3, 4,     5,     6,      7,       8,       9,       10,
# 1, 1, 2, 3,     5,     8,     13,      21,
# 1, 1+2 = 3, 3+2=5, 5+3=8, 8+5=13, 13+8=21, 21+13=34, 34+21=55
#
def fibonacci(numero):
   
    if numero < 2:
        return numero
    else:        
        print(numero, end=" ")
        return (fibonacci(numero - 1) + fibonacci(numero - 2))

n = 0
while True:
    n = int(input("Ingrese un Nº, [0=Fin]: "))
    if n == 0:
        print("Fin...")
        break
    else:
        print("\x1b[1;33m" +  f"Funcion Fibonacci({n})= " , "\x1b[0;m", end=" ")
        print("\x1b[1;34m" , fibonacci(n), "\x1b[0;m" )
