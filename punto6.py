def main():

    numeros = input("Ingrese los números separados por espacios: ")
    lista = [int(num) for num in numeros.split()]
    suma = sum(lista)
    print(f"La suma de los números en la lista {lista} es: {suma}")
main()