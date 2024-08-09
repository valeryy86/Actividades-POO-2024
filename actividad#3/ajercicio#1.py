class Vehiculo:

    def __init__ (self, kilometraje, velocidad_maxima):
        self.kilometraje= kilometraje
        self.velocidad_maxima = velocidad_maxima

mi_vehiculo= Vehiculo(12000, "250 k/h" )
print("El kilometraje de mi vehículo es {} y la velocidad máxima es {}".format(mi_vehiculo.kilometraje, mi_vehiculo.velocidad_maxima))

mi_vehiculo2= Vehiculo (15000, "370 k/h")
print("El kilometraje de mi vehículo es {} y la velocidad máxima es {}".format(mi_vehiculo2.kilometraje, mi_vehiculo2.velocidad_maxima))
