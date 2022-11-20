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

    def agregarMonstruo(self, mon):
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

    '''<< CONSULTAS >>''' #¿¿¿¿---------- ???????????
    def obtenerMonstruos(self):
        return self.monstruos

    def obtenerPuertas(self):        
        return self.puertas
