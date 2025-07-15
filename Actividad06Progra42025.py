productos={}
cantidad=int(input("Ingrese la cantidad de productos"))

for i in range(cantidad):
    print(f"Productos: {i+1}")
    codigoProducto=input("Ingrese el codigo del producto: ")
    nombreProducto=input("Ingrese el Nombre del Producto: ")
    categoriaProducto=input("Ingrese la Categoria del producto: ")
    talla=input("Ingrese la talla: ")
    precioProducto=int(input("Ingrese el precio del producto: "))
    cantidadStock=int(input("Ingrese la cantidad en stock: "))

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


