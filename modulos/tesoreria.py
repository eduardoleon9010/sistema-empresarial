# -*- coding: utf-8 -*-

# ============================================================
# MODULO DE TESORERIA
# Archivo: modulos/tesoreria.py
# ============================================================
#
# Este modulo contiene la logica financiera relacionada con:
#
# 1. Registro de prestamos.
# 2. Registro de devoluciones.
# 3. Consulta de cartera.
# 4. Control del fondo disponible.
#
# Los valores monetarios se manejan mediante Decimal para
# evitar errores de precision propios de los numeros float.
# ============================================================

from decimal import Decimal, InvalidOperation


# ============================================================
# FUNCION AUXILIAR PARA MANEJO DE DINERO
# ============================================================

def convertir_dinero(valor):
    """
    Convierte un valor recibido a Decimal con dos decimales.

    Se utiliza para evitar errores de precision monetaria.

    Parametro:
        valor: numero recibido como texto, entero, float o Decimal.

    Retorna:
        Decimal con dos posiciones decimales.

    Si el valor no puede convertirse, retorna None.
    """

    try:

        return Decimal(
            str(valor)
        ).quantize(
            Decimal("0.01")
        )

    except (
        InvalidOperation,
        ValueError,
        TypeError
    ):

        return None


# ============================================================
# REGISTRAR PRESTAMO
# ============================================================

def registrar_prestamo(estado, empleado, monto):
    """
    Registra un nuevo prestamo.

    Parametros:
        estado:
            Diccionario general del sistema.

        empleado:
            Nombre del empleado.

        monto:
            Valor solicitado.

    Retorna:
        Diccionario con el resultado de la operacion.
    """

    # --------------------------------------------------------
    # VALIDAR EMPLEADO
    # --------------------------------------------------------

    if not empleado:

        return {
            "modulo": "tesoreria",
            "resultado": "empleado_invalido"
        }

    # --------------------------------------------------------
    # CONVERTIR MONTO
    # --------------------------------------------------------

    monto = convertir_dinero(monto)

    if monto is None:

        return {
            "modulo": "tesoreria",
            "resultado": "entrada_invalida",
            "motivo": "monto_no_numerico"
        }

    # --------------------------------------------------------
    # VALIDAR MONTO POSITIVO
    # --------------------------------------------------------

    if monto <= Decimal("0.00"):

        return {
            "modulo": "tesoreria",
            "resultado": "monto_invalido"
        }

    # --------------------------------------------------------
    # OBTENER FONDO ACTUAL
    # --------------------------------------------------------

    fondo = convertir_dinero(
        estado["fondo_prestamos_disponible"]
    )

    # --------------------------------------------------------
    # VALIDAR FONDO
    # --------------------------------------------------------

    if fondo is None:

        return {
            "modulo": "tesoreria",
            "resultado": "fondo_invalido"
        }

    # --------------------------------------------------------
    # VALIDAR DISPONIBILIDAD
    # --------------------------------------------------------

    if monto > fondo:

        return {
            "modulo": "tesoreria",
            "resultado": "fondos_insuficientes",
            "fondo_disponible": float(fondo)
        }

    # --------------------------------------------------------
    # CALCULAR NUEVO FONDO
    # --------------------------------------------------------

    nuevo_fondo = (
        fondo - monto
    ).quantize(
        Decimal("0.01")
    )

    # --------------------------------------------------------
    # OBTENER DEUDA ACTUAL
    # --------------------------------------------------------

    deuda_actual = convertir_dinero(
        estado["prestamos_activos"].get(
            empleado,
            0
        )
    )

    if deuda_actual is None:

        deuda_actual = Decimal("0.00")

    # --------------------------------------------------------
    # CALCULAR NUEVA DEUDA
    # --------------------------------------------------------

    nueva_deuda = (
        deuda_actual + monto
    ).quantize(
        Decimal("0.01")
    )

    # --------------------------------------------------------
    # ACTUALIZAR ESTADO
    # --------------------------------------------------------

    estado["fondo_prestamos_disponible"] = float(
        nuevo_fondo
    )

    estado["prestamos_activos"][empleado] = float(
        nueva_deuda
    )

    # --------------------------------------------------------
    # RETORNAR RESULTADO
    # --------------------------------------------------------

    return {

        "modulo": "tesoreria",

        "resultado": "prestamo_registrado",

        "empleado": empleado,

        "monto": float(monto),

        "fondo_disponible": float(
            nuevo_fondo
        ),

        "deuda": float(
            nueva_deuda
        )
    }


# ============================================================
# REGISTRAR DEVOLUCION
# ============================================================

def registrar_devolucion(estado, empleado, monto):
    """
    Registra una devolucion parcial o total de un prestamo.
    """

    # --------------------------------------------------------
    # VALIDAR EXISTENCIA DE CARTERA
    # --------------------------------------------------------

    if not estado["prestamos_activos"]:

        return {
            "modulo": "tesoreria",
            "resultado": "sin_deudas"
        }

    # --------------------------------------------------------
    # VALIDAR EMPLEADO
    # --------------------------------------------------------

    if empleado not in estado["prestamos_activos"]:

        return {
            "modulo": "tesoreria",
            "resultado": "empleado_sin_deuda"
        }

    # --------------------------------------------------------
    # OBTENER DEUDA
    # --------------------------------------------------------

    deuda = convertir_dinero(
        estado["prestamos_activos"][empleado]
    )

    # --------------------------------------------------------
    # CONVERTIR ABONO
    # --------------------------------------------------------

    monto = convertir_dinero(
        monto
    )

    if monto is None:

        return {
            "modulo": "tesoreria",
            "resultado": "entrada_invalida",
            "motivo": "monto_no_numerico"
        }

    # --------------------------------------------------------
    # VALIDAR MONTO
    # --------------------------------------------------------

    if monto <= Decimal("0.00"):

        return {
            "modulo": "tesoreria",
            "resultado": "monto_invalido"
        }

    # --------------------------------------------------------
    # VALIDAR ABONO CONTRA DEUDA
    # --------------------------------------------------------

    if monto > deuda:

        return {
            "modulo": "tesoreria",
            "resultado": "abono_superior_a_deuda",
            "deuda": float(deuda)
        }

    # --------------------------------------------------------
    # CALCULAR NUEVA DEUDA
    # --------------------------------------------------------

    deuda_restante = (
        deuda - monto
    ).quantize(
        Decimal("0.01")
    )

    # --------------------------------------------------------
    # OBTENER FONDO
    # --------------------------------------------------------

    fondo = convertir_dinero(
        estado["fondo_prestamos_disponible"]
    )

    # --------------------------------------------------------
    # CALCULAR NUEVO FONDO
    # --------------------------------------------------------

    nuevo_fondo = (
        fondo + monto
    ).quantize(
        Decimal("0.01")
    )

    # --------------------------------------------------------
    # ACTUALIZAR FONDO
    # --------------------------------------------------------

    estado["fondo_prestamos_disponible"] = float(
        nuevo_fondo
    )

    # --------------------------------------------------------
    # ACTUALIZAR CARTERA
    # --------------------------------------------------------

    if deuda_restante == Decimal("0.00"):

        del estado["prestamos_activos"][empleado]

    else:

        estado["prestamos_activos"][empleado] = float(
            deuda_restante
        )

    # --------------------------------------------------------
    # RETORNAR RESULTADO
    # --------------------------------------------------------

    return {

        "modulo": "tesoreria",

        "resultado": "devolucion_registrada",

        "empleado": empleado,

        "abono": float(monto),

        "deuda_restante": float(
            deuda_restante
        ),

        "fondo_disponible": float(
            nuevo_fondo
        )
    }


# ============================================================
# CONSULTAR ESTADO DE CARTERA
# ============================================================

def obtener_estado_cartera(estado):
    """
    Devuelve el estado actual del fondo y de los prestamos.
    """

    return {

        "fondo_disponible":
            estado[
                "fondo_prestamos_disponible"
            ],

        "prestamos_activos":
            estado[
                "prestamos_activos"
            ].copy()
    }
    
    
    
    
    
    
# ============================================================
# RESUMEN DE TESORERIA
# ============================================================

def obtener_resumen_tesoreria(estado):
    """
    Obtiene un resumen general del estado de tesoreria.

    Incluye:
        - Fondo disponible para prestamos.
        - Total de cartera.
        - Cantidad de prestamos activos.
    """

    fondo_disponible = convertir_dinero(
        estado.get(
            "fondo_prestamos_disponible",
            0
        )
    )

    if fondo_disponible is None:
        fondo_disponible = Decimal("0.00")

    prestamos_activos = estado.get(
        "prestamos_activos",
        {}
    )

    cartera_total = Decimal("0.00")

    for monto in prestamos_activos.values():

        deuda = convertir_dinero(monto)

        if deuda is not None:
            cartera_total += deuda

    cartera_total = cartera_total.quantize(
        Decimal("0.01")
    )

    return {
        "fondo_disponible": float(
            fondo_disponible
        ),

        "cartera_total": float(
            cartera_total
        ),

        "prestamos_activos": len(
            prestamos_activos
        )
    }