def main():
    numeros = input("Ingrese los números separados por espacios: ")
    lista = numeros.split()

    lista_invertida = lista[::-1]

    print("Lista original:", lista)
    print("Lista invertida:", lista_invertida)

main()