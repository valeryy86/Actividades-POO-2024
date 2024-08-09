def main():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    matriz = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = 2
            fila.append(valor)
        matriz.append(fila)

    print("La matriz ingresada es:")
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()
main()