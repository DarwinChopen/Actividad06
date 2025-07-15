productos={}
cantidad=int(input("Ingrese la cantidad de productos"))

for i in range(cantidad):
    print(f"Productos: {i+1}")
    while True:
        codigoProducto=input("Ingrese el Codigo del Producto: ")
        if codigoProducto in productos:
            print("Este codigo ya existe, Ingrese otro")
        else:
            break
    nombreProducto=input("Ingrese el Nombre del Producto: ")
    categoriaProducto=input("Ingrese la Categoria del producto: ")
    talla=input("Ingrese la talla: ")
    while True:
        precioProducto=float(input("Ingrese el precio del Producto: "))
        if precioProducto<0:
            print("El precio debe ser mayor que 0")
        else:
            break
    while True:
        cantidadStock = int(input("Ingrese la cantidad en stock: "))
        if cantidadStock<0:
            print("La cantidad en stock debe ser positiva")
        else:
            break

    productos[codigoProducto]={
        "nombre":nombreProducto,
        "categoria":categoriaProducto,
        "talla":talla,
        "precio":precioProducto,
        "stock":cantidadStock
    }
print(f"Listado de Productos")
for codigoProducto,datos in productos.items():

    print(f"Codigo {codigoProducto}")
    print(f"Nombre: {datos["nombre"]}")
    print(f"Categoria: {datos["categoria"]}")
    print(f"Talla: {datos["talla"]}")
    print(f"Precio: {datos["precio"]}")
    print(f"Stock: {datos["stock"]}")
print("Busqueda de producto")
buscado=input("Ingrese el codigo a buscar: ")
if buscado in productos:
    print(f"Nombre: {productos[buscado]["nombre"]}")
    print(f"Categoria: {productos[buscado]["categoria"]}")
    print(f"Talla: {productos[buscado]["talla"]}")
    print(f"Precio: {productos[buscado]["precio"]}")
    print(f"Stock: {productos[buscado]["stock"]}")

print("Inventario")
total=0
for codigoProducto,datos in productos.items():
    subtotal=datos["precio"]*datos["stock"]
    total+=subtotal
    print(f"Codigo {codigoProducto}")
    print(f"Nombre: {datos["nombre"]}")
    print(f"Categoria: {datos["categoria"]}")
    print(f"Talla: {datos["talla"]}")
    print(f"Precio: {datos["precio"]}")
    print(f"Stock: {datos["stock"]}")
    print(f"Subtotal: {subtotal}")
print(f"Total del inverntario es: {total}")

print("Por Categoria")




