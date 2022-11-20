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

class TesterMonstersInc:
    def main(self):
        opc = 2
        if opc == 1:
            monstruo1 = Monstruo('bobi', 'lobizon')
            monstersInc = MonstersInc
            monstersInc.agregarMonstruo()
        else:
            # esta lista no hay q hacerla a mano
            humano1 = Humano('Cris')
            humano2 = Humano('Marga')
            humanos = [humano1, humano2]
            humano1.establecerEstadoAsustado(True)
            humano2.establecerEstadoAsustado(True)
            humanos_asustados = []            
            #print(humanos)
            for hum in humanos:
                if hum.obtenerEstadoAsustado():
                    humanos_asustados.append(hum)
                print(humanos_asustados)
                
if __name__=='__main__':
    testerMonstersInc = TesterMonstersInc()
    testerMonstersInc.main() 
