def mostrar_menu():
    print("\n1. Insertar cliente.")
    print("2. Modificar cliente.")
    print("3. Eliminar registro.")
    print("4. Ver todos los clientes")
    print("5. Sumatorio de precios")
    print("0. Salir.")

def crear_cliente():
    try:
        cliente = {}
        cliente["Nombre"] = input("Introduce el nombre del cliente que quieres agregar: ")
        cliente["Número"] = input("Introduce el número de teléfono del cliente: ")
        cliente["Suscripción"] = float(input("Introduce la suscripción del cliente: "))
    except ValueError:
        print("Dato introducido incorrecto")
    else:
        return cliente

def mostrar_clientes(p_clientes):
    print("\nClientes: ")
    for cliente in p_clientes:
        print(cliente)

def buscar_cliente(p_clientes): 
    try:
        indice = int(input("Introduce la posición (1-X) donde se encuentra el cliente a modificar: ")) -1
        if(0 > indice or indice >= len(p_clientes)):
            raise IndexError
    except IndexError:
        print("El índice introducido no se encuentra dentro de la lista.")
    except ValueError:
        print("Dato introducido incorrecto.")
    else:
        return p_clientes[indice]
    
def modificar_cliente(cliente):
    try:
        cliente["Nombre"] = input("Introduce el nuevo nombre: ") or cliente["Nombre"]
        cliente["Número"] = input("Introduce el nuevo número: ") or cliente["Número"]
        cliente["Suscripción"] = float(input("Introduce la nueva suscripción: ")) or cliente["Suscripción"]
    except ValueError:
        print("Dato introducido incorrecto.")
    else:
        return cliente

def sumar_suscripciones(p_clientes):
    suma = 0
    for cliente in p_clientes:
        suma += cliente["Suscripción"]
    return suma

def main():
    clientes = []
    while True:
        mostrar_menu()
        opcion = int(input("Elije la operación que deseas realizar: "))
        if opcion == 1:
            clientes.append(crear_cliente())
                
        elif opcion == 2:
            if clientes:
                mostrar_clientes(clientes)
                cliente = buscar_cliente(clientes)    
                clientes.append(modificar_cliente(cliente))
            else:
                print("\nNo hay clientes para modificar.") 


        elif opcion == 3:
            if clientes:
                mostrar_clientes(clientes)
                cliente = buscar_cliente(clientes)
                clientes.remove(cliente)
                print(f"Cliente eliminado.")
            else:
                print("\nNo hay clientes para eliminar.")

        elif opcion == 4:
            if clientes:
                mostrar_clientes(clientes)
            else:
                print("\nNo hay clientes en la lista.")

        elif opcion == 5:
            if clientes:
                print(f"La suma total de las suscripciones es {sumar_suscripciones(clientes)}")
            else:
                print("\nNo hay clientes en la lista.")
                
        elif opcion == 0:
            print("\nSaliendo del programa...")
            break
        
        else:
            print("\nOpción no válida, por favor selecciona una opción del menú.")
main()