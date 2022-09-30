class Humano:
    especie = "humano"

    def __init__(self, nombre):
        self.nombre = nombre
        self.estadoAsustado = False

    def establecerNombre(self, nom):
        self.nombre = nom

    def establecerEstadoAsustado(self, est = True):
        self.estadoAsustado = est

    # Consultas

    def obtenerNombre(self):
        return self.nombre
    # Consultas

    def obtenerEstadoAsustado(self ):
        return self.estadoAsustado

# boo = Humano('Boo',True)  
# print( boo.obtenerNombre() )
# print( boo.obtenerEstadoAsustado() )