# TiendaPy – Tienda Don Aurelio

**Sistema de gestión de inventario y ventas desarrollado en Python.**

## 1\. Descripción

TiendaPy es una aplicación de consola desarrollada en Python para gestionar el inventario, registrar ventas, controlar existencias y generar reportes diarios de una tienda de barrio.

## 2\. Objetivo

Facilitar la administración de productos y ventas, reducir errores de cálculo y conservar la información mediante archivos de texto plano.

## 3\. Funcionalidades

- Registro de productos.
- Consulta de productos por código y categoría.
- Modificación de precios y existencias.
- Eliminación de productos.
- Registro de ventas con varios productos.
- Aplicación automática de descuentos.
- Cálculo del pago y cambio.
- Validación de existencias disponibles.
- Alertas de stock mínimo y productos agotados.
- Cierre diario de ventas.
- Almacenamiento persistente del inventario y del historial de ventas.

## 4\. Tecnologías utilizadas

- Python 3.10 o superior.
- Archivos de texto plano.
- Git y GitHub para el control de versiones.

## 5\. Requisitos

- Python 3.10 o superior.
- Visual Studio Code o cualquier editor de código.
- No requiere bibliotecas externas.

## 6\. Estructura del proyecto

``` text
TiendaPy/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── inventario.txt
│   └── ventas.txt
│
└── src/
    ├── main.py
    ├── inventario.py
    ├── ventas.py
    ├── reportes.py
    ├── persistencia.py
    └── validaciones.py
```

## 7\. Instalación y ejecución

Para ejecutar el programa:

1. Descargar o clonar el repositorio.
2. Abrir la carpeta principal del proyecto.
3. Abrir una terminal desde esa ubicación.
4. Ejecutar el siguiente comando:

``` bash
python src/main.py
```

En Windows también se puede utilizar:

``` bash
py src/main.py
```

## 8\. Sistema de descuentos

El programa aplica los siguientes descuentos según el subtotal de la compra:

| Valor de compra | Descuento |
| --- | ---: |
| Desde $50.000 COP | 5 % |
| Desde $100.000 COP | 10 % |

## 9\. Persistencia de datos

La información se almacena en archivos de texto dentro de la carpeta `data`:

- `inventario.txt`: almacena los productos y sus existencias.
- `ventas.txt`: conserva el historial de ventas realizadas.

Los datos permanecen disponibles al cerrar y volver a ejecutar el programa.

## 10\. Autora

**Francy Daniela Quintero Bravo**

Código estudiantil: 20262020143

Proyecto desarrollado para el curso **Python 0 a 100 – Curso ACM**.

---

**Proyecto académico – TiendaPy | Tienda Don Aurelio**
