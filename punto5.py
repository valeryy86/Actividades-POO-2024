def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F es igual a {celsius:.2f}°C")

temp_f = float(input("Ingrese la temperatura en Fahrenheit: "))
fahrenheit_a_celsius(temp_f)