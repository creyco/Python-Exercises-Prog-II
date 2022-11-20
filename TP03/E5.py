from humano import *
from puerta import *
from monstruo3 import *

#-----------------------------------------------MonstersInc-------#
class MonstersInc:
    def __init__(self):
        self.monstruos = []
        #{'asustador': Monstruo , 'asistente': Monstruo}
        self.puertas = []

    def agregarMonstruo(self, mon: Monstruo):
        if mon["asustador"].tipo == "asustador" and mon["asistente"].tipo == "asistente":
            self.monstruos.append(mon)        

    def agregarPuerta(self, pue: Puerta):
        self.puertas.append(pue)
  
    def eliminarMonstruo(self, mon: Monstruo):
        for monstruo in self.monstruos:
           print(monstruo)
           for k,v in monstruo.items():
                if v.equals(mon):
                    monstruo.pop(k)
                    print('\neliminando monstruo...')
                    break

    def eliminarPuerta(self, pue: Puerta):
        for p in self.puertas:
            if p.equals(pue):
                self.puertas.remove(p)
                break

    '''<< CONSULTAS >>''' # ¿¿¿---------- ???
    def obtenerMonstruos(self):
        return self.monstruos

    def obtenerPuertas(self):        
        return self.puertas

#----------------------------------------------TesterMonstersInc------        
class TesterMonstersInc:
    
    def main(self):
        m_Inc = MonstersInc()

        # 5.a Agregar y eliminar monstruos, humanos y puertas.           
                      
        sully = Monstruo("Sullivan", "leon", "asustador")
        mike = Monstruo ("Mike", "ciclope", "asistente")               

        m_Inc.agregarMonstruo({'asustador': sully, 'asistente': mike})
        
        sully.establecerPareja(mike)

        boo = Humano("Boo")
        Too = Humano("Too")
        
        p1 = Puerta(1, boo) # no requiere pasar montruo como parametro
        p2 = Puerta(2, Too)
        m_Inc.agregarPuerta(p1)      

        mike.activarPuerta(p1)
        print('Puerta activa: ' , p1.estadoActiva)
        
        # 5.b 
        print(sully.obtenerEnergia())
        sully.asustar(p1)
        print(sully.obtenerEnergia())
 
        boo.obtenerEstadoAsustado() # no pide parametro este metodo
        # 5.c 
        sully.divertir(boo) # aca el parametro debe ser de tipo humano
        sully.obtenerEnergia()
        print('Power: ',sully.energia)
               
        print( 'boo Asustado?: ', boo.obtenerEstadoAsustado() )

        sully.dormir() # no pide parametro este metodo
        sully.obtenerEnergia()
        sully.despertar() # no pide parametro este metodo
        mike.dormir()


if __name__=='__main__':
    testerMonstersInc = TesterMonstersInc()
    testerMonstersInc.main() 
