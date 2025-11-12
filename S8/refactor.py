def pedir_numero(mensaje):
    """Pide un número entero al usuario y maneja errores de entrada."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Por favor, introduce un número positivo.")
                continue
            return valor
        except ValueError:
            print("Error: debes introducir un número entero.")


def obtener_notas(cantidad):
    """Solicita las notas de los alumnos y las guarda en una lista."""
    notas = []
    for i in range(cantidad):
        nota = pedir_numero(f"Nota del alumno {i + 1}: ")
        while nota > 10:  # Validamos rango de 0 a 10
            print("La nota debe estar entre 0 y 10.")
            nota = pedir_numero(f"Nota del alumno {i + 1}: ")
        notas.append(nota)
    return notas


def calcular_media(notas):
    """Calcula la media de una lista de notas."""
    if not notas:
        return 0
    return sum(notas) / len(notas)


def mostrar_aprobados(notas):
    """Muestra las notas aprobadas (>= 5)."""
    aprobados = [n for n in notas if n >= 5]
    if aprobados:
        print(f"Ha aprobado: {len(aprobados)} {"alumnos." if len(aprobados)>1 else "alumno"}")
    else:
        print("No hay alumnos aprobados.")


def programa():
    """Programa principal."""
    print("=== Cálculo de media y aprobados ===")
    n = pedir_numero("¿Cuántos alumnos? ")
    notas = obtener_notas(n)
    media = calcular_media(notas)
    print(f"\nMedia de la clase: {media:.2f}")
    mostrar_aprobados(notas)


# Ejecución del programa
if __name__ == "__main__":
    try:
        programa()
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
