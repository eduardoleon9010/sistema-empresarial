<p align="center">
  <img
    src="https://drive.google.com/uc?export=view&id=1d5Vnn1J0bDWThA2wTt5ZKwsNmVFBRRV4"
    alt="Sistema de Gestión Empresarial Unificado"
    width="100%"
  />
</p>


<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web%20Application-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Estado-V1%20Funcional-2EA44F?style=for-the-badge" alt="Estado">
  <img src="https://img.shields.io/badge/Investigación-Aplicada-6f42c1?style=for-the-badge" alt="Investigación aplicada">
</p>

<p align="center">
  <strong>Prototipo modular para la gestión financiera, contable, de nómina y tesorería de pequeñas organizaciones.</strong>
</p>

<p align="center">
  <a href="https://sistema-empresarial-v1.onrender.com/">
    <img src="https://img.shields.io/badge/Ver%20demostración-Online-0A7B83?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Ver demostración">
  </a>
</p>


## Sobre el proyecto

El **Sistema de Gestión Empresarial Unificado** es un prototipo web desarrollado en **Python y Flask** como una propuesta tecnológica aplicada a una necesidad concreta de pequeñas organizaciones: mantener información coherente y oportunamente actualizada sobre sus operaciones financieras y administrativas.

El proyecto integra cuatro áreas principales:

* **Finanzas**
* **Contabilidad**
* **Nómina**
* **Tesorería**

Además, incorpora un **dashboard** para consolidar indicadores y facilitar la navegación entre los diferentes módulos.

El desarrollo parte de una idea sencilla pero fundamental:

> **Una operación empresarial no debería quedar aislada como un dato; debe producir un estado coherente que pueda ser consultado, explicado y verificado.**

En esta primera versión, el mayor énfasis está puesto en la **lógica de negocio, la consistencia de las operaciones y la validación funcional**, antes que en la incorporación de infraestructura avanzada.


## ¿Qué problema aborda?

En pequeñas organizaciones, la información administrativa puede encontrarse distribuida entre hojas de cálculo, registros manuales, comprobantes y diferentes archivos.

Esta fragmentación puede dificultar responder preguntas aparentemente simples:

* ¿Cuál es el saldo disponible?
* ¿Cuánto dinero existe en el fondo de préstamos?
* ¿Qué empleados tienen obligaciones pendientes?
* ¿Cuánto se ha devuelto?
* ¿Cómo cambió el estado financiero después de una operación?
* ¿La información presentada por los diferentes módulos es coherente?

Este proyecto explora una alternativa: **centralizar la lógica de operación en un prototipo modular capaz de relacionar las operaciones con el estado empresarial resultante.**


## Objetivo

### Objetivo general

Desarrollar y validar funcionalmente un prototipo modular en Python que contribuya al control y la trazabilidad de operaciones financieras y de tesorería, con énfasis en préstamos a empleados y devoluciones de un fondo financiero en pequeñas organizaciones.

### Objetivos específicos

1. Caracterizar necesidades relacionadas con saldos, operaciones financieras, préstamos, devoluciones e información empresarial.
2. Diseñar e implementar una arquitectura modular para Finanzas, Contabilidad, Nómina y Tesorería.
3. Incorporar validaciones para entradas inválidas, fondos insuficientes, abonos superiores a la deuda y otras situaciones límite.
4. Validar funcionalmente la V1 mediante escenarios controlados y pruebas de aceptación.


## Arquitectura funcional

```text
                    ┌──────────────────────────┐
                    │       DASHBOARD          │
                    │ Indicadores y navegación │
                    └────────────┬─────────────┘
                                 │
          ┌──────────────────────┼──────────────────────┐
          │                      │                      │
          ▼                      ▼                      ▼
   ┌─────────────┐        ┌─────────────┐       ┌─────────────┐
   │  FINANZAS   │        │ CONTABILIDAD│       │   NÓMINA    │
   │             │        │             │       │             │
   │ Ingresos    │        │ Ventas      │       │ Empleados   │
   │ Gastos      │        │ Gastos      │       │ Nómina      │
   │ Saldo       │        │ Utilidad    │       │ Pagos       │
   └─────────────┘        └─────────────┘       └─────────────┘
                                 │
                                 ▼
                         ┌─────────────┐
                         │ TESORERÍA   │
                         │             │
                         │ Fondo       │
                         │ Préstamos   │
                         │ Devoluciones│
                         │ Cartera     │
                         └─────────────┘
```

La separación modular permite trabajar y probar cada dominio de manera independiente, manteniendo una estructura preparada para futuras etapas de evolución.


## Módulos

### Finanzas

Permite registrar y consultar:

* Ingresos.
* Gastos.
* Saldo bancario.
* Indicadores financieros.

### Contabilidad

Integra información relacionada con:

* Ventas.
* Gastos.
* Utilidad.
* Cuentas por cobrar.
* Estado de impuestos.

### Nómina

Permite consultar:

* Empleados.
* Resumen de nómina.
* Estado de pago.

### Tesorería

Es uno de los componentes centrales de la V1 y gestiona:

* Fondo de préstamos.
* Préstamos a empleados.
* Devoluciones.
* Cartera.
* Obligaciones pendientes.

### Dashboard

Consolida indicadores y permite navegar entre los diferentes módulos del sistema.


## Tecnología

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,flask,html,css,git,github" alt="Tecnologías utilizadas">
</p>

| Tecnología | Uso                              |
| ---------- | -------------------------------- |
| **Python** | Lenguaje principal               |
| **Flask**  | Framework web                    |
| **HTML**   | Interfaz de usuario              |
| **CSS**    | Presentación visual              |
| **Git**    | Control de versiones             |
| **GitHub** | Repositorio y gestión del código |

La V1 utiliza manejo explícito de valores monetarios mediante `Decimal` para las operaciones financieras y aplica validaciones sobre préstamos y devoluciones.


## Principio central de Tesorería

El módulo de tesorería implementa una relación lógica entre:

```text
Fondo disponible
       │
       ├── Préstamo ──────► Disminuye el fondo
       │                         │
       │                         ▼
       │                    Aumenta deuda
       │
       └── Devolución ────► Aumenta el fondo
                                 │
                                 ▼
                            Disminuye deuda
```

La regla fundamental es que el **estado posterior debe poder explicarse a partir del estado anterior y de la operación registrada**.


## Validación funcional

La V1 fue sometida a escenarios controlados de aceptación funcional.

### Finanzas

| Prueba |            Operación |          Resultado |
| ------ | -------------------: | -----------------: |
| F-01   | Ingreso $100.000 COP | Saldo $781.106 COP |
| F-02   |    Gasto $50.000 COP | Saldo $731.106 COP |

### Tesorería

| Prueba |               Operación |                               Resultado |
| ------ | ----------------------: | --------------------------------------: |
| T-01   |   Préstamo $100.000 COP | Fondo $900.000 COP + deuda $100.000 COP |
| T-02   | Devolución $100.000 COP |   Fondo $1.000.000 COP + cartera $0 COP |

Los escenarios principales alcanzaron los criterios de aceptación definidos.


## Un resultado importante: encontrar un defecto real

Durante la prueba de aceptación se identificó un defecto de integración en la ruta de **Contabilidad**.

La aplicación intentaba utilizar:

```python
obtener_estado_impuestos(estado)
```

sin que la función estuviera importada correctamente en `app.py`.

Esto produjo un `NameError`.

El defecto fue localizado, corregido y posteriormente verificado mediante recompilación y una nueva ejecución de la ruta.

Este resultado es especialmente importante para el proyecto porque demuestra que la prueba no fue únicamente demostrativa: **la validación permitió encontrar, corregir y volver a probar un problema real de integración.**


## Estado de la V1

<p align="center">

| Componente               | Estado                                       |
| ------------------------ | -------------------------------------------- |
| Dashboard                | Implementado y probado                       |
| Finanzas                 | Implementado y probado                       |
| Contabilidad             | Implementado y probado después de corrección |
| Nómina                   | Implementado y probado                       |
| Tesorería                | Implementado y probado                       |
| Validaciones funcionales | Implementadas                                |
| Pruebas de aceptación    | Realizadas                                   |
| Base de datos SQL        | Pendiente                                    |
| Autenticación            | Pendiente                                    |
| Auditoría                | Pendiente                                    |
| Integración bancaria     | Pendiente                                    |

</p>


## Ejecución local

### 1. Clonar el repositorio

```bash
git clone https://github.com/USUARIO/REPOSITORIO.git
cd REPOSITORIO
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar la aplicación

```bash
python app.py
```

Posteriormente, acceder desde el navegador a:

```text
http://127.0.0.1:5000
```

> Los comandos anteriores asumen que el repositorio conserva la estructura de ejecución de la V1 y que `app.py` es el punto de entrada de la aplicación.


## Estructura conceptual

```text
.
├── app.py
├── requirements.txt
│
├── módulos/
│   ├── finanzas/
│   ├── contabilidad/
│   ├── nomina/
│   └── tesoreria/
│
├── templates/
│   ├── dashboard.html
│   ├── finanzas.html
│   ├── contabilidad.html
│   ├── nomina.html
│   └── tesoreria.html
│
└── static/
    ├── css/
    └── js/
```

La estructura exacta puede variar según la organización actual del repositorio.


## Demostración

La versión demostrativa de la aplicación se encuentra disponible en:

<p align="center">
  <a href="https://sistema-empresarial-v1.onrender.com/">
    <img src="https://img.shields.io/badge/ABRIR%20SISTEMA-Sistema%20Empresarial%20V1-0A7B83?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Abrir sistema">
  </a>
</p>

**Demostración:**
https://sistema-empresarial-v1.onrender.com/

La aplicación permite observar la integración de los módulos de Finanzas, Contabilidad, Nómina y Tesorería. La disponibilidad del prototipo facilita la inspección del artefacto y la reproducción de los escenarios básicos de aceptación.

## Alcance de la V1

Esta versión está deliberadamente delimitada.

La V1 **no incorpora todavía**:

* Base de datos persistente.
* Recuperación histórica después de reiniciar la aplicación.
* Autenticación avanzada.
* Perfiles y roles de usuario.
* Auditoría completa.
* Copias de respaldo.
* Integración automática con bancos.
* Integración con billeteras o proveedores de pago.
* Conciliación bancaria automática.
* Validación con usuarios administrativos reales.
* Medición de impacto económico.
* Evaluación formal de usabilidad.

Esto no representa una falla accidental del proyecto. Es una decisión de alcance: **primero comprobar la lógica fundamental; después ampliar la infraestructura.**

## Ruta de evolución

### V2 — Persistencia y seguridad

```text
SQLite
   ↓
CRUD
   ↓
Usuarios y roles
   ↓
Control de acceso
   ↓
Auditoría
   ↓
Pruebas de regresión
   ↓
Evaluación de usabilidad
```

### V3 — Integración y contexto real

```text
Proveedor de pagos
        ↓
Conciliación
        ↓
Datos reales
        ↓
Pruebas con usuarios
        ↓
Medición de tiempos
        ↓
Medición de errores
        ↓
Evaluación de utilidad
```

La hoja de ruta propuesta en el proyecto contempla precisamente la incorporación progresiva de persistencia, seguridad, auditoría, pruebas, usabilidad e integración.


## Enfoque de investigación

Este repositorio no representa únicamente un ejercicio de programación.

El proyecto articula:

**Problema → Requerimientos → Diseño → Desarrollo → Pruebas → Defecto → Corrección → Validación → Nuevas preguntas**

La V1 se plantea como una experiencia de **investigación aplicada y desarrollo tecnológico**, donde el software funciona como un artefacto mediante el cual una necesidad organizacional puede convertirse en reglas computables y posteriormente verificarse.

Por esta razón, el proyecto documenta tanto los resultados positivos como los problemas encontrados durante la validación.

## ¿Qué demuestra realmente este proyecto?

La evidencia disponible permite afirmar que la V1:

* Es un prototipo funcional.
* Integra cuatro módulos empresariales.
* Ejecuta operaciones financieras y de tesorería.
* Actualiza los estados de acuerdo con las reglas implementadas.
* Permite verificar escenarios controlados.
* Detectó y corrigió un defecto real de integración.
* Puede utilizarse como base para nuevas etapas de desarrollo e investigación.

Sin embargo, **no permite afirmar todavía** que el sistema:

* Aumente la rentabilidad de una empresa.
* Reduzca costos de forma estadísticamente demostrada.
* Sea superior a soluciones comerciales.
* Sea seguro para producción.
* Haya sido validado con usuarios reales.
* Realice integración bancaria automática.

Esta delimitación forma parte del rigor del proyecto: **se presenta lo que fue construido, se demuestra lo que fue probado y se reconoce aquello que todavía debe investigarse.**


## Contribución

La innovación de este proyecto es **aplicada e incremental**.

No se plantea que Python, Flask o la automatización de saldos sean tecnologías nuevas. La contribución está en la articulación de estos elementos alrededor de una necesidad concreta:

> **Consolidar información empresarial y mantener una relación verificable entre fondo disponible, préstamos, obligaciones y devoluciones.**

La V1 constituye así una base tecnológica sobre la cual pueden desarrollarse nuevas investigaciones relacionadas con persistencia, seguridad, usabilidad, interoperabilidad y uso en contextos organizacionales reales.


## Investigación y desarrollo continuo

Este proyecto está concebido como un sistema en evolución.

```text
                 ┌───────────────────────┐
                 │      PROBLEMA REAL    │
                 └───────────┬───────────┘
                             ↓
                 ┌───────────────────────┐
                 │      INVESTIGACIÓN    │
                 └───────────┬───────────┘
                             ↓
                 ┌───────────────────────┐
                 │       PROTOTIPO       │
                 └───────────┬───────────┘
                             ↓
                 ┌───────────────────────┐
                 │       VALIDACIÓN      │
                 └───────────┬───────────┘
                             ↓
                 ┌───────────────────────┐
                 │       APRENDIZAJE     │
                 └───────────┬───────────┘
                             ↓
                 ┌───────────────────────┐
                 │    NUEVA ITERACIÓN    │
                 └───────────────────────┘
```

La intención no es simplemente agregar funcionalidades, sino que cada nueva versión responda a una necesidad técnica o a una pregunta de investigación.


## Licencia

MIT

## Autoría

<p align="center">
  <strong>Proyecto desarrollado por</strong>
</p>

<table align="center">
  <tr>
    <td align="center" width="45%">
      <h3>Sandra Marcela Cardona Giraldo</h3>
      <p>Investigación · Desarrollo de software</p>
      <a href="https://www.linkedin.com/in/USUARIO_AUTOR_1/" target="_blank">
        <img
          src="https://img.shields.io/badge/LinkedIn-Perfil%20profesional-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"
          alt="LinkedIn Autor 1"
        />
      </a>
    </td>

    <td width="10%"></td>

    <td align="center" width="45%">
      <h3>Leon, E.</h3>
      <p>Investigación · Desarrollo de software</p>
      <a href="[https://www.linkedin.com/in/USUARIO_AUTOR_2/](https://www.linkedin.com/in/mbaleon/)" target="_blank">
        <img
          src="https://img.shields.io/badge/LinkedIn-Perfil%20profesional-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"
          alt="LinkedIn Autor 2"
        />
      </a>
    </td>
  </tr>
</table>

<br>

<p align="center">
  <em>
    Desarrollo de software · Investigación aplicada · Innovación tecnológica
  </em>
</p>


## Contexto académico y tecnológico

Este proyecto fue desarrollado como una experiencia de **investigación formativa, desarrollo de software e innovación tecnológica aplicada**, orientada a transformar una necesidad empresarial concreta en un prototipo funcional y verificable.

El trabajo integra conocimientos de **programación, desarrollo web, gestión empresarial, sistemas de información, automatización y validación funcional**.

### Línea temática

<p align="center">
  <img src="https://img.shields.io/badge/Gestión%20empresarial-0A7B83?style=flat-square" alt="Gestión empresarial">
  <img src="https://img.shields.io/badge/Automatización-0A7B83?style=flat-square" alt="Automatización">
  <img src="https://img.shields.io/badge/Sistemas%20de%20información-0A7B83?style=flat-square" alt="Sistemas de información">
  <img src="https://img.shields.io/badge/Desarrollo%20tecnológico-0A7B83?style=flat-square" alt="Desarrollo tecnológico">
</p>


<p align="center">
  <strong>Sistema de Gestión Empresarial Unificado</strong>
  <br>
  <em>De una necesidad empresarial concreta a un prototipo verificable.</em>
</p>

<p align="center">
  <sub>Versión 1 · Prototipo funcional · Python + Flask</sub>
</p>
