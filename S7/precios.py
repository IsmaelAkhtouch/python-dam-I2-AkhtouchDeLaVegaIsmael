# precios.py
# Programa principal que usa el módulo auxprecios en un menú interactivo
import auxprecios

def pedir_precios():
    """Permite al usuario introducir precios manualmente, con validación."""
    precios = []
    while True:
        entrada = input("Introduce los precios (escribe '0' para terminar): ")
        if entrada == "0":
            break
        try:
            precio = float(entrada)
            if precio < 0:
                print("El precio no puede ser negativo. Inténtalo de nuevo.")
            else:
                precios.append(precio)
        except ValueError:
            print("Entrada no válida. Escribe un número.")
    return precios

precios = []  # Lista vacía inicial
while True:
    print("""
    ======== MENÚ DE ANÁLISIS DE PRECIOS ========
    1. Introducir lista de precios
    2. Calcular precio medio
    3. Mostrar precio máximo
    4. Mostrar precio mínimo
    5. Calcular suma total
    6. Mostrar resumen completo
    0. Salir
    =============================================
    """)
    opcion = input("Selecciona una opción (0-6): ")

    if opcion == "1":
        precios = pedir_precios()
        print(f"\nSe han guardado {len(precios)} precios.")
    elif opcion == "2":
        if precios:
            print(f"Precio medio: {auxprecios.precio_medio(precios):.2f}")
        else:
            print("No hay precios cargados.")
    elif opcion == "3":
        if precios:
            print(f"Precio máximo: {auxprecios.precio_maximo(precios):.2f}")
        else:
            print("No hay precios cargados.")
    elif opcion == "4":
        if precios:
            print(f"🪙 Precio mínimo: {auxprecios.precio_minimo(precios):.2f}")
        else:
            print("No hay precios cargados.")
    elif opcion == "5":
        if precios:
            print(f"💵 Suma total: {auxprecios.total_precios(precios):.2f}")
        else:
            print("No hay precios cargados.")
    elif opcion == "6":
        precios = auxprecios.resumen_precios(precios)
        if precios:
            print("Datos generales de los precios listados: ")
            for clave , valor in precios.items():
                print(f"{clave}: {valor}")
        else:
            print("No hay precios cargados.")
    elif opcion == "0":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")


