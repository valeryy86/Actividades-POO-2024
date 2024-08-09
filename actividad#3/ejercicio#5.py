class Carta:

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    def __repr__(self):
        return f"{self.valor} de {self.pinta}"
    
    CORAZONES = "Corazones"
    DIAMANTES = "Diamantes"
    TREBOLES = "Tréboles"
    PICAS = "Picas"
    
mi_carta = Carta("As", Carta.CORAZONES)
print(mi_carta)

mi_carta2 = Carta("8", Carta.DIAMANTES)
print(mi_carta2)

mi_carta3 = Carta("Rey", Carta.TREBOLES)
print(mi_carta3)

mi_carta4 = Carta("3", Carta.PICAS)
print(mi_carta4)



