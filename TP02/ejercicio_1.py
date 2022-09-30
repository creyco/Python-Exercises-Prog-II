class Monstruo:
    # << atributos de clase >>
    maxEnergia = 100    # a. El atributo de clase maxEnergía debe tener un valor de 100.
                        # b. El valor inicial de energia debe ser igual a maxEnergía.
    def __init__(self, nombre, especie, energia = maxEnergia): # constructor de Monstruo
    # Atributos de instancia        
        self.nombre = nombre
        self.especie = especie
        self.energia = energia

    # << Comandos Metodos >>

    def establecerNombre(self, nom):
        self.nombre = nom

    def establecerEspecie(self, esp):
        self.especie = esp

    def establecerEnergia(self, ene):
        self.energia = ene
    
    def asustar(self, ene):
        self.energia -= ene
    
    # def divertir(self, ene):
    #     self.energia -= ene        

    # Consultas

    def obtenerNombre(self):
        return self.nombre

    def obtenerEspecie(self):
        return self.especie

    def obtenerEnergia(self):
        return self.energia

    # def asustar(self, ene):
    #     return self.energia - ene

    def __str__(self):
        return self.nombre + ' ' + self.especie + ' ' + str(self.energia) 

    def __eq__(self, otro):
        if (isinstance(otro, Monstruo)):
            equiv = self.nombre == otro.nombre and self.especie == otro.especie and self.energia == otro.energia
        else:
            equiv = False
        return equiv                
