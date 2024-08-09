def main():
    numeros = []
    while True:
        datos = input("Ingrese un número (presione Enter cuando desee terminar): ")
        if datos == "":
            break
    numeros.append(float(datos))

    if len(numeros) > 0:
        suma = sum(numeros)

        media = suma / len(numeros)

        print(f"La media aritmética de los {len(numeros)} números ingresados es: {media}")
    else:
        print("No se ingresaron números.")
main()