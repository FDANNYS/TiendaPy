from datetime import date


def mostrar_alertas(inventario):
    print("\n--- ALERTAS DE INVENTARIO ---")

    proveedores = {}

    for producto in inventario:
        if producto["stock"] <= producto["stock_minimo"]:

            proveedor = producto["proveedor"]

            if proveedor not in proveedores:
                proveedores[proveedor] = []

            proveedores[proveedor].append(producto)

    if not proveedores:
        print("No hay productos que necesiten reabastecimiento.")
        return

    for proveedor, productos in proveedores.items():
        print(f"\nProveedor: {proveedor}")

        for producto in productos:
            estado = "AGOTADO" if producto["stock"] == 0 else "REABASTECER"

            print(
                f"{producto['codigo']} - {producto['nombre']} "
                f"| Stock: {producto['stock']} "
                f"| Mínimo: {producto['stock_minimo']} "
                f"| Estado: {estado}"
            )


def cargar_ventas_del_dia(ruta):
    ventas = []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:

            for linea in archivo:
                datos = linea.strip().split("|")

                if len(datos) != 3:
                    continue

                if datos[0] == date.today().isoformat():
                    try:
                        venta = {
                            "fecha": datos[0],
                            "total": float(datos[1]),
                            "detalle": datos[2]
                        }

                        ventas.append(venta)

                    except ValueError:
                        continue

    except FileNotFoundError:
        print("Todavía no existe el historial de ventas.")

    return ventas


def generar_cierre(inventario, ruta):
    print("\n--- CIERRE DEL DIA ---")

    ventas = cargar_ventas_del_dia(ruta)

    if not ventas:
        print("No se registraron ventas durante el día.")
        return

    total_vendido = 0
    cantidades_vendidas = {}
    categorias = set()

    for venta in ventas:
        total_vendido += venta["total"]

        productos_venta = venta["detalle"].split(";")

        for elemento in productos_venta:
            try:
                codigo, cantidad = elemento.split(":")
                cantidad = int(cantidad)

                cantidades_vendidas[codigo] = (
                    cantidades_vendidas.get(codigo, 0) + cantidad
                )

                for producto in inventario:
                    if producto["codigo"] == codigo:
                        categorias.add(producto["categoria"])

            except ValueError:
                continue

    numero_ventas = len(ventas)
    ticket_promedio = total_vendido / numero_ventas

    print("Fecha:", date.today())
    print("Total vendido: $", total_vendido)
    print("Número de ventas:", numero_ventas)
    print("Ticket promedio: $", round(ticket_promedio, 2))

    if cantidades_vendidas:
        codigo_mas_vendido = max(
            cantidades_vendidas,
            key=cantidades_vendidas.get
        )

        nombre = codigo_mas_vendido

        for producto in inventario:
            if producto["codigo"] == codigo_mas_vendido:
                nombre = producto["nombre"]
                break

        print(
            "Producto más vendido:",
            nombre,
            "- Unidades:",
            cantidades_vendidas[codigo_mas_vendido]
        )

    print("\n--- PRODUCTOS SIN VENTAS ---")

    productos_sin_ventas = [
        producto for producto in inventario
        if producto["codigo"] not in cantidades_vendidas
    ]

    if productos_sin_ventas:
        for producto in productos_sin_ventas:
            print(producto["nombre"])
    else:
        print("Todos los productos tuvieron ventas.")

    print("\n--- CATEGORIAS CON MOVIMIENTO ---")

    if categorias:
        for categoria in sorted(categorias):
            print(categoria)
    else:
        print("No hubo movimiento por categorías.")