from utils import leer_archivo, print_title, formatear_encabezado, formatear_detalle
from tabulate import tabulate

HEADERS_ENCABEZADO = [
    "RNC",
    "Fecha de Proceso",
    "Cantidad de Empleados",
    "No. de Cuenta",
    "Código del Banco",
    "Referencia del Pago",
    "Monto Total",
]

HEADERS_DETALLE = [
    "Cédula del Empleado",
    "No. de Cuenta",
    "Monto a Pagar",
    "Tipo de Cuenta",
    "Código del Banco Destino",
]


def main():
    try:
        lineas = leer_archivo("nomina-unapec-2025.txt")
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return 1
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return 1

    encabezado = [row[1:] for row in lineas if row[0] == "E"]
    detalles = [row[1:] for row in lineas if row[0] == "D"]

    if not encabezado:
        print("No se encontró información de encabezado válida.")
        return 1

    if not detalles:
        print("No se encontró información de detalles válida.")
        return 1

    formatear_encabezado(encabezado[0])

    print_title("Encabezado")
    print(tabulate(encabezado, headers=HEADERS_ENCABEZADO, tablefmt="grid"))

    formatear_detalle(detalles)

    print_title("Detalle")
    print(tabulate(detalles, headers=HEADERS_DETALLE, tablefmt="grid"))

    return 0


if __name__ == "__main__":
    main()
