from monstruo import *
from humano import *

sullivan = Monstruo("James P. Sullivan", "leon")
mike = Monstruo("Mike Wazowski", "ciclope")
boo = Humano("boo")

print('''
\x1b[1;33m______________________________________________________________Ej.4
''')

print(sullivan.obtenerEnergia())
print(mike.obtenerEnergia())
print(boo.obtenerEstadoAsustado())
sullivan.asustar(boo)

print(sullivan.obtenerEnergia())
print(mike.obtenerEnergia())
print(boo.obtenerEstadoAsustado())

mike.divertir(boo)

print(sullivan.obtenerEnergia())
print(mike.obtenerEnergia())
print(boo.obtenerEstadoAsustado())



print('''
\x1b[1;33m______________________________________________________________FIN\x1b[0;m
''')

