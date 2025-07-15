
while True:
    print("Menu ejercicio Diccionaroos")
    print("1. Agregar Productos")
    print("2. Listado productos")
    print("3. Buscar Productos")
    print("4. Inventario")
    print("5. Salir")
    try:
        opcion=int(input("Ingrese una Opcion: "))
    except ValueError:
        print("Ingrese un entero")
    match opcion:
        case 1:
            productos = {}
            cantidad = int(input(f"\nIngrese la cantidad de productos: "))

            for i in range(cantidad):
                print(f"\nProducto # {i + 1}:")
                while True:
                    codigoProducto = input(f"\nIngrese el Codigo del Producto: ")
                    if codigoProducto in productos:
                       print("Este codigo ya existe, Ingrese otro")
                    else:
                       break
                nombreProducto = input("Ingrese el Nombre del Producto: ")
                categoriaProducto = input("Ingrese la Categoria del producto: ")
                talla = input("Ingrese la talla: ")
                while True:
                    precioProducto = float(input("Ingrese el precio del Producto: "))
                    if precioProducto < 0:
                       print("El precio debe ser mayor que 0")
                    else:
                       break
                while True:
                    cantidadStock = int(input("Ingrese la cantidad en stock: "))
                    if cantidadStock < 0:
                       print("La cantidad en stock debe ser positiva")
                    else:
                        break

                productos[codigoProducto] = {
                    "nombre": nombreProducto,
                    "categoria": categoriaProducto,
                    "talla": talla,
                    "precio": precioProducto,
                    "stock": cantidadStock
                }
        case 2:
             print(f"\nListado de Productos")
             for codigoProducto, datos in productos.items():
               print(f"\nCodigo {codigoProducto}")
               print(f"Nombre: {datos["nombre"]}")
               print(f"Categoria: {datos["categoria"]}")
               print(f"Talla: {datos["talla"]}")
               print(f"Precio: {datos["precio"]}")
               print(f"Stock: {datos["stock"]}")
        case 3:
             buscado = input(f"\nIngrese el codigo a buscar: ")
             if buscado in productos:
               print(f"\nNombre: {productos[buscado]["nombre"]}")
               print(f"Categoria: {productos[buscado]["categoria"]}")
               print(f"Talla: {productos[buscado]["talla"]}")
               print(f"Precio: {productos[buscado]["precio"]}")
               print(f"Stock: {productos[buscado]["stock"]}")
        case 4:
             print(f"\nInventario")
             total = 0
             for codigoProducto, datos in productos.items():
                 subtotal = datos["precio"] * datos["stock"]
                 total += subtotal
                 print(f"\nCodigo {codigoProducto}")
                 print(f"Nombre: {datos["nombre"]}")
                 print(f"Categoria: {datos["categoria"]}")
                 print(f"Talla: {datos["talla"]}")
                 print(f"Precio: {datos["precio"]}")
                 print(f"Stock: {datos["stock"]}")
                 print(f"Subtotal: {subtotal}")
             print(f"Total del inverntario es: {total}")
        case 5:
            print("Saliendo...")
            break
        case _:
             print("Opcion invalida")




