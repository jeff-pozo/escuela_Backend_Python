
colones = input("Ingresa tu cantidad de Colones: ")
colones = float(colones)
precio_dolar = 687.04
conversion = colones / precio_dolar
conversion = round(conversion, 2)
conversion = str(conversion)
print("Tu dinero equivale a: $" + conversion + " dolares")
