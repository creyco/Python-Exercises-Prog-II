class Humano:

    especie = "humano"

    def __init__(self, nom):
        self.nombre = nom
        self.estadoAsustado = False
    
    def establecerNombre(self, nom):
        self.nombre = nom

    def establecerEstadoAsustado(self, est):
        self.estadoAsustado = est

    def obtenerNombre(self):
        return self.nombre

    def obtenerEstadoAsustado(self):
        return self.estadoAsustado

    def equals(self, mon):
        return self.nombre == mon.obtenerNombre()
    
    def __str__(self):
        return self.nombre + ' ' + self.especie + ' ' + str(self.estadoAsustado)

    def __repr__(self):
        return self.__str__()