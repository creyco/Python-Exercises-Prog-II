class Humano:
    especie = "humano"

    def __init__(self, nombre):
        self.nombre = nombre
        self.estadoAsustado = False

    def establecerNombre(self, nombre):
        self.nombre = nombre

    def establecerEstadoAsustado(self, estadoAsustado):
        self.estadoAsustado = estadoAsustado
        return estadoAsustado

    # Consultas

    def obtenerNombre(self):
        return self.nombre
    
    def obtenerEstadoAsustado(self):
        return self.estadoAsustado

    # Ejercicio 5
    def equals(self, nom):
        return self.nombre == nom.obtenerNombre()

    def __str__(self):
        return self.nombre + ' ' + self.especie + ' ' + str(self.estadoAsustado) 

    def __repr__(self):
            return self.__str__()
