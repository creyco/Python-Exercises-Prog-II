from ejercicio_5 import *

# Solución de los puntos 6.a., 6.b, 6.c, ...
# No testeada
#
class TesterMonstersInc:             

    @staticmethod
    def main():     
        '''
        5.a
        '''          
        monstersinc = MonstersInc()

        # Agregar Monstruos        
        while True:            
            print("M O N S T R U O S")
            nom = input("Ingrese Nombre: ")
            esp = input("Ingrese Especie: ")
            print("------------------------------------")
            a = input("Confirma el Alta S/N: ").upper()
            if a == "S":                                
                mon = Monstruo(nom, esp)
                monstersinc.agregarMonstruo(mon)       
            else:
                break           

        # Agregar Humanos
        while True:
            print("H U M A N O S")
            nom = input("Ingrese Nombre: ")
            print("------------------------------------")
            a = input("Confirma el Alta S/N: ").upper()
            if a == "S":   
                hum = Humano(nom)            
                monstersinc.agregarHumano(hum)      
            else:
                break                                
# 5.b
        # Eliminar monstruo
        while True:            
            print("ELIMINAR - M O N S T R U O S")
            nom = input("Ingrese Nombre: ")            
            print("------------------------------------")
            a = input("Confirma el Alta S/N: ").upper()
            if a == "S":                                                
                monstersinc.eliminarMonstruo(nom)       
            else:
                break                   
# 6.a
        # Agregar Monstruo
        monstruo10 = Monstruo("cuco", "gargola")
        monstersinc.agregarMonstruo(monstruo10)
        
        # Agregar Humano
        mario = Humano("mario")
        monstersinc.agregarHumano(mario)
#6.b         
        monstruos = monstersinc.obtenerMonstruos()
        for mon in monstruos:            
            if mon.obtenerEnergia() > 0:
                print(f"Tiene {mon.energia} % DE ENERGIA")
#6.c
        humanos = monstersinc.obtenerHumanos()
        for hum in humanos:
            if hum.obtenerEstadoAsustado():
                print(f"{hum.nombre} esta asustado")
            else:
                print(f"{hum.nombre} NO esta asustado")
  

if __name__ == '__main__':
    testerMonstersInc = TesterMonstersInc()
    testerMonstersInc.main()

