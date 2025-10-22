tienda = {}
while True:
    try:
        print("\n1. Insertar producto.")
        print("2. Modificar producto.")
        print("3. Eliminar registro.")
        print("4. Ver todos los productos")
        print("5. Sumatorio de precios")
        print("0. Salir.")
        opcion = int(input("Elije la operación que deseas realizar: "))
        if opcion == 1:
            producto = input("\nIntroduce el nombre del producto a insertar: ")
            if producto in tienda:
                print("\nEl producto ya existe.")
            else:
                precio = float(input("\nIntroduce el precio del producto: "))
                tienda[producto] = precio
                print(f"\nProducto '{producto}' insertado con precio {precio}.")
                
        elif opcion == 2:
            producto = input("\nIntroduce el nombre del producto a modificar: ")
            if producto in tienda:
                precio = float(input("\nIntroduce el nuevo precio del producto: "))
                tienda[producto] = precio
                print(f"\nProducto '{producto}' modificado con nuevo precio {precio}.")
            else:
                print("\nEl producto no existe.")
                
        elif opcion == 3:
            producto = input("\nIntroduce el nombre del producto a eliminar: ")
            if producto in tienda:
                del tienda[producto]
                print(f"\nProducto '{producto}' eliminado.")
            else:
                print("\nEl producto no existe.")
        
        elif opcion == 4:
            if tienda:
                print("\nLista de productos:")
                for producto, precio in tienda.items():
                    print(f"- {producto}: {precio:.2f}€")
            else:
                print("\nNo hay productos en la tienda.")

        elif opcion == 5:
            if tienda:
                print(f"La suma del precio de todos los productos es: {sum(tienda.values)}")
            else:
                print("No hay productos introducidos.")
                
        elif opcion == 0:
            print("\nSaliendo del programa...")
            break
            
        else:
            print("\nOpción no válida, por favor selecciona una opción del menú.")
        
    except ValueError:
        print("Valor introducido incorrecto")