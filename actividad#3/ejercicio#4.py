import math

class Circulo:
    def __init__(self, centro, radio):
        self.centro=centro
        self.radio=radio

    def area(self):
        area= 3.14*(self.radio**2)
        return area
    
    def perimetro(self):
        perimetro= 2*3.14*self.radio
        return perimetro
    
    def pertenece(self, punto):
        distancia = math.sqrt((punto [0] - self.centro[0])**2 + (punto[1]- self.centro[1])**2)
        return distancia == self.radio
    
mi_circulo=Circulo((3,5), 6)

area_circulo= mi_circulo.area()
print("el area del circulo es: {}" .format (area_circulo))

perimetro_circulo = mi_circulo.perimetro()
print("el perimetro del circulo es: {}" .format(perimetro_circulo))

punto=(9,5)
punto_pertenece=mi_circulo.pertenece(punto)
if punto_pertenece:
    print("el punto {} pertenece a la circunferencia" .format(punto))
else:
    print("el punto {} no pertenece a la circunferencia" .format (punto))






        
