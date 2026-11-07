def cargar_inventario(ruta):
    inventario = []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for numero, linea in enumerate(archivo, start=1):

                if not linea.strip():
                    continue

                datos = linea.strip().split("|")

                if len(datos) != 7:
                    print(f"Advertencia: línea {numero} incorrecta.")
                    continue

                try:
                    producto = {
                        "codigo": datos[0],
                        "nombre": datos[1],
                        "categoria": datos[2],
                        "precio": float(datos[3]),
                        "stock": int(datos[4]),
                        "stock_minimo": int(datos[5]),
                        "proveedor": datos[6]
                    }

                    inventario.append(producto)

                except ValueError:
                    print(f"Advertencia: datos incorrectos en la línea {numero}.")

    except FileNotFoundError:
        print("No se encontró el archivo de inventario.")

    return inventario


def guardar_inventario(inventario, ruta):
    with open(ruta, "w", encoding="utf-8") as archivo:

        for producto in inventario:
            linea = (
                f"{producto['codigo']}|"
                f"{producto['nombre']}|"
                f"{producto['categoria']}|"
                f"{producto['precio']}|"
                f"{producto['stock']}|"
                f"{producto['stock_minimo']}|"
                f"{producto['proveedor']}\n"
            )

            archivo.write(linea)