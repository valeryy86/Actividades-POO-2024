class Rectangulo:
    def __init__ (self, lado_v, lado_h):
        self.lado_h=lado_h
        self.lado_v=lado_v

    def es_cuadrado(self):
        return self.lado_h == self.lado_v
            

    def perimetro(self):
        perimetro= 2*(self.lado_v + self.lado_h)
        return perimetro
    
    def area(self):
        area = (self.lado_v * self.lado_h)
        return area
    


mi_rectangulo=Rectangulo( 7, 10)
print("lado vertical: {}, lado horizontal: {}".format (mi_rectangulo.lado_v, mi_rectangulo.lado_h))

if mi_rectangulo.es_cuadrado():
    print("Es un cuadrado")

else:
    perimetro_rectangulo= mi_rectangulo.perimetro()
    print("el perimetro del rectángulo es {}" .format (perimetro_rectangulo))

    area_rectangulo=mi_rectangulo.area()
    print("el area del rectángulo es: {}" .format (area_rectangulo))

