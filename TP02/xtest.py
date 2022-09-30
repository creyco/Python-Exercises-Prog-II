from ejercicio_5 import *

# Solución de los puntos 6.a., 6.b, 6.c, ...
# No testeada
#
class TesterMonstersInc:             

    @staticmethod
    def main():       
# 5.a
        monstersinc = MonstersInc()
        
        # Agregar Monstruos        
        print("*****************")
        print("M O N S T R U O S")
        print("------------------------------------")
        nomMon = ["mike", "sullivan", "yeti", "randall"]
        espMon = ["monstruo1","ciclope","yeti","monstruo2"]
        
        for x,y in zip(nomMon, espMon):
            #print("Nombre: ", x, " Especie: ", y )         
            monstersinc.agregarMonstruo(Monstruo(x, y))           
        monstruos = monstersinc.obtenerMonstruos()
        print(monstruos)
        # for m in monstruos:
        #     print(m)
        
        print("**************")

        #Agregar Humanos
        print("H U M A N O S")
        print("------------------------------------")
        l_hum = ["jose","ana","pepo","nancy"]
        for l in l_hum:
            #print(l)
            monstersinc.agregarHumano(Humano(l))            
        humanos = monstersinc.obtenerHumanos()  
        print(humanos)   
        # for h in humanos:
        #     print(h)
        #estados =  monstersinc.obtenerEstadoAsustado()

# 5.b   
        print("****************************")
        print("ELIMINAR - M O N S T R U O S")
        print("------------------------------------")
        #nomMon = ["sullivan", "randall"]
        monstruos = monstersinc.obtenerMonstruos()
        print(monstruos)
        # for m in monstruos:
        #     print(m)

        # for mon in nomMon:  
        #     print(mon)  
        #     monstersinc.eliminarMonstruo(Monstruo(mon))
        #            
        monstruos = monstersinc.obtenerMonstruos()
        # for m in monstruos:
        #     print(m)
                
            # for i in range(0,3):
            #     mon = Monstruo(nomMon(i), espMon(i))
            #     monstersinc.agregarMonstruo(mon)       
            # else:
            #     break           

        #Agregar Humanos
        # l_hum = ["jose","ana","pepo","nancy"]
        # for l in l_hum:
        #     print(l)
        #     monstersinc.agregarHumano(l)
        # humanos = monstersinc.obtenerHumanos()            
        # print(humanos)
        #bool(random.getrandbits(1))
        
        
        # humano = Monstruo.asustar(humanos[1])
        # humanos_asustados = []
        # for hum in humanos:
        #     if hum.obtenerEstadoAsustado():
        #        humanos_asustados.append(hum)
        # print(humanos_asustados)     
        
        # while True:
        #     print("H U M A N O S")
        #     nom = input("Ingrese Nombre: ")
        #     print("------------------------------------")
        #     a = input("Confirma el Alta S/N: ").upper()
        #     if a == "S":   
        #         hum = Humano(nom)            
        #         monstersinc.agregarHumano(hum)      
        #     else:
        #         break                                
# 5.b
        # Eliminar monstruo
        # while True:            
        #     print("ELIMINAR - M O N S T R U O S")
        #     nom = input("Ingrese Nombre: ")            
        #     print("------------------------------------")
        #     a = input("Confirma el Alta S/N: ").upper()
        #     if a == "S":                                                
        #         monstersinc.eliminarMonstruo(nom)       
        #     else:
        #         break                   

# 6.a
        # Agregar Monstruo
        # monstruo10 = Monstruo("cuco", "gargola")
        # monstersinc.agregarMonstruo(monstruo10)
        
        # Agregar Humano
        # edu = Humano("mario")
        # juan = Humano("juan")
        # #humano = [edu,juan]
        # monstersinc.agregarHumano(edu)
        # monstersinc.agregarHumano(juan)
#6.b         
        # monstruos = monstersinc.obtenerMonstruos()
        # for mon in monstruos:            
        #     if mon.obtenerEnergia() > 0:
        #         print(f"Tiene {mon.energia} % DE ENERGIA")


#6.c
        # humanos = monstersinc.obtenerHumanos()
        # print(humanos)
        # for hum in humanos:
        #     if hum.obtenerEstadoAsustado():
        #         print(f"{hum.nombre} esta asustado")
        #     else:
        #         print(f"{hum.nombre} NO esta asustado")
  

if __name__ == '__main__':
    testerMonstersInc = TesterMonstersInc()
    testerMonstersInc.main()

