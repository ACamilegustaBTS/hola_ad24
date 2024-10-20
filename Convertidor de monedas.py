matriz_conversion = [
    ["libras", "euros", "dolares"],
    [0.041, 0.050, 0.055]
]

def obtener_tasa(matriz, moneda):
    """ Obtiene la tasa de conversión de la moneda dada desde la matriz de conversiones.
    Parámetros:
    matriz: Matriz que contiene las tasas de conversión.
    moneda: La moneda para la cual se quiere obtener la tasa de conversión.
    Regresa:
    La tasa de conversión de la moneda, o None si la moneda no está en la matriz."""
    if moneda in matriz[0]:
        indice = matriz[0].index(moneda)
        return matriz[1][indice]
    else:
        return None

def convertir_moneda(pesos, tasa):
    """Convierte una cantidad en pesos mexicanos a otra moneda usando la tasa de conversión.
    Parámetros:
    pesos: La cantidad en pesos mexicanos.
    tasa: La tasa de conversión.
    Regresa:
    La cantidad convertida a la otra moneda."""
    return pesos * tasa

def solicitar_datos():
    """Solicita al usuario que ingrese cantidades en pesos mexicanos y la moneda a convertir.
    Regresa:
    Dos listas, una con las cantidades en pesos y otra con las monedas convertidas."""
    lista_pesos = []
    lista_opcion = []

    while True:
        pesos = float(input("Ingresa la cantidad en pesos mexicanos: "))
        opcion = input("Selecciona la moneda (libras, euros, dolares): ").lower()
        
        lista_pesos.append(pesos)
        lista_opcion.append(opcion)
        
        continuar = input("¿Deseas agregar otra conversión? (si/no): ").lower()
        if continuar != "si":
            break

    return lista_pesos, lista_opcion

lista_pesos, lista_opcion = solicitar_datos()
for i in range(len(lista_pesos)):
    pesos = lista_pesos[i]
    opcion = lista_opcion[i]
    tasa = obtener_tasa(matriz_conversion, opcion)
    if tasa is not None:
        convertido = convertir_moneda(pesos, tasa)
        print(f"{pesos} pesos mexicanos son {convertido:.2f} {opcion}")
    else:
        print(f"Tasa de conversión no disponible para {opcion}")
