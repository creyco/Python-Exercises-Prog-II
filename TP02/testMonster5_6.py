from ejercicio_5 import *

# Solución de los puntos 5.a, 5.b, 6.a., 6.b, 6.c, ...
class TesterMonstersInc:             

    @staticmethod
    def main():       
# 5.a   
        monstersinc = MonstersInc()
        # Agregar Monstruos        
        
        monstruo1 = Monstruo("Sullivan", "leon")
        monstersinc.agregarMonstruo(monstruo1)       
        monstruo2 = Monstruo("Mike", "ciclope")
        monstersinc.agregarMonstruo(monstruo2)
        
        # Agregar Humanos
        juan = Humano("juan")
        monstersinc.agregarHumano(juan)      
        marta = Humano("marta")
        monstersinc.agregarHumano(marta)

# 5.b
        # Eliminar monstruo
        monstersinc.eliminarMonstruo(monstruo1)
        monstersinc.eliminarMonstruo(monstruo2)

# 6.a
        # Agregar Monstruo
        monstruo10 = Monstruo("cuco", "gargola")
        monstersinc.agregarMonstruo(monstruo10)
        
        # Agregar Humano
        mario = Humano("mario")
        monstersinc.agregarHumano(mario)
#6.b         
        monstruos = monstersinc.obtenerMonstruos()
        print(monstruos)
        ener=input("Ingrese que Nivel de Energia Filtrar %: ")
        if ener.isdigit():
            ener = int(ener)
            if ener < 0 or ener > 100:
                print("error")
            else:    
                MonstruosPowerMas = []
                MonstruosPowerMin = []                
                for mon in monstruos:            
                    if mon.obtenerEnergia() < ener :
                        MonstruosPowerMin.append(mon)
                    else:
                        MonstruosPowerMas.append(mon)

        for x,y in zip(MonstruosPowerMin, MonstruosPowerMas):
            print (x,y)
        
        #print(f"Tiene {mon.energia} % DE ENERGIA")

#6.c
        humanos = monstersinc.obtenerHumanos()

        asustados = input("Ingrese 1=Asustados 0=N0 asustados: ")
        susto = True if asustados == 1 else False
        
        for hum in humanos:
            print(f"{hum.nombre} ", end=" ")
            if hum.obtenerEstadoAsustado() == susto:
                print("esta asustado")
            else:
                print("NO esta asustado")
  

if __name__ == '__main__':
    testerMonstersInc = TesterMonstersInc()
    testerMonstersInc.main()

