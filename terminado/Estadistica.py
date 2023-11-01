class Estadistica:
    def __init__(self,temporadas,puntos_totales,promedio_puntos,rebotes_totales,promedio_rebotes,asistencias_totales,promedio_asistencias,robos_totales,bloqueos_totales,porcentaje_tiros_de_campo,porcentaje_tiros_libres,porcentaje_tiros_triples):
        self.temporadas= temporadas
        self.puntos_totales = puntos_totales
        self.promedio_puntos= promedio_puntos
        self.rebotes_totales = rebotes_totales
        self.promedio_rebotes = promedio_rebotes
        self.asistencias_totales = asistencias_totales
        self.promedio_asistencias = promedio_asistencias
        self.robos_totales = robos_totales
        self.bloqueos_totales = bloqueos_totales
        self.porcentaje_tiros_de_campo = porcentaje_tiros_de_campo
        self.porcentaje_tiros_libres = porcentaje_tiros_libres
        self.porcentaje_tiros_triples = porcentaje_tiros_triples



    #getters
    def temporadas(self):
        return self.temporadas
    def puntos_totales(self):
        return self.puntos_totales
    def promedio_puntos(self):
        return self.promedio_puntos
    def rebotes_totales(self):
        return self.rebotes_totales
    def promedio_rebotes(self):
        return self.promedio_rebotes
    def asistencias_totales(self):
        return self.asistencias_totales
    def promedio_asistencias(self):
        return self.promedio_asistencias
    def robos_totales(self):
        return self.robos_totales
    def bloqueos_totales(self):
        return self.bloqueos_totales
    def porcentaje_tiros_de_campo(self):
        return self.porcentaje_tiros_de_campo
    def porcentaje_tiros_libres(self):
        return self.porcentaje_tiros_libres
    def porcentaje_tiros_triples(self):
        return self.porcentaje_tiros_triples
    
    #setters
    def temporadas(self,temporadas):
        self.temporadas = temporadas
    def  puntos_totales(self,puntos_totales):
        self.puntos_totales = puntos_totales
    def promedio_puntos(self,promedio_puntos):
        self.promedio_puntos = promedio_puntos
    def rebotes_totales(self,rebotes_totales):
        self.rebotes_totales = rebotes_totales
    def promedio_rebotes(self,promedio_rebotes):
        self.promedio_rebotes = promedio_rebotes
    def asistencias_totales(self,asistencias_totales):
        self.asistencias_totales = asistencias_totales
    def promedio_asistencias(self,promedio_asistencias):
        self.promedio_asistencias = promedio_asistencias
    def robos_totales(self,robos_totales):
        self.robos_totales = robos_totales
    def bloqueos_totales(self,bloqueos_totales):
        self.bloqueos_totales = bloqueos_totales
    def porcentaje_tiros_de_campo(self,porcentaje_tiros_de_campo):
        self.porcentaje_tiros_de_campo = porcentaje_tiros_de_campo
    def porcentaje_tiros_libres(self,porcentaje_tiros_libres):
        self.porcentaje_tiros_libres = porcentaje_tiros_libres
    def porcentaje_tiros_triples(self,porcentaje_tiros_triples):
        self.porcentaje_tiros_triples = porcentaje_tiros_triples