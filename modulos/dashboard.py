# -*- coding: utf-8 -*-

# ============================================================
# MODULO DE DASHBOARD
# ============================================================
#
# Centraliza los principales indicadores del sistema.
#
# Este modulo no modifica el estado.
# Solamente consulta la informacion existente.
# ============================================================

from modulos.finanzas import (
    obtener_resumen_financiero,
    obtener_indicadores_financieros
)

from modulos.nomina import (
    calcular_nomina,
    obtener_empleados
)

from modulos.contabilidad import (
    obtener_resumen_contable,
    obtener_estado_impuestos
)

from modulos.tesoreria import (
    obtener_resumen_tesoreria
)


def obtener_indicadores_dashboard(estado):
    """
    Obtiene los principales indicadores generales
    del sistema empresarial.
    """

    finanzas = obtener_resumen_financiero(estado)

    indicadores_financieros = (
        obtener_indicadores_financieros(estado)
    )

    contabilidad = obtener_resumen_contable(estado)

    impuestos = obtener_estado_impuestos(estado)

    nomina = calcular_nomina(estado)

    empleados = obtener_empleados(estado)

    tesoreria = obtener_resumen_tesoreria(estado)

    return {
        "finanzas": finanzas,
        "indicadores_financieros": indicadores_financieros,
        "contabilidad": contabilidad,
        "impuestos": impuestos,
        "nomina": nomina,
        "empleados": empleados,
        "tesoreria": tesoreria
    }