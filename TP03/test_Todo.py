from humano import *

#--------------------------------------------------Monstruo-------#
class Monstruo:

    maxEnergia = 100
    minEnergia = 15         # 1.a y 3.a 

    def __init__(self, nom, esp, tipo):
        self.nombre = nom
        self.especie = esp
        self.pareja = None 				# 3.c monstruo pareja, va el nombre y debe ser de tipo dif. 
        self.energia = self.maxEnergia
        self.estadoDormido = False  
        ''' 1.a '''
        if tipo in ['asustador','asistente']:
            self.tipo = tipo                
        ''' 3.b requiere tipo = ["asustador" , "asistente"] '''

    ''' << COMANDOS >>'''
    def establecerNombre(self, nom):
        self.nombre = nom

    def establecerEspecie(self, esp):
        self.especie = esp
    
    def establecerPareja(self, mou):  
        ''' asistente activa puertas, 
            necesito un minimo de energia (asustar o divertir) '''        
        if mou != None and self.tipo != mou.tipo:                                      
           self.pareja = mou
        #    print(mou.nombre, mou.tipo, mou.pareja)
        #    print(self.nombre, self.tipo, self.pareja)
        #    input('aki---')

    ''' el monstruo pareja de un monstro asustador debe ser 
        monstruo asistente  '''

    def establecerEnergia(self, ene):
        if ene in range(0,self.maxEnergia + 1): #aca no es necesario el +1 
           self.energia = ene    # podes colocar un else con un print para que muestre un msj en que caso de qe no cumpla el if
         
    def establecerEstadoDormido(self, est):
        self.estadoDormido = est

    def asustar(self, pue):
        if pue != None and isinstance(pue, Puerta) \
            and pue.estadoActiva and pue.humano != None and pue.monstruo != None:   #  te  faltaria eso self.energia >= 15 and pue.obtenerEstadoActiva() and self.tipo == 'asustador'  
            ''' 3.e '''

            pue.establecerEstadoAsustado(True)
            print('asustando')
            if self.energia - 10 < 0:                               
                self.energia = 0                                
            else:
                self.energia -= 10
            '''1.d.ii'''
        else:
            print('no se cumplen las condiciones para asustar')  #esto podes implementar para  los demas metodos
    def divertir(self, hum: Humano):
        hum.establecerEstadoAsustado(False)
        if self.energia - 20 < 0:
            self.energia = 0
        else:
            self.energia -= 20
        '''1.d.ii'''

    def dormir(self):
        if self.energia <= self.maxEnergia:                                 
            '''1.b_i'''
            self.estadoDormido = True  
            print(self.nombre,'durmiendo') 
            if self.energia > Monstruo.maxEnergia + 15:
                self.energia = Monstruo.maxEnergia
            else:
                self.energia += 15

    def despertar(self):
        self.estadoDormido = False
        '''1.c'''
        
    def activarPuerta(self, pue): # te faltaba este metodo
        if self.tipo == 'asistente' and not pue.obtenerEstadoEnUso():
            pue.establecerEstadoActiva(True)
            pue.establecerMonstruo(self.pareja)
            print(self.nombre, 'Activando Puerta: ', pue.numero, '\n')
        else:
            print(self.nombre, 'No puede activar esta Puerta!\n')    

    '''<< CONSULTAS >>'''
    def obtenerNombre(self):
        return self.nombre

    def obtenerEspecie(self):
        return self.especie

    def obtenerEnergia(self):
        return self.energia

    def obtenerEstadoDormido(self):
        return self.estadoDormido

    def equals(self, mon):
        return self.nombre == mon.obtenerNombre() and self.especie == mon.obtenerEspecie()
    
    def __str__(self):
        return self.nombre + ' ' + self.especie + ' ' + self.tipo 
        # + ' ' + self.pareja + ' ' + str(self.energia)

    def __repr__(self):
        return self.__str__()



##-------------------------------------------------------Puerta----#
class Puerta:
    def __init__(self, num, hum: Humano):   # Requiere hum ligado
        self.numero = num        
        self.humano = hum      
        self.monstruo = None   # no requiere pasar montruo como parametro
        self.estadoActiva = False  
        '''
            2.a/c crea atributo de instancia numero puerta - inmutable (c) y no cuenta con un método (pasar valor)            
            2.b inicialmente, el atributo de instancia monstruo = Null -> None            
        '''
    def establecerHumano(self, hum: Humano):
        self.humano = hum   

    def establecerMonstruo(self, mon: Monstruo):
        self.monstruo = mon      
    def establecerEstadoActiva(self,est): #requiere parametro booleano para establcer el estado de puerta
        self.estadoActiva = True

    '''<< CONSULTAS >>'''     
    def obtenerNumero(self):
        return self.numero 
    
    def obtenerHumano(self):
        return self.humano

    def obtenerMonstruo(self):
        return self.monstruo
    
    def obtenerEstadoActiva(self):
        return self.estadoActiva 

    def obtenerEstadoEnUso(self):  
        '''2.d debe devolver True cuando el valor atributo estadoActiva es True 
        y monstruo tenga un valor distinto de None.'''
        if self.estadoActiva and self.monstruo != None:                       
            return True
        else:     
            return False

    def equals(self, pue):         
        return self == pue.obtenerMonstruo() 
        #and self.estadoActiva == pue.estadoActiva    

    def __str__(self):
        return str(self.numero) + ' ' + str(self.humano ) 
        #+ ' ' + str(self.monstruo)

    def __repr__(self):
        return self.__str__()                            

'''
RESPONDE esta pregunta
i) Luego de implementar este método, 
¿su ejecución estará refiriendo a una comparación de estados internos 
(igualdad en profundidad) o de identidad (igualdad superficial)? 

'''
#-----------------------------------------------MonstersInc-------#
class MonstersInc:

    def __init__(self):
        self.monstruos = []
        #{'asustador': Monstruo , 'asistente': Monstruo}
        ''' 4.a. Monstruos deja de ser una lista de objetos de tipo Monstruo para pasar a ser
una lista de diccionarios de la siguiente forma:
{“asustador”: Monstruo, “asistente”: Monstruo}
Donde tanto “asustador” y “asistente” están enlazados por el atributo pareja, y
estos cuentan con la restricción de ser de tipo “asustador” y “asistente”,
respectivamente.'''
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

##------------------------------------------testerMonstersInc--#
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
        sully.asustar(boo)
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
    