Guía Técnica Avanzada para la Implementación de ERPNext en el Sector Agrícola

Introducción: Arquitectura de una Solución Agrícola en Frappe/ERPNext

Propósito del Documento

Este informe técnico sirve como una guía de referencia exhaustiva para desarrolladores expertos y arquitectos de soluciones que buscan implementar el framework Frappe y ERPNext en el sector agrícola. El enfoque se centra en la personalización profunda, la automatización de procesos y la adaptación a contextos operativos y regulatorios complejos, utilizando el agronegocio en Guatemala como caso de estudio para la gestión de recursos humanos.

Filosofía Arquitectónica Central: "El Lote como Proyecto"

La base de una implementación agrícola robusta en ERPNext reside en una decisión arquitectónica fundamental: modelar cada unidad productiva (lote, parcela o potrero) como un Project dentro del sistema. Esta estrategia convierte al módulo de Proyectos en el eje central que unifica todas las operaciones. Cada ciclo de cultivo, desde la preparación del terreno hasta la cosecha y actividades post-cosecha, se gestiona como una Task principal dentro del proyecto correspondiente.

Este enfoque permite una trazabilidad y contabilidad de costos de precisión inigualable. Los insumos consumidos (módulo Stock), la mano de obra empleada (módulo Human Resources), las actividades productivas (módulo Manufacturing) y las transacciones financieras (módulo Accounting) se vinculan directamente a un lote específico. El resultado es una visión de 360 grados de la rentabilidad y eficiencia de cada metro cuadrado de la explotación agrícola.

Abordaje de la Complejidad Agrícola

El sector agrícola se caracteriza por su alta variabilidad: ciclos de cultivo estacionales, activos biológicos que crecen y cambian de valor, múltiples modalidades de pago a trabajadores y una necesidad imperativa de trazabilidad. Si bien el módulo de Agricultura nativo de ERPNext ofrece un excelente punto de partida para gestionar unidades de tierra y ciclos de cultivo , las operaciones del mundo real exigen una personalización extensiva. La flexibilidad inherente del Frappe Framework, a través de la creación de DocTypes personalizados, scripts de servidor y flujos de trabajo, es la clave para modelar con éxito esta complejidad y construir un sistema que se adapte fielmente a la realidad del campo.

Sección I: Adaptación de Módulos Estándar para la Agricultura

A. Manufacturing: Modelado de Flujos de Producción Agrícola

El módulo de Manufactura, diseñado para la producción industrial, puede ser ingeniosamente adaptado para gestionar los procesos biológicos de la agricultura.

    El Ciclo de Cultivo como Orden de Trabajo (Work Order): Cada ciclo de cultivo se representa mediante una Work Order. En esta analogía, las "materias primas" son las semillas y los insumos agrícolas, y el "producto terminado" es la cosecha cuantificada. Esta estructura permite planificar la producción, asignar recursos y rastrear los costos de transformación de insumos en producto final.

    Lista de Materiales (BOM) para Insumos del Cultivo: Para cada tipo de cultivo, se crea una BOM (Bill of Materials) que detalla las cantidades teóricas de insumos necesarios por unidad de superficie (ej. por hectárea). Esta BOM incluye semillas, fertilizantes, pesticidas y otros consumibles. Al crear una Work Order para un lote de un área determinada, el sistema puede calcular automáticamente la cantidad planificada de insumos, facilitando la planificación de compras y la gestión de inventarios.

    Operaciones y Estaciones de Trabajo como Fases Agrícolas: Las fases fenológicas del cultivo (preparación de tierra, siembra, germinación, crecimiento vegetativo, floración, cosecha) se modelan como Operations dentro de la Work Order. Las Workstations pueden representar los lotes o parcelas físicas donde se ejecutan estas operaciones, permitiendo un seguimiento detallado del progreso del ciclo productivo en cada ubicación específica.

B. Stock Management: Gestión de Inventarios de Cosecha y Consumibles

Una gestión de inventario precisa es vital para el control de costos y la trazabilidad.

    Estructura de Almacenes (Warehouse): Se recomienda una estructura de almacenes jerárquica para reflejar la realidad física y lógica de la finca. Un almacén principal (Warehouse) puede contener sub-almacenes como "Insumos Agrícolas", "Cosecha en Campo" (producto recién recolectado), "Producto Terminado" (cosecha clasificada y lista para venta) y "Maquinaria y Repuestos". Esta estructura facilita el control de existencias y la valoración de inventarios en cada etapa.

    Trazabilidad con Lotes (Batch): El uso de Batch es mandatorio para la trazabilidad. Cada lote de cosecha debe ser registrado con un número de Batch único que lo vincule a su Project (lote de origen), fecha de cosecha y ciclo de cultivo. De igual manera, los insumos como fertilizantes y pesticidas deben ser gestionados por lotes para controlar fechas de caducidad y cumplir con normativas de seguridad alimentaria.

    Movimientos de Inventario (Stock Entry): El consumo de insumos se registra a través de un Stock Entry de tipo "Material Issue", debitando el inventario del almacén de "Insumos Agrícolas" y asignando el costo a la Work Order correspondiente. La entrada de la cosecha al inventario se realiza con un Stock Entry de tipo "Material Receipt", acreditando el producto en el almacén de "Cosecha en Campo" o "Producto Terminado".

C. Human Resources: Gestión de Trabajadores Agrícolas (Contexto Guatemala)

El módulo de RRHH estándar de ERPNext está diseñado principalmente para salarios fijos o por horas, un modelo que no se ajusta a la realidad del pago por producción (a destajo), predominante en la agricultura guatemalteca. Por tanto, es necesaria una reingeniería del proceso de nómina.

La remuneración en el campo se basa en unidades de producción: quintales de café cosechados, toneladas de caña cortadas, o "tareas" completadas. Aunque la legislación guatemalteca establece salarios mínimos diarios y mensuales , la práctica operativa es el pago por rendimiento. El sistema ERP debe ser capaz de registrar esta producción diaria y, crucialmente, verificar que la remuneración total del período cumpla o exceda el salario mínimo legal.

Además, las prestaciones laborales obligatorias como el Bono 14 y el Aguinaldo, así como las deducciones del Instituto Guatemalteco de Seguridad Social (IGSS), se calculan sobre el salario ordinario devengado, que en este modelo es la suma de los pagos por producción. Esto implica que el flujo de datos para la nómina no puede originarse en una 

Salary Structure fija. Debe nacer de un registro de producción diario por trabajador, cuyos montos se agregan para constituir la base del Salary Slip.

Diseño de la Solución Propuesta:

    DocTypes Personalizados: Es fundamental crear nuevos DocTypes para modelar la estructura organizativa y operativa del trabajo de campo.

        Cuadrilla: Para agrupar trabajadores bajo la supervisión de un Caporal o jefe de equipo. Contiene un enlace al Employee que actúa como supervisor y una tabla hija con la lista de los Employee miembros.

        Registro de Producción Diario: Este DocType es el corazón de la gestión de nómina a destajo. Registra la fecha, la Cuadrilla, el Lote de Cultivo (vinculado al Project), y contiene una tabla hija (produccion_detalle) donde se anota por cada trabajador: la tarea realizada, la unidad de medida (ej. Tonelada), la cantidad producida, la tarifa por unidad y el pago total calculado.

    Flujo de Nómina Modificado: El proceso de nómina se automatiza mediante un Server Script que se ejecuta al crear una Payroll Entry.

        El script itera sobre los empleados seleccionados en la Payroll Entry.

        Para cada empleado, busca todos los Registro de Producción Diario dentro del período de pago.

        Suma todos los montos de total_pago para calcular el ingreso total por producción del empleado.

        Este total se inserta dinámicamente en el Salary Slip del empleado, en un Salary Component de tipo "Earning" llamado "Producción a Destajo".

    Cálculo de Prestaciones y Deducciones: Los Salary Components para las deducciones del IGSS (4.83% para el trabajador) y para las provisiones de prestaciones (Bono 14, Aguinaldo, Indemnización) se configuran con fórmulas que utilizan el componente "Producción a Destajo" como base de cálculo. Esto asegura que todos los cálculos se realicen sobre el ingreso real devengado, en cumplimiento con la normativa laboral guatemalteca.

D. Accounting: Contabilidad Específica para el Agronegocio

La contabilidad agrícola requiere una estructura que refleje la naturaleza única de sus activos y costos.

    Plan de Cuentas (Chart of Accounts): Es crucial personalizar el plan de cuentas para incluir conceptos como "Activos Biológicos" (para valorar los cultivos en crecimiento), "Work in Progress - Agrícola" (para acumular los costos del ciclo de cultivo) y cuentas de gastos detalladas por tipo de insumo (ej. "Costo de Fertilización", "Costo de Riego", "Costo de Mano de Obra Directa").

    Contabilidad de Costos por Proyecto: La vinculación de todas las transacciones al Project (lote) es la clave para una contabilidad de costos efectiva. Cada Stock Entry de consumo de insumos, cada Salary Slip y cada registro de depreciación de maquinaria debe ser etiquetado con el Project correspondiente. Esto permite generar un Profit and Loss Statement filtrado por proyecto, ofreciendo una visión precisa y granular de la rentabilidad de cada lote.

E. Projects: Gestión Avanzada de Lotes, Parcelas y Ciclos de Cultivo

El módulo de Proyectos se convierte en el centro neurálgico de la operación agrícola.

    Estructura Jerárquica: Se debe implementar una estructura de Projects en árbol que refleje la geografía de la finca: Finca Principal (Proyecto Padre) -> Campo A (Sub-proyecto) -> Lote A-01 (Sub-proyecto). Esto permite la agregación de datos a cualquier nivel.

    Tareas como Ciclos y Actividades: Dentro de cada Project de nivel más bajo (Lote), se crea una Task principal para cada ciclo de cultivo (ej. "Ciclo de Café 2024-2025"). Las sub-tareas dentro de esta Task principal representan las actividades agronómicas específicas: "Poda", "Primera Fertilización", "Control de Roya", "Cosecha", etc..

    Integración y Visibilidad: Esta arquitectura proporciona una visibilidad completa. Al acceder al dashboard del Project "Lote A-01", un gerente puede visualizar de forma centralizada todas las Work Orders asociadas, los Stock Entries de insumos, los Salary Slips de los trabajadores que laboraron en ese lote, y los Sales Invoices generados por la venta de la cosecha de esa parcela específica.

Sección II: Diseño de DocTypes Personalizados para el Sector Agrícola

A. Arquitectura y Mejores Prácticas

La creación de DocTypes personalizados es la base para adaptar ERPNext a las necesidades específicas de la agricultura.

    Convenciones de Nomenclatura: Se recomienda utilizar un prefijo estandarizado, como "AGRI", para todos los DocTypes, campos y scripts personalizados. Por ejemplo, AGRI Lote de Cultivo. Esto previene colisiones de nombres con futuras actualizaciones del core y mejora la legibilidad y mantenimiento del código.

    Modularidad: Todas las personalizaciones (DocTypes, scripts, reportes) deben ser encapsuladas en una Custom App, por ejemplo, "Agri Management". Este enfoque modulariza el desarrollo, facilita el control de versiones con Git y simplifica drásticamente el proceso de actualización de la instancia de ERPNext, ya que el código personalizado está aislado del núcleo del sistema.

    DocTypes Agrícolas Esenciales: La gestión agrícola requiere modelar entidades que no existen en el ERP estándar. Un Lote de Cultivo es la unidad física de tierra con propiedades geoespaciales y de suelo. Un Ciclo de Cultivo es la instancia temporal de un cultivo en un lote. Un Registro de Aplicación traza qué insumos se usaron, cuándo y dónde. Un Registro de Cosecha captura el rendimiento. Y una Cuadrilla modela la estructura organizativa del personal de campo. Estos DocTypes forman la columna vertebral de la operación.

Nombre del DocType	Módulo	Propósito	Campos Clave	Relaciones
AGRI Lote de Cultivo	Agriculture	Representa una parcela física de tierra.	lote_id, area_hectareas (Float), coordenadas_gps (Geolocation), tipo_suelo (Link a AGRI Tipo de Suelo), project (Link a Project)	Padre de AGRI Ciclo de Cultivo.
AGRI Ciclo de Cultivo	Agriculture	Gestiona un ciclo de siembra a cosecha.	cultivo (Link a Item), lote (Link a AGRI Lote de Cultivo), fecha_siembra (Date), fecha_estimada_cosecha (Date), estado (Select), work_order (Link a Work Order)	Hijo de AGRI Lote de Cultivo.
AGRI Registro de Aplicación	Stock	Registra el uso de insumos (fertilizantes, pesticidas).	ciclo_cultivo (Link a AGRI Ciclo de Cultivo), fecha_aplicacion (Date), insumo (Link a Item), cantidad (Float), stock_entry (Link a Stock Entry)	Vinculado a AGRI Ciclo de Cultivo y Stock Entry.
AGRI Registro de Cosecha	Stock	Registra la producción obtenida de un lote.	ciclo_cultivo (Link a AGRI Ciclo de Cultivo), fecha_cosecha (Date), cantidad_cosechada (Float), unidad (Link a UOM), almacen_destino (Link a Warehouse)	Vinculado a AGRI Ciclo de Cultivo.
AGRI Cuadrilla	Human Resources	Organiza a los trabajadores de campo.	nombre_cuadrilla, caporal (Link a Employee), miembros (Table: Employee)	Estructura organizativa para RRHH.
AGRI Registro de Producción Diario	Human Resources	Registra el trabajo a destajo para la nómina.	fecha (Date), cuadrilla (Link a AGRI Cuadrilla), lote (Link a AGRI Lote de Cultivo), produccion_detalle (Table: Employee, tarea, cantidad, tarifa, total_pago)	La base para el cálculo de la nómina.

B. Campos Calculados y Fórmulas Automáticas

Los campos calculados pueden mostrar información valiosa sin necesidad de almacenamiento redundante.

    Ejemplo en AGRI Lote de Cultivo: Se puede añadir un campo Read Only llamado "Rendimiento Promedio (Ton/Ha)". Este campo no se almacena en la base de datos, sino que se calcula en tiempo real mediante un Server Script o un método de controlador. El script consultaría todos los AGRI Registro de Cosecha asociados a los ciclos de cultivo de ese lote, sumaría la cantidad_cosechada, y la dividiría por el campo area_hectareas del lote.

    JSON de Ejemplo (AGRI Lote de Cultivo): A continuación se muestra una estructura JSON simplificada para la definición del DocType AGRI Lote de Cultivo, ilustrando la configuración de sus campos.

JSON

{
 "doctype": "DocType",
 "name": "AGRI Lote de Cultivo",
 "module": "Agriculture",
 "custom": 1,
 "autoname": "field:lote_id",
 "fields":,
 "permissions":
}

C. Relaciones entre Documentos (Link Fields)

Los Link Fields son esenciales para construir un modelo de datos relacional y coherente. Por ejemplo, en el DocType AGRI Ciclo de Cultivo, el campo lote es un Link a AGRI Lote de Cultivo. Esto no solo asegura la integridad referencial, sino que también permite funcionalidades avanzadas. Mediante un Client Script, se puede usar cur_frm.add_fetch para que, al seleccionar un lote, campos como area_hectareas se copien automáticamente al formulario del ciclo de cultivo, reduciendo la entrada manual de datos y posibles errores.

D. Validaciones Personalizadas (Custom Scripts)

Los Custom Scripts permiten implementar lógica de negocio directamente en el cliente (navegador), proporcionando retroalimentación inmediata al usuario.

    Ejemplo de Client Script: Para el DocType AGRI Registro de Aplicación, se puede implementar una validación que asegure que solo se apliquen insumos permitidos para un cultivo específico. Al seleccionar un insumo (ej. un pesticida) en la tabla hija, un Client Script puede hacer una llamada al servidor (frappe.call) para ejecutar una función Python que verifique si ese insumo está autorizado para el tipo de cultivo del AGRI Ciclo de Cultivo actual. Si no está permitido, el script puede lanzar una alerta (frappe.throw) y evitar que se guarde el registro.

    Código de Ejemplo (Client Script):

JavaScript

// Aplicado al DocType hijo del Registro de Aplicación
frappe.ui.form.on('AGRI Registro Aplicacion Detalle', {
    insumo: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.insumo && frm.doc.ciclo_cultivo) {
            frappe.call({
                method: "agri_management.api.validate_insumo_for_cultivo",
                args: {
                    insumo: row.insumo,
                    ciclo_cultivo: frm.doc.ciclo_cultivo
                },
                callback: function(r) {
                    if (r.message &&!r.message.is_valid) {
                        frm.fields_dict.insumos.grid.grid_rows_by_docname[cdn].set_value('insumo', '');
                        frappe.throw(__("El insumo {0} no está permitido para este cultivo.", [row.insumo]));
                    }
                }
            });
        }
    }
});

E. Workflows para Procesos Agrícolas

El Workflow de Frappe permite definir y hacer cumplir los procesos de negocio. Para el DocType AGRI Ciclo de Cultivo, se puede diseñar un flujo de trabajo con los siguientes estados: "Planificado", "En Progreso", "Cosechado" y "Cerrado". Se definen las transiciones permitidas entre estos estados (ej. de "En Progreso" a "Cosechado") y los roles de usuario que tienen permiso para ejecutar cada transición (ej. solo el "Gerente de Finca" puede mover un ciclo al estado "Cerrado"). Esto asegura que los procesos se sigan de manera ordenada y con las aprobaciones adecuadas.

Sección III: Automatización de Procesos Agrícolas

A. Server Scripts para Cálculos Automáticos

Los Server Scripts son fragmentos de código Python que se ejecutan en el servidor en respuesta a eventos de documentos (como guardar o enviar), permitiendo una automatización potente y segura.

La automatización de la contabilidad de costos es un caso de uso primordial. El acto de registrar una cosecha no es solo una operación logística, sino un evento contable significativo: transforma un activo en crecimiento (Work in Progress) en un activo de inventario (Producto Terminado). El valor de este nuevo inventario debe reflejar todos los costos acumulados durante el ciclo de cultivo, que están registrados en la Work Order asociada.

Un Server Script en el DocType AGRI Registro de Cosecha, configurado para ejecutarse en el evento After Submit, puede automatizar este complejo proceso. El script creará automáticamente un Stock Entry de tipo "Material Receipt" para ingresar la cantidad cosechada en el almacén correspondiente. Simultáneamente, puede obtener el costo total de la Work Order asociada y crear un Journal Entry para reclasificar este valor de la cuenta "Work in Progress - Agrícola" a la cuenta "Inventario de Producto Terminado", asegurando que la contabilidad refleje la operación en tiempo real.

    Código de Ejemplo (Server Script en Python):

Python

# DocType: AGRI Registro de Cosecha
# Script Type: After Submit

# Evitar ejecución duplicada
if doc.get("stock_entry_generado"):
    return

try:
    # Obtener el ciclo de cultivo y la orden de trabajo asociada
    ciclo_cultivo = frappe.get_doc("AGRI Ciclo de Cultivo", doc.ciclo_cultivo)
    
    # Crear la entrada de stock para recibir la cosecha
    se = frappe.new_doc("Stock Entry")
    se.purpose = "Material Receipt"
    se.set("posting_date", doc.fecha_cosecha)
    se.to_warehouse = doc.almacen_destino
    
    # Obtener el costo de la Work Order (si está completada)
    # Para este ejemplo, se asume un costo estándar. En un caso real, se obtendría de la WO.
    costo_estandar_por_unidad = frappe.db.get_value("Item Price", {"item_code": ciclo_cultivo.cultivo, "price_list": "Standard Buying"}, "price_list_rate") or 0

    se.append("items", {
        "item_code": ciclo_cultivo.cultivo,
        "qty": doc.cantidad_cosechada,
        "uom": doc.unidad,
        "t_warehouse": doc.almacen_destino,
        "basic_rate": costo_estandar_por_unidad,
        "project": ciclo_cultivo.project
    })
    
    se.insert(ignore_permissions=True)
    se.submit()

    # Marcar el registro de cosecha para evitar duplicados
    frappe.db.set_value("AGRI Registro de Cosecha", doc.name, "stock_entry_generado", se.name)
    frappe.msgprint(f"Entrada de Stock {se.name} creada exitosamente.")

except Exception as e:
    frappe.log_error(frappe.get_traceback(), "Error en Server Script de Registro de Cosecha")
    frappe.throw("Ocurrió un error al generar la entrada de stock.")

B. Client Scripts para Validaciones en Tiempo Real

Los Client Scripts mejoran la experiencia del usuario al proporcionar cálculos y validaciones instantáneas. En el AGRI Registro de Producción Diario, un script puede configurarse en la tabla hija para que, cada vez que se modifique el campo cantidad o tarifa, el campo total_pago se recalcule y actualice automáticamente en la misma fila, sin necesidad de guardar el documento.

C. Hooks de Documento (before_save, after_insert)

Los Hooks, definidos en el archivo hooks.py de la aplicación personalizada, permiten ejecutar funciones Python en eventos específicos del ciclo de vida del documento. Un hook doc_events en el Salary Slip para el evento before_save es ideal para implementar validaciones complejas. Por ejemplo, antes de guardar una nómina, se puede ejecutar una función que verifique si la suma de los ingresos por producción de un trabajador es inferior al salario mínimo legal para el período. Si es así, la función puede añadir automáticamente un nuevo Salary Component de tipo "Earning" llamado "Ajuste Salario Mínimo" para cubrir la diferencia y garantizar el cumplimiento normativo.

D. Scheduled Jobs para Procesos Recurrentes

Las tareas recurrentes se pueden automatizar mediante Scheduled Jobs. Se puede configurar un trabajo programado para que se ejecute diariamente y revise todos los AGRI Ciclo de Cultivo activos. Basándose en las Operations planificadas en la Work Order asociada, el script puede crear automáticamente documentos ToDo y asignarlos al "Gerente de Finca" para las actividades programadas de esa semana, como "Aplicar Fertilizante - Semana 4" o "Monitoreo de Plagas".

E. Email Alerts y Notificaciones

El sistema de Notification de ERPNext puede configurarse para enviar alertas automáticas. Por ejemplo, se puede crear una notificación que se active con el evento on_submit del DocType AGRI Registro de Cosecha. Esta notificación enviará un correo electrónico al rol "Jefe de Almacén", informándole de la nueva producción que está en camino al almacén, incluyendo detalles como el lote de origen, el producto y la cantidad.

Sección IV: Inteligencia de Negocio: Reportes y Análisis Agrícola

A. Query Reports Personalizados

Para reportes operativos rápidos que no requieren lógica compleja, los Query Reports son la herramienta ideal. Permiten escribir consultas SQL directamente para extraer y presentar datos de la base de datos.

    Ejemplo de Query Report: "Producción Diaria por Cuadrilla y Lote"
    Este reporte proporciona una vista rápida del rendimiento diario de los equipos de trabajo.

SQL

SELECT
    rpd.fecha,
    rpd.cuadrilla,
    rpd.lote,
    rpdd.employee AS codigo_trabajador,
    emp.employee_name AS nombre_trabajador,
    rpdd.tarea,
    rpdd.cantidad,
    rpdd.tarifa,
    rpdd.total_pago
FROM
    `tabAGRI Registro de Produccion Diario` AS rpd
JOIN
    `tabAGRI Produccion Detalle` AS rpdd ON rpd.name = rpdd.parent
JOIN
    `tabEmployee` AS emp ON rpdd.employee = emp.name
WHERE
    rpd.docstatus = 1
ORDER BY
    rpd.fecha DESC, rpd.cuadrilla;

B. Script Reports para Análisis Complejo

Para análisis que requieren lógica de negocio, cálculos avanzados y la consolidación de datos de múltiples fuentes, los Script Reports en Python son la solución.

La rentabilidad en la agricultura solo puede medirse con precisión a nivel de lote y ciclo de cultivo. Sin embargo, los datos de costos (insumos, mano de obra, depreciación de maquinaria) y los ingresos (ventas) están distribuidos en diferentes documentos (Stock Entry, Salary Slip, Journal Entry, Sales Invoice). Estos documentos, en la arquitectura propuesta, están unificados por su vínculo a un Project específico.

Un Script Report de "Análisis de Rentabilidad por Lote" permite consolidar esta información. El reporte tomaría un Project y un rango de fechas como filtros. El script en Python ejecutaría múltiples consultas frappe.db.sql para agregar:

    El costo de todos los insumos consumidos (desde Stock Ledger Entry) vinculados al proyecto.

    El costo total de la mano de obra (desde Salary Slip) asignada al proyecto.

    Los costos indirectos y de depreciación (desde Journal Entry) asociados al proyecto.

    Los ingresos totales por la venta de la cosecha (desde Sales Invoice Item) vinculada al proyecto.

Finalmente, el script presentaría una tabla detallada con el desglose de ingresos, costos por categoría y el margen de beneficio neto para el lote seleccionado.

    Esqueleto de Código (Script Report en Python):

Python

import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return

def get_data(filters):
    if not filters.get("project"):
        return

    project = filters.get("project")
    
    # Lógica para obtener costos de insumos
    costo_insumos = frappe.db.sql("""
        SELECT SUM(stock_value_difference) 
        FROM `tabStock Ledger Entry` 
        WHERE project = %(project)s AND voucher_type = 'Stock Entry'
    """, {"project": project}) or 0

    # Lógica para obtener costos de mano de obra
    costo_mano_obra = frappe.db.sql("""
        SELECT SUM(gross_pay) 
        FROM `tabSalary Slip` 
        WHERE project = %(project)s AND docstatus = 1
    """, {"project": project}) or 0

    # Lógica para obtener ingresos por ventas
    ingresos_ventas = frappe.db.sql("""
        SELECT SUM(base_amount) 
        FROM `tabSales Invoice Item` 
        WHERE project = %(project)s AND docstatus = 1
    """, {"project": project}) or 0

    rentabilidad = ingresos_ventas - (costo_insumos + costo_mano_obra)

    data =
    
    return data

C. Dashboard y KPIs Agrícolas

Los Dashboards personalizables permiten a los gerentes monitorear la salud de la operación de un vistazo. Se puede diseñar un dashboard para el "Gerente de Finca" con Dashboard Charts que visualicen KPIs (Key Performance Indicators) cruciales:

    Rendimiento por Hectárea: Un gráfico de tipo "Number Card" que muestra el resultado de (SUM(cantidad_cosechada) / SUM(area_hectareas)) de los DocTypes AGRI Registro de Cosecha y AGRI Lote de Cultivo.

    Costo por Tonelada Producida: Un gráfico que divide los costos totales acumulados en un Project por la cantidad total cosechada.

    Estado de Ciclos de Cultivo: Un gráfico de pastel que muestra la distribución de los AGRI Ciclo de Cultivo por su campo estado ("Planificado", "En Progreso", etc.).

D. Gráficos de Productividad y Costos

Dentro de los Script Reports, se pueden integrar gráficos para una visualización más intuitiva de los datos. El reporte "Análisis de Rentabilidad por Lote" puede incluir un gráfico de barras que compare los componentes del costo (insumos, mano de obra, maquinaria) entre diferentes lotes, facilitando la identificación de áreas de mejora.

E. Exportación de Datos

Todos los reportes en ERPNext, ya sean estándar, Query o Script, ofrecen la funcionalidad de exportar los datos a formatos como CSV o Microsoft Excel. Esto permite a los usuarios realizar análisis más profundos o integrar la información con otras herramientas de inteligencia de negocio.

Sección V: Integración y Gestión de Datos

A. REST API para Aplicaciones Móviles

El Frappe Framework expone automáticamente todos los DocTypes, incluidos los personalizados, a través de una API REST completa. Esto es fundamental para integrar el ERP con aplicaciones móviles de campo, que pueden ser utilizadas por supervisores o caporales para registrar datos en tiempo real.

Una aplicación de campo necesitaría funcionalidades clave: autenticar al usuario (caporal), obtener la lista de trabajadores en su cuadrilla, ver las tareas asignadas y, lo más importante, registrar la producción diaria. Cada una de estas acciones se corresponde con un endpoint de la API REST.

    Endpoints Clave para una Aplicación de Campo:

Objetivo	Método HTTP	Endpoint	Payload de Ejemplo (POST/PUT)	Respuesta Esperada
Autenticar Usuario	POST	/api/method/login	{"usr": "caporal@finca.com", "pwd": "..."}	{"message": "Logged In"}
Obtener Lotes Asignados	GET	/api/resource/AGRI Lote de Cultivo?fields=["name","lote_id"]	N/A	Lista de documentos de Lote.
Crear Registro de Producción	POST	/api/resource/AGRI Registro de Produccion Diario	{"fecha": "2024-07-29", "lote": "LOTE-A-01", "produccion_detalle": [{"employee": "EMP-001", "cantidad": 1.5, "tarifa": 100}]}	Documento del nuevo registro creado.

    Código de Ejemplo (Python requests para crear un registro):
    Este script simula una aplicación externa que envía los datos de producción del día al ERPNext.

Python

import requests
import json

# URL de la instancia de ERPNext y credenciales
ERP_URL = "https://su-finca.erpnext.com"
API_KEY = "su_api_key"
API_SECRET = "su_api_secret"

# Datos del nuevo registro de producción
payload = {
    "doctype": "AGRI Registro de Produccion Diario",
    "fecha": "2024-07-29",
    "cuadrilla": "CUADRILLA-01",
    "lote": "LOTE-A-01",
    "produccion_detalle":
}

headers = {
    "Authorization": f"token {API_KEY}:{API_SECRET}",
    "Content-Type": "application/json"
}

# Realizar la solicitud POST para crear el documento
response = requests.post(f"{ERP_URL}/api/resource/AGRI Registro de Produccion Diario", headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    print("Registro de producción creado exitosamente:")
    print(response.json()['data'])
else:
    print("Error al crear el registro:")
    print(response.status_code, response.text)

B. Webhook para Sistemas Externos

Los Webhooks permiten a ERPNext notificar a sistemas externos en tiempo real cuando ocurren eventos específicos. Por ejemplo, se puede configurar un Webhook que se dispare en el evento on_submit de un AGRI Registro de Aplicación. Cuando un supervisor registra la aplicación de un pesticida, el webhook puede enviar un payload JSON a una URL de un sistema de cumplimiento normativo o de seguridad alimentaria, informando el producto utilizado, la dosis, el lote y la fecha.

C. Importación Masiva de Datos

La herramienta Data Import es esencial para la carga inicial de datos y para actualizaciones masivas. Para importar datos a un DocType con una tabla hija (como un Sales Order con sus Items), el formato del archivo CSV es crucial. La primera fila contiene los datos del documento padre y la primera fila de la tabla hija. Las filas subsiguientes para la misma tabla hija deben tener las columnas del documento padre en blanco. Una nueva fila con datos en las columnas del padre indica el comienzo de un nuevo documento.

D. Backup y Sincronización

La integridad de los datos operativos es crítica. Es indispensable establecer una política de backups robusta. El comando bench backup de Frappe permite crear copias de seguridad completas de la base de datos y los archivos. Se deben programar backups automáticos y frecuentes, y almacenarlos en una ubicación externa y segura. Además, se deben documentar y probar periódicamente los procedimientos de restauración para garantizar una rápida recuperación ante desastres.

E. Multi-company Setup

La funcionalidad multi-empresa de ERPNext es ideal para agronegocios que operan con múltiples razones sociales o gestionan fincas como entidades legales separadas. Permite mantener la contabilidad, los inventarios y los datos operativos completamente segregados para cada compañía dentro de una única instancia de ERPNext. Al mismo tiempo, ofrece la capacidad de generar reportes consolidados a nivel de grupo, proporcionando una visión integral del rendimiento del conglomerado.

Conclusión

La implementación de ERPNext en el sector agrícola, aunque compleja, ofrece un retorno de inversión sustancial en términos de eficiencia operativa, control de costos y toma de decisiones basada en datos. La clave del éxito radica en una arquitectura de solución bien concebida, centrada en el concepto de "El Lote como Proyecto", y en la personalización profunda del sistema para reflejar los procesos únicos del agronegocio.

El modelo presentado en esta guía, que combina el uso inteligente de módulos estándar con DocTypes personalizados para operaciones clave (como el Registro de Producción Diario) y una automatización robusta a través de scripts y hooks, proporciona una base sólida. Permite una trazabilidad completa desde el insumo hasta el cliente final, una contabilidad de costos precisa a nivel de lote y una gestión de recursos humanos adaptada a las modalidades de pago por producción, asegurando al mismo tiempo el cumplimiento de las normativas locales. Al aprovechar la flexibilidad del Frappe Framework, es posible transformar ERPNext en un sistema de gestión agrícola integral y altamente competitivo.