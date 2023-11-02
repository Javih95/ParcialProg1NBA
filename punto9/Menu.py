import re
from Jugador import Jugador
from Estadistica import Estadistica
from Equipo import Equipo
import csv
from Funciones import *

while True:
    print("Menú de opciones:")
    print("1. Mostrar la lista de todos los jugadores del Dream Team")
    print("2. Mostrar estadísticas de un jugador por su índice")
    print("3. Mostrar y guardar estadísticas de un jugador en un archivo CSV")
    print("4. Buscar un jugador por su nombre")
    print("5. Calcular y mostrar el promedio de puntos de todo el equipo")
    print("6. Verificar si un jugador es miembro del Salón de la Fama")
    print("7. Calcular al jugador con la mayor cantidad de rebotes totales")
    print("8. Ordenar el listado de manera descendente(el mayor arriba),mostrarlo y permitir guardar ")
    print("9.filtrar y ordenar los datos por el jugador que sumando los robos totales más los bloqueos totales")
    print("10. Salir")
    opcion = input("Ingrese el número de la opción que desea seleccionar: ")
    if re.match(r'^[1-9]$', opcion):
        opcion = int(opcion)
        match opcion:
            case 1:
                mostrar_nombre_posicion()
                break
            case 2:
                indice_y_mostrar_estadisticas()
                break
            case 3:
                guardar_estadisticas(jugador_seleccionado)
                break
            case 4:
                buscar()
                break
            case 5:
                calcular_promedio_equipo()
                break
            case 6:
                buscar_salon_de_la_fama()
                break
            case 7:
                jugador_mas_rebotes()
                break
            case 8:
                mostrar_bloqueos_totales()
                break
            case 9:
                filtrar_y_mostrar()
                break
            case 10:
                break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida del menú.")