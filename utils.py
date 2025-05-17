import locale

from datetime import datetime
from stdnum.do import cedula

locale.setlocale(locale.LC_ALL, "es_DO.UTF-8")

RNC_UNAPEC = "401005107"
NO_CUENTA_UNAPEC = "807931407"

codigos_bancos = [
    "APAP",  # Asociación Popular de Ahorros y Préstamos
    "BHDL",  # Banco BHD León
    "BANR",  # Banco de Reservas
    "SCOT",  # Scotiabank República Dominicana
    "PROM",  # Banco Promerica
    "CIBAO",  # Asociación Cibao de Ahorros y Préstamos
    "ADEMI",  # Banco Ademi
    "CARI",  # Banco Caribe
    "VIMEN",  # Banco Vimenca
    "ALNAP",  # Asociación La Nacional de Ahorros y Préstamos
    "BSCI",  # Banco Santa Cruz
]


def pedir_informacion(mensaje, validacion, mensaje_de_error):
    while True:
        valor = input(mensaje)
        if validacion(valor):
            return valor
        print(mensaje_de_error)


def guardar_en_archivo(nombre_archivo, lineas):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for linea in lineas:
            archivo.write(linea + "\n")

    print("Archivo creado correctamente.")


def leer_archivo(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lineas = []
        for linea in archivo:
            lineas.append(linea.split(","))

    return lineas


def format_date(date):
    return datetime.strptime(date, "%Y%m%d").strftime("%d/%m/%y")


def print_title(title):
    print(f"\n==== {title} ====")


def format_cedula(cedula_raw):
    return cedula.format(cedula_raw)


def format_monto(monto):
    return locale.currency(int(monto), grouping=True)


def formatear_encabezado(row):
    row[1] = format_date(row[1])
    row[-1] = format_monto(row[-1])


def formatear_detalle(detalles):
    for row in detalles:
        row[0] = format_cedula(row[0])
        row[2] = format_monto(row[2])
        row[3] = "Cuenta Corriente" if row[3] == "C" else "Cuenta de Ahorros"
