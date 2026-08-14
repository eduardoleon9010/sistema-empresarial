# -*- coding: utf-8 -*-

# ============================================================
# MODULO DE FINANZAS
# ============================================================
#
# Contiene la logica financiera basica del prototipo.
#
# Por ahora trabaja con el estado en memoria.
# ============================================================


def obtener_resumen_financiero(estado):
    """
    Obtiene un resumen financiero general.
    """

    ventas_totales = float(
        estado.get("ventas_totales", 0)
    )

    ventas_efectivo = float(
        estado.get("ventas_efectivo", 0)
    )

    ventas_fiadas = float(
        estado.get("ventas_fiadas", 0)
    )

    gastos_operacionales = float(
        estado.get("gastos_operacionales", 0)
    )

    saldo_banco = float(
        estado.get("saldo_banco", 0)
    )

    fondo_prestamos = float(
        estado.get("fondo_prestamos_disponible", 0)
    )

    prestamos_activos = estado.get(
        "prestamos_activos",
        {}
    )

    cartera_prestamos = sum(
        float(valor)
        for valor in prestamos_activos.values()
    )

    utilidad_operativa = (
        ventas_totales - gastos_operacionales
    )

    liquidez_disponible = (
        saldo_banco + fondo_prestamos
    )

    return {
        "ventas_totales": ventas_totales,
        "ventas_efectivo": ventas_efectivo,
        "ventas_fiadas": ventas_fiadas,
        "gastos_operacionales": gastos_operacionales,
        "utilidad_operativa": utilidad_operativa,
        "saldo_banco": saldo_banco,
        "fondo_prestamos": fondo_prestamos,
        "cartera_prestamos": cartera_prestamos,
        "liquidez_disponible": liquidez_disponible
    }


def obtener_indicadores_financieros(estado):
    """
    Calcula indicadores financieros basicos.
    """

    resumen = obtener_resumen_financiero(estado)

    ventas = resumen["ventas_totales"]

    utilidad = resumen["utilidad_operativa"]

    if ventas > 0:

        margen_utilidad = (
            utilidad / ventas
        ) * 100

    else:

        margen_utilidad = 0.0

    return {
        "margen_utilidad": margen_utilidad
    }


# ============================================================
# MOVIMIENTOS DE CAJA
# ============================================================


def registrar_ingreso(estado, concepto, monto):
    """
    Registra un ingreso de dinero y aumenta
    el saldo bancario.
    """

    try:

        monto = float(monto)

    except (TypeError, ValueError):

        return {
            "resultado": "entrada_invalida"
        }

    if monto <= 0:

        return {
            "resultado": "monto_invalido"
        }

    saldo_actual = float(
        estado.get("saldo_banco", 0)
    )

    estado["saldo_banco"] = round(
        saldo_actual + monto,
        2
    )

    return {
        "resultado": "ingreso_registrado",
        "concepto": concepto,
        "monto": monto,
        "saldo_banco": estado["saldo_banco"]
    }


def registrar_gasto(estado, concepto, monto):
    """
    Registra un gasto y disminuye
    el saldo bancario.
    """

    try:

        monto = float(monto)

    except (TypeError, ValueError):

        return {
            "resultado": "entrada_invalida"
        }

    if monto <= 0:

        return {
            "resultado": "monto_invalido"
        }

    saldo_actual = float(
        estado.get("saldo_banco", 0)
    )

    if monto > saldo_actual:

        return {
            "resultado": "fondos_insuficientes",
            "monto": monto,
            "saldo_banco": saldo_actual
        }

    estado["saldo_banco"] = round(
        saldo_actual - monto,
        2
    )

    return {
        "resultado": "gasto_registrado",
        "concepto": concepto,
        "monto": monto,
        "saldo_banco": estado["saldo_banco"]
    }