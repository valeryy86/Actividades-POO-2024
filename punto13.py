def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    calculo= int(input(" 1. suma \n 2. resta \n 3. multiplicación \n 4. división. \n Elija una opción: "))

    if calculo == 1:
        suma = num1 + num2 
        print (f"el resultado es: {suma}")
    elif calculo == 2 :
        resta = num1 - num2 
        print (f"el resultado es: {resta}")
    elif calculo == 3 :
        multiplicación = num1 * num2 
        print (f"el resultado es: {multiplicación}")
    elif calculo == 4 :
        división = num1 / num2 
        print (f"el resultado es: {división}")
main()