def main():
    numeros = input("Ingrese números separados por espacios: ")
    lista = [int(num) for num in numeros.split()]

    maximo = max(lista)
    minimo = min(lista)

    print(f"El número más grande es: {maximo}")
    print(f"El número más pequeño es: {minimo}")
main()