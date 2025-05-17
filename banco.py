from utils import leer_archivo, format_date, print_title, format_cedula, format_monto
from tabulate import tabulate


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

    procesar_encabezado(encabezado[0])

    print_title("Encabezado")
    print(tabulate(encabezado, headers=["RNC", "Fecha de Proceso", "Cantidad de Empleados", "No. de Cuenta", "Código del Banco", "Referencia del Pago","Monto Total"], tablefmt="grid"))

    procesar_detalle(detalles)

    print_title("Detalle")

    print(tabulate(detalles, headers=["Cédula del Empleado", "No. de Cuenta", "Monto a Pagar", "Tipo de Cuenta", "Código del Banco Destino"], tablefmt="grid"))

    return 0


def procesar_encabezado(row):
    row[1] = format_date(row[1])
    row[-1] = format_monto(row[-1])
    return row


def procesar_detalle(detalles):
    for row in detalles:
        row[0] = format_cedula(row[0])
        row[2] = format_monto(row[2])
        row[3] = "Cuenta Corriente" if row[3] == "C" else "Cuenta de Ahorros"
    return row


if (__name__ == "__main__"):
    main()