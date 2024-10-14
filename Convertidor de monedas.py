def obtener_tasa(matriz, moneda):
    # Encuentra el índice de la moneda en la primera fila
    if moneda in matriz[0]:
        indice = matriz[0].index(moneda)
        return matriz[1][indice]
    else:
        return None

def convertir_moneda(pesos, tasa):
    return pesos * tasa

def solicitar_datos():
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

matriz_conversion = [
    ["libras", "euros", "dolares"],
    [0.041, 0.050, 0.055]
]

lista_pesos, lista_opcion = solicitar_datos()

for i in range(len(lista_pesos)):
    pesos = lista_pesos[i]
    opcion = lista_opcion[i]
    tasa = obtener_tasa(matriz_conversion, opcion)
    if tasa is not None:
        convertido = convertir_moneda(pesos, tasa)
        print(f"{pesos} pesos mexicanos equivalen a {convertido:.2f} {opcion}.")
    else:
        print(f"Opción no válida en la posición {i+1}.")

print("Fin")
