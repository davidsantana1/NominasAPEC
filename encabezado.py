from datetime import datetime
from utils import pedir_informacion, codigos_bancos, NO_CUENTA_UNAPEC, RNC_UNAPEC


def pedir_datos_encabezado():
    empleados = pedir_informacion(
        "¿Cuántos empleados desea registrar? ",
        lambda x: x.isdigit() and 0 < int(x) <= 99999,
        "Cantidad incorrecta.",
    )

    codigo_banco = (
        pedir_informacion(
            "Ingrese el código del banco (APAP, BHDL, BANR, SCOT, etc.): ",
            lambda x: x.upper() in codigos_bancos,
            "Código de banco incorrecto.",
        )
    ).upper()

    referencia_pago = pedir_informacion(
        "Ingrese la referencia del pago (Ej: QUINCENA0525): ",
        lambda x: 0 < len(x) <= 15,
        "Referencia incorrecta. La referencia no puede estar vacía ni tener más de 15 caracteres.",
    )

    monto_total = pedir_informacion(
        "Ingrese el monto total (sin puntos ni comas): ",
        lambda x: x.isdigit() and len(x) <= 12,
        "Monto incorrecto.",
    )

    return {
        "cantidad_de_empleados": empleados,
        "codigo_del_banco": codigo_banco,
        "referencia_del_pago": referencia_pago,
        "total_de_monto": monto_total,
    }


def crear_encabezado(
    cantidad_de_empleados, codigo_del_banco, referencia_del_pago, total_de_monto
):
    fechaProceso = datetime.today().strftime("%Y%m%d")

    return f"E{RNC_UNAPEC}{fechaProceso}{cantidad_de_empleados.zfill(5)}{NO_CUENTA_UNAPEC.zfill(20)}{codigo_del_banco}{referencia_del_pago.ljust(15)}{total_de_monto.zfill(12)}"
