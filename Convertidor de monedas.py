# Tasas de conversión
TASA_LIBRAS = 0.041
TASA_EUROS = 0.050
TASA_DOLARES = 0.055

def convertir_moneda(pesos, tasa):
    return pesos * tasa

def solicitar_datos():
    pesos = float(input("Ingresa la cantidad en pesos mexicanos: "))
    opcion = input("Selecciona la moneda (libras, euros, dolares): ").lower()
    return pesos, opcion

def obtener_tasa(opcion):
    if opcion == "libras":
        return TASA_LIBRAS
    elif opcion == "euros":
        return TASA_EUROS
    elif opcion == "dolares":
        return TASA_DOLARES
    else:
        return None

# Ejecución del programa
pesos, opcion = solicitar_datos()
tasa = obtener_tasa(opcion)

if tasa is not None:
    convertido = convertir_moneda(pesos, tasa)
    print(f"{pesos} pesos mexicanos equivalen a {convertido:.2f} {opcion}.")
else:
    print("Opción no válida.")

