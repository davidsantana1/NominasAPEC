from utils import pedir_informacion, codigos_bancos


def pedir_datos_detalle():
    print("--- Datos de Nuevo Empleado ---")
    cedula = pedir_informacion(
        "Ingrese la cédula del empleado: ",
        lambda x: len(x) == 11 and x.isdigit(),
        "Cédula incorrecta.",
    )

    cuenta = pedir_informacion(
        "Ingrese el número de cuenta del empleado: ",
        lambda x: len(x) >= 8 and len(x) <= 20 and x.isdigit(),
        "Número de cuenta incorrecto.",
    )

    monto = pedir_informacion(
        "Ingrese el monto a pagar al empleado: ",
        lambda x: x.isdigit() and len(x) <= 10,
        "Monto incorrecto.",
    )

    tipo_cuenta = (
        pedir_informacion(
            "Ingrese el tipo de cuenta ('C' para Cuenta Corriente, 'A' para Cuenta de Ahorros): ",
            lambda x: x.upper() == "C" or x.upper() == "A",
            "Tipo de cuenta incorrecto.",
        )
    ).upper()

    codigo_banco = (
        pedir_informacion(
            "Ingrese el código del banco (APAP, BHDL, BANR, SCOT, etc.): ",
            lambda x: x.upper() in codigos_bancos,
            "Código de banco incorrecto.",
        )
    ).upper()

    return {
        "cedula_empleado": cedula,
        "cuenta_empleado": cuenta,
        "monto_a_pagar": monto,
        "tipo_de_cuenta": tipo_cuenta,
        "codigo_banco_destino": codigo_banco,
    }


def crear_detalle(
    cedula_empleado,
    cuenta_empleado,
    monto_a_pagar,
    tipo_de_cuenta,
    codigo_banco_destino,
):
    return f"D{cedula_empleado}{cuenta_empleado.zfill(20)}{monto_a_pagar.zfill(10)}{tipo_de_cuenta}{codigo_banco_destino}"
