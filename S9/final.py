import json
import os


def cargar_personajes(archivo="personajes.json"):
    """Carga la lista de personajes desde un archivo JSON."""
    if os.path.exists(archivo):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error al leer el archivo. Se iniciará una lista vacía.")
    return []


def guardar_personajes(personajes, archivo="personajes.json"):
    """Guarda la lista de personajes en un archivo JSON."""
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(personajes, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar los personajes: {e}")


def pedir_entero(mensaje, minimo=None, maximo=None):
    """Pide un número entero validando los posibles errores."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual que {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"El valor debe ser menor o igual que {maximo}.")
                continue
            return valor
        except ValueError:
            print("Error: debes introducir un número entero.")


def crear_personaje():
    """Crea un nuevo personaje."""
    nombre = input("Introduce el nombre del personaje: ").strip()
    ataque = pedir_entero("Ataque (0–100): ", 0, 100)
    defensa = pedir_entero("Defensa (0–100): ", 0, 100)
    vida = pedir_entero("Vida (0–500): ", 0, 500)
    return {"nombre": nombre, "ataque": ataque, "defensa": defensa, "vida": vida}


def mostrar_personajes(personajes):
    """Muestra todos los personajes creados."""
    if not personajes:
        print("No hay personajes creados.")
        return
    print("\n=== LISTA DE PERSONAJES ===")
    for i, p in enumerate(personajes, start=1):
        print(f"{i}. {p['nombre']} | Ataque: {p['ataque']} | Defensa: {p['defensa']} | Vida: {p['vida']}")
    print()


def modificar_personaje(personajes):
    """Permite modificar las estadísticas de un personaje existente."""
    if not personajes:
        print("No hay personajes para modificar.")
        return

    mostrar_personajes(personajes)
    indice = pedir_entero("Selecciona el número del personaje a modificar: ", 1, len(personajes)) - 1
    personaje = personajes[indice]

    print(f"Modificando a {personaje['nombre']}. Deja en blanco si no quieres cambiar un valor.")
    try:
        nuevo_ataque = input(f"Ataque actual ({personaje['ataque']}): ")
        if nuevo_ataque:
            personaje["ataque"] = int(nuevo_ataque)
        nueva_defensa = input(f"Defensa actual ({personaje['defensa']}): ")
        if nueva_defensa:
            personaje["defensa"] = int(nueva_defensa)
        nueva_vida = input(f"Vida actual ({personaje['vida']}): ")
        if nueva_vida:
            personaje["vida"] = int(nueva_vida)
        print("✅ Personaje actualizado correctamente.")
    except ValueError:
        print("Error: introdujiste un valor no válido. No se realizaron cambios.")


def eliminar_personaje(personajes):
    """Elimina un personaje de la lista."""
    if not personajes:
        print("No hay personajes para eliminar.")
        return

    mostrar_personajes(personajes)
    indice = pedir_entero("Selecciona el número del personaje a eliminar: ", 1, len(personajes)) - 1
    eliminado = personajes.pop(indice)
    print(f"✅ Personaje '{eliminado['nombre']}' eliminado correctamente.")


def menu():
    """Muestra el menú principal y gestiona la interacción."""
    personajes = cargar_personajes()

    while True:
        print("\n=== MENÚ DE PERSONAJES ===")
        print("1. Crear personaje")
        print("2. Mostrar personajes")
        print("3. Modificar personaje")
        print("4. Eliminar personaje")
        print("5. Guardar y salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            personaje = crear_personaje()
            personajes.append(personaje)
            print(f"✅ Personaje '{personaje['nombre']}' creado correctamente.")

        elif opcion == "2":
            mostrar_personajes(personajes)

        elif opcion == "3":
            modificar_personaje(personajes)

        elif opcion == "4":
            eliminar_personaje(personajes)

        elif opcion == "5":
            guardar_personajes(personajes)
            print("💾 Datos guardados. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    try:
        menu()
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
