#Cada jugador tendrá como atributos una lista de logros, un nombre, posición y un
#objeto de clase Estadistica.

from Estadistica import Estadistica
class Jugador:
    def __init__(self, nombre, posicion,logros,Estadistica):
        self.logros = logros
        self.nombre= nombre
        self.posicion= posicion
        self.estadistica= Estadistica
    #getters
    def nombre(self):
        return self.nombre
    def posicion(self):
        return self.posicion
    def logros(self):
        return self.logros
    def estadistica(self):
        return self.estadistica
    
    #setters
    def nombre(self,nombre):
        self.nombre = nombre
    def posicion(self,posicion):
        self.posicion = posicion
    def logros(self,logros):
        self.logros = logros
    def estadistica(self,Estadistica):
        self.estadistica = Estadistica