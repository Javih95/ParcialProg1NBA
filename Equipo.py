#La Clase Equipo será la encargada de levantar el archivo JSON y realizar todas las
#tareas relacionadas a archivos. También se encargará de crear a cada jugador al leer el
#JSON y agregarlos a una lista de jugadores la cual deberá ser atributo de la clase
#Equipo.
from Jugador import Jugador
from Estadistica import Estadistica
import json


class Equipo:
    def __init__ (self,archivo):
        self.lista_jugadores = []
        self.cargar_datos(archivo)
    def cargar_datos(self,archivo):
        with open(archivo) as file:
            datos = json.load(file)
            for jugador_datos in datos["jugadores"]:
                estadisticas_datos = jugador_datos["estadisticas"]
                temporadas = estadisticas_datos.get("temporadas",)
                puntos_totales =estadisticas_datos.get("puntos_totales")
                promedio_puntos = estadisticas_datos.get("promedio_puntos_por_partido")
                rebotes_totales = estadisticas_datos.get("rebotes_totales")
                promedio_rebotes= estadisticas_datos.get("promedio_rebotes_por_partido")
                asistencias_totales = estadisticas_datos.get("asistencias_totales")
                promedio_asistencias = estadisticas_datos.get("promedio_asistencias")
                robos_totales = estadisticas_datos.get("robos_totales")
                bloqueos_totales = estadisticas_datos.get("bloqueos_totales")
                porcentaje_tiros_de_campo = estadisticas_datos.get("porcentaje_tiros_de_campo")
                porcentaje_tiros_libres= estadisticas_datos.get("porcentaje_tiros_libres")
                porcentaje_tiros_triples = estadisticas_datos.get("porcentaje_tiros_triples")
                
                estadisticas = Estadistica(temporadas,puntos_totales,promedio_puntos,rebotes_totales,promedio_rebotes,asistencias_totales,promedio_asistencias,robos_totales,bloqueos_totales,porcentaje_tiros_de_campo,porcentaje_tiros_libres,porcentaje_tiros_triples)
                nombre = jugador_datos.get("nombre")
                posicion = jugador_datos.get("posicion")
                logros = jugador_datos.get("logros")
                
                jugador = Jugador(nombre,posicion,logros,estadisticas)
                
                self.lista_jugadores.append(jugador)