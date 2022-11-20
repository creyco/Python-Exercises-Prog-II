# from humano import *
# from puerta import *
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
    def establecerEnergia(self, ene):
        if ene in range(0,self.maxEnergia + 1): #aca no es necesario el +1 
           self.energia = ene    # podes colocar un else con un print para que muestre un msj en que caso de qe no cumpla el if         
    def establecerEstadoDormido(self, est):
        self.estadoDormido = est
    
    def asustar(self, pue):
        if pue != None and pue.estadoActiva and pue.monstruo != None:   
            ''' 3.e '''
            pue.monstruo.establecerEstadoAsustado(True)
            print('asustando')
            if self.energia - 10 < 0:                               
                self.energia = 0                                
            else:
                self.energia -= 10
            '''1.d.ii'''
        else:
            print('no se cumplen las condiciones para asustar')  #esto podes implementar para  los demas metodos

    def divertir(self, hum):
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
