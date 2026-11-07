def validar_texto(mensaje):
    while True:
        dato = input(mensaje).strip()

        if dato:
            return dato

        print("Error: este campo no puede estar vacío.")


def validar_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero <= 0:
                print("Error: ingrese un número mayor que cero.")
            else:
                return numero

        except ValueError:
            print("Error: debe ingresar un número entero.")


def validar_decimal(mensaje):
    while True:
        try:
            numero = float(input(mensaje))

            if numero <= 0:
                print("Error: ingrese un número mayor que cero.")
            else:
                return numero

        except ValueError:
            print("Error: debe ingresar un número válido.")