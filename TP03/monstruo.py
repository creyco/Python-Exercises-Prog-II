from humano import *

class Monstruo:

    maxEnergia = 100

    def __init__(self, nom, esp):
        self.nombre = nom
        self.especie = esp
        self.energia = Monstruo.maxEnergia
        self.estadoDormido = False
    
    def establecerNombre(self, nom):
        self.nombre = nom

    def establecerEspecie(self, esp):
        self.especie = esp

    def establecerEnergia(self, ene):
        self.energia = ene

    def establecerEstadoDormido(self, est):
        self.estadoDormido = est

    def asustar(self, hum: Humano):
        if not self.estadoDormido and not hum.estadoAsustado:
            hum.establecerEstadoAsustado(True)
            if self.energia - 10 < 0:
                self.energia = 0
            else:
                self.energia -= 10

    def divertir(self, hum: Humano):
        hum.establecerEstadoAsustado(False)
        if self.energia - 20 < 0:
            self.energia = 0
        else:
            self.energia -= 20

    def dormir(self):
        self.estadoDormido = True
        if self.energia > Monstruo.maxEnergia - 15:
            self.energia = Monstruo.maxEnergia
        else:
            self.energia += 15

    def despertar(self):
        self.estadoDormido = False

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
        return self.nombre + ' ' + self.especie + ' ' + str(self.energia)

    def __repr__(self):
        return self.__str__()