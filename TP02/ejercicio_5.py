'''
5.a. Los comandos agregarMonstruo y agregarHumano deben agregar un objeto
de tipo Monstruo o un objeto de tipo Humano a las listas monstruos y
humanos de dicho objeto, respectivamente.
5.b. Los comandos eliminarMonstruo y eliminarHumano deben eliminar un objeto
de tipo Monstruo o un objeto de tipo Humano de las listas monstruos y
humanos de dicho objeto, respectivamente.'''

from monstruo import *
from humano import *

class MonstersInc:
    
    def __init__(self):
    
        self.monstruos = [] #lista de monstruos
        self.humanos = []   #lista de humanos

    # << COMANDOS >>
    def agregarMonstruo(self, mon: Monstruo):        
        self.monstruos.append(mon)
           
    def agregarHumano(self, hum: Humano):
        self.humanos.append(hum)       
        
    def eliminarMonstruo(self, mon: Monstruo):
        for m in self.monstruos:            
            if m == mon:
                self.monstruos.remove(m)
        
    def eliminarHumano(self, hum: Humano):
        for m in self.humanos:
            if m == hum:
                self.humanos.remove(m)        
        
    # << CONSULTAS >>
    def obtenerMonstruos(self):
        return self.monstruos

    def obtenerHumanos(self):
        return self.humanos

