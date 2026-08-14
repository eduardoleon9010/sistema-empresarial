# -*- coding: utf-8 -*-

# ============================================================
# MODULO DE NOMINA
# Archivo: modulos/nomina.py
# ============================================================


def obtener_empleados(estado):
    """
    Devuelve los empleados registrados en el estado general.
    """

    return estado.get("empleados", {}).copy()


def calcular_nomina(estado):
    """
    Calcula el total de nomina con base en los empleados.
    """

    empleados = estado.get("empleados", {})

    total = 0.0

    for datos in empleados.values():

        sueldo = float(
            datos.get("sueldo_base", 0)
        )

        total += sueldo

    return {
        "empleados": len(empleados),
        "total_nomina": round(total, 2)
    }


def registrar_pago_nomina(estado):
    """
    Registra el pago de la nomina y descuenta
    el valor correspondiente del saldo bancario.
    """

    nomina = calcular_nomina(estado)

    total = nomina["total_nomina"]

    saldo_banco = float(
        estado.get("saldo_banco", 0)
    )

    # --------------------------------------------------------
    # VALIDAR FONDOS
    # --------------------------------------------------------

    if total > saldo_banco:

        return {
            "resultado": "fondos_insuficientes",
            "total_nomina": total,
            "saldo_banco": saldo_banco
        }

    # --------------------------------------------------------
    # DESCONTAR NOMINA DEL BANCO
    # --------------------------------------------------------

    estado["saldo_banco"] = round(
        saldo_banco - total,
        2
    )

    # --------------------------------------------------------
    # ACTUALIZAR ESTADO DE NOMINA
    # --------------------------------------------------------

    estado["nomina_pagada"] = True

    estado["total_nomina_pendiente"] = 0.0

    # --------------------------------------------------------
    # RESULTADO
    # --------------------------------------------------------

    return {
        "resultado": "nomina_pagada",
        "total_nomina": total,
        "saldo_banco": estado["saldo_banco"]
    }