from encabezado import pedir_datos_encabezado, crear_encabezado
from detalle import pedir_datos_detalle, crear_detalle
from utils import guardar_en_archivo, leer_archivo


def main():
    datos_encabezado = pedir_datos_encabezado()

    lineas = []

    encabezado = crear_encabezado(**datos_encabezado)
    lineas.append(encabezado)

    for _ in range(int(datos_encabezado["cantidad_de_empleados"])):
        datos_detalle = pedir_datos_detalle()
        detalle = crear_detalle(**datos_detalle)
        lineas.append(detalle)

    guardar_en_archivo("nomina-unapec-2025.txt", lineas)


def crear_nominas(datos_encabezado, lista_detalles):
    crear_encabezado(**datos_encabezado)

    for detalle in lista_detalles:
        crear_detalle(**detalle)
    

if __name__ == "__main__":
    main()
