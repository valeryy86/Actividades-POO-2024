import math

class Punto:
    def __init__(self, coordenada_x, coordenada_y):
        self.coordenada_x=coordenada_x
        self.coordenada_y=coordenada_y

    def punto_nuevo(self, nueva_coordenada_x, nueva_coordenada_y):
        self.coordenada_x=nueva_coordenada_x
        self.coordenada_y=nueva_coordenada_y



    def distancia_puntos (self, punto_a_medir):
        distancia_puntos=math.sqrt((punto_a_medir.coordenada_x - self.coordenada_x )**2 + (punto_a_medir.coordenada_y - self.coordenada_y)**2)
        return distancia_puntos
    
mi_punto=Punto(2,3)
print(" x1 = {} \n y1 = {}".format (mi_punto.coordenada_x, mi_punto.coordenada_y))

mi_otro_punto=Punto(5,4)
print(" x2 = {} \n y2 = {}".format (mi_otro_punto.coordenada_x, mi_otro_punto.coordenada_y))

distancia_entre_puntos=mi_punto.distancia_puntos(mi_otro_punto)
print("la distancia es {}".format (distancia_entre_puntos))