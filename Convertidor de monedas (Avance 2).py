# Tasas de conversión
tasa_libras = 0.041
tasa_euros = 0.050
tasa_dolares = 0.055

# Entrada de usuario
pesos = float(input("Ingresa la cantidad en pesos mexicanos: "))
opcion = input("Selecciona la moneda (libras, euros, dolares): ").lower()

# Conversión
if opcion == "libras":
    convertido = pesos * tasa_libras
elif opcion == "euros":
    convertido = pesos * tasa_euros
elif opcion == "dolares":
    convertido = pesos * tasa_dolares
else:
    convertido = None
    print("Opción no válida.")

# Salida
if convertido is not None:
    print(f"{pesos} pesos mexicanos equivalen a {convertido:.2f} {opcion}.")