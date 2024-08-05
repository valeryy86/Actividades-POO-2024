def main():
    texto = input("Ingrese una palabra o frase: ")

    texto_limpio = texto.lower().replace(" ", "")

    texto_invertido = texto_limpio[::-1]

    if texto_limpio == texto_invertido:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
main()