import os

from persistencia import cargar_inventario, guardar_inventario
from inventario import (
    registrar_producto,
    consultar_producto,
    modificar_producto,
    eliminar_producto
)
from ventas import registrar_venta
from reportes import mostrar_alertas, generar_cierre


# Rutas de los archivos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RUTA_INVENTARIO = os.path.join(
    BASE_DIR, "data", "inventario.txt"
)

RUTA_VENTAS = os.path.join(
    BASE_DIR, "data", "ventas.txt"
)


def mostrar_menu():
    print("\n================================")
    print("       TIENDAPY - DON AURELIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Consultar productos")
    print("3. Modificar producto")
    print("4. Eliminar producto")
    print("5. Registrar venta")
    print("6. Alertas de inventario")
    print("7. Cierre del día")
    print("8. Guardar inventario")
    print("9. Salir")
    print("================================")


def main():
    os.makedirs(os.path.dirname(RUTA_INVENTARIO), exist_ok=True)

    inventario = cargar_inventario(RUTA_INVENTARIO)

    print("\n¡Bienvenido a TiendaPy!")
    print("Inventario cargado:", len(inventario), "productos.")

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                registrar_producto(inventario)
                guardar_inventario(inventario, RUTA_INVENTARIO)

            elif opcion == "2":
                consultar_producto(inventario)

            elif opcion == "3":
                modificar_producto(inventario)
                guardar_inventario(inventario, RUTA_INVENTARIO)

            elif opcion == "4":
                eliminar_producto(inventario)
                guardar_inventario(inventario, RUTA_INVENTARIO)

            elif opcion == "5":
                registrar_venta(inventario, RUTA_VENTAS)
                guardar_inventario(inventario, RUTA_INVENTARIO)

            elif opcion == "6":
                mostrar_alertas(inventario)

            elif opcion == "7":
                generar_cierre(inventario, RUTA_VENTAS)

            elif opcion == "8":
                guardar_inventario(inventario, RUTA_INVENTARIO)
                print("Inventario guardado correctamente.")

            elif opcion == "9":
                guardar_inventario(inventario, RUTA_INVENTARIO)
                print("Inventario guardado.")
                print("¡Gracias por utilizar TiendaPy!")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()