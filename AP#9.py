import math
from collections import Counter

direccion_a_grados = {
    "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5, "E": 90, "ESE": 112.5,
    "SE": 135, "SSE": 157.5, "S": 180, "SSW": 202.5, "SW": 225, "WSW": 247.5,
    "W": 270, "WNW": 292.5, "NW": 315, "NNW": 337.5
}

grados_a_direccion = {v: k for k, v in direccion_a_grados.items()}

class DatosMeteorologicos:
    def __init__(self, datos: str):
        self.datos = datos

    def procesar_datos(self):
        temperaturas = []
        humedades = []
        presiones = []
        velocidades_viento = []
        direcciones_viento = []

        with open(self.datos, 'r') as archivo:
            lineas = archivo.readlines()
            
        i = 0
        while i < len(lineas):
            try:
                if "Temperatura" in lineas[i]:
                    temperatura = float(lineas[i].split(":")[1].strip())
                    temperaturas.append(temperatura)
                elif "Humedad" in lineas[i]:
                    humedad = float(lineas[i].split(":")[1].strip())
                    humedades.append(humedad)
                elif "Presion" in lineas[i]:
                    presion = float(lineas[i].split(":")[1].strip())
                    presiones.append(presion)
                elif "Viento" in lineas[i]:
                    viento_datos = lineas[i].split(":")[1].strip()
                    velocidad_viento, direccion_viento = viento_datos.split(',')
                    velocidades_viento.append(float(velocidad_viento))
                    direcciones_viento.append(direccion_viento.strip())
                i += 1

            except (IndexError, ValueError) as e:
                print(f"Error procesando la línea: {lineas[i].strip()} -> {e}")
                i += 1
                continue

        temp_promedio = sum(temperaturas) / len(temperaturas) if temperaturas else 0
        hum_promedio = sum(humedades) / len(humedades) if humedades else 0
        pres_promedio = sum(presiones) / len(presiones) if presiones else 0
        viento_promedio = sum(velocidades_viento) / len(velocidades_viento) if velocidades_viento else 0

        grados_viento = [direccion_a_grados[d] for d in direcciones_viento if d in direccion_a_grados]
        promedio_grados = sum(grados_viento) / len(grados_viento) if grados_viento else 0

        direccion_predominante = min(grados_a_direccion.keys(), key=lambda x: abs(x - promedio_grados))

        return temp_promedio, hum_promedio, pres_promedio, viento_promedio, grados_a_direccion[direccion_predominante]

datos = DatosMeteorologicos('C:/Users/user/Downloads/datos.txt')
estadisticas = datos.procesar_datos()
print(f"Temperatura promedio: {estadisticas[0]:.2f} °C")
print(f"Humedad promedio: {estadisticas[1]:.2f} %")
print(f"Presión promedio: {estadisticas[2]:.2f} hPa")
print(f"Velocidad promedio del viento: {estadisticas[3]:.2f} km/h")
print(f"Dirección predominante del viento: {estadisticas[4]}")