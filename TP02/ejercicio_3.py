from ejercicio_1 import *
from ejercicio_2 import *

"""
c. Si se instanciase un segundo objeto como el siguiente:
sullivan2 = Monstruo("James P. Sullivan", "leon")

AL usar espacios distintos de memoria, indica que se trata de 2 objetos distintos de una misma clase
Se almacena en memoria el estado del objeto

ii. ¿Son objetos equivalentes? Explique que significa que dos objetos lo
sean.

iii. ¿Los objetos ligados a sullivan y sullivan2 comparten la misma posición
de memoria?
"""

sullivan = Monstruo("James P. Sullivan", "leon")
mike = Monstruo("Mike Wazowski", "ciclope")
boo = Humano("Boo")

# 3_a)
print("\x1b[1;33m3_A")
print(
    f"Nombre: {sullivan.obtenerNombre()} |Especie: {sullivan.especie} |maxEnergia: {sullivan.energia}")
print(
    f"Nombre: {mike.obtenerNombre()} |Especie: {mike.especie} |maxEnergia: {mike.energia}")
print(
    f"Nombre: {boo.obtenerNombre()} |Especie: {boo.especie} |Asustado?: {boo.estadoAsustado} \x1b[0;m")


# ciclo preguntando
while True:
    print("Energía: ", sullivan.energia, end=" ")
    if sullivan.energia == 0:
        break

    asusta = input("Asustar S|N: ").capitalize().strip()
    asusta = True if asusta == "S" else False

    if asusta and sullivan.energia > 0:
        sullivan.asustar(10)
        
    else:
        break
#
# ciclo automatico !asustando¡ con for
#
print("\x1b[1;33m")
print(
    f"Nombre: {mike.nombre} |Especie: {mike.especie}  |maxEnergia: {sullivan.energia} \x1b[0;m")
print("Energia \x1b[0;m")
for i in range(0, 10):
    mike.asustar(10)
    print(mike.energia, end=" ")
print()

# 3_b. ¿Cuál es el valor del atributo de clase especie asociado al objeto referenciado
print("\x1b[1;33m3_b. ¿Cuál es el valor del atributo de clase especie asociado al objeto referenciado")
print(boo.obtenerNombre(), end=" ")
if not boo.obtenerEstadoAsustado():
    print(boo.especie)
    # por el identificador boo?
    print("Boo: No Asustado \x1b[0;m")

boo.establecerEstadoAsustado()
if boo.obtenerEstadoAsustado():
    #    print(boo.especie)
    print("Boo: Asustado")

# 3_c_i.
print(
''' 
\x1b[1;33m3_c_i    
i. ¿Los identificadores sullivan y sullivan2 hacen referencia al mismo
objeto? ¿o son objetos idénticos completamente distintos?\x1b[0;m
                                                 RESPUESTA << SON DISTINTOS >>
''')

# 3_c    # métodos mágicos
print(
''' 
\x1b[1;33m3_c_ii ¿Son objetos equivalentes? Explique que significa que dos objetos lo sean.
sullivan Y sullivan2 
==> se instancian de una misma clase ==> son objetos distintos 
==> las referencias apuntan a espacios de memoria diferentes  \x1b[0;m                            
==> ¿tienen los mismo datos? SI <<son equivalentes>> 
                             NO <<son no equivalentes>>
''')
#
# tester
#
#sullivan = Monstruo("James P. Sullivan", "leon")
sullivan2 = Monstruo("James P. Sullivan", "leon")

print("\x1b[2;31;43m")
print(f"Nombre: {sullivan.nombre}  |Especie {sullivan.especie} |Energia: {sullivan.energia}  |id: {id(sullivan)}" )
print(f"Nombre: {sullivan2.nombre}  |Especie {sullivan2.especie} |Energia: {sullivan2.energia}  |id: {id(sullivan2)}" , "\x1b[0;0m")

if id(sullivan) != id(sullivan2):
    print("OBJETOS DISTINTOS", end=" ")
else:
    print("OBJETOS IGUALES" , end=" ")

equiv = sullivan == sullivan2       # OPERADOR DE IGUALDAD - ACTUA X VALOR, compara el estado interno
if equiv:
    print('Equivalentes')
else:
    print('No Equivalentes')
print("\x1b[0;m")
