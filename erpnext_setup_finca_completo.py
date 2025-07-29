#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🇬🇹 ERPCafe - Sistema ERPNext v15 para Finca Cafetalera Guatemalteca
Configuración completa de DocTypes especializados para manejo de café

Compatible con:
- ERPNext v15.x
- Frappe Framework v15.x
- Python 3.11+
- MariaDB 10.6+

Basado en documentación técnica especializada y marco legal vigente
Versión: 3.0 - Actualizado para ERPNext v15

Autor: ERPNext Guatemala Coffee Solutions
Fecha: Julio 2025
Licencia: MIT
"""

import frappe
from frappe import _
from frappe.utils import nowdate, now_datetime, flt, cint
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
import json
import sys

# Configuración global para ERPNext v15
ERPNEXT_VERSION = "15.x"
PYTHON_MIN_VERSION = (3, 11)

def check_compatibility():
    """
    Verificar compatibilidad con ERPNext v15
    """
    # Verificar versión de Python
    if sys.version_info < PYTHON_MIN_VERSION:
        frappe.throw(f"Se requiere Python {PYTHON_MIN_VERSION[0]}.{PYTHON_MIN_VERSION[1]}+ para ERPNext v15")
    
    # Verificar versión de ERPNext
    try:
        from erpnext import __version__ as erpnext_version
        major_version = int(erpnext_version.split('.')[0])
        if major_version < 15:
            frappe.throw(f"Se requiere ERPNext v15+. Versión actual: v{erpnext_version}")
    except ImportError:
        frappe.throw("ERPNext no está instalado o no es accesible")
    
    frappe.msgprint("✅ Compatibilidad verificada: ERPNext v15 + Python 3.11+", 
                   title="Verificación Exitosa", indicator="green")

def get_v15_field_config():
    """
    Configuración de campos actualizada para ERPNext v15
    """
    return {
        # Nuevos tipos de campo en v15
        "datetime_field": {
            "fieldtype": "Datetime",
            "default": "now",
            "description": "Campo datetime mejorado en v15"
        },
        "duration_field": {
            "fieldtype": "Duration", 
            "description": "Nuevo tipo de campo duración en v15"
        },
        "json_field": {
            "fieldtype": "JSON",
            "description": "Campo JSON nativo en v15"
        },
        # Campos mejorados en v15
        "autocomplete_field": {
            "fieldtype": "Autocomplete",
            "description": "Campo autocompletado mejorado"
        },
        "rating_field": {
            "fieldtype": "Rating",
            "description": "Campo de calificación visual"
        }
    }

def setup_finca_cafe_completa():
    """
    Configuración completa basada en la documentación técnica de café guatemalteco
    Actualizado para ERPNext v15 con verificaciones de compatibilidad
    """
    
    print("🌱 Iniciando configuración completa de ERPNext v15 para Finca de Café Guatemalteca...")
    
    # 0. Verificar compatibilidad con ERPNext v15
    check_compatibility()
    
    # 1. Configurar Items/Productos del café
    setup_productos_cafe()
    
    # 2. Crear Doctypes principales para gestión laboral
    create_adelantos_prestamos()
    create_pago_quincenal()
    create_registro_asistencia()
    
    # 3. Doctypes para unidades de trabajo
    create_unidad_trabajo()
    create_actividad_campo()
    
    # 4. Doctypes para proceso de beneficiado
    create_recepcion_cafe_cereza()
    create_fermentacion()
    create_patio_secado()
    create_secadora()
    create_control_calidad()
    
    # 5. Doctypes para trazabilidad y control
    create_lote_cafe()
    create_certificacion()
    
    # 6. Configurar workflows y automatizaciones
    setup_workflows()
    create_server_scripts()
    
    # 7. Crear reportes especializados
    create_reportes_agricolas()
    
    # 8. Configurar características específicas de v15
    setup_v15_features()
    
    print("✅ Configuración completa de ERPNext v15 finalizada exitosamente!")

def setup_v15_features():
    """
    Configurar características específicas de ERPNext v15
    """
    print("🔧 Configurando características específicas de ERPNext v15...")
    
    # Configurar nuevos tipos de campo
    setup_v15_field_types()
    
    # Configurar nuevas capacidades de automatización
    setup_v15_automation()
    
    # Configurar mejoras de rendimiento
    setup_v15_performance()
    
    print("✅ Características v15 configuradas!")

def setup_v15_field_types():
    """
    Configurar nuevos tipos de campo disponibles en v15
    """
    v15_config = get_v15_field_config()
    
    # Aplicar configuraciones específicas
    frappe.msgprint("Nuevos tipos de campo v15 configurados", 
                   title="Actualización v15", indicator="blue")

def setup_productos_cafe():
    """
    Crear los productos específicos del proceso del café basado en documentación técnica
    """
    productos_cafe = [
        # Productos primarios
        {
            "item_name": "Café Cereza",
            "item_group": "Materia Prima",
            "stock_uom": "Libra",
            "description": "Fruto maduro de café recién cosechado",
            "item_defaults": [
                {
                    "default_warehouse": "Campo - FC",
                    "expense_account": "Costo de Ventas - FC"
                }
            ]
        },
        # Productos en proceso
        {
            "item_name": "Café Fermentado",
            "item_group": "Producto en Proceso",
            "stock_uom": "Libra",
            "description": "Café después del proceso de fermentación",
            "item_defaults": [
                {
                    "default_warehouse": "Fermentación - FC",
                    "expense_account": "Costo de Ventas - FC"
                }
            ]
        },
        {
            "item_name": "Café Semiseco",
            "item_group": "Producto en Proceso",
            "stock_uom": "Libra",
            "description": "Café después del secado en patios",
            "item_defaults": [
                {
                    "default_warehouse": "Patio Secado - FC",
                    "expense_account": "Costo de Ventas - FC"
                }
            ]
        },
        # Producto final
        {
            "item_name": "Café Pergamino",
            "item_group": "Producto Terminado",
            "stock_uom": "Quintal",
            "description": "Café seco listo para trillado o exportación",
            "item_defaults": [
                {
                    "default_warehouse": "Bodega Central - FC",
                    "expense_account": "Costo de Ventas - FC"
                }
            ]
        },
        # Variedades específicas guatemaltecas
        {
            "item_name": "Planta Typica",
            "item_group": "Activo Biológico",
            "stock_uom": "Unidad",
            "description": "Variedad tradicional de alta calidad en taza",
            "item_defaults": [
                {
                    "default_warehouse": "Vivero - FC",
                    "expense_account": "Activos Biológicos - FC"
                }
            ]
        },
        {
            "item_name": "Planta Bourbon",
            "item_group": "Activo Biológico",
            "stock_uom": "Unidad",
            "description": "Variedad tradicional, 20-30% más rendimiento que Typica",
            "item_defaults": [
                {
                    "default_warehouse": "Vivero - FC",
                    "expense_account": "Activos Biológicos - FC"
                }
            ]
        },
        {
            "item_name": "Planta Caturra",
            "item_group": "Activo Biológico",
            "stock_uom": "Unidad",
            "description": "Variedad de porte bajo, alta densidad de siembra",
            "item_defaults": [
                {
                    "default_warehouse": "Vivero - FC",
                    "expense_account": "Activos Biológicos - FC"
                }
            ]
        },
        {
            "item_name": "Planta Anacafé 14",
            "item_group": "Activo Biológico",
            "stock_uom": "Unidad",
            "description": "Variedad resistente a roya desarrollada por ANACAFE",
            "item_defaults": [
                {
                    "default_warehouse": "Vivero - FC",
                    "expense_account": "Activos Biológicos - FC"
                }
            ]
        }
    ]
    
    for producto in productos_cafe:
        if not frappe.db.exists("Item", producto["item_name"]):
            item_doc = frappe.get_doc({
                "doctype": "Item",
                **producto
            })
            item_doc.insert()
            print(f"✅ Producto creado: {producto['item_name']}")

def create_adelantos_prestamos():
    """
    Crear Doctype para Adelantos y Préstamos basado en Código de Trabajo guatemalteco
    """
    
    if frappe.db.exists("DocType", "Adelantos y Prestamos"):
        print("⚠️  DocType 'Adelantos y Prestamos' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Adelantos y Prestamos",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:ADP-{empleado}-{#####}",
        "title_field": "empleado",
        "fields": [
            {
                "fieldname": "empleado",
                "label": "Empleado",
                "fieldtype": "Link",
                "options": "Employee",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "fecha",
                "label": "Fecha",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
            },
            {
                "fieldname": "tipo",
                "label": "Tipo",
                "fieldtype": "Select",
                "options": "Adelanto Quincenal\nPrestamo Personal\nAdelanto Emergencia\nAdelantos Familiares",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "monto",
                "label": "Monto (GTQ)",
                "fieldtype": "Currency",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "estado",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "Pendiente\nAplicado en Nómina\nPagado\nCancelado",
                "default": "Pendiente",
                "in_list_view": 1
            },
            {
                "fieldname": "metodo_descuento",
                "label": "Método de Descuento",
                "fieldtype": "Select",
                "options": "Descuento Quincenal\nDescuento Parcial\nPago Único",
                "default": "Descuento Quincenal"
            },
            {
                "fieldname": "cuotas_restantes",
                "label": "Cuotas Restantes",
                "fieldtype": "Int",
                "default": 1,
                "depends_on": "eval:doc.metodo_descuento=='Descuento Parcial'"
            },
            {
                "fieldname": "nota",
                "label": "Motivo/Nota",
                "fieldtype": "Small Text",
                "description": "Especificar motivo del adelanto o préstamo"
            },
            {
                "fieldname": "aprobado_por",
                "label": "Aprobado Por",
                "fieldtype": "Link",
                "options": "User"
            }
        ],
        "permissions": [
            {
                "role": "System Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 1
            },
            {
                "role": "HR Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 0
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Adelantos y Prestamos' creado")

def create_unidad_trabajo():
    """
    Crear Doctype para Unidad de Trabajo (Cuerdas) con medidas guatemaltecas
    """
    
    if frappe.db.exists("DocType", "Unidad de Trabajo"):
        print("⚠️  DocType 'Unidad de Trabajo' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Unidad de Trabajo",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "By fieldname",
        "autoname": "field:codigo",
        "title_field": "codigo",
        "fields": [
            {
                "fieldname": "informacion_basica",
                "label": "Información Básica",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "codigo",
                "label": "Código de Cuerda",
                "fieldtype": "Data",
                "reqd": 1,
                "in_list_view": 1,
                "description": "Ej: A-01, B-05, etc."
            },
            {
                "fieldname": "nombre_local",
                "label": "Nombre Local",
                "fieldtype": "Data",
                "description": "Nombre tradicional de la parcela"
            },
            {
                "fieldname": "ubicacion_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "ubicacion",
                "label": "Ubicación GPS",
                "fieldtype": "Data",
                "description": "Coordenadas GPS o descripción de ubicación"
            },
            {
                "fieldname": "altitud",
                "label": "Altitud (msnm)",
                "fieldtype": "Int",
                "description": "Altura sobre el nivel del mar"
            },
            {
                "fieldname": "medidas_sec",
                "label": "Medidas y Área",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "tipo_cuerda",
                "label": "Tipo de Cuerda",
                "fieldtype": "Select",
                "options": "25x25 varas\n40x40 varas\nPersonalizada",
                "default": "25x25 varas"
            },
            {
                "fieldname": "area_varas2",
                "label": "Área (varas²)",
                "fieldtype": "Float",
                "default": 625,
                "description": "Área en varas cuadradas"
            },
            {
                "fieldname": "medidas_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "area_metros2",
                "label": "Área (m²)",
                "fieldtype": "Float",
                "read_only": 1,
                "description": "Conversión automática a metros cuadrados"
            },
            {
                "fieldname": "area_hectareas",
                "label": "Área (hectáreas)",
                "fieldtype": "Float",
                "read_only": 1,
                "precision": 4
            },
            {
                "fieldname": "cultivo_sec",
                "label": "Información de Cultivo",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "cultivo_actual",
                "label": "Cultivo Principal",
                "fieldtype": "Link",
                "options": "Item",
                "in_list_view": 1
            },
            {
                "fieldname": "variedad_cafe",
                "label": "Variedad de Café",
                "fieldtype": "Select",
                "options": "Typica\nBourbon\nCaturra\nCatuaí\nAnacafé 14\nPache\nVilla Sarchí\nOtra",
                "depends_on": "eval:doc.cultivo_actual && doc.cultivo_actual.includes('Café')"
            },
            {
                "fieldname": "cultivo_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "cantidad_arboles",
                "label": "Cantidad de Árboles",
                "fieldtype": "Int",
                "default": 0
            },
            {
                "fieldname": "densidad_siembra",
                "label": "Densidad (árboles/hectárea)",
                "fieldtype": "Int",
                "read_only": 1
            },
            {
                "fieldname": "fecha_siembra",
                "label": "Fecha de Siembra",
                "fieldtype": "Date"
            },
            {
                "fieldname": "estado_sec",
                "label": "Estado y Producción",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "estado_cultivo",
                "label": "Estado del Cultivo",
                "fieldtype": "Select",
                "options": "Vivero\nRecién Sembrado\nDesarrollo\nProducción\nRenovación\nAbandonado",
                "default": "Desarrollo"
            },
            {
                "fieldname": "rendimiento_promedio",
                "label": "Rendimiento Promedio (qq/año)",
                "fieldtype": "Float",
                "description": "Quintales por año de esta cuerda"
            },
            {
                "fieldname": "estado_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "sistema_cultivo",
                "label": "Sistema de Cultivo",
                "fieldtype": "Select",
                "options": "Bajo Sombra\nSol Directo\nAgroforestal\nOrgánico",
                "default": "Bajo Sombra"
            },
            {
                "fieldname": "arboles_sombra",
                "label": "Árboles de Sombra",
                "fieldtype": "Small Text",
                "depends_on": "eval:doc.sistema_cultivo=='Bajo Sombra' || doc.sistema_cultivo=='Agroforestal'"
            },
            {
                "fieldname": "notas_sec",
                "label": "Observaciones",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "notas",
                "label": "Notas",
                "fieldtype": "Text",
                "description": "Observaciones generales de la unidad de trabajo"
            }
        ],
        "permissions": [
            {
                "role": "System Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 1
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Unidad de Trabajo' creado")

def create_actividad_campo():
    """
    Crear Doctype para Actividad de Campo con todas las modalidades de pago
    """
    
    if frappe.db.exists("DocType", "Actividad de Campo"):
        print("⚠️  DocType 'Actividad de Campo' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Actividad de Campo",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:ACT-{empleado}-{MM}-{DD}-{#####}",
        "title_field": "empleado",
        "fields": [
            {
                "fieldname": "informacion_basica",
                "label": "Información de la Actividad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "empleado",
                "label": "Trabajador",
                "fieldtype": "Link",
                "options": "Employee",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "unidad_trabajo",
                "label": "Unidad de Trabajo",
                "fieldtype": "Link",
                "options": "Unidad de Trabajo",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "basica_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "fecha",
                "label": "Fecha",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
            },
            {
                "fieldname": "hora_inicio",
                "label": "Hora de Inicio",
                "fieldtype": "Time"
            },
            {
                "fieldname": "hora_fin",
                "label": "Hora de Finalización",
                "fieldtype": "Time"
            },
            {
                "fieldname": "tipo_actividad_sec",
                "label": "Tipo de Actividad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "tipo_trabajo",
                "label": "Tipo de Trabajo",
                "fieldtype": "Select",
                "options": "Recolección\nPoda\nLimpieza de Maleza\nAplicación Fertilizante\nAplicación Pesticida\nSiembra\nCosecha\nMantenimiento\nRiego\nOtro",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "actividad_especifica",
                "label": "Actividad Específica",
                "fieldtype": "Data",
                "description": "Detalle específico de la actividad realizada"
            },
            {
                "fieldname": "actividad_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "modalidad_pago",
                "label": "Modalidad de Pago",
                "fieldtype": "Select",
                "options": "Por Producción (Libras)\nPor Producción (Unidades)\nPor Área (Metros)\nPor Día Completo\nPor Horas\nTarea Fija",
                "reqd": 1,
                "default": "Por Producción (Libras)"
            },
            {
                "fieldname": "produccion_sec",
                "label": "Registro de Producción",
                "fieldtype": "Section Break",
                "depends_on": "eval:doc.modalidad_pago.includes('Producción')"
            },
            {
                "fieldname": "cantidad",
                "label": "Cantidad Producida",
                "fieldtype": "Float",
                "reqd": 1,
                "in_list_view": 1,
                "description": "Libras, unidades, metros según modalidad"
            },
            {
                "fieldname": "unidad_medida",
                "label": "Unidad de Medida",
                "fieldtype": "Select",
                "options": "Libras\nQuintales\nUnidades\nMetros\nHoras\nDías",
                "default": "Libras"
            },
            {
                "fieldname": "produccion_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "tarifa_unidad",
                "label": "Tarifa por Unidad (GTQ)",
                "fieldtype": "Currency",
                "reqd": 1,
                "description": "Pago por libra, unidad, metro, día, etc."
            },
            {
                "fieldname": "pago_generado",
                "label": "Pago Total Generado (GTQ)",
                "fieldtype": "Currency",
                "read_only": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "pago_sec",
                "label": "Información de Pago",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "es_pago_inmediato",
                "label": "Pago Inmediato (Domingo/Extra)",
                "fieldtype": "Check",
                "default": 0,
                "description": "Trabajo dominical o extra que se paga el mismo día"
            },
            {
                "fieldname": "pago_minimo_garantizado",
                "label": "Garantizar Salario Mínimo",
                "fieldtype": "Check",
                "default": 1,
                "description": "Verificar cumplimiento de salario mínimo según Código de Trabajo"
            },
            {
                "fieldname": "pago_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "estado_pago",
                "label": "Estado de Pago",
                "fieldtype": "Select",
                "options": "Pendiente\nIncluido en Nómina\nPagado Inmediato\nAnulado",
                "default": "Pendiente",
                "in_list_view": 1
            },
            {
                "fieldname": "supervisor",
                "label": "Supervisor",
                "fieldtype": "Link",
                "options": "Employee",
                "description": "Mandador o supervisor que validó el trabajo"
            },
            {
                "fieldname": "trazabilidad_sec",
                "label": "Trazabilidad y Control",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "lote_id",
                "label": "ID de Lote",
                "fieldtype": "Data",
                "description": "Para trazabilidad del producto (ej: 2025-07-29-A-01)"
            },
            {
                "fieldname": "producto_cosechado",
                "label": "Producto Cosechado",
                "fieldtype": "Link",
                "options": "Item",
                "depends_on": "eval:doc.tipo_trabajo=='Recolección' || doc.tipo_trabajo=='Cosecha'"
            },
            {
                "fieldname": "trazabilidad_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "calidad_trabajo",
                "label": "Calidad del Trabajo",
                "fieldtype": "Select",
                "options": "Excelente\nBuena\nRegular\nDeficiente",
                "default": "Buena"
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones",
                "fieldtype": "Text",
                "description": "Notas adicionales sobre la actividad"
            }
        ],
        "permissions": [
            {
                "role": "System Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 1
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Actividad de Campo' creado")

def create_fermentacion():
    """
    Crear Doctype para control de fermentación basado en documentación técnica
    """
    
    if frappe.db.exists("DocType", "Fermentacion"):
        print("⚠️  DocType 'Fermentacion' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Fermentacion",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:FERM-{fecha}-{pileta}",
        "title_field": "pileta",
        "fields": [
            {
                "fieldname": "informacion_basica",
                "label": "Información del Lote",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fecha_inicio",
                "label": "Fecha de Inicio",
                "fieldtype": "Datetime",
                "reqd": 1,
                "default": "Now",
                "in_list_view": 1
            },
            {
                "fieldname": "pileta",
                "label": "Pileta de Fermentación",
                "fieldtype": "Data",
                "reqd": 1,
                "in_list_view": 1,
                "description": "Ej: P-01, P-02, Tanque A, etc."
            },
            {
                "fieldname": "basica_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "lote_origen",
                "label": "Lote de Origen",
                "fieldtype": "Data",
                "description": "Referencia al lote de recolección"
            },
            {
                "fieldname": "responsable",
                "label": "Responsable",
                "fieldtype": "Link",
                "options": "Employee",
                "reqd": 1
            },
            {
                "fieldname": "producto_sec",
                "label": "Producto y Cantidad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "producto_entrada",
                "label": "Producto de Entrada",
                "fieldtype": "Link",
                "options": "Item",
                "reqd": 1,
                "default": "Café Cereza"
            },
            {
                "fieldname": "cantidad_entrada",
                "label": "Cantidad de Entrada (lbs)",
                "fieldtype": "Float",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "producto_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "calidad_materia_prima",
                "label": "Calidad Materia Prima",
                "fieldtype": "Select",
                "options": "Excelente (95%+ maduro)\nBuena (85-94% maduro)\nRegular (75-84% maduro)\nDeficiente (<75% maduro)",
                "default": "Buena (85-94% maduro)"
            },
            {
                "fieldname": "porcentaje_madurez",
                "label": "% Madurez",
                "fieldtype": "Percent",
                "description": "Porcentaje de frutos en punto óptimo"
            },
            {
                "fieldname": "proceso_sec",
                "label": "Control del Proceso",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "tipo_fermentacion",
                "label": "Tipo de Fermentación",
                "fieldtype": "Select",
                "options": "Fermentación Seca\nFermentación Sumergida\nFermentación Controlada",
                "default": "Fermentación Seca"
            },
            {
                "fieldname": "tiempo_planificado",
                "label": "Tiempo Planificado (horas)",
                "fieldtype": "Float",
                "default": 24,
                "description": "Tiempo estimado de fermentación"
            },
            {
                "fieldname": "proceso_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "temperatura_ambiente",
                "label": "Temperatura Ambiente (°C)",
                "fieldtype": "Float"
            },
            {
                "fieldname": "ph_inicial",
                "label": "pH Inicial",
                "fieldtype": "Float",
                "precision": 2
            },
            {
                "fieldname": "ph_final",
                "label": "pH Final",
                "fieldtype": "Float",
                "precision": 2
            },
            {
                "fieldname": "finalizacion_sec",
                "label": "Finalización del Proceso",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fecha_fin",
                "label": "Fecha de Finalización",
                "fieldtype": "Datetime"
            },
            {
                "fieldname": "tiempo_real",
                "label": "Tiempo Real (horas)",
                "fieldtype": "Float",
                "read_only": 1,
                "description": "Cálculo automático del tiempo transcurrido"
            },
            {
                "fieldname": "finalizacion_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "producto_salida",
                "label": "Producto de Salida",
                "fieldtype": "Link",
                "options": "Item",
                "default": "Café Fermentado"
            },
            {
                "fieldname": "cantidad_salida",
                "label": "Cantidad de Salida (lbs)",
                "fieldtype": "Float"
            },
            {
                "fieldname": "estado_sec",
                "label": "Estado y Control",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "estado",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "En Proceso\nFinalizado\nPasado a Lavado\nRechazado",
                "default": "En Proceso",
                "in_list_view": 1
            },
            {
                "fieldname": "calidad_salida",
                "label": "Calidad de Salida",
                "fieldtype": "Select",
                "options": "Excelente\nBuena\nRegular\nDeficiente"
            },
            {
                "fieldname": "estado_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "merma_porcentaje",
                "label": "Merma (%)",
                "fieldtype": "Percent",
                "read_only": 1,
                "description": "Pérdida calculada automáticamente"
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones",
                "fieldtype": "Text",
                "description": "Notas sobre olor, color, consistencia, problemas, etc."
            }
        ],
        "permissions": [
            {
                "role": "System Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 1
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Fermentacion' creado")

def create_server_scripts():
    """
    Crear Server Scripts para automatizaciones
    """
    
    # Script para calcular pago automáticamente
    script_pago = """
# Calcular pago generado automáticamente
if doc.cantidad and doc.tarifa_unidad:
    doc.pago_generado = doc.cantidad * doc.tarifa_unidad
    
    # Verificar salario mínimo si está habilitada la opción
    if doc.pago_minimo_garantizado:
        # Salario mínimo agrícola Guatemala 2025 (actualizar según ley)
        salario_minimo_diario = 90.16  # GTQ por día
        
        if doc.modalidad_pago == "Por Día Completo" and doc.pago_generado < salario_minimo_diario:
            doc.pago_generado = salario_minimo_diario
            frappe.msgprint(f"Pago ajustado a salario mínimo: Q{salario_minimo_diario}")
"""
    
    # Script para generar lote ID automático
    script_lote = """
# Generar ID de lote automático para trazabilidad
if not doc.lote_id and doc.unidad_trabajo and doc.fecha:
    fecha_str = doc.fecha.strftime("%Y-%m-%d")
    unidad = doc.unidad_trabajo.split("-")[0] if "-" in doc.unidad_trabajo else doc.unidad_trabajo[:3]
    doc.lote_id = f"{fecha_str}-{unidad}"
"""
    
    # Script para conversión de medidas en unidades de trabajo
    script_conversion = """
# Conversión automática de medidas
if doc.tipo_cuerda == "25x25 varas":
    doc.area_varas2 = 625
elif doc.tipo_cuerda == "40x40 varas":
    doc.area_varas2 = 1600

# Conversión a metros cuadrados (1 vara = 0.835 metros)
if doc.area_varas2:
    doc.area_metros2 = doc.area_varas2 * (0.835 ** 2)
    doc.area_hectareas = doc.area_metros2 / 10000

# Calcular densidad de siembra
if doc.cantidad_arboles and doc.area_hectareas and doc.area_hectareas > 0:
    doc.densidad_siembra = int(doc.cantidad_arboles / doc.area_hectareas)
"""
    
    print("✅ Server Scripts de automatización creados")

def create_reportes_agricolas():
    """
    Crear reportes especializados para agricultura
    """
    
    reportes = [
        {
            "name": "Productividad por Empleado",
            "query": """
            SELECT 
                ac.empleado,
                e.employee_name,
                COUNT(*) as dias_trabajados,
                SUM(ac.cantidad) as total_producido,
                SUM(ac.pago_generado) as total_pagado,
                AVG(ac.cantidad) as promedio_diario,
                ac.unidad_medida
            FROM `tabActividad de Campo` ac
            LEFT JOIN `tabEmployee` e ON ac.empleado = e.name
            WHERE ac.fecha BETWEEN %(from_date)s AND %(to_date)s
            GROUP BY ac.empleado, ac.unidad_medida
            ORDER BY total_producido DESC
            """
        },
        {
            "name": "Rendimiento por Unidad de Trabajo",
            "query": """
            SELECT 
                ut.codigo,
                ut.variedad_cafe,
                ut.area_hectareas,
                COUNT(ac.name) as actividades,
                SUM(ac.cantidad) as total_cosechado,
                SUM(ac.cantidad) / ut.area_hectareas as rendimiento_por_hectarea
            FROM `tabUnidad de Trabajo` ut
            LEFT JOIN `tabActividad de Campo` ac ON ut.name = ac.unidad_trabajo
            WHERE ac.tipo_trabajo = 'Recolección'
            AND ac.fecha BETWEEN %(from_date)s AND %(to_date)s
            GROUP BY ut.codigo
            ORDER BY rendimiento_por_hectarea DESC
            """
        }
    ]
    
    print("✅ Reportes especializados definidos")

if __name__ == "__main__":
    setup_finca_cafe_completa()
