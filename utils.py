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
