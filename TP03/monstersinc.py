from monstruo import *
from humano import *

class MonstersInc:

    def __init__(self):
        self.monstruos = []
        self.humanos = []

    def agregarMonstruo(self, mon: Monstruo):
        self.monstruos.append(mon)
        
    def agregarHumano(self, hum: Humano):
        self.humanos.append(hum)

    def eliminarMonstruo(self, mon: Monstruo):
        for monstruo in self.monstruos:
            if monstruo.equals(mon):
                self.monstruos.remove(monstruo)
                break
        
    def eliminarHumano(self, hum: Humano):
        for humano in self.humanos:
            if humano.equals(hum):
                self.humanos.remove(humano)
                break

    def obtenerMonstruos(self):
        return self.monstruos

    def obtenerHumanos(self):
        return self.humanos