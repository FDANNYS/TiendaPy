from validaciones import validar_texto, validar_entero, validar_decimal


def registrar_producto(inventario):
    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = validar_texto("Código del producto: ").upper()

    for producto in inventario:
        if producto["codigo"] == codigo:
            raise ValueError("Ya existe un producto con ese código.")

    nombre = validar_texto("Nombre: ")
    categoria = validar_texto("Categoría: ")
    precio = validar_decimal("Precio: ")
    stock = validar_entero("Stock inicial: ")
    stock_minimo = validar_entero("Stock mínimo: ")
    proveedor = validar_texto("Proveedor: ")

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "stock_minimo": stock_minimo,
        "proveedor": proveedor
    }

    inventario.append(producto)

    print("\nProducto registrado correctamente.")


def consultar_producto(inventario):
    print("\n--- CONSULTAR PRODUCTO ---")
    print("1. Buscar por código")
    print("2. Buscar por categoría")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        codigo = input("Ingrese el código: ").strip().upper()

        resultados = [
            p for p in inventario
            if p["codigo"] == codigo
        ]

    elif opcion == "2":
        categoria = input("Ingrese la categoría: ").strip().lower()

        resultados = [
            p for p in inventario
            if p["categoria"].lower() == categoria
        ]

    else:
        print("Opción no válida.")
        return

    if not resultados:
        print("No se encontraron productos.")
        return

    for producto in resultados:
        mostrar_producto(producto)


def mostrar_producto(producto):
    print("\n------------------------------")
    print("Código:", producto["codigo"])
    print("Nombre:", producto["nombre"])
    print("Categoría:", producto["categoria"])
    print("Precio: $", producto["precio"])
    print("Stock:", producto["stock"])
    print("Stock mínimo:", producto["stock_minimo"])
    print("Proveedor:", producto["proveedor"])
    print("------------------------------")


def modificar_producto(inventario):
    print("\n--- MODIFICAR PRODUCTO ---")

    codigo = input("Código del producto: ").strip().upper()

    for producto in inventario:
        if producto["codigo"] == codigo:

            print("Producto encontrado:")
            mostrar_producto(producto)

            print("\n¿Qué desea modificar?")
            print("1. Precio")
            print("2. Stock")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                producto["precio"] = validar_decimal(
                    "Nuevo precio: "
                )

            elif opcion == "2":
                producto["stock"] = validar_entero(
                    "Nuevo stock: "
                )

            else:
                print("Opción no válida.")
                return

            print("Producto modificado correctamente.")
            return

    print("No se encontró el producto.")


def eliminar_producto(inventario):
    print("\n--- ELIMINAR PRODUCTO ---")

    codigo = input("Código del producto: ").strip().upper()

    for producto in inventario:
        if producto["codigo"] == codigo:

            mostrar_producto(producto)

            confirmacion = input(
                "¿Está seguro de eliminarlo? (S/N): "
            ).strip().upper()

            if confirmacion == "S":
                inventario.remove(producto)
                print("Producto eliminado correctamente.")
            else:
                print("Operación cancelada.")

            return

    print("No se encontró el producto.")