from datetime import date
from validaciones import validar_entero


def calcular_descuento(subtotal):
    if subtotal >= 100000:
        return subtotal * 0.10
    elif subtotal >= 50000:
        return subtotal * 0.05
    else:
        return 0


def registrar_venta(inventario, ruta):
    print("\n--- REGISTRO DE VENTA ---")

    carrito = []
    subtotal = 0

    while True:
        codigo = input(
            "\nCódigo del producto (o FIN para terminar): "
        ).strip().upper()

        if codigo == "FIN":
            break

        producto_encontrado = None

        for producto in inventario:
            if producto["codigo"] == codigo:
                producto_encontrado = producto
                break

        if producto_encontrado is None:
            print("Producto no encontrado.")
            continue

        cantidad = validar_entero("Cantidad: ")

        cantidad_en_carrito = 0

        for item in carrito:
            if item["producto"]["codigo"] == codigo:
                cantidad_en_carrito += item["cantidad"]

        if cantidad + cantidad_en_carrito > producto_encontrado["stock"]:
           raise ValueError(
                "No hay suficiente stock disponible. "
                "La venta fue cancelada."
            )
           
        carrito.append({
            "producto": producto_encontrado,
            "cantidad": cantidad
        })

        subtotal += producto_encontrado["precio"] * cantidad

        print("Producto agregado al carrito.")

    if not carrito:
        print("No se registró ninguna venta.")
        return

    print("\n--- RESUMEN DE VENTA ---")

    for item in carrito:
        producto = item["producto"]
        cantidad = item["cantidad"]
        valor = producto["precio"] * cantidad

        print(
            producto["nombre"],
            "| Cantidad:", cantidad,
            "| Valor: $", valor
        )

    descuento = calcular_descuento(subtotal)
    total = subtotal - descuento

    print("\nSubtotal: $", subtotal)
    print("Descuento: $", descuento)
    print("Total a pagar: $", total)

    while True:
        try:
            pago = float(input("Dinero recibido: "))

            if pago <= 0:
                print("El pago debe ser mayor que cero.")
            elif pago < total:
                print("El pago es insuficiente. Intente nuevamente.")
            else:
                break
            
        except ValueError:
            print("Ingrese un valor numérico válido.")

    cambio = pago - total

    print("Cambio: $", cambio)

    confirmacion = input("¿Desea confirmar la venta? (S/N): ").strip().upper()
    while confirmacion not in ("S", "N"):
        print("Opción no válida.")
        confirmacion = input("¿Desea confirmar la venta? (S/N): ").strip().upper()

    if confirmacion == "N":
        print("Venta cancelada. No se modificó el inventario.")
        return

    for item in carrito:
        producto = item["producto"]
        producto["stock"] -= item["cantidad"]

    guardar_venta(ruta, total, carrito)

    print("\n¡Venta registrada correctamente!")


def guardar_venta(ruta, total, carrito):
    fecha = date.today().isoformat()

    detalle = []

    for item in carrito:
        codigo = item["producto"]["codigo"]
        cantidad = item["cantidad"]

        detalle.append(f"{codigo}:{cantidad}")

    linea = f"{fecha}|{total}|{';'.join(detalle)}\n"

    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(linea)