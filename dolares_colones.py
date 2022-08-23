dolares = input("Ingresa tu cantidad de Dolares: ")
dolares = float(dolares)
precio_colon = 687.04
conversion = dolares * precio_colon
conversion = round(conversion, 2)
conversion = str(conversion)
print("Tu dinero equivale a: " + conversion + "colones")