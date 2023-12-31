from Jugador import Jugador
from Estadistica import Estadistica
from Equipo import Equipo
import re
import csv
ruta_archivo = "dream_team.json"
equipo = Equipo(ruta_archivo)
#1) Mostrar la lista de todos los jugadores del Dream Team. Con el formato: Nombre Jugador - Posición
def mostrar_nombre_posicion():
    for jugador in equipo.lista_jugadores:
        print(f"{jugador.nombre} - {jugador.posicion}")
#mostrar_nombre_posicion()
#2) Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas 
def indice_y_mostrar_estadisticas():
    while True:
        largo_lista = len(equipo.lista_jugadores)
        seleccion_usuario = input(f"Ingrese el índice del jugador que desea ver (del 0 al {largo_lista-1}) :")
        patron = "^[0-9]+$"
        if re.match(patron, seleccion_usuario):
            indice = int(seleccion_usuario)
            if 0 <= indice < largo_lista:
                break
            else:
                print("El índice ingresado no es válido. Intente nuevamente.")
        else:
            print("Ingrese un índice numérico válido.")
    jugador_seleccionado = equipo.lista_jugadores[indice]
    nombre = jugador_seleccionado.nombre
    posicion = jugador_seleccionado.posicion
    estadisticas = jugador_seleccionado.estadistica
    temp= f"Temporadas jugadas {estadisticas.temporadas} \n"
    puntos_tot = f"Puntos totales: {estadisticas.puntos_totales}\n"
    prom_puntos = f"Promedio de puntos por partido: {estadisticas.promedio_puntos}\n"
    rebotes = f"Rebotes totales: {estadisticas.rebotes_totales}\n"
    prom_reb = f"Promedio de rebotes por partido: {estadisticas.promedio_rebotes}\n"
    asist = f"Asistencias totales: {estadisticas.asistencias_totales}\n"
    prom_asis = f"Promedio de asistencias por partido: {estadisticas.promedio_asistencias}\n"
    robos = f"Robos totales: {estadisticas.robos_totales}\n"
    bloqueos = f"Bloqueos totales: {estadisticas.bloqueos_totales}\n"
    tiros_campo = f"Porcentaje de tiros de campo: {estadisticas.porcentaje_tiros_de_campo}%\n"
    tiros_libres = f"Porcentaje de tiros libres: {estadisticas.porcentaje_tiros_libres}%\n"
    triples = f"Porcentaje de tiros triples: {estadisticas.porcentaje_tiros_triples}%"
    mensaje = f"Estadísticas del jugador {nombre} ({posicion}):\n{temp}{puntos_tot}{prom_puntos}{rebotes}{prom_reb}{asist}{prom_asis}{robos}{bloqueos}{tiros_campo}{tiros_libres}{triples}"
    print(mensaje)
    return jugador_seleccionado 
    return estadisticas
#indice_y_mostrar_estadisticas()
#3) Después de mostrar las estadísticas,permite al usuario guardarlas en un archivo CSV.

def guardar_estadisticas(jugador_seleccionado):
    jugador_seleccionado = indice_y_mostrar_estadisticas()
    with open("estadicticas_archivo.csv", 'w+' , newline="") as fichero:
        escribir_fichero= csv.writer(fichero, delimiter=";")  
        jugador = jugador_seleccionado
        estadisticas = jugador.estadistica
        nombre = ["Nombre:", jugador.nombre]
        posicion = ["Posicion:", jugador.posicion]
        temporadas = ["Temporadas:",estadisticas.temporadas]
        puntos_totales = ["Puntos totales:", estadisticas.puntos_totales]
        promedio_de_puntos = ["promedio de puntos por partido:",estadisticas.promedio_puntos]
        rebotes_totales = ["rebotes totales:", estadisticas.rebotes_totales]
        promedio_de_rebotes = ["promedio de rebotes por partido:",estadisticas.promedio_rebotes]
        asistencias_totales = ["asistencias totales:", estadisticas.asistencias_totales]
        promedio_asistencias = ["promedio de asistencias por partido:",estadisticas.promedio_asistencias]
        robos_totales= ["robos totales:", estadisticas.robos_totales]
        bloqueos_totales=["bloqueos totales:", estadisticas.bloqueos_totales]
        tiros_de_campo =["porcentaje tiros de campo:", estadisticas.porcentaje_tiros_de_campo]
        tiros_libres= ["porcentaje tiros libres:", estadisticas.porcentaje_tiros_libres]
        tiros_triples =["porcentaje tiros triples:", estadisticas.porcentaje_tiros_triples]
        mensaje = [nombre,posicion,temporadas,puntos_totales,promedio_de_puntos,rebotes_totales,promedio_de_rebotes,asistencias_totales,promedio_asistencias,robos_totales,bloqueos_totales,tiros_de_campo,tiros_libres,tiros_triples]
        escribir_fichero.writerows(mensaje)
#guardar_estadisticas(jugador_seleccionado)
#4) Permitir al usuario buscar un jugador por su nombrey mostrar sus logros
lista_jugadores= equipo.lista_jugadores
def buscar_por_nombre(nombre):
    jugadores_encontrados = []
    for jugador in lista_jugadores:
        if re.search(nombre, jugador.nombre, re.IGNORECASE):
            jugadores_encontrados.append(jugador)
    return jugadores_encontrados
def buscar():
    while True:
        nombre_buscado = input("Ingrese el nombre del jugador que desea buscar: ")
        def validar_nombre(texto):
            patron = r"^[A-Za-z]{3,}$"
            return bool(re.match(patron, texto))
        if validar_nombre(nombre_buscado):
            jugadores_encontrados = buscar_por_nombre(nombre_buscado)
            if jugadores_encontrados:
                for jugador in jugadores_encontrados:
                    logros=jugador.logros
                    print(f"Nombre: {jugador.nombre} \nLogros:")
                    if logros:
                        for logro in logros:
                            print(logro)
                    else:
                        print("No se encontraron logros para este jugador.")
                break
            else:
                print(f"No se encontraron jugadores con el nombre '{nombre_buscado}'.")
        else:
            print("El nombre ingresado no es válido. Debe contener almemos 3 letras.")
#buscar()
#5) Calcular y mostrar el promedio de puntos de todo el equipo, ordenado por nombre de manera ascendente.
def calcular_promedio_equipo():
    acumulador_puntos_equipo = 0
    promedios_puntos_jugadores = []
    for jugador in lista_jugadores:
        estadisticas = jugador.estadistica
        promedios_puntos_jugadores.append((jugador.nombre,estadisticas.promedio_puntos))
        acumulador_puntos_equipo += float(estadisticas.promedio_puntos)
        promedio_puntos_por_partido = acumulador_puntos_equipo / len(lista_jugadores)
    print(f"Promedio de puntos por partido de todo el equipo:{promedio_puntos_por_partido:.2f}")
    promedios_puntos_jugadores.sort(key=lambda x: x[1])
    print("Promedio de puntos de todo el equipo ordenado por nombre (ascendente):")
    for nombre, promedio_puntos in promedios_puntos_jugadores:
        print(f"{nombre}: {promedio_puntos:.1f} puntos por partido")
calcular_promedio_equipo()