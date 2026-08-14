# ============================================================
# ESTADO INICIAL DEL SISTEMA
# Archivo: datos/estado.py
# ============================================================
#
# Por ahora los datos permanecen en memoria.
#
# En una etapa posterior este archivo sera reemplazado por
# una base de datos.
# ============================================================


estado = {

    # --------------------------------------------------------
    # INFORMACION FINANCIERA
    # --------------------------------------------------------

    "ventas_efectivo": 3000000.0,

    "ventas_fiadas": 1000000.0,

    "ventas_totales": 4000000.0,

    "gastos_operacionales": 2900000.0,

    "saldo_banco": 681106.0,


    # --------------------------------------------------------
    # FONDO DE PRESTAMOS
    # --------------------------------------------------------

    "fondo_prestamos_disponible": 1000000.0,

    "prestamos_activos": {},


    # --------------------------------------------------------
    # ESTADO DE NOMINA
    # --------------------------------------------------------

    "nomina_pagada": True,

    "total_nomina_pendiente": 0.0,


    # --------------------------------------------------------
    # ESTADO DE IMPUESTOS
    # --------------------------------------------------------

    "impuestos_pagados": False,


    # --------------------------------------------------------
    # EMPLEADOS
    # --------------------------------------------------------

    "empleados": {

        "Juan Perez": {
            "sueldo_base": 1500000.0
        },

        "Maria Lopez": {
            "sueldo_base": 2000000.0
        },

        "Pedro Gomez": {
            "sueldo_base": 1300000.0
        }

    }

}