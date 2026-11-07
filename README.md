TiendaPy – Tienda Don Aurelio

Descripción

TiendaPy es una aplicación de consola desarrollada en Python para gestionar el inventario, registrar ventas, controlar existencias y generar reportes diarios de una tienda de barrio.

Objetivo

Facilitar la administración de productos y ventas, reducir errores de cálculo y conservar la información mediante archivos de texto plano.

Requisitos

- Python 3.10 o superior.
- Visual Studio Code o cualquier editor de código.
- No requiere dependencias externas.

Funcionalidades

1. Registro de productos.
2. Consulta por código y categoría.
3. Modificación de precios y stock.
4. Eliminación de productos.
5. Registro de ventas con varios productos.
6. Aplicación de descuentos del 5 % y 10 %.
7. Cálculo de pago y cambio.
8. Validación de existencias.
9. Alertas de stock bajo y productos agotados.
10. Cierre diario de ventas.
11. Persistencia de inventario e historial de ventas.

Estructura del proyecto

- "src/main.py": menú principal.
- "src/inventario.py": gestión de productos.
- "src/ventas.py": registro de ventas y descuentos.
- "src/reportes.py": alertas y cierre diario.
- "src/persistencia.py": lectura y escritura de archivos.
- "src/validaciones.py": validación de datos.
- "data/inventario.txt": información de productos.
- "data/ventas.txt": historial de ventas.

Ejecución

Desde la carpeta principal ejecutar:

python src/main.py

En Windows también se puede ejecutar:

py src/main.py

Persistencia

La información del inventario se almacena en "data/inventario.txt" y las ventas se guardan en "data/ventas.txt".

Los datos permanecen disponibles al cerrar y volver a ejecutar el programa.

Descuentos

- Compras desde $50.000 COP: 5 %.
- Compras desde $100.000 COP: 10 %.

Uso del sistema

Al ejecutar el programa, se mostrará un menú principal con las opciones disponibles.

El usuario podrá registrar, consultar, modificar y eliminar productos, registrar ventas, consultar alertas de inventario y generar el cierre diario.

La información se almacena automáticamente en archivos de texto plano dentro de la carpeta data.

Autores
Francy Daniela Quintero Bravo - 20262020143
Proyecto desarrollado para el curso Python 0 a 100 – Curso ACM.