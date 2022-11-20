from humano import *
from monstruo import *

class Puerta:

    def __init__(self, num, hum: Humano):   # Requiere hum ligado
        self.numero = num        
        self.humano = hum      
        self.monstruo = None   
        self.estadoActiva = False  
        '''
            2.a/c crea atributo de instancia numero puerta - inmutable (c) y no cuenta con un método (pasar valor)            
            2.b inicialmente, el atributo de instancia monstruo = Null -> None            
        '''
    def establecerHumano(self, hum: Humano):
        self.humano = hum   
        
    def establecerMonstruo(self, mon: Monstruo):
        self.monstruo = mon 

    def establecerEstadoActiva(self):
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

