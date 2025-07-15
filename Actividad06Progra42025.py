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
