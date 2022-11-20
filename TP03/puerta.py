##-------------------------------------------------------Puerta----#
class Puerta:
    def __init__(self, num, hum):   # Requiere hum ligado
        self.numero = num        
        self.humano = hum      
        self.monstruo = None   # no requiere pasar montruo como parametro
        self.estadoActiva = False  
        '''
            2.a/c crea atributo de instancia numero puerta - inmutable (c) y no cuenta con un método (pasar valor)            
            2.b inicialmente, el atributo de instancia monstruo = Null -> None            
        '''
    def establecerHumano(self, hum):
        self.humano = hum   
    def establecerMonstruo(self, mon):
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

    # def equals(self, pue):         
    #     return self == pue.obtenerMonstruo() 
    #     #and self.estadoActiva == pue.estadoActiva    
    def equals(self, pue):
        return (self.numero == pue.obtenerNumero() and
                self.estadoActiva == pue.obtenerEstadoActiva() and
                self.humano == pue.obtenerHumano() and
                self.monstruo == pue.obtenerMonstruo())

    # def __str__(self):
    #     return str(self.numero) + ' ' + str(self.humano ) 
    #     #+ ' ' + str(self.monstruo)
    # def __repr__(self):
    #     return self.__str__()                            
    
    def __repr__(self):
        return str(self.numero) + ' ' + self.humano.obtenerNombre() + ' ' + (self.monstruo.obtenerNombre() if self.monstruo != None else 'None')