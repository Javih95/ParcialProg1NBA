#Cada jugador tendrá como atributos una lista de logros, un nombre, posición y un
#objeto de clase Estadistica.

from Estadistica import Estadistica
class Jugador:
    def __init__(self, nombre, posicion,logros,Estadistica):
        self.logros = logros
        self.nombre= nombre
        self.posicion= posicion
        self.estadistica= Estadistica
    