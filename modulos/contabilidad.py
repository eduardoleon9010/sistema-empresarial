# -*- coding: utf-8 -*-

# ============================================================
# MODULO DE CONTABILIDAD
# ============================================================
#
# Este modulo contiene la logica basica de contabilidad
# del prototipo.
#
# Por ahora trabaja directamente con el estado en memoria.
# Posteriormente podra conectarse a una base de datos.
# ============================================================


def obtener_resumen_contable(estado):
    """
    Obtiene un resumen contable basico del sistema.
    """

    ventas_efectivo = float(
        estado.get("ventas_efectivo", 0)
    )

    ventas_fiadas = float(
        estado.get("ventas_fiadas", 0)
    )

    ventas_totales = float(
        estado.get("ventas_totales", 0)
    )

    gastos_operacionales = float(
        estado.get("gastos_operacionales", 0)
    )

    saldo_banco = float(
        estado.get("saldo_banco", 0)
    )

    utilidad_operativa = (
        ventas_totales - gastos_operacionales
    )

    cuentas_por_cobrar = ventas_fiadas

    return {
        "ventas_efectivo": ventas_efectivo,
        "ventas_fiadas": ventas_fiadas,
        "ventas_totales": ventas_totales,
        "gastos_operacionales": gastos_operacionales,
        "saldo_banco": saldo_banco,
        "cuentas_por_cobrar": cuentas_por_cobrar,
        "utilidad_operativa": utilidad_operativa
    }


def obtener_estado_impuestos(estado):
    """
    Consulta el estado actual de los impuestos.
    """

    impuestos_pagados = estado.get(
        "impuestos_pagados",
        False
    )

    return {
        "impuestos_pagados": impuestos_pagados
    }