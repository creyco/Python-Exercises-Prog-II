#from humano import Humano

class Monstruo:
    # << atributos de clase >>
    maxEnergia = 100    # a. El atributo de clase maxEnergía debe tener un valor de 100.
                        # b. El valor inicial de energia debe ser igual a maxEnergía.
    def __init__(self, nombre, especie): # constructor de Monstruo
    # Atributos de instancia
        
        self.nombre = nombre
        self.especie = especie
        self.energia = self.maxEnergia

    # << Comandos Metodos >>

    def establecerNombre(self, nom):
        self.nombre = nom

    def establecerEspecie(self, esp):
        self.especie = esp

    def establecerEnergia(self, ene):
        self.energia = ene
    
    def asustar(self, humano):     
        self.estadoAsustado = True           
        self.energia -= 10        
        return humano.establecerEstadoAsustado(self.estadoAsustado)
    
    def divertir(self, humano):
        self.estadoAsustado = False
        self.energia -= 20  
        return humano.establecerEstadoAsustado(self.estadoAsustado)     

    #<<CONSULTAS>>

    def obtenerNombre(self):
        return self.nombre

    def obtenerEspecie(self):
        return self.especie

    def obtenerEnergia(self):
        return self.energia
   
    def __str__(self):
        return self.nombre + ' ' + self.especie + ' ' + str(self.energia) 

    def __repr__(self):
            return self.__str__()


 
