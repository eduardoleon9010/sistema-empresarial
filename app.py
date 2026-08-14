# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from decimal import Decimal, InvalidOperation

from datos.estado import estado

from modulos.nomina import (
    calcular_nomina,
    obtener_empleados,
    registrar_pago_nomina
)

from modulos.contabilidad import (
    obtener_resumen_contable,
    obtener_estado_impuestos
)

from modulos.finanzas import (
    obtener_resumen_financiero,
    obtener_indicadores_financieros,
    registrar_ingreso,
    registrar_gasto
)

from modulos.tesoreria import (
    registrar_prestamo,
    registrar_devolucion,
    obtener_estado_cartera
)

from modulos.dashboard import obtener_indicadores_dashboard


# ============================================================
# CREACION DE LA APLICACION
# ============================================================

app = Flask(__name__)


# ============================================================
# PAGINA PRINCIPAL
# ============================================================
@app.route("/")
def inicio():
    """
    Muestra el dashboard principal del sistema.
    """

    indicadores = obtener_indicadores_dashboard(estado)

    return render_template(
        "inicio.html",
        indicadores=indicadores
    )


# ============================================================
# MODULO DE NOMINA
# ============================================================

@app.route("/nomina", methods=["GET", "POST"])
def nomina():

    # ========================================================
    # PROCESAR PAGO DE NOMINA
    # ========================================================

    if request.method == "POST":

        resultado = registrar_pago_nomina(estado)

        # ----------------------------------------------------
        # NOMINA PAGADA
        # ----------------------------------------------------

        if resultado["resultado"] == "nomina_pagada":

            mensaje = (
                f"Nomina pagada correctamente: "
                f"${resultado['total_nomina']:,.2f}. "
                f"Saldo bancario restante: "
                f"${resultado['saldo_banco']:,.2f}"
            )

            return redirect(
                url_for(
                    "nomina",
                    mensaje=mensaje,
                    tipo="exito"
                )
            )

        # ----------------------------------------------------
        # FONDOS INSUFICIENTES
        # ----------------------------------------------------

        if resultado["resultado"] == "fondos_insuficientes":

            mensaje = (
                "No es posible pagar la nomina. "
                f"Se requieren "
                f"${resultado['total_nomina']:,.2f}, "
                f"pero el saldo bancario disponible es "
                f"${resultado['saldo_banco']:,.2f}."
            )

            return redirect(
                url_for(
                    "nomina",
                    mensaje=mensaje,
                    tipo="error"
                )
            )

    # ========================================================
    # MOSTRAR INFORMACION
    # ========================================================

    empleados = obtener_empleados(estado)

    resumen_nomina = calcular_nomina(estado)

    mensaje = request.args.get("mensaje")

    tipo_mensaje = request.args.get("tipo")

    return render_template(
        "nomina.html",
        estado=estado,
        empleados=empleados,
        nomina=resumen_nomina,
        mensaje=mensaje,
        tipo_mensaje=tipo_mensaje
    )


# ============================================================
# MODULO DE CONTABILIDAD
# ============================================================

@app.route("/contabilidad")
def contabilidad():

    resumen = obtener_resumen_contable(estado)

    impuestos = obtener_estado_impuestos(estado)

    return render_template(
        "contabilidad.html",
        estado=estado,
        resumen=resumen,
        impuestos=impuestos
    )


# ============================================================
# MODULO DE FINANZAS
# ============================================================
@app.route("/finanzas", methods=["GET", "POST"])
def finanzas():
    """
    Gestiona el modulo de finanzas.

    GET:
        Muestra el resumen financiero.

    POST:
        Registra un ingreso o un gasto.

    Utiliza el mismo estado general del sistema.
    """

    if request.method == "POST":

        print("DATOS RECIBIDOS FINANZAS:", request.form)

        tipo_operacion = request.form.get(
            "accion"
        )

        concepto = request.form.get(
            "concepto",
            ""
        ).strip()

        monto_texto = request.form.get(
            "monto",
            "0"
        ).strip()


        try:

            monto = float(monto_texto)

        except ValueError:

            return redirect(
                url_for(
                    "finanzas",
                    mensaje="El monto ingresado no es valido.",
                    tipo="error"
                )
            )

        if monto <= 0:

            return redirect(
                url_for(
                    "finanzas",
                    mensaje="El monto debe ser mayor que cero.",
                    tipo="error"
                )
            )

        if not concepto:

            return redirect(
                url_for(
                    "finanzas",
                    mensaje="Debe ingresar un concepto.",
                    tipo="error"
                )
            )

        # ----------------------------------------------------
        # REGISTRAR INGRESO
        # ----------------------------------------------------

        if tipo_operacion == "ingreso":

            resultado = registrar_ingreso(
                estado,
                concepto,
                monto
            )

            mensaje = (
                f"Ingreso registrado: "
                f"${resultado['monto']:,.2f}. "
                f"Saldo bancario: "
                f"${resultado['saldo_banco']:,.2f}."
            )

            return redirect(
                url_for(
                    "finanzas",
                    mensaje=mensaje,
                    tipo="exito"
                )
            )

        # ----------------------------------------------------
        # REGISTRAR GASTO
        # ----------------------------------------------------

        if tipo_operacion == "gasto":

            resultado = registrar_gasto(
                estado,
                concepto,
                monto
            )

            if resultado["resultado"] == "fondos_insuficientes":

                mensaje = (
                    "No es posible registrar el gasto. "
                    f"El saldo bancario disponible es "
                    f"${resultado['saldo_banco']:,.2f}."
                )

                return redirect(
                    url_for(
                        "finanzas",
                        mensaje=mensaje,
                        tipo="error"
                    )
                )

            mensaje = (
                f"Gasto registrado: "
                f"${resultado['monto']:,.2f}. "
                f"Saldo bancario: "
                f"${resultado['saldo_banco']:,.2f}."
            )

            return redirect(
                url_for(
                    "finanzas",
                    mensaje=mensaje,
                    tipo="exito"
                )
            )

        return redirect(
            url_for(
                "finanzas",
                mensaje="Operacion financiera no reconocida.",
                tipo="error"
            )
        )

    # ========================================================
    # MOSTRAR INFORMACION
    # ========================================================

    resumen = obtener_resumen_financiero(estado)

    indicadores = obtener_indicadores_financieros(estado)

    mensaje = request.args.get("mensaje")

    tipo_mensaje = request.args.get("tipo")

    return render_template(
        "finanzas.html",
        estado=estado,
        resumen=resumen,
        indicadores=indicadores,
        mensaje=mensaje,
        tipo_mensaje=tipo_mensaje
    )

# ============================================================
# MODULO DE TESORERIA
# ============================================================

@app.route("/tesoreria", methods=["GET", "POST"])
def tesoreria():
    """
    Gestiona las operaciones del modulo de tesoreria.

    GET:
        Muestra el fondo disponible y la cartera.

    POST:
        Procesa un prestamo o una devolucion.

    Se utiliza el patron:

        POST -> REDIRECT -> GET

    para evitar que al actualizar la pagina se repita
    la ultima operacion financiera.
    """

    # ========================================================
    # PROCESAR OPERACIONES POST
    # ========================================================

    if request.method == "POST":

        # ----------------------------------------------------
        # IDENTIFICAR LA OPERACION
        # ----------------------------------------------------

        accion = request.form.get(
            "accion",
            ""
        ).strip()

        empleado = request.form.get(
            "empleado",
            ""
        ).strip()

        monto_texto = request.form.get(
            "monto",
            ""
        ).strip()

        # ====================================================
        # REGISTRAR DEVOLUCION
        # ====================================================

        if accion == "devolucion":

            resultado = registrar_devolucion(
                estado,
                empleado,
                monto_texto
            )

            # ------------------------------------------------
            # DEVOLUCION REGISTRADA
            # ------------------------------------------------

            if resultado["resultado"] == "devolucion_registrada":

                mensaje = (
                    f"Devolucion registrada: "
                    f"${resultado['abono']:,.2f}. "
                    f"Saldo pendiente: "
                    f"${resultado['deuda_restante']:,.2f}. "
                    f"Fondo disponible: "
                    f"${resultado['fondo_disponible']:,.2f}"
                )

                return redirect(
                    url_for(
                        "tesoreria",
                        mensaje=mensaje,
                        tipo="exito"
                    )
                )

            # ------------------------------------------------
            # NO EXISTEN DEUDAS
            # ------------------------------------------------

            if resultado["resultado"] == "sin_deudas":

                return redirect(
                    url_for(
                        "tesoreria",
                        mensaje=(
                            "No existen empleados "
                            "con deudas pendientes."
                        ),
                        tipo="error"
                    )
                )

            # ------------------------------------------------
            # EMPLEADO SIN DEUDA
            # ------------------------------------------------

            if resultado["resultado"] == "empleado_sin_deuda":

                return redirect(
                    url_for(
                        "tesoreria",
                        mensaje=(
                            "El empleado no tiene "
                            "una deuda activa."
                        ),
                        tipo="error"
                    )
                )

            # ------------------------------------------------
            # MONTO NO NUMERICO
            # ------------------------------------------------

            if resultado["resultado"] == "entrada_invalida":

                return redirect(
                    url_for(
                        "tesoreria",
                        mensaje="El monto debe ser numerico.",
                        tipo="error"
                    )
                )

            # ------------------------------------------------
            # MONTO MENOR O IGUAL A CERO
            # ------------------------------------------------

            if resultado["resultado"] == "monto_invalido":

                return redirect(
                    url_for(
                        "tesoreria",
                        mensaje=(
                            "El abono debe ser mayor que cero."
                        ),
                        tipo="error"
                    )
                )

            # ------------------------------------------------
            # ABONO MAYOR QUE LA DEUDA
            # ------------------------------------------------

            if resultado["resultado"] == "abono_superior_a_deuda":

                return redirect(
                    url_for(
                        "tesoreria",
                        mensaje=(
                            "El monto ingresado es mayor "
                            "a la deuda."
                        ),
                        tipo="error"
                    )
                )

        # ====================================================
        # REGISTRAR PRESTAMO
        # ====================================================

        if accion == "prestamo":

            # ------------------------------------------------
            # VALIDAR NOMBRE
            # ------------------------------------------------

            if not empleado:

                return redirect(
                    url_for(
                        "tesoreria",
                        mensaje=(
                            "Debe indicar el nombre "
                            "del empleado."
                        ),
                        tipo="error"
                    )
                )

            # ------------------------------------------------
            # VALIDAR MONTO
            # ------------------------------------------------

            try:

                monto = float(monto_texto)

            except (ValueError, TypeError):

                return redirect(
                    url_for(
                        "tesoreria",
                        mensaje="El monto debe ser numerico.",
                        tipo="error"
                    )
                )

            # ------------------------------------------------
            # VALIDAR MONTO POSITIVO
            # ------------------------------------------------

            if monto <= 0:

                return redirect(
                    url_for(
                        "tesoreria",
                        mensaje=(
                            "El monto debe ser mayor que cero."
                        ),
                        tipo="error"
                    )
                )

            # ------------------------------------------------
            # REGISTRAR PRESTAMO
            # ------------------------------------------------

            resultado = registrar_prestamo(
                estado,
                empleado,
                monto
            )

            # ------------------------------------------------
            # PRESTAMO REGISTRADO
            # ------------------------------------------------

            if resultado["resultado"] == "prestamo_registrado":

                mensaje = (
                    f"Prestamo aprobado: "
                    f"${resultado['monto']:,.2f} "
                    f"a {resultado['empleado']}."
                )

                return redirect(
                    url_for(
                        "tesoreria",
                        mensaje=mensaje,
                        tipo="exito"
                    )
                )

            # ------------------------------------------------
            # FONDOS INSUFICIENTES
            # ------------------------------------------------

            if resultado["resultado"] == "fondos_insuficientes":

                mensaje = (
                    "No hay fondos suficientes. "
                    f"Disponibles: "
                    f"${resultado['fondo_disponible']:,.2f}"
                )

                return redirect(
                    url_for(
                        "tesoreria",
                        mensaje=mensaje,
                        tipo="error"
                    )
                )

            # ------------------------------------------------
            # MONTO NO NUMERICO
            # ------------------------------------------------

            if resultado["resultado"] == "entrada_invalida":

                return redirect(
                    url_for(
                        "tesoreria",
                        mensaje="El monto debe ser numerico.",
                        tipo="error"
                    )
                )

            # ------------------------------------------------
            # MONTO INVALIDO
            # ------------------------------------------------

            if resultado["resultado"] == "monto_invalido":

                return redirect(
                    url_for(
                        "tesoreria",
                        mensaje=(
                            "El monto debe ser mayor que cero."
                        ),
                        tipo="error"
                    )
                )

    # ========================================================
    # MOSTRAR INFORMACION
    # ========================================================

    mensaje = request.args.get(
        "mensaje"
    )

    tipo_mensaje = request.args.get(
        "tipo"
    )

    cartera = obtener_estado_cartera(
        estado
    )

    return render_template(
        "tesoreria.html",
        estado=estado,
        cartera=cartera,
        mensaje=mensaje,
        tipo_mensaje=tipo_mensaje
    )


# ============================================================
# EJECUCION
# ============================================================

if __name__ == "__main__":

    app.run(debug=True)