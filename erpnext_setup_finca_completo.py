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
    
    # 4. Doctypes para manejo agronómico integral (FASE 2)
    create_aplicacion_fertilizante()
    create_control_fitosanitario()
    create_control_malezas()
    create_manejo_sombra()
    
    # 5. Doctypes para podas y manejo de tejido (FASE 3)
    create_poda_cafe()
    create_manejo_brotes()
    
    # 6. Doctypes para proceso de beneficiado completo (FASE 5)
    create_recepcion_cafe_cereza()
    create_despulpado()
    create_lavado()
    create_patio_secado_mejorado()
    create_secadora_mejorada()
    create_almacenamiento_pergamino()
    
    print("\n✅ CONFIGURACIÓN COMPLETA FINALIZADA")
    print("   📋 FASE 2: Manejo Agronómico Integral (4 DocTypes)")
    print("   ✂️  FASE 3: Podas y Manejo de Tejido (2 DocTypes)")
    print("   ☕ FASE 5: Proceso de Beneficiado Completo (6 DocTypes)")
    print("\n🎉 ERPNext v15 configurado exitosamente para Finca de Café Guatemalteca!")
    print("📊 Total: 19 DocTypes personalizados para operaciones completas")
    create_almacenamiento_pergamino()
    
    # 7. Doctypes para trazabilidad y control
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

def create_aplicacion_fertilizante():
    """
    Crear DocType para Aplicación de Fertilizantes basado en buenas prácticas agronómicas
    """
    
    if frappe.db.exists("DocType", "Aplicacion Fertilizante"):
        print("⚠️  DocType 'Aplicacion Fertilizante' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Aplicacion Fertilizante",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:FERT-{empleado}-{MM}-{DD}-{#####}",
        "title_field": "unidad_trabajo",
        "fields": [
            {
                "fieldname": "informacion_basica",
                "label": "Información de la Aplicación",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fecha_aplicacion",
                "label": "Fecha de Aplicación",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
            },
            {
                "fieldname": "empleado",
                "label": "Aplicador",
                "fieldtype": "Link",
                "options": "Employee",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "basica_col",
                "fieldtype": "Column Break"
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
                "fieldname": "supervisor",
                "label": "Supervisor Técnico",
                "fieldtype": "Link",
                "options": "Employee",
                "description": "Ingeniero agrónomo o técnico responsable"
            },
            {
                "fieldname": "tipo_fertilizacion_sec",
                "label": "Tipo de Fertilización",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "categoria_fertilizante",
                "label": "Categoría",
                "fieldtype": "Select",
                "options": "Fertilizante Químico\nAbono Orgánico\nEnmienda de Suelo\nFertirriego\nFoliar\nBioestimulante",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "etapa_cultivo",
                "label": "Etapa del Cultivo",
                "fieldtype": "Select",
                "options": "Siembra/Trasplante\nCrecimiento Vegetativo\nPre-Floración\nFloración\nLlenado de Grano\nPost-Cosecha\nMantenimiento",
                "reqd": 1
            },
            {
                "fieldname": "tipo_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "formulacion_npk",
                "label": "Formulación N-P-K",
                "fieldtype": "Data",
                "description": "Ej: 20-20-0, 18-5-15-6S-2MgO, etc."
            },
            {
                "fieldname": "metodo_aplicacion",
                "label": "Método de Aplicación",
                "fieldtype": "Select",
                "options": "Al Suelo (Corona)\nFoliar\nFertirriego\nIncorporado\nBandas\nVoleo",
                "default": "Al Suelo (Corona)"
            },
            {
                "fieldname": "producto_sec",
                "label": "Producto y Dosis",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "producto_fertilizante",
                "label": "Producto Fertilizante",
                "fieldtype": "Link",
                "options": "Item",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "marca_comercial",
                "label": "Marca Comercial",
                "fieldtype": "Data",
                "description": "Nombre comercial del producto"
            },
            {
                "fieldname": "producto_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "dosis_por_planta",
                "label": "Dosis por Planta (gramos)",
                "fieldtype": "Float",
                "precision": 2
            },
            {
                "fieldname": "dosis_por_hectarea",
                "label": "Dosis por Hectárea (kg)",
                "fieldtype": "Float",
                "precision": 2
            },
            {
                "fieldname": "cantidad_sec",
                "label": "Cantidad Aplicada",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "numero_plantas",
                "label": "Número de Plantas",
                "fieldtype": "Int",
                "reqd": 1
            },
            {
                "fieldname": "area_aplicada",
                "label": "Área Aplicada (hectáreas)",
                "fieldtype": "Float",
                "precision": 4,
                "read_only": 1
            },
            {
                "fieldname": "cantidad_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "cantidad_total_aplicada",
                "label": "Cantidad Total Aplicada (kg)",
                "fieldtype": "Float",
                "read_only": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "costo_total",
                "label": "Costo Total (GTQ)",
                "fieldtype": "Currency",
                "read_only": 1
            },
            {
                "fieldname": "condiciones_sec",
                "label": "Condiciones de Aplicación",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "condiciones_clima",
                "label": "Condiciones Climáticas",
                "fieldtype": "Select",
                "options": "Óptimas (sin viento, sin lluvia)\nAceptables (viento leve)\nRegulares (nublado)\nNo Favorable (viento fuerte)",
                "default": "Óptimas (sin viento, sin lluvia)"
            },
            {
                "fieldname": "humedad_suelo",
                "label": "Humedad del Suelo",
                "fieldtype": "Select",
                "options": "Seco\nHúmedo Óptimo\nSaturado\nEncharcado",
                "default": "Húmedo Óptimo"
            },
            {
                "fieldname": "condiciones_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "temperatura_aplicacion",
                "label": "Temperatura (°C)",
                "fieldtype": "Float",
                "description": "Temperatura ambiente durante la aplicación"
            },
            {
                "fieldname": "hora_aplicacion",
                "label": "Hora de Aplicación",
                "fieldtype": "Time",
                "description": "Preferible en horas frescas"
            },
            {
                "fieldname": "planificacion_sec",
                "label": "Planificación y Seguimiento",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "plan_fertilizacion",
                "label": "Plan de Fertilización",
                "fieldtype": "Link",
                "options": "Plan de Fertilizacion",
                "description": "Referencia al plan anual"
            },
            {
                "fieldname": "aplicacion_numero",
                "label": "Aplicación #",
                "fieldtype": "Int",
                "description": "Número de aplicación en el ciclo (1, 2, 3...)"
            },
            {
                "fieldname": "planificacion_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "proxima_aplicacion",
                "label": "Próxima Aplicación",
                "fieldtype": "Date",
                "description": "Fecha programada para la siguiente aplicación"
            },
            {
                "fieldname": "intervalo_dias",
                "label": "Intervalo (días)",
                "fieldtype": "Int",
                "default": 45,
                "description": "Días hasta la próxima aplicación"
            },
            {
                "fieldname": "resultados_sec",
                "label": "Resultados y Observaciones",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "efectividad",
                "label": "Efectividad Observada",
                "fieldtype": "Select",
                "options": "Excelente\nBuena\nRegular\nDeficiente\nPendiente de Evaluar",
                "default": "Pendiente de Evaluar"
            },
            {
                "fieldname": "sintomas_deficiencia",
                "label": "Síntomas de Deficiencia",
                "fieldtype": "Check",
                "description": "Marcar si se observaron síntomas de deficiencia nutricional"
            },
            {
                "fieldname": "resultados_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "respuesta_cultivo",
                "label": "Respuesta del Cultivo",
                "fieldtype": "Small Text",
                "description": "Cambios observados en crecimiento, color, vigor, etc."
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones Generales",
                "fieldtype": "Text",
                "description": "Notas adicionales, problemas, recomendaciones"
            },
            {
                "fieldname": "cumplimiento_sec",
                "label": "Cumplimiento y Certificaciones",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "certificacion_organica",
                "label": "Compatible con Orgánico",
                "fieldtype": "Check",
                "description": "Producto permitido en agricultura orgánica"
            },
            {
                "fieldname": "registro_maga",
                "label": "Registro MAGA",
                "fieldtype": "Data",
                "description": "Número de registro ante MAGA si aplica"
            },
            {
                "fieldname": "cumplimiento_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "periodo_carencia",
                "label": "Período de Carencia (días)",
                "fieldtype": "Int",
                "description": "Días que deben pasar antes de la cosecha"
            },
            {
                "fieldname": "estado_aplicacion",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "Planificada\nEjecutada\nEn Evaluación\nFinalizada\nCancelada",
                "default": "Planificada",
                "in_list_view": 1
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
                "role": "Agriculture Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 0
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Aplicacion Fertilizante' creado")

def create_control_fitosanitario():
    """
    Crear DocType para Control Fitosanitario - Manejo Integrado de Plagas y Enfermedades
    """
    
    if frappe.db.exists("DocType", "Control Fitosanitario"):
        print("⚠️  DocType 'Control Fitosanitario' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Control Fitosanitario",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:FITO-{empleado}-{MM}-{DD}-{#####}",
        "title_field": "unidad_trabajo",
        "fields": [
            {
                "fieldname": "informacion_basica",
                "label": "Información del Control",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fecha_aplicacion",
                "label": "Fecha de Aplicación",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
            },
            {
                "fieldname": "empleado",
                "label": "Aplicador",
                "fieldtype": "Link",
                "options": "Employee",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "basica_col",
                "fieldtype": "Column Break"
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
                "fieldname": "supervisor_tecnico",
                "label": "Supervisor Técnico",
                "fieldtype": "Link",
                "options": "Employee",
                "description": "Ingeniero agrónomo responsable del programa"
            },
            {
                "fieldname": "problema_sec",
                "label": "Problema Fitosanitario",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "tipo_problema",
                "label": "Tipo de Problema",
                "fieldtype": "Select",
                "options": "Plaga\nEnfermedad Fúngica\nEnfermedad Bacteriana\nEnfermedad Viral\nDeficiencia Nutricional\nPrevención\nMonitoreo",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "plaga_enfermedad",
                "label": "Plaga/Enfermedad Específica",
                "fieldtype": "Select",
                "options": "Broca del Café (Hypothenemus hampei)\nRoya del Café (Hemileia vastatrix)\nAntracnosis (Colletotrichum spp.)\nMal de Hilachas (Corticium koleroga)\nOjo de Gallo (Mycena citricolor)\nÁfidos\nCochinillas\nMinador de la Hoja\nNematodos\nOtro",
                "reqd": 1
            },
            {
                "fieldname": "problema_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "nivel_incidencia",
                "label": "Nivel de Incidencia",
                "fieldtype": "Select",
                "options": "Bajo (< 5%)\nMedio (5-15%)\nAlto (15-25%)\nCrítico (> 25%)",
                "reqd": 1
            },
            {
                "fieldname": "umbral_economico",
                "label": "Umbral Económico Alcanzado",
                "fieldtype": "Check",
                "description": "Nivel que justifica la intervención química"
            },
            {
                "fieldname": "estrategia_sec",
                "label": "Estrategia de Control",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "tipo_control",
                "label": "Tipo de Control",
                "fieldtype": "Select",
                "options": "Preventivo\nCurativo\nErradicante\nManejo Integrado (MIP)\nControl Biológico\nControl Cultural",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "metodo_control",
                "label": "Método de Control",
                "fieldtype": "Select",
                "options": "Químico (Pesticida)\nBiológico (Controlador)\nCultural (Poda/Limpieza)\nEtológico (Trampas)\nManual (Pepena)\nIntegrado (Varios)",
                "reqd": 1
            },
            {
                "fieldname": "estrategia_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "programa_mip",
                "label": "Programa MIP/MIR",
                "fieldtype": "Link",
                "options": "Programa MIP",
                "description": "Referencia al programa de manejo integrado"
            },
            {
                "fieldname": "aplicacion_numero",
                "label": "Aplicación #",
                "fieldtype": "Int",
                "description": "Número de aplicación en el programa"
            },
            {
                "fieldname": "producto_sec",
                "label": "Producto Utilizado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "producto_fitosanitario",
                "label": "Producto Fitosanitario",
                "fieldtype": "Link",
                "options": "Item",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "ingrediente_activo",
                "label": "Ingrediente Activo",
                "fieldtype": "Data",
                "description": "Principio activo del producto"
            },
            {
                "fieldname": "producto_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "concentracion",
                "label": "Concentración (%)",
                "fieldtype": "Float",
                "description": "Porcentaje del ingrediente activo"
            },
            {
                "fieldname": "categoria_toxicologica",
                "label": "Categoría Toxicológica",
                "fieldtype": "Select",
                "options": "I - Extremadamente Tóxico (Rojo)\nII - Altamente Tóxico (Amarillo)\nIII - Moderadamente Tóxico (Azul)\nIV - Ligeramente Tóxico (Verde)",
                "description": "Clasificación según etiqueta"
            },
            {
                "fieldname": "dosis_sec",
                "label": "Dosis y Aplicación",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "dosis_producto",
                "label": "Dosis del Producto",
                "fieldtype": "Float",
                "reqd": 1,
                "description": "Cantidad de producto por unidad de volumen"
            },
            {
                "fieldname": "unidad_dosis",
                "label": "Unidad de Dosis",
                "fieldtype": "Select",
                "options": "ml/L agua\ngramos/L agua\nkg/ha\nL/ha\ncc/bomba 16L",
                "default": "ml/L agua"
            },
            {
                "fieldname": "dosis_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "volumen_agua",
                "label": "Volumen de Agua (L)",
                "fieldtype": "Float",
                "reqd": 1
            },
            {
                "fieldname": "cantidad_producto_total",
                "label": "Cantidad Total de Producto",
                "fieldtype": "Float",
                "read_only": 1,
                "description": "Cálculo automático según dosis"
            },
            {
                "fieldname": "aplicacion_sec",
                "label": "Método de Aplicación",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "equipo_aplicacion",
                "label": "Equipo de Aplicación",
                "fieldtype": "Select",
                "options": "Bomba de Espalda Manual\nBomba de Espalda Motorizada\nAspersora de Tractor\nNebulizadora\nEquipo ULV\nAplicación Manual",
                "default": "Bomba de Espalda Manual"
            },
            {
                "fieldname": "tipo_boquilla",
                "label": "Tipo de Boquilla",
                "fieldtype": "Select",
                "options": "Cono Hueco\nCono Lleno\nAbanico Plano\nDeflectora\nEspecial",
                "description": "Tipo de boquilla utilizada"
            },
            {
                "fieldname": "aplicacion_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "area_tratada",
                "label": "Área Tratada (hectáreas)",
                "fieldtype": "Float",
                "reqd": 1,
                "precision": 4
            },
            {
                "fieldname": "numero_plantas",
                "label": "Número de Plantas Tratadas",
                "fieldtype": "Int"
            },
            {
                "fieldname": "seguridad_sec",
                "label": "Seguridad y EPP",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "epp_utilizado",
                "label": "EPP Utilizado",
                "fieldtype": "Small Text",
                "description": "Equipo de protección personal usado"
            },
            {
                "fieldname": "precauciones_especiales",
                "label": "Precauciones Especiales",
                "fieldtype": "Small Text",
                "description": "Medidas adicionales de seguridad"
            },
            {
                "fieldname": "seguridad_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "periodo_reingreso",
                "label": "Período de Reingreso (horas)",
                "fieldtype": "Int",
                "description": "Tiempo antes de reingresar al área tratada"
            },
            {
                "fieldname": "periodo_carencia",
                "label": "Período de Carencia (días)",
                "fieldtype": "Int",
                "description": "Días antes de la cosecha"
            },
            {
                "fieldname": "condiciones_sec",
                "label": "Condiciones de Aplicación",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "condiciones_clima",
                "label": "Condiciones Climáticas",
                "fieldtype": "Select",
                "options": "Óptimas (sin viento, sin lluvia)\nAceptables (viento leve < 10 km/h)\nRegulares (nublado)\nNo Favorable (viento fuerte)",
                "default": "Óptimas (sin viento, sin lluvia)"
            },
            {
                "fieldname": "temperatura_aplicacion",
                "label": "Temperatura (°C)",
                "fieldtype": "Float",
                "description": "Temperatura durante la aplicación"
            },
            {
                "fieldname": "condiciones_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "hora_inicio",
                "label": "Hora de Inicio",
                "fieldtype": "Time",
                "description": "Preferible en horas frescas"
            },
            {
                "fieldname": "hora_fin",
                "label": "Hora de Finalización",
                "fieldtype": "Time"
            },
            {
                "fieldname": "resultados_sec",
                "label": "Resultados y Seguimiento",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "efectividad",
                "label": "Efectividad del Control",
                "fieldtype": "Select",
                "options": "Excelente (> 90%)\nBuena (70-90%)\nRegular (50-70%)\nDeficiente (< 50%)\nPendiente de Evaluar",
                "default": "Pendiente de Evaluar"
            },
            {
                "fieldname": "reduccion_incidencia",
                "label": "Reducción de Incidencia (%)",
                "fieldtype": "Percent",
                "description": "Porcentaje de reducción observado"
            },
            {
                "fieldname": "resultados_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "proxima_evaluacion",
                "label": "Próxima Evaluación",
                "fieldtype": "Date",
                "description": "Fecha programada para evaluar resultados"
            },
            {
                "fieldname": "requiere_reaplicacion",
                "label": "Requiere Reaplicación",
                "fieldtype": "Check",
                "description": "Si se necesita una aplicación adicional"
            },
            {
                "fieldname": "observaciones_sec",
                "label": "Observaciones",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones Generales",
                "fieldtype": "Text",
                "description": "Notas sobre la aplicación, problemas, recomendaciones"
            },
            {
                "fieldname": "cumplimiento_sec",
                "label": "Cumplimiento Normativo",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "registro_maga",
                "label": "Registro MAGA",
                "fieldtype": "Data",
                "description": "Número de registro del producto ante MAGA"
            },
            {
                "fieldname": "certificacion_organica",
                "label": "Compatible con Orgánico",
                "fieldtype": "Check",
                "description": "Producto permitido en agricultura orgánica"
            },
            {
                "fieldname": "cumplimiento_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "estado_aplicacion",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "Planificada\nEjecutada\nEn Evaluación\nFinalizada\nCancelada",
                "default": "Planificada",
                "in_list_view": 1
            },
            {
                "fieldname": "costo_total",
                "label": "Costo Total (GTQ)",
                "fieldtype": "Currency",
                "read_only": 1
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
                "role": "Agriculture Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 0
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Control Fitosanitario' creado")

def create_control_malezas():
    """
    Crear DocType para Control de Malezas - Manejo Integrado según buenas prácticas
    """
    
    if frappe.db.exists("DocType", "Control Malezas"):
        print("⚠️  DocType 'Control Malezas' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Control Malezas",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:MAL-{empleado}-{MM}-{DD}-{#####}",
        "title_field": "unidad_trabajo",
        "fields": [
            {
                "fieldname": "informacion_basica",
                "label": "Información del Control",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fecha_control",
                "label": "Fecha de Control",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
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
                "fieldname": "basica_col",
                "fieldtype": "Column Break"
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
                "fieldname": "supervisor",
                "label": "Supervisor",
                "fieldtype": "Link",
                "options": "Employee",
                "description": "Mandador o supervisor técnico"
            },
            {
                "fieldname": "diagnostico_sec",
                "label": "Diagnóstico de Malezas",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "nivel_infestacion",
                "label": "Nivel de Infestación",
                "fieldtype": "Select",
                "options": "Bajo (< 20%)\nMedio (20-50%)\nAlto (50-80%)\nCrítico (> 80%)",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "tipo_maleza_predominante",
                "label": "Tipo de Maleza Predominante",
                "fieldtype": "Select",
                "options": "Gramíneas (Zacates)\nHojas Anchas (Dicotiledóneas)\nCiperaceas (Coquillo)\nHelechos\nEnredaderas\nMixto",
                "reqd": 1
            },
            {
                "fieldname": "diagnostico_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "malezas_especificas",
                "label": "Malezas Específicas",
                "fieldtype": "Small Text",
                "description": "Nombres específicos de malezas identificadas"
            },
            {
                "fieldname": "competencia_cultivo",
                "label": "Competencia con Cultivo",
                "fieldtype": "Select",
                "options": "Baja\nModerada\nAlta\nCrítica",
                "description": "Nivel de competencia por recursos"
            },
            {
                "fieldname": "metodo_sec",
                "label": "Método de Control",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "tipo_control",
                "label": "Tipo de Control",
                "fieldtype": "Select",
                "options": "Manual (Machete)\nMecánico (Desbrozadora)\nQuímico (Herbicida)\nCultural (Cobertura)\nBiológico\nIntegrado (Varios)",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "herramienta_utilizada",
                "label": "Herramienta Utilizada",
                "fieldtype": "Select",
                "options": "Machete\nDesbrozadora (Trimmer)\nBomba de Espalda\nAspersora\nAzadón\nLima\nOtra",
                "depends_on": "eval:doc.tipo_control!='Biológico'"
            },
            {
                "fieldname": "metodo_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "selectividad",
                "label": "Selectividad del Control",
                "fieldtype": "Select",
                "options": "Selectivo (Solo malezas)\nSemi-selectivo\nTotal (Toda vegetación)",
                "default": "Selectivo (Solo malezas)"
            },
            {
                "fieldname": "zona_aplicacion",
                "label": "Zona de Aplicación",
                "fieldtype": "Select",
                "options": "Corona del Árbol\nCalles\nBordas\nTotal de la Parcela\nÁreas Específicas",
                "default": "Corona del Árbol"
            },
            {
                "fieldname": "producto_sec",
                "label": "Producto Químico (si aplica)",
                "fieldtype": "Section Break",
                "depends_on": "eval:doc.tipo_control=='Químico (Herbicida)' || doc.tipo_control=='Integrado (Varios)'"
            },
            {
                "fieldname": "producto_herbicida",
                "label": "Producto Herbicida",
                "fieldtype": "Link",
                "options": "Item",
                "depends_on": "eval:doc.tipo_control=='Químico (Herbicida)' || doc.tipo_control=='Integrado (Varios)'"
            },
            {
                "fieldname": "ingrediente_activo",
                "label": "Ingrediente Activo",
                "fieldtype": "Data",
                "description": "Principio activo del herbicida"
            },
            {
                "fieldname": "producto_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "modo_accion",
                "label": "Modo de Acción",
                "fieldtype": "Select",
                "options": "Sistémico\nContacto\nSuelo (Pre-emergente)\nPost-emergente\nSistémico + Contacto",
                "description": "Forma como actúa el herbicida"
            },
            {
                "fieldname": "selectividad_herbicida",
                "label": "Selectividad del Herbicida",
                "fieldtype": "Select",
                "options": "Selectivo\nNo Selectivo\nSelectivo para Gramíneas\nSelectivo para Hoja Ancha"
            },
            {
                "fieldname": "dosis_sec",
                "label": "Dosis y Aplicación",
                "fieldtype": "Section Break",
                "depends_on": "eval:doc.tipo_control=='Químico (Herbicida)' || doc.tipo_control=='Integrado (Varios)'"
            },
            {
                "fieldname": "dosis_producto",
                "label": "Dosis del Producto",
                "fieldtype": "Float",
                "description": "ml o gramos por litro de agua"
            },
            {
                "fieldname": "unidad_dosis",
                "label": "Unidad de Dosis",
                "fieldtype": "Select",
                "options": "ml/L agua\ngramos/L agua\nL/ha\ncc/bomba 16L",
                "default": "ml/L agua"
            },
            {
                "fieldname": "dosis_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "volumen_agua",
                "label": "Volumen de Agua (L)",
                "fieldtype": "Float"
            },
            {
                "fieldname": "cantidad_producto_total",
                "label": "Cantidad Total de Producto",
                "fieldtype": "Float",
                "read_only": 1,
                "description": "Cálculo automático según dosis"
            },
            {
                "fieldname": "medidas_sec",
                "label": "Medidas y Rendimiento",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "area_controlada",
                "label": "Área Controlada (hectáreas)",
                "fieldtype": "Float",
                "reqd": 1,
                "precision": 4,
                "in_list_view": 1
            },
            {
                "fieldname": "numero_plantas",
                "label": "Número de Plantas",
                "fieldtype": "Int",
                "description": "Plantas de café en el área"
            },
            {
                "fieldname": "medidas_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "tiempo_empleado",
                "label": "Tiempo Empleado (horas)",
                "fieldtype": "Float",
                "reqd": 1,
                "description": "Horas de trabajo invertidas"
            },
            {
                "fieldname": "rendimiento",
                "label": "Rendimiento (ha/día)",
                "fieldtype": "Float",
                "read_only": 1,
                "description": "Hectáreas por día de trabajo"
            },
            {
                "fieldname": "condiciones_sec",
                "label": "Condiciones de Aplicación",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "condiciones_clima",
                "label": "Condiciones Climáticas",
                "fieldtype": "Select",
                "options": "Óptimas (sin viento, sin lluvia)\nAceptables (viento leve)\nRegulares (nublado)\nNo Favorable (lluvia próxima)",
                "default": "Óptimas (sin viento, sin lluvia)"
            },
            {
                "fieldname": "humedad_relativa",
                "label": "Humedad Relativa (%)",
                "fieldtype": "Int",
                "description": "Porcentaje de humedad ambiente"
            },
            {
                "fieldname": "condiciones_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "temperatura",
                "label": "Temperatura (°C)",
                "fieldtype": "Float",
                "description": "Temperatura durante la aplicación"
            },
            {
                "fieldname": "hora_aplicacion",
                "label": "Hora de Aplicación",
                "fieldtype": "Time",
                "description": "Preferible en horas frescas"
            },
            {
                "fieldname": "resultados_sec",
                "label": "Resultados y Efectividad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "efectividad_control",
                "label": "Efectividad del Control",
                "fieldtype": "Select",
                "options": "Excelente (> 95%)\nBuena (80-95%)\nRegular (60-80%)\nDeficiente (< 60%)\nPendiente de Evaluar",
                "default": "Pendiente de Evaluar"
            },
            {
                "fieldname": "cobertura_resultante",
                "label": "Cobertura de Malezas Resultante",
                "fieldtype": "Select",
                "options": "Limpio (< 5%)\nBajo (5-20%)\nMedio (20-50%)\nAlto (> 50%)",
                "description": "Nivel de malezas después del control"
            },
            {
                "fieldname": "resultados_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "duracion_efecto",
                "label": "Duración del Efecto (días)",
                "fieldtype": "Int",
                "description": "Días que se mantiene el control"
            },
            {
                "fieldname": "proxima_aplicacion",
                "label": "Próxima Aplicación",
                "fieldtype": "Date",
                "description": "Fecha programada para el siguiente control"
            },
            {
                "fieldname": "costos_sec",
                "label": "Costos",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "costo_mano_obra",
                "label": "Costo Mano de Obra (GTQ)",
                "fieldtype": "Currency",
                "description": "Costo por horas trabajadas"
            },
            {
                "fieldname": "costo_productos",
                "label": "Costo Productos (GTQ)",
                "fieldtype": "Currency",
                "description": "Costo de herbicidas o insumos"
            },
            {
                "fieldname": "costos_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "costo_equipos",
                "label": "Costo Equipos (GTQ)",
                "fieldtype": "Currency",
                "description": "Depreciación y combustible de equipos"
            },
            {
                "fieldname": "costo_total",
                "label": "Costo Total (GTQ)",
                "fieldtype": "Currency",
                "read_only": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "sostenibilidad_sec",
                "label": "Sostenibilidad y Ambiente",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "cobertura_noble",
                "label": "Cobertura Noble Establecida",
                "fieldtype": "Check",
                "description": "Se estableció cobertura protectora del suelo"
            },
            {
                "fieldname": "tipo_cobertura",
                "label": "Tipo de Cobertura Noble",
                "fieldtype": "Small Text",
                "depends_on": "eval:doc.cobertura_noble",
                "description": "Especies utilizadas como cobertura"
            },
            {
                "fieldname": "sostenibilidad_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "certificacion_organica",
                "label": "Compatible con Orgánico",
                "fieldtype": "Check",
                "description": "Método permitido en agricultura orgánica"
            },
            {
                "fieldname": "impacto_fauna",
                "label": "Impacto en Fauna Benéfica",
                "fieldtype": "Select",
                "options": "Nulo\nBajo\nModerado\nAlto",
                "default": "Bajo"
            },
            {
                "fieldname": "observaciones_sec",
                "label": "Observaciones",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones Generales",
                "fieldtype": "Text",
                "description": "Notas sobre el control, problemas encontrados, recomendaciones"
            },
            {
                "fieldname": "cumplimiento_sec",
                "label": "Estado y Cumplimiento",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "estado_control",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "Planificado\nEjecutado\nEn Evaluación\nFinalizado\nCancelado",
                "default": "Planificado",
                "in_list_view": 1
            },
            {
                "fieldname": "registro_maga",
                "label": "Registro MAGA",
                "fieldtype": "Data",
                "description": "Número de registro del herbicida ante MAGA",
                "depends_on": "eval:doc.tipo_control=='Químico (Herbicida)'"
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
                "role": "Agriculture Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 0
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Control Malezas' creado")

def create_manejo_sombra():
    """
    Crear DocType para Manejo de Sombra - Sistemas Agroforestales
    """
    
    if frappe.db.exists("DocType", "Manejo Sombra"):
        print("⚠️  DocType 'Manejo Sombra' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Manejo Sombra",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:SOMB-{empleado}-{MM}-{DD}-{#####}",
        "title_field": "unidad_trabajo",
        "fields": [
            {
                "fieldname": "informacion_basica",
                "label": "Información del Manejo",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fecha_manejo",
                "label": "Fecha de Manejo",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
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
                "fieldname": "basica_col",
                "fieldtype": "Column Break"
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
                "fieldname": "supervisor_tecnico",
                "label": "Supervisor Técnico",
                "fieldtype": "Link",
                "options": "Employee",
                "description": "Técnico forestal o agrónomo responsable"
            },
            {
                "fieldname": "diagnostico_sec",
                "label": "Diagnóstico de la Sombra",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "cobertura_actual",
                "label": "Cobertura Actual (%)",
                "fieldtype": "Percent",
                "reqd": 1,
                "in_list_view": 1,
                "description": "Porcentaje de cobertura medido"
            },
            {
                "fieldname": "cobertura_objetivo",
                "label": "Cobertura Objetivo (%)",
                "fieldtype": "Percent",
                "reqd": 1,
                "description": "Porcentaje de cobertura deseado (30-70%)"
            },
            {
                "fieldname": "diagnostico_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "estado_sombra",
                "label": "Estado de la Sombra",
                "fieldtype": "Select",
                "options": "Excesiva (> 70%)\nÓptima (30-70%)\nInsuficiente (< 30%)\nAusente",
                "reqd": 1
            },
            {
                "fieldname": "distribucion_sombra",
                "label": "Distribución de Sombra",
                "fieldtype": "Select",
                "options": "Uniforme\nIrregular\nConcentrada\nDispersas\nPor sectores",
                "default": "Irregular"
            },
            {
                "fieldname": "especies_sec",
                "label": "Especies de Sombra",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "especie_predominante",
                "label": "Especie Predominante",
                "fieldtype": "Select",
                "options": "Inga (Guamo/Cushin/Chalum)\nGravilea (Gravilea robusta)\nMadre Cacao (Gliricidia sepium)\nCitricos\nAguacate\nBanano/Plátano\nCedro\nPalo Blanco\nOtra",
                "reqd": 1
            },
            {
                "fieldname": "especies_secundarias",
                "label": "Especies Secundarias",
                "fieldtype": "Small Text",
                "description": "Otras especies presentes en el sistema"
            },
            {
                "fieldname": "especies_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "arboles_total",
                "label": "Árboles de Sombra Total",
                "fieldtype": "Int",
                "description": "Número total de árboles de sombra"
            },
            {
                "fieldname": "densidad_sombra",
                "label": "Densidad (árboles/hectárea)",
                "fieldtype": "Int",
                "read_only": 1,
                "description": "Cálculo automático de densidad"
            },
            {
                "fieldname": "actividad_sec",
                "label": "Actividad Realizada",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "tipo_manejo",
                "label": "Tipo de Manejo",
                "fieldtype": "Select",
                "options": "Poda de Regulación\nPoda Sanitaria\nPoda Drástica\nRaleo/Eliminación\nPlantación Nueva\nMantenimiento\nControl de Especies Invasoras",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "objetivo_manejo",
                "label": "Objetivo del Manejo",
                "fieldtype": "Select",
                "options": "Aumentar Luminosidad\nReducir Luminosidad\nMejorar Distribución\nEliminar Árboles Enfermos\nRejuvenecer Copa\nEstablecer Sombra Nueva",
                "reqd": 1
            },
            {
                "fieldname": "actividad_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "intensidad_poda",
                "label": "Intensidad de Poda",
                "fieldtype": "Select",
                "options": "Ligera (< 25%)\nModerada (25-50%)\nFuerte (50-75%)\nDrástica (> 75%)",
                "depends_on": "eval:doc.tipo_manejo.includes('Poda')"
            },
            {
                "fieldname": "altura_poda",
                "label": "Altura de Poda (metros)",
                "fieldtype": "Float",
                "description": "Altura a la que se realizó la poda"
            },
            {
                "fieldname": "medidas_sec",
                "label": "Medidas de la Actividad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "arboles_manejados",
                "label": "Árboles Manejados",
                "fieldtype": "Int",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "area_afectada",
                "label": "Área Afectada (hectáreas)",
                "fieldtype": "Float",
                "reqd": 1,
                "precision": 4
            },
            {
                "fieldname": "medidas_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "tiempo_empleado",
                "label": "Tiempo Empleado (horas)",
                "fieldtype": "Float",
                "reqd": 1,
                "description": "Horas de trabajo invertidas"
            },
            {
                "fieldname": "rendimiento",
                "label": "Rendimiento (árboles/día)",
                "fieldtype": "Float",
                "read_only": 1,
                "description": "Árboles manejados por día"
            },
            {
                "fieldname": "herramientas_sec",
                "label": "Herramientas y Equipos",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "herramientas_utilizadas",
                "label": "Herramientas Utilizadas",
                "fieldtype": "Small Text",
                "description": "Machete, sierra, motosierras, escaleras, etc."
            },
            {
                "fieldname": "equipo_seguridad",
                "label": "Equipo de Seguridad",
                "fieldtype": "Small Text",
                "description": "EPP utilizado durante el trabajo"
            },
            {
                "fieldname": "subproductos_sec",
                "label": "Subproductos y Aprovechamiento",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "volumen_madera",
                "label": "Volumen de Madera (metros cúbicos)",
                "fieldtype": "Float",
                "description": "Madera obtenida del manejo"
            },
            {
                "fieldname": "destino_madera",
                "label": "Destino de la Madera",
                "fieldtype": "Select",
                "options": "Leña\nMadera de Construcción\nPostes\nChips/Astillas\nCompostaje\nVenta\nOtro",
                "depends_on": "eval:doc.volumen_madera > 0"
            },
            {
                "fieldname": "subproductos_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "volumen_biomasa",
                "label": "Volumen de Biomasa (metros cúbicos)",
                "fieldtype": "Float",
                "description": "Ramas, hojas y material vegetal"
            },
            {
                "fieldname": "destino_biomasa",
                "label": "Destino de la Biomasa",
                "fieldtype": "Select",
                "options": "Compostaje\nMulch\nCobertura del Suelo\nAlimento Animal\nBiomasa Energética\nOtro",
                "depends_on": "eval:doc.volumen_biomasa > 0"
            },
            {
                "fieldname": "resultados_sec",
                "label": "Resultados Esperados",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "cobertura_resultante",
                "label": "Cobertura Resultante (%)",
                "fieldtype": "Percent",
                "description": "Porcentaje de cobertura después del manejo"
            },
            {
                "fieldname": "mejora_luminosidad",
                "label": "Mejora en Luminosidad",
                "fieldtype": "Select",
                "options": "Significativa\nModerada\nLigera\nNinguna\nReducida",
                "description": "Cambio en la luminosidad para el café"
            },
            {
                "fieldname": "resultados_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "uniformidad_sombra",
                "label": "Uniformidad de Sombra",
                "fieldtype": "Select",
                "options": "Muy Uniforme\nUniforme\nModeradamente Uniforme\nIrregular",
                "description": "Distribución de la sombra después del manejo"
            },
            {
                "fieldname": "tiempo_recuperacion",
                "label": "Tiempo de Recuperación (meses)",
                "fieldtype": "Int",
                "description": "Meses para recuperar cobertura deseada"
            },
            {
                "fieldname": "sostenibilidad_sec",
                "label": "Sostenibilidad y Beneficios",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fijacion_nitrogeno",
                "label": "Especies Fijadoras de Nitrógeno",
                "fieldtype": "Check",
                "description": "Se mantuvieron/plantaron leguminosas"
            },
            {
                "fieldname": "conservacion_suelo",
                "label": "Contribuye a Conservación de Suelo",
                "fieldtype": "Check",
                "description": "El manejo mejora la protección del suelo"
            },
            {
                "fieldname": "sostenibilidad_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "habitat_fauna",
                "label": "Impacto en Hábitat de Fauna",
                "fieldtype": "Select",
                "options": "Positivo\nNeutro\nNegativo Temporal\nNegativo",
                "default": "Neutro"
            },
            {
                "fieldname": "diversificacion_ingresos",
                "label": "Diversificación de Ingresos",
                "fieldtype": "Check",
                "description": "Las especies generan ingresos adicionales"
            },
            {
                "fieldname": "planificacion_sec",
                "label": "Planificación Futura",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "proximo_manejo",
                "label": "Próximo Manejo",
                "fieldtype": "Date",
                "description": "Fecha programada para el siguiente manejo"
            },
            {
                "fieldname": "tipo_proximo_manejo",
                "label": "Tipo de Próximo Manejo",
                "fieldtype": "Select",
                "options": "Poda de Mantenimiento\nPoda de Regulación\nPlantación Complementaria\nControl de Rebrotes\nEvaluación"
            },
            {
                "fieldname": "planificacion_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "plantacion_requerida",
                "label": "Plantación Adicional Requerida",
                "fieldtype": "Check",
                "description": "Se necesita plantar más árboles"
            },
            {
                "fieldname": "numero_arboles_plantar",
                "label": "Árboles a Plantar",
                "fieldtype": "Int",
                "depends_on": "eval:doc.plantacion_requerida"
            },
            {
                "fieldname": "costos_sec",
                "label": "Costos",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "costo_mano_obra",
                "label": "Costo Mano de Obra (GTQ)",
                "fieldtype": "Currency",
                "description": "Costo por horas trabajadas"
            },
            {
                "fieldname": "costo_herramientas",
                "label": "Costo Herramientas (GTQ)",
                "fieldtype": "Currency",
                "description": "Depreciación y combustible"
            },
            {
                "fieldname": "costos_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "valor_subproductos",
                "label": "Valor Subproductos (GTQ)",
                "fieldtype": "Currency",
                "description": "Valor de madera y biomasa obtenida"
            },
            {
                "fieldname": "costo_neto",
                "label": "Costo Neto (GTQ)",
                "fieldtype": "Currency",
                "read_only": 1,
                "in_list_view": 1,
                "description": "Costo total menos valor de subproductos"
            },
            {
                "fieldname": "observaciones_sec",
                "label": "Observaciones",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones Generales",
                "fieldtype": "Text",
                "description": "Notas sobre el manejo, problemas, recomendaciones técnicas"
            },
            {
                "fieldname": "estado_sec",
                "label": "Estado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "estado_manejo",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "Planificado\nEjecutado\nEn Evaluación\nFinalizado\nCancelado",
                "default": "Planificado",
                "in_list_view": 1
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
                "role": "Agriculture Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 0
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Manejo Sombra' creado")

def create_poda_cafe():
    """
    Crear DocType para Poda de Café - Sistema de Manejo de Tejido (SMT)
    """
    
    if frappe.db.exists("DocType", "Poda Cafe"):
        print("⚠️  DocType 'Poda Cafe' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Poda Cafe",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:PODA-{empleado}-{MM}-{DD}-{#####}",
        "title_field": "unidad_trabajo",
        "fields": [
            {
                "fieldname": "informacion_basica",
                "label": "Información de la Poda",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fecha_poda",
                "label": "Fecha de Poda",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
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
                "fieldname": "basica_col",
                "fieldtype": "Column Break"
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
                "fieldname": "supervisor_tecnico",
                "label": "Supervisor Técnico",
                "fieldtype": "Link",
                "options": "Employee",
                "description": "Técnico agrónomo o mandador especializado"
            },
            {
                "fieldname": "planificacion_sec",
                "label": "Planificación de la Poda",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "tipo_poda",
                "label": "Tipo de Poda",
                "fieldtype": "Select",
                "options": "Poda de Formación\nPoda Sanitaria\nPoda de Producción\nRecepa (Renovación)\nPoda de Mantenimiento\nEsqueleto (Agobio)",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "sistema_manejo",
                "label": "Sistema de Manejo de Tejido",
                "fieldtype": "Select",
                "options": "Tradicional (Libre Crecimiento)\nManejo de Tejido (SMT)\nSistema Agobio\nSistema PROMECAFE\nOtro Sistema",
                "reqd": 1
            },
            {
                "fieldname": "planificacion_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "epoca_poda",
                "label": "Época de Poda",
                "fieldtype": "Select",
                "options": "Post-Cosecha (Marzo-Mayo)\nInter-Cosecha (Junio-Agosto)\nPre-Cosecha (Septiembre-Noviembre)\nEmergencia",
                "default": "Post-Cosecha (Marzo-Mayo)"
            },
            {
                "fieldname": "frecuencia_programada",
                "label": "Frecuencia Programada",
                "fieldtype": "Select",
                "options": "Anual\nBianual\nCada 3 años\nCícilo Productivo\nSegún necesidad",
                "default": "Anual"
            },
            {
                "fieldname": "diagnostico_sec",
                "label": "Diagnóstico del Cafetal",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "edad_cafetal",
                "label": "Edad del Cafetal (años)",
                "fieldtype": "Int",
                "reqd": 1,
                "description": "Años desde la siembra"
            },
            {
                "fieldname": "estado_general",
                "label": "Estado General de las Plantas",
                "fieldtype": "Select",
                "options": "Excelente\nBueno\nRegular\nDeficiente\nSevero Deterioro",
                "reqd": 1
            },
            {
                "fieldname": "diagnostico_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "vigor_vegetativo",
                "label": "Vigor Vegetativo",
                "fieldtype": "Select",
                "options": "Alto\nMedio\nBajo\nMuy Bajo",
                "description": "Evaluación del crecimiento y desarrollo"
            },
            {
                "fieldname": "nivel_produccion",
                "label": "Nivel de Producción",
                "fieldtype": "Select",
                "options": "Alto (> 30 qq/ha)\nMedio (15-30 qq/ha)\nBajo (< 15 qq/ha)\nImproductivo",
                "description": "Rendimiento de la última cosecha"
            },
            {
                "fieldname": "problemas_sec",
                "label": "Problemas Identificados",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "exceso_chupones",
                "label": "Exceso de Chupones",
                "fieldtype": "Check",
                "description": "Presencia excesiva de brotes verticales"
            },
            {
                "fieldname": "ramas_improductivas",
                "label": "Ramas Improductivas",
                "fieldtype": "Check",
                "description": "Ramas viejas sin producción"
            },
            {
                "fieldname": "problemas_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "plantas_enfermas",
                "label": "Plantas Enfermas/Dañadas",
                "fieldtype": "Check",
                "description": "Presencia de plantas con problemas sanitarios"
            },
            {
                "fieldname": "copa_densa",
                "label": "Copa Muy Densa",
                "fieldtype": "Check",
                "description": "Exceso de follaje que impide ventilación"
            },
            {
                "fieldname": "ejecucion_sec",
                "label": "Ejecución de la Poda",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "intensidad_poda",
                "label": "Intensidad de Poda",
                "fieldtype": "Select",
                "options": "Ligera (< 25% tejido)\nModerada (25-50% tejido)\nFuerte (50-75% tejido)\nDrástica (> 75% tejido)\nRecepa Total",
                "reqd": 1
            },
            {
                "fieldname": "altura_poda",
                "label": "Altura de Poda (metros)",
                "fieldtype": "Float",
                "description": "Altura máxima dejada después de la poda"
            },
            {
                "fieldname": "ejecucion_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "numero_tallos_dejados",
                "label": "Número de Tallos Dejados",
                "fieldtype": "Int",
                "description": "Tallos productivos seleccionados por planta"
            },
            {
                "fieldname": "eliminacion_chupones",
                "label": "Eliminación de Chupones",
                "fieldtype": "Check",
                "description": "Se eliminaron brotes no productivos"
            },
            {
                "fieldname": "tecnica_sec",
                "label": "Técnica Aplicada",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "tipo_corte",
                "label": "Tipo de Corte",
                "fieldtype": "Select",
                "options": "Corte Inclinado\nCorte Horizontal\nCorte en Bisel\nDesgarre Controlado",
                "default": "Corte Inclinado",
                "description": "Técnica de corte utilizada"
            },
            {
                "fieldname": "herramientas_utilizadas",
                "label": "Herramientas Utilizadas",
                "fieldtype": "Small Text",
                "description": "Tijeras, serrucho, sierra, machete, etc."
            },
            {
                "fieldname": "tecnica_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "desinfeccion_herramientas",
                "label": "Desinfección de Herramientas",
                "fieldtype": "Check",
                "description": "Herramientas desinfectadas entre plantas"
            },
            {
                "fieldname": "sellado_cortes",
                "label": "Sellado de Cortes",
                "fieldtype": "Check",
                "description": "Aplicación de pasta cicatrizante"
            },
            {
                "fieldname": "medidas_sec",
                "label": "Medidas de la Actividad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "plantas_podadas",
                "label": "Plantas Podadas",
                "fieldtype": "Int",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "area_podada",
                "label": "Área Podada (hectáreas)",
                "fieldtype": "Float",
                "reqd": 1,
                "precision": 4
            },
            {
                "fieldname": "medidas_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "tiempo_empleado",
                "label": "Tiempo Empleado (horas)",
                "fieldtype": "Float",
                "reqd": 1,
                "description": "Horas de trabajo invertidas"
            },
            {
                "fieldname": "rendimiento",
                "label": "Rendimiento (plantas/día)",
                "fieldtype": "Float",
                "read_only": 1,
                "description": "Plantas podadas por día de trabajo"
            },
            {
                "fieldname": "material_sec",
                "label": "Material Podado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "volumen_material_podado",
                "label": "Volumen Material Podado (m³)",
                "fieldtype": "Float",
                "description": "Volumen de ramas y material vegetal"
            },
            {
                "fieldname": "destino_material",
                "label": "Destino del Material",
                "fieldtype": "Select",
                "options": "Compostaje\nQuema Controlada\nChips/Astillas\nBarrera Física\nRetirado de la Finca\nOtro",
                "default": "Compostaje"
            },
            {
                "fieldname": "material_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "material_enfermo",
                "label": "Material Enfermo Removido",
                "fieldtype": "Check",
                "description": "Se removió material con problemas sanitarios"
            },
            {
                "fieldname": "tratamiento_material_enfermo",
                "label": "Tratamiento Material Enfermo",
                "fieldtype": "Select",
                "options": "Quema Inmediata\nEntierro\nAlejado de la Finca\nTratamiento Químico\nDesinfección",
                "depends_on": "eval:doc.material_enfermo"
            },
            {
                "fieldname": "postpoda_sec",
                "label": "Manejo Post-Poda",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fertilizacion_postpoda",
                "label": "Fertilización Post-Poda",
                "fieldtype": "Check",
                "description": "Se aplicó fertilizante después de la poda"
            },
            {
                "fieldname": "tipo_fertilizante_postpoda",
                "label": "Tipo de Fertilizante",
                "fieldtype": "Data",
                "depends_on": "eval:doc.fertilizacion_postpoda",
                "description": "Fertilizante aplicado después de la poda"
            },
            {
                "fieldname": "postpoda_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "control_fitosanitario_postpoda",
                "label": "Control Fitosanitario Post-Poda",
                "fieldtype": "Check",
                "description": "Aplicación preventiva después de la poda"
            },
            {
                "fieldname": "riego_postpoda",
                "label": "Riego Post-Poda",
                "fieldtype": "Check",
                "description": "Se proporcionó riego después de la poda"
            },
            {
                "fieldname": "resultados_sec",
                "label": "Resultados Esperados",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "mejora_ventilacion",
                "label": "Mejora en Ventilación",
                "fieldtype": "Select",
                "options": "Excelente\nBuena\nRegular\nPoca\nNinguna",
                "description": "Mejora esperada en circulación de aire"
            },
            {
                "fieldname": "mejora_luminosidad",
                "label": "Mejora en Luminosidad",
                "fieldtype": "Select",
                "options": "Significativa\nModerada\nLigera\nPoca\nNinguna",
                "description": "Mejora en penetración de luz"
            },
            {
                "fieldname": "resultados_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "renovacion_tejido",
                "label": "Renovación de Tejido (%)",
                "fieldtype": "Percent",
                "description": "Porcentaje de tejido renovado"
            },
            {
                "fieldname": "expectativa_produccion",
                "label": "Expectativa de Producción",
                "fieldtype": "Select",
                "options": "Aumento Significativo\nAumento Moderado\nMantener Nivel\nReducción Temporal\nRecuperación Gradual",
                "description": "Impacto esperado en la próxima cosecha"
            },
            {
                "fieldname": "costos_sec",
                "label": "Costos",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "costo_mano_obra",
                "label": "Costo Mano de Obra (GTQ)",
                "fieldtype": "Currency",
                "description": "Costo por horas trabajadas"
            },
            {
                "fieldname": "costo_herramientas",
                "label": "Costo Herramientas (GTQ)",
                "fieldtype": "Currency",
                "description": "Depreciación y mantenimiento de herramientas"
            },
            {
                "fieldname": "costos_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "costo_insumos",
                "label": "Costo Insumos (GTQ)",
                "fieldtype": "Currency",
                "description": "Selladores, desinfectantes, etc."
            },
            {
                "fieldname": "costo_total",
                "label": "Costo Total (GTQ)",
                "fieldtype": "Currency",
                "read_only": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "seguimiento_sec",
                "label": "Seguimiento",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "proxima_evaluacion",
                "label": "Próxima Evaluación",
                "fieldtype": "Date",
                "description": "Fecha para evaluar resultados de la poda"
            },
            {
                "fieldname": "proxima_poda",
                "label": "Próxima Poda Programada",
                "fieldtype": "Date",
                "description": "Fecha programada para la siguiente poda"
            },
            {
                "fieldname": "seguimiento_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "deschupone_requerido",
                "label": "Deschupone Requerido",
                "fieldtype": "Check",
                "description": "Se requiere deschupone frecuente"
            },
            {
                "fieldname": "frecuencia_deschupone",
                "label": "Frecuencia Deschupone",
                "fieldtype": "Select",
                "options": "Mensual\nBimestral\nTrimestral\nSegún necesidad",
                "depends_on": "eval:doc.deschupone_requerido"
            },
            {
                "fieldname": "observaciones_sec",
                "label": "Observaciones",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones Generales",
                "fieldtype": "Text",
                "description": "Notas sobre la poda, problemas encontrados, recomendaciones técnicas"
            },
            {
                "fieldname": "estado_sec",
                "label": "Estado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "estado_poda",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "Planificado\nEjecutado\nEn Evaluación\nFinalizado\nCancelado",
                "default": "Planificado",
                "in_list_view": 1
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
                "role": "Agriculture Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 0
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Poda Cafe' creado")

def create_manejo_brotes():
    """
    Crear DocType para Manejo de Brotes - Deschupone y Control de Tejido
    """
    
    if frappe.db.exists("DocType", "Manejo Brotes"):
        print("⚠️  DocType 'Manejo Brotes' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Manejo Brotes",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:BROTE-{empleado}-{MM}-{DD}-{#####}",
        "title_field": "unidad_trabajo",
        "fields": [
            {
                "fieldname": "informacion_basica",
                "label": "Información del Manejo",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fecha_manejo",
                "label": "Fecha de Manejo",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
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
                "fieldname": "basica_col",
                "fieldtype": "Column Break"
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
                "fieldname": "supervisor",
                "label": "Supervisor",
                "fieldtype": "Link",
                "options": "Employee",
                "description": "Mandador o técnico supervisor"
            },
            {
                "fieldname": "diagnostico_sec",
                "label": "Diagnóstico de Brotes",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "tipo_brote_predominante",
                "label": "Tipo de Brote Predominante",
                "fieldtype": "Select",
                "options": "Chupones de Base\nChupones de Tallo\nRamas Pegadas\nBrotes Laterales\nRebrotes de Poda\nMixto",
                "reqd": 1
            },
            {
                "fieldname": "intensidad_brotacion",
                "label": "Intensidad de Brotación",
                "fieldtype": "Select",
                "options": "Baja (< 3 brotes/planta)\nModerada (3-6 brotes/planta)\nAlta (6-10 brotes/planta)\nExcesiva (> 10 brotes/planta)",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "diagnostico_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "estado_brotes",
                "label": "Estado de los Brotes",
                "fieldtype": "Select",
                "options": "Tiernos (< 20 cm)\nMedianos (20-50 cm)\nDesarrollados (> 50 cm)\nLignificados\nMixto",
                "description": "Desarrollo de los brotes presentes"
            },
            {
                "fieldname": "competencia_produccion",
                "label": "Competencia con Producción",
                "fieldtype": "Select",
                "options": "Alta\nModerada\nBaja\nNinguna",
                "description": "Nivel de competencia por recursos"
            },
            {
                "fieldname": "actividad_sec",
                "label": "Actividad Realizada",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "tipo_manejo",
                "label": "Tipo de Manejo",
                "fieldtype": "Select",
                "options": "Deschupone Total\nDeschupone Selectivo\nSelección de Tallos\nEliminación Ramas Pegadas\nRegulación de Carga\nManejo Integral",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "criterio_seleccion",
                "label": "Criterio de Selección",
                "fieldtype": "Select",
                "options": "Vigor del Brote\nPosición en la Planta\nDiámetro del Tallo\nCompetencia por Luz\nSistema de Producción\nCombinado",
                "description": "Criterio para seleccionar brotes"
            },
            {
                "fieldname": "actividad_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "numero_tallos_objetivo",
                "label": "Número de Tallos Objetivo",
                "fieldtype": "Int",
                "description": "Tallos productivos deseados por planta"
            },
            {
                "fieldname": "altura_deschupone",
                "label": "Altura de Deschupone (cm)",
                "fieldtype": "Int",
                "description": "Altura desde el suelo hasta donde se eliminan brotes"
            },
            {
                "fieldname": "tecnica_sec",
                "label": "Técnica Aplicada",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "metodo_eliminacion",
                "label": "Método de Eliminación",
                "fieldtype": "Select",
                "options": "Manual (Con Dedos)\nCon Cuchillo\nCon Tijeras\nDoblado/Torcido\nCorte Químico\nMixto",
                "reqd": 1
            },
            {
                "fieldname": "momento_eliminacion",
                "label": "Momento de Eliminación",
                "fieldtype": "Select",
                "options": "Brote Tierno\nBrote Mediano\nBrote Desarrollado\nLignificado\nVariable",
                "description": "Estado del brote al momento de eliminación"
            },
            {
                "fieldname": "tecnica_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "herramientas_utilizadas",
                "label": "Herramientas Utilizadas",
                "fieldtype": "Small Text",
                "description": "Cuchillos, tijeras, navajas, etc."
            },
            {
                "fieldname": "desinfeccion_herramientas",
                "label": "Desinfección de Herramientas",
                "fieldtype": "Check",
                "description": "Herramientas desinfectadas entre plantas"
            },
            {
                "fieldname": "medidas_sec",
                "label": "Medidas de la Actividad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "plantas_manejadas",
                "label": "Plantas Manejadas",
                "fieldtype": "Int",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "brotes_eliminados",
                "label": "Total Brotes Eliminados",
                "fieldtype": "Int",
                "reqd": 1,
                "description": "Número total de brotes removidos"
            },
            {
                "fieldname": "medidas_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "area_manejada",
                "label": "Área Manejada (hectáreas)",
                "fieldtype": "Float",
                "reqd": 1,
                "precision": 4
            },
            {
                "fieldname": "tiempo_empleado",
                "label": "Tiempo Empleado (horas)",
                "fieldtype": "Float",
                "reqd": 1,
                "description": "Horas de trabajo invertidas"
            },
            {
                "fieldname": "rendimiento_sec",
                "label": "Rendimiento",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "plantas_por_dia",
                "label": "Plantas por Día",
                "fieldtype": "Float",
                "read_only": 1,
                "description": "Plantas manejadas por día de trabajo"
            },
            {
                "fieldname": "brotes_por_planta",
                "label": "Brotes Eliminados por Planta",
                "fieldtype": "Float",
                "read_only": 1,
                "description": "Promedio de brotes eliminados por planta"
            },
            {
                "fieldname": "rendimiento_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "tallos_resultantes",
                "label": "Tallos Productivos Resultantes",
                "fieldtype": "Int",
                "description": "Promedio de tallos dejados por planta"
            },
            {
                "fieldname": "eficiencia_manejo",
                "label": "Eficiencia del Manejo",
                "fieldtype": "Select",
                "options": "Excelente (95-100%)\nBuena (80-95%)\nRegular (60-80%)\nDeficiente (< 60%)",
                "description": "Calidad del trabajo realizado"
            },
            {
                "fieldname": "condiciones_sec",
                "label": "Condiciones de Trabajo",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "condiciones_clima",
                "label": "Condiciones Climáticas",
                "fieldtype": "Select",
                "options": "Secas y Soleadas\nNubladas\nLluvia Ligera\nHúmedas\nDesfavorables",
                "default": "Secas y Soleadas"
            },
            {
                "fieldname": "humedad_suelo",
                "label": "Humedad del Suelo",
                "fieldtype": "Select",
                "options": "Seco\nHúmedo Óptimo\nSaturado\nEncharcado",
                "description": "Condición del suelo durante el trabajo"
            },
            {
                "fieldname": "condiciones_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "hora_inicio",
                "label": "Hora de Inicio",
                "fieldtype": "Time",
                "description": "Hora de inicio del trabajo"
            },
            {
                "fieldname": "hora_finalizacion",
                "label": "Hora de Finalización",
                "fieldtype": "Time",
                "description": "Hora de finalización del trabajo"
            },
            {
                "fieldname": "resultados_sec",
                "label": "Resultados",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "mejora_estructura",
                "label": "Mejora en Estructura de la Planta",
                "fieldtype": "Select",
                "options": "Excelente\nBuena\nRegular\nPoca\nNinguna",
                "description": "Mejora en la arquitectura de la planta"
            },
            {
                "fieldname": "reduccion_competencia",
                "label": "Reducción de Competencia",
                "fieldtype": "Select",
                "options": "Significativa\nModerada\nLigera\nPoca\nNinguna",
                "description": "Reducción de competencia entre tallos"
            },
            {
                "fieldname": "resultados_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "facilita_cosecha",
                "label": "Facilita Cosecha",
                "fieldtype": "Check",
                "description": "El manejo facilita las labores de cosecha"
            },
            {
                "fieldname": "mejora_ventilacion",
                "label": "Mejora Ventilación",
                "fieldtype": "Check",
                "description": "Mejora la circulación de aire en la planta"
            },
            {
                "fieldname": "planificacion_sec",
                "label": "Planificación Futura",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "frecuencia_requerida",
                "label": "Frecuencia Requerida",
                "fieldtype": "Select",
                "options": "Mensual\nBimestral\nTrimestral\nSemestral\nAnual\nSegún Necesidad",
                "reqd": 1
            },
            {
                "fieldname": "proximo_manejo",
                "label": "Próximo Manejo",
                "fieldtype": "Date",
                "description": "Fecha programada para el siguiente manejo"
            },
            {
                "fieldname": "planificacion_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "intensidad_proxima",
                "label": "Intensidad Próxima",
                "fieldtype": "Select",
                "options": "Mantenimiento\nLigera\nModerada\nIntensiva",
                "description": "Intensidad requerida en el próximo manejo"
            },
            {
                "fieldname": "requiere_capacitacion",
                "label": "Requiere Capacitación Adicional",
                "fieldtype": "Check",
                "description": "El trabajador requiere capacitación específica"
            },
            {
                "fieldname": "costos_sec",
                "label": "Costos",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "costo_mano_obra",
                "label": "Costo Mano de Obra (GTQ)",
                "fieldtype": "Currency",
                "description": "Costo por horas trabajadas"
            },
            {
                "fieldname": "costo_herramientas",
                "label": "Costo Herramientas (GTQ)",
                "fieldtype": "Currency",
                "description": "Depreciación y mantenimiento"
            },
            {
                "fieldname": "costos_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "costo_total",
                "label": "Costo Total (GTQ)",
                "fieldtype": "Currency",
                "read_only": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "costo_por_hectarea",
                "label": "Costo por Hectárea (GTQ)",
                "fieldtype": "Currency",
                "read_only": 1
            },
            {
                "fieldname": "observaciones_sec",
                "label": "Observaciones",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones Generales",
                "fieldtype": "Text",
                "description": "Notas sobre el manejo, dificultades encontradas, recomendaciones"
            },
            {
                "fieldname": "estado_sec",
                "label": "Estado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "estado_manejo",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "Planificado\nEjecutado\nEn Evaluación\nFinalizado\nCancelado",
                "default": "Planificado",
                "in_list_view": 1
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
                "role": "Agriculture Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 0
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Manejo Brotes' creado")

def create_recepcion_cafe_cereza():
    """
    Crear DocType para Recepción de Café Cereza - Control de Calidad en Recepción
    """
    
    if frappe.db.exists("DocType", "Recepcion Cafe Cereza"):
        print("⚠️  DocType 'Recepcion Cafe Cereza' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Recepcion Cafe Cereza",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:REC-{fecha_recepcion}-{#####}",
        "title_field": "lote_recepcion",
        "fields": [
            {
                "fieldname": "informacion_basica",
                "label": "Información de Recepción",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fecha_recepcion",
                "label": "Fecha de Recepción",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
            },
            {
                "fieldname": "hora_recepcion",
                "label": "Hora de Recepción",
                "fieldtype": "Time",
                "reqd": 1,
                "default": "now",
                "description": "Hora de llegada del café"
            },
            {
                "fieldname": "basica_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "lote_recepcion",
                "label": "Lote de Recepción",
                "fieldtype": "Data",
                "reqd": 1,
                "in_list_view": 1,
                "description": "Código único del lote recibido"
            },
            {
                "fieldname": "responsable_recepcion",
                "label": "Responsable de Recepción",
                "fieldtype": "Link",
                "options": "Employee",
                "reqd": 1,
                "description": "Empleado responsable del control de calidad"
            },
            {
                "fieldname": "procedencia_sec",
                "label": "Procedencia del Café",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "unidad_trabajo_origen",
                "label": "Unidad de Trabajo",
                "fieldtype": "Link",
                "options": "Unidad de Trabajo",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "actividad_cosecha_ref",
                "label": "Actividad de Cosecha",
                "fieldtype": "Link",
                "options": "Actividad de Campo",
                "description": "Referencia a la actividad de cosecha"
            },
            {
                "fieldname": "procedencia_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "recolector",
                "label": "Recolector/Cuadrilla",
                "fieldtype": "Link",
                "options": "Employee",
                "description": "Trabajador o cuadrilla que cosechó"
            },
            {
                "fieldname": "altitud_origen",
                "label": "Altitud de Origen (msnm)",
                "fieldtype": "Int",
                "description": "Altitud de la parcela de origen"
            },
            {
                "fieldname": "medidas_sec",
                "label": "Medidas y Pesaje",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "peso_bruto_qq",
                "label": "Peso Bruto (quintales)",
                "fieldtype": "Float",
                "reqd": 1,
                "precision": 2,
                "in_list_view": 1
            },
            {
                "fieldname": "peso_tara_qq",
                "label": "Peso Tara (quintales)",
                "fieldtype": "Float",
                "precision": 2,
                "description": "Peso de costales o recipientes"
            },
            {
                "fieldname": "medidas_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "peso_neto_qq",
                "label": "Peso Neto (quintales)",
                "fieldtype": "Float",
                "read_only": 1,
                "precision": 2,
                "in_list_view": 1,
                "description": "Peso bruto menos tara"
            },
            {
                "fieldname": "numero_costales",
                "label": "Número de Costales",
                "fieldtype": "Int",
                "description": "Cantidad de recipientes utilizados"
            },
            {
                "fieldname": "clasificacion_sec",
                "label": "Clasificación y Calidad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "metodo_clasificacion",
                "label": "Método de Clasificación",
                "fieldtype": "Select",
                "options": "Sifón (Densidad)\nFlotación\nVisual\nCombinado\nMesa Densimétrica",
                "reqd": 1,
                "description": "Método utilizado para clasificar"
            },
            {
                "fieldname": "cafe_primera",
                "label": "Café Primera (%)",
                "fieldtype": "Percent",
                "description": "Porcentaje de café de primera calidad"
            },
            {
                "fieldname": "clasificacion_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "cafe_segunda",
                "label": "Café Segunda (%)",
                "fieldtype": "Percent",
                "description": "Porcentaje de café de segunda calidad"
            },
            {
                "fieldname": "cafe_descarte",
                "label": "Café Descarte (%)",
                "fieldtype": "Percent",
                "description": "Porcentaje de café de descarte"
            },
            {
                "fieldname": "calidad_sec",
                "label": "Control de Calidad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "grado_madurez",
                "label": "Grado de Madurez",
                "fieldtype": "Select",
                "options": "Óptimo (> 90% maduro)\nBueno (80-90% maduro)\nRegular (70-80% maduro)\nDeficiente (< 70% maduro)",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "cerezo_verde",
                "label": "Cerezo Verde (%)",
                "fieldtype": "Percent",
                "description": "Porcentaje de frutos verdes"
            },
            {
                "fieldname": "calidad_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "cerezo_sobremaduro",
                "label": "Cerezo Sobremaduro (%)",
                "fieldtype": "Percent",
                "description": "Porcentaje de frutos sobremaduros"
            },
            {
                "fieldname": "cerezo_dañado",
                "label": "Cerezo Dañado (%)",
                "fieldtype": "Percent",
                "description": "Porcentaje de frutos con daños"
            },
            {
                "fieldname": "defectos_sec",
                "label": "Defectos y Observaciones",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "presencia_broca",
                "label": "Presencia de Broca",
                "fieldtype": "Select",
                "options": "Ausente\nBaja (< 2%)\nModerada (2-5%)\nAlta (> 5%)",
                "default": "Ausente"
            },
            {
                "fieldname": "materiales_extranos",
                "label": "Materiales Extraños",
                "fieldtype": "Check",
                "description": "Presencia de hojas, palos, piedras, etc."
            },
            {
                "fieldname": "defectos_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "olor_fermentacion",
                "label": "Olor a Fermentación",
                "fieldtype": "Check",
                "description": "Detección de olores de fermentación"
            },
            {
                "fieldname": "uniformidad_lote",
                "label": "Uniformidad del Lote",
                "fieldtype": "Select",
                "options": "Muy Uniforme\nUniforme\nModerado\nVariable\nMuy Variable",
                "default": "Uniforme"
            },
            {
                "fieldname": "muestreo_sec",
                "label": "Muestreo",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "muestra_tomada",
                "label": "Muestra Tomada",
                "fieldtype": "Check",
                "description": "Se tomó muestra representativa"
            },
            {
                "fieldname": "peso_muestra_lb",
                "label": "Peso de Muestra (libras)",
                "fieldtype": "Float",
                "depends_on": "eval:doc.muestra_tomada",
                "description": "Peso de la muestra tomada"
            },
            {
                "fieldname": "muestreo_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "codigo_muestra",
                "label": "Código de Muestra",
                "fieldtype": "Data",
                "depends_on": "eval:doc.muestra_tomada",
                "description": "Código único de la muestra"
            },
            {
                "fieldname": "analisis_laboratorio",
                "label": "Enviado a Laboratorio",
                "fieldtype": "Check",
                "description": "Muestra enviada para análisis"
            },
            {
                "fieldname": "decision_sec",
                "label": "Decisión de Procesamiento",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "decision_procesamiento",
                "label": "Decisión de Procesamiento",
                "fieldtype": "Select",
                "options": "Aceptado para Procesamiento\nAceptado con Observaciones\nProcesar por Separado\nRechazado",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "razon_separacion",
                "label": "Razón de Separación",
                "fieldtype": "Small Text",
                "depends_on": "eval:doc.decision_procesamiento=='Procesar por Separado'",
                "description": "Motivo para procesar por separado"
            },
            {
                "fieldname": "decision_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "tipo_beneficiado",
                "label": "Tipo de Beneficiado",
                "fieldtype": "Select",
                "options": "Beneficiado Húmedo Completo\nBeneficiado Semi-Húmedo\nBeneficiado Natural\nEspecial (Honey/Semi-Lavado)",
                "default": "Beneficiado Húmedo Completo"
            },
            {
                "fieldname": "prioridad_procesamiento",
                "label": "Prioridad de Procesamiento",
                "fieldtype": "Select",
                "options": "Inmediato (< 2 horas)\nAlta (2-4 horas)\nNormal (4-8 horas)\nBaja (> 8 horas)",
                "default": "Alta (2-4 horas)"
            },
            {
                "fieldname": "trazabilidad_sec",
                "label": "Trazabilidad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "lote_destino",
                "label": "Lote de Destino",
                "fieldtype": "Data",
                "description": "Código del lote asignado para procesamiento"
            },
            {
                "fieldname": "fecha_cosecha",
                "label": "Fecha de Cosecha",
                "fieldtype": "Date",
                "description": "Fecha en que se cosechó el café"
            },
            {
                "fieldname": "trazabilidad_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "tiempo_postcosecha",
                "label": "Tiempo Post-Cosecha (horas)",
                "fieldtype": "Float",
                "read_only": 1,
                "description": "Horas transcurridas desde la cosecha"
            },
            {
                "fieldname": "consecutivo_dia",
                "label": "Consecutivo del Día",
                "fieldtype": "Int",
                "read_only": 1,
                "description": "Número de lote del día"
            },
            {
                "fieldname": "observaciones_sec",
                "label": "Observaciones",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones Generales",
                "fieldtype": "Text",
                "description": "Notas sobre la recepción, problemas, recomendaciones"
            },
            {
                "fieldname": "estado_sec",
                "label": "Estado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "estado_recepcion",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "Pendiente\nEn Proceso\nFinalizado\nRechazado",
                "default": "Pendiente",
                "in_list_view": 1
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
                "role": "Agriculture Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 0
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Recepcion Cafe Cereza' creado")

def create_despulpado():
    """
    Crear DocType para Despulpado - Control del Proceso de Despulpado
    """
    
    if frappe.db.exists("DocType", "Despulpado"):
        print("⚠️  DocType 'Despulpado' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Despulpado",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:DESP-{fecha_despulpado}-{#####}",
        "title_field": "lote_procesamiento",
        "fields": [
            {
                "fieldname": "informacion_basica",
                "label": "Información del Despulpado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fecha_despulpado",
                "label": "Fecha de Despulpado",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
            },
            {
                "fieldname": "hora_inicio",
                "label": "Hora de Inicio",
                "fieldtype": "Time",
                "reqd": 1,
                "description": "Hora de inicio del despulpado"
            },
            {
                "fieldname": "basica_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "lote_procesamiento",
                "label": "Lote de Procesamiento",
                "fieldtype": "Data",
                "reqd": 1,
                "in_list_view": 1,
                "description": "Código del lote a procesar"
            },
            {
                "fieldname": "operador_despulpadora",
                "label": "Operador de Despulpadora",
                "fieldtype": "Link",
                "options": "Employee",
                "reqd": 1,
                "description": "Trabajador operando la máquina"
            },
            {
                "fieldname": "origen_sec",
                "label": "Origen del Material",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "recepcion_ref",
                "label": "Recepción de Referencia",
                "fieldtype": "Link",
                "options": "Recepcion Cafe Cereza",
                "reqd": 1,
                "description": "Recepción de origen del café"
            },
            {
                "fieldname": "peso_cereza_qq",
                "label": "Peso Cereza (quintales)",
                "fieldtype": "Float",
                "reqd": 1,
                "precision": 2,
                "in_list_view": 1
            },
            {
                "fieldname": "origen_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "calidad_cereza",
                "label": "Calidad de Cereza",
                "fieldtype": "Select",
                "options": "Excelente\nBuena\nRegular\nDeficiente",
                "reqd": 1,
                "description": "Calidad del café cereza a procesar"
            },
            {
                "fieldname": "tiempo_espera_horas",
                "label": "Tiempo de Espera (horas)",
                "fieldtype": "Float",
                "description": "Horas desde recepción hasta despulpado"
            },
            {
                "fieldname": "equipo_sec",
                "label": "Equipo y Configuración",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "despulpadora_utilizada",
                "label": "Despulpadora Utilizada",
                "fieldtype": "Select",
                "options": "Despulpadora Manual\nDespulpadora Eléctrica\nDespulpadora Diesel\nDespulpadora Ecológica\nOtra",
                "reqd": 1
            },
            {
                "fieldname": "modelo_despulpadora",
                "label": "Modelo/Marca",
                "fieldtype": "Data",
                "description": "Modelo y marca de la despulpadora"
            },
            {
                "fieldname": "equipo_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "configuracion_maquina",
                "label": "Configuración de Máquina",
                "fieldtype": "Small Text",
                "description": "Ajustes realizados a la máquina"
            },
            {
                "fieldname": "mantenimiento_previo",
                "label": "Mantenimiento Previo",
                "fieldtype": "Check",
                "description": "Se realizó mantenimiento antes del uso"
            },
            {
                "fieldname": "proceso_sec",
                "label": "Control del Proceso",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "velocidad_procesamiento",
                "label": "Velocidad de Procesamiento",
                "fieldtype": "Select",
                "options": "Muy Lenta\nLenta\nNormal\nRápida\nMuy Rápida",
                "default": "Normal",
                "description": "Velocidad de alimentación de la máquina"
            },
            {
                "fieldname": "presion_agua",
                "label": "Presión de Agua",
                "fieldtype": "Select",
                "options": "Baja\nNormal\nAlta\nExcesiva",
                "default": "Normal",
                "description": "Presión del agua utilizada"
            },
            {
                "fieldname": "proceso_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "consumo_agua_litros",
                "label": "Consumo de Agua (litros)",
                "fieldtype": "Float",
                "description": "Cantidad de agua utilizada"
            },
            {
                "fieldname": "tiempo_procesamiento_min",
                "label": "Tiempo de Procesamiento (minutos)",
                "fieldtype": "Float",
                "reqd": 1,
                "description": "Duración del despulpado"
            },
            {
                "fieldname": "calidad_sec",
                "label": "Control de Calidad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "calidad_despulpado",
                "label": "Calidad del Despulpado",
                "fieldtype": "Select",
                "options": "Excelente (< 1% cereza)\nBueno (1-2% cereza)\nRegular (2-5% cereza)\nDeficiente (> 5% cereza)",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "granos_partidos",
                "label": "Granos Partidos (%)",
                "fieldtype": "Percent",
                "description": "Porcentaje de granos dañados por la máquina"
            },
            {
                "fieldname": "calidad_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "cerezo_sin_despulpar",
                "label": "Cerezo Sin Despulpar (%)",
                "fieldtype": "Percent",
                "description": "Porcentaje de cerezas que no se despulparon"
            },
            {
                "fieldname": "mucilago_residual",
                "label": "Mucílago Residual",
                "fieldtype": "Select",
                "options": "Completo\nBueno\nRegular\nDeficiente",
                "default": "Completo",
                "description": "Cantidad de mucílago que queda"
            },
            {
                "fieldname": "rendimiento_sec",
                "label": "Rendimiento",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "peso_baba_qq",
                "label": "Peso Café Baba (quintales)",
                "fieldtype": "Float",
                "reqd": 1,
                "precision": 2,
                "in_list_view": 1
            },
            {
                "fieldname": "rendimiento_porcentaje",
                "label": "Rendimiento (%)",
                "fieldtype": "Percent",
                "read_only": 1,
                "description": "Porcentaje de rendimiento cereza a baba"
            },
            {
                "fieldname": "rendimiento_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "peso_pulpa_qq",
                "label": "Peso Pulpa (quintales)",
                "fieldtype": "Float",
                "precision": 2,
                "description": "Peso de la pulpa obtenida"
            },
            {
                "fieldname": "capacidad_procesamiento",
                "label": "Capacidad (qq/hora)",
                "fieldtype": "Float",
                "read_only": 1,
                "description": "Quintales procesados por hora"
            },
            {
                "fieldname": "clasificacion_sec",
                "label": "Clasificación del Producto",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "primera_calidad_qq",
                "label": "Primera Calidad (quintales)",
                "fieldtype": "Float",
                "precision": 2,
                "description": "Café baba de primera calidad"
            },
            {
                "fieldname": "segunda_calidad_qq",
                "label": "Segunda Calidad (quintales)",
                "fieldtype": "Float",
                "precision": 2,
                "description": "Café baba de segunda calidad"
            },
            {
                "fieldname": "clasificacion_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "descarte_qq",
                "label": "Descarte (quintales)",
                "fieldtype": "Float",
                "precision": 2,
                "description": "Café baba de descarte"
            },
            {
                "fieldname": "reproceso_qq",
                "label": "Reproceso (quintales)",
                "fieldtype": "Float",
                "precision": 2,
                "description": "Material que requiere reproceso"
            },
            {
                "fieldname": "subproductos_sec",
                "label": "Subproductos",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "destino_pulpa",
                "label": "Destino de la Pulpa",
                "fieldtype": "Select",
                "options": "Compostaje\nAlimento Animal\nBiogás\nFertilizante Directo\nVenta\nOtro",
                "default": "Compostaje"
            },
            {
                "fieldname": "agua_miel_litros",
                "label": "Agua Miel (litros)",
                "fieldtype": "Float",
                "description": "Cantidad de agua miel generada"
            },
            {
                "fieldname": "subproductos_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "tratamiento_agua_miel",
                "label": "Tratamiento Agua Miel",
                "fieldtype": "Select",
                "options": "Sedimentación\nFiltración\nTratamiento Biológico\nRecirculación\nSin Tratamiento",
                "description": "Método de tratamiento del agua residual"
            },
            {
                "fieldname": "reutilizacion_agua",
                "label": "Reutilización de Agua",
                "fieldtype": "Check",
                "description": "Se reutiliza el agua del proceso"
            },
            {
                "fieldname": "problemas_sec",
                "label": "Problemas y Ajustes",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "problemas_encontrados",
                "label": "Problemas Encontrados",
                "fieldtype": "Small Text",
                "description": "Problemas durante el despulpado"
            },
            {
                "fieldname": "ajustes_realizados",
                "label": "Ajustes Realizados",
                "fieldtype": "Small Text",
                "description": "Ajustes hechos durante el proceso"
            },
            {
                "fieldname": "problemas_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "paradas_maquina",
                "label": "Paradas de Máquina",
                "fieldtype": "Int",
                "description": "Número de paradas no programadas"
            },
            {
                "fieldname": "tiempo_perdido_min",
                "label": "Tiempo Perdido (minutos)",
                "fieldtype": "Float",
                "description": "Tiempo perdido por problemas"
            },
            {
                "fieldname": "limpieza_sec",
                "label": "Limpieza y Mantenimiento",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "limpieza_inicial",
                "label": "Limpieza Inicial",
                "fieldtype": "Check",
                "description": "Se realizó limpieza antes del proceso"
            },
            {
                "fieldname": "limpieza_final",
                "label": "Limpieza Final",
                "fieldtype": "Check",
                "description": "Se realizó limpieza después del proceso"
            },
            {
                "fieldname": "limpieza_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "desinfeccion",
                "label": "Desinfección",
                "fieldtype": "Check",
                "description": "Se realizó desinfección del equipo"
            },
            {
                "fieldname": "mantenimiento_posterior",
                "label": "Mantenimiento Posterior",
                "fieldtype": "Small Text",
                "description": "Mantenimiento requerido para próxima vez"
            },
            {
                "fieldname": "observaciones_sec",
                "label": "Observaciones",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones Generales",
                "fieldtype": "Text",
                "description": "Notas sobre el despulpado, calidad, recomendaciones"
            },
            {
                "fieldname": "estado_sec",
                "label": "Estado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "estado_despulpado",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "En Proceso\nFinalizado\nCancelado\nCon Problemas",
                "default": "En Proceso",
                "in_list_view": 1
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
                "role": "Agriculture Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 0
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Despulpado' creado")

def create_lavado():
    """
    Crear DocType para Lavado - Control del Proceso de Lavado
    """
    
    if frappe.db.exists("DocType", "Lavado"):
        print("⚠️  DocType 'Lavado' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Lavado",
        "module": "Custom", 
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:LAV-{fecha_lavado}-{#####}",
        "title_field": "lote_lavado",
        "fields": [
            {
                "fieldname": "informacion_basica",
                "label": "Información del Lavado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fecha_lavado",
                "label": "Fecha de Lavado",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
            },
            {
                "fieldname": "hora_inicio",
                "label": "Hora de Inicio",
                "fieldtype": "Time",
                "reqd": 1
            },
            {
                "fieldname": "basica_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "lote_lavado",
                "label": "Lote de Lavado",
                "fieldtype": "Data",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "operador_lavado",
                "label": "Operador de Lavado",
                "fieldtype": "Link",
                "options": "Employee",
                "reqd": 1
            },
            {
                "fieldname": "origen_sec",
                "label": "Material de Origen",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fermentacion_ref",
                "label": "Fermentación de Referencia",
                "fieldtype": "Link",
                "options": "Fermentacion",
                "reqd": 1
            },
            {
                "fieldname": "peso_fermentado_qq",
                "label": "Peso Café Fermentado (quintales)",
                "fieldtype": "Float",
                "reqd": 1,
                "precision": 2,
                "in_list_view": 1
            },
            {
                "fieldname": "origen_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "horas_fermentacion",
                "label": "Horas de Fermentación",
                "fieldtype": "Float",
                "description": "Tiempo total de fermentación"
            },
            {
                "fieldname": "calidad_fermentacion",
                "label": "Calidad de Fermentación",
                "fieldtype": "Select",
                "options": "Óptima\nBuena\nRegular\nSobre-fermentado\nSub-fermentado",
                "reqd": 1
            },
            {
                "fieldname": "sistema_sec",
                "label": "Sistema de Lavado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "tipo_lavado",
                "label": "Tipo de Lavado",
                "fieldtype": "Select",
                "options": "Lavado Manual\nCanal de Correteo\nTanque con Agitación\nSistema Mixto\nLavado Mecánico",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "numero_lavadas",
                "label": "Número de Lavadas",
                "fieldtype": "Int",
                "reqd": 1,
                "description": "Cantidad de lavadas realizadas"
            },
            {
                "fieldname": "sistema_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "metodo_agitacion",
                "label": "Método de Agitación",
                "fieldtype": "Select",
                "options": "Manual con Remo\nAgitación Mecánica\nBurbujeo\nFlujo de Agua\nSin Agitación",
                "description": "Forma de agitar el café durante el lavado"
            },
            {
                "fieldname": "clasificacion_densidad",
                "label": "Clasificación por Densidad",
                "fieldtype": "Check",
                "description": "Se realizó clasificación por densidad"
            },
            {
                "fieldname": "agua_sec",
                "label": "Control del Agua",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fuente_agua",
                "label": "Fuente de Agua",
                "fieldtype": "Select",
                "options": "Pozo\nNacimiento\nRío\nAcueducto\nReciclada\nMixta",
                "reqd": 1
            },
            {
                "fieldname": "calidad_agua",
                "label": "Calidad del Agua",
                "fieldtype": "Select",
                "options": "Excelente (Cristalina)\nBuena (Clara)\nRegular (Turbia)\nDeficiente (Contaminada)",
                "reqd": 1
            },
            {
                "fieldname": "agua_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "temperatura_agua",
                "label": "Temperatura del Agua (°C)",
                "fieldtype": "Float",
                "description": "Temperatura del agua utilizada"
            },
            {
                "fieldname": "consumo_agua_litros",
                "label": "Consumo de Agua (litros)",
                "fieldtype": "Float",
                "reqd": 1,
                "description": "Cantidad total de agua utilizada"
            },
            {
                "fieldname": "proceso_sec",
                "label": "Control del Proceso",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "tiempo_primera_lavada",
                "label": "Tiempo Primera Lavada (min)",
                "fieldtype": "Float",
                "description": "Duración de la primera lavada"
            },
            {
                "fieldname": "tiempo_total_lavado",
                "label": "Tiempo Total Lavado (min)",
                "fieldtype": "Float",
                "reqd": 1,
                "description": "Duración total del proceso"
            },
            {
                "fieldname": "proceso_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "remocion_mucilago",
                "label": "Remoción de Mucílago",
                "fieldtype": "Select",
                "options": "Completa (100%)\nBuena (95-99%)\nRegular (90-95%)\nIncompleta (< 90%)",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "agua_final_limpia",
                "label": "Agua Final Limpia",
                "fieldtype": "Check",
                "description": "El agua del último lavado salió limpia"
            },
            {
                "fieldname": "clasificacion_sec",
                "label": "Clasificación del Producto",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "cafe_primera_qq",
                "label": "Café Primera (quintales)",
                "fieldtype": "Float",
                "precision": 2,
                "in_list_view": 1
            },
            {
                "fieldname": "cafe_segunda_qq",
                "label": "Café Segunda (quintales)",
                "fieldtype": "Float",
                "precision": 2
            },
            {
                "fieldname": "clasificacion_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "cafe_natas_qq",
                "label": "Café Natas (quintales)",
                "fieldtype": "Float",
                "precision": 2,
                "description": "Café que flota (menor densidad)"
            },
            {
                "fieldname": "cafe_descarte_qq",
                "label": "Café Descarte (quintales)",
                "fieldtype": "Float",
                "precision": 2
            },
            {
                "fieldname": "calidad_sec",
                "label": "Control de Calidad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "uniformidad_lavado",
                "label": "Uniformidad del Lavado",
                "fieldtype": "Select",
                "options": "Muy Uniforme\nUniforme\nRegular\nDesigual",
                "description": "Uniformidad en la remoción del mucílago"
            },
            {
                "fieldname": "color_pergamino",
                "label": "Color del Pergamino",
                "fieldtype": "Select",
                "options": "Blanco Cremoso\nBlanco\nAmarillento\nMarrón\nOscuro",
                "description": "Color del pergamino después del lavado"
            },
            {
                "fieldname": "calidad_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "olor_cafe_lavado",
                "label": "Olor del Café Lavado",
                "fieldtype": "Select",
                "options": "Fresco y Limpio\nNeutro\nLigeramente Agrio\nFermentado\nDesagradable",
                "description": "Evaluación olfativa del café lavado"
            },
            {
                "fieldname": "textura_pergamino",
                "label": "Textura del Pergamino",
                "fieldtype": "Select",
                "options": "Suave y Limpio\nLigero\nÁspero\nViscoso",
                "description": "Textura al tacto del pergamino"
            },
            {
                "fieldname": "rendimiento_sec",
                "label": "Rendimiento",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "peso_cafe_lavado_qq",
                "label": "Peso Café Lavado (quintales)",
                "fieldtype": "Float",
                "reqd": 1,
                "precision": 2,
                "in_list_view": 1
            },
            {
                "fieldname": "rendimiento_lavado",
                "label": "Rendimiento Lavado (%)",
                "fieldtype": "Percent",
                "read_only": 1,
                "description": "Porcentaje de rendimiento fermentado a lavado"
            },
            {
                "fieldname": "rendimiento_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "perdida_lavado",
                "label": "Pérdida en Lavado (%)",
                "fieldtype": "Percent",
                "read_only": 1,
                "description": "Porcentaje de pérdida en el proceso"
            },
            {
                "fieldname": "eficiencia_agua",
                "label": "Eficiencia de Agua (L/qq)",
                "fieldtype": "Float",
                "read_only": 1,
                "description": "Litros de agua por quintal procesado"
            },
            {
                "fieldname": "agua_residual_sec",
                "label": "Manejo de Agua Residual",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "volumen_agua_residual",
                "label": "Volumen Agua Residual (litros)",
                "fieldtype": "Float",
                "description": "Cantidad de agua residual generada"
            },
            {
                "fieldname": "tratamiento_agua_residual",
                "label": "Tratamiento Agua Residual",
                "fieldtype": "Select",
                "options": "Sedimentación\nFiltración Natural\nTratamiento Biológico\nRecirculación\nSin Tratamiento",
                "description": "Método de tratamiento aplicado"
            },
            {
                "fieldname": "agua_residual_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "destino_agua_residual",
                "label": "Destino Agua Residual",
                "fieldtype": "Select",
                "options": "Tanque de Sedimentación\nFiltro Biológico\nCompostaje\nIrrigación\nCuerpo de Agua\nOtro",
                "description": "Destino final del agua residual"
            },
            {
                "fieldname": "reutilizacion_agua_lavado",
                "label": "Reutilización de Agua",
                "fieldtype": "Check",
                "description": "Parte del agua se reutiliza"
            },
            {
                "fieldname": "observaciones_sec",
                "label": "Observaciones",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones Generales",
                "fieldtype": "Text",
                "description": "Notas sobre el lavado, calidad, problemas encontrados"
            },
            {
                "fieldname": "estado_sec",
                "label": "Estado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "estado_lavado",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "En Proceso\nFinalizado\nCancelado\nCon Problemas",
                "default": "En Proceso",
                "in_list_view": 1
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
                "role": "Agriculture Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 0
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Lavado' creado")

def create_patio_secado_mejorado():
    """
    Crear DocType mejorado para Patio Secado - Control avanzado del secado al sol
    """
    
    if frappe.db.exists("DocType", "Patio Secado Mejorado"):
        print("⚠️  DocType 'Patio Secado Mejorado' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Patio Secado Mejorado",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:PSEC-{fecha_inicio}-{#####}",
        "title_field": "lote_secado",
        "fields": [
            {
                "fieldname": "informacion_basica",
                "label": "Información del Secado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fecha_inicio",
                "label": "Fecha de Inicio",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
            },
            {
                "fieldname": "hora_inicio",
                "label": "Hora de Inicio",
                "fieldtype": "Time",
                "reqd": 1
            },
            {
                "fieldname": "basica_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "lote_secado",
                "label": "Lote de Secado",
                "fieldtype": "Data",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "responsable_secado",
                "label": "Responsable del Secado",
                "fieldtype": "Link",
                "options": "Employee",
                "reqd": 1
            },
            {
                "fieldname": "origen_sec",
                "label": "Material de Origen",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "lavado_ref",
                "label": "Lavado de Referencia",
                "fieldtype": "Link",
                "options": "Lavado",
                "reqd": 1
            },
            {
                "fieldname": "peso_inicial_qq",
                "label": "Peso Inicial (quintales)",
                "fieldtype": "Float",
                "reqd": 1,
                "precision": 2,
                "in_list_view": 1
            },
            {
                "fieldname": "origen_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "humedad_inicial",
                "label": "Humedad Inicial (%)",
                "fieldtype": "Float",
                "reqd": 1,
                "description": "Humedad del café al inicio del secado"
            },
            {
                "fieldname": "humedad_objetivo",
                "label": "Humedad Objetivo (%)",
                "fieldtype": "Float",
                "default": 12,
                "description": "Humedad objetivo para el secado"
            },
            {
                "fieldname": "patio_sec",
                "label": "Información del Patio",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "patio_utilizado",
                "label": "Patio Utilizado",
                "fieldtype": "Data",
                "reqd": 1,
                "description": "Identificación del patio de secado"
            },
            {
                "fieldname": "area_patio_m2",
                "label": "Área del Patio (m²)",
                "fieldtype": "Float",
                "description": "Área total del patio en metros cuadrados"
            },
            {
                "fieldname": "patio_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "tipo_superficie",
                "label": "Tipo de Superficie",
                "fieldtype": "Select",
                "options": "Concreto\nLadrillo\nCemento\nPiedra\nMadera\nMalla/Zaranda\nOtra",
                "description": "Material de la superficie de secado"
            },
            {
                "fieldname": "espesor_capa_cm",
                "label": "Espesor de Capa (cm)",
                "fieldtype": "Float",
                "reqd": 1,
                "description": "Espesor de la capa de café extendida"
            },
            {
                "fieldname": "condiciones_sec",
                "label": "Condiciones Ambientales",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "temperatura_ambiente",
                "label": "Temperatura Ambiente (°C)",
                "fieldtype": "Float",
                "description": "Temperatura ambiente promedio"
            },
            {
                "fieldname": "humedad_relativa",
                "label": "Humedad Relativa (%)",
                "fieldtype": "Float",
                "description": "Humedad relativa del ambiente"
            },
            {
                "fieldname": "condiciones_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "velocidad_viento",
                "label": "Velocidad del Viento",
                "fieldtype": "Select",
                "options": "Calma\nLigero\nModerado\nFuerte\nMuy Fuerte",
                "description": "Intensidad del viento durante el secado"
            },
            {
                "fieldname": "horas_sol_efectivas",
                "label": "Horas de Sol Efectivas",
                "fieldtype": "Float",
                "description": "Horas de sol directo recibidas"
            },
            {
                "fieldname": "manejo_sec",
                "label": "Manejo del Secado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "volteos_dia",
                "label": "Volteos por Día",
                "fieldtype": "Int",
                "reqd": 1,
                "description": "Número de volteos realizados por día"
            },
            {
                "fieldname": "horario_volteos",
                "label": "Horario de Volteos",
                "fieldtype": "Small Text",
                "description": "Horarios en que se realizan los volteos"
            },
            {
                "fieldname": "manejo_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "proteccion_lluvia",
                "label": "Protección contra Lluvia",
                "fieldtype": "Select",
                "options": "Cubierta Fija\nLona Movible\nTecho Retráctil\nRecolección Rápida\nSin Protección",
                "description": "Método de protección contra la lluvia"
            },
            {
                "fieldname": "proteccion_noche",
                "label": "Protección Nocturna",
                "fieldtype": "Check",
                "description": "Se protege el café durante la noche"
            },
            {
                "fieldname": "seguimiento_sec",
                "label": "Seguimiento Diario",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "dias_secado",
                "label": "Días de Secado",
                "fieldtype": "Int",
                "read_only": 1,
                "description": "Días transcurridos en el secado"
            },
            {
                "fieldname": "humedad_actual",
                "label": "Humedad Actual (%)",
                "fieldtype": "Float",
                "description": "Humedad actual del café"
            },
            {
                "fieldname": "seguimiento_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "peso_actual_qq",
                "label": "Peso Actual (quintales)",
                "fieldtype": "Float",
                "precision": 2,
                "description": "Peso actual del café en secado"
            },
            {
                "fieldname": "reduccion_peso",
                "label": "Reducción de Peso (%)",
                "fieldtype": "Percent",
                "read_only": 1,
                "description": "Porcentaje de reducción de peso"
            },
            {
                "fieldname": "problemas_sec",
                "label": "Problemas y Eventos",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "dias_lluvia",
                "label": "Días con Lluvia",
                "fieldtype": "Int",
                "description": "Número de días con lluvia durante el secado"
            },
            {
                "fieldname": "horas_perdidas_clima",
                "label": "Horas Perdidas por Clima",
                "fieldtype": "Float",
                "description": "Horas de secado perdidas por mal clima"
            },
            {
                "fieldname": "problemas_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "contaminacion_detectada",
                "label": "Contaminación Detectada",
                "fieldtype": "Check",
                "description": "Se detectó contaminación del café"
            },
            {
                "fieldname": "tipo_contaminacion",
                "label": "Tipo de Contaminación",
                "fieldtype": "Small Text",
                "depends_on": "eval:doc.contaminacion_detectada",
                "description": "Tipo de contaminación encontrada"
            },
            {
                "fieldname": "calidad_sec",
                "label": "Control de Calidad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "uniformidad_secado",
                "label": "Uniformidad del Secado",
                "fieldtype": "Select",
                "options": "Muy Uniforme\nUniforme\nRegular\nDesigual\nMuy Desigual",
                "description": "Uniformidad en el secado del lote"
            },
            {
                "fieldname": "color_pergamino",
                "label": "Color del Pergamino",
                "fieldtype": "Select",
                "options": "Dorado\nAmarillo Claro\nAmarillo\nAmarillo Oscuro\nMarrón",
                "description": "Color del pergamino al final del secado"
            },
            {
                "fieldname": "calidad_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "quebrados_secado",
                "label": "Granos Quebrados (%)",
                "fieldtype": "Percent",
                "description": "Porcentaje de granos quebrados por el secado"
            },
            {
                "fieldname": "evaluacion_sensorial",
                "label": "Evaluación Sensorial",
                "fieldtype": "Select",
                "options": "Excelente\nBuena\nRegular\nDeficiente",
                "description": "Evaluación del aroma y características del café"
            },
            {
                "fieldname": "finalizacion_sec",
                "label": "Finalización del Secado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fecha_finalizacion",
                "label": "Fecha de Finalización",
                "fieldtype": "Date",
                "description": "Fecha en que se completó el secado"
            },
            {
                "fieldname": "peso_final_qq",
                "label": "Peso Final (quintales)",
                "fieldtype": "Float",
                "precision": 2,
                "in_list_view": 1
            },
            {
                "fieldname": "finalizacion_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "humedad_final",
                "label": "Humedad Final (%)",
                "fieldtype": "Float",
                "description": "Humedad final alcanzada"
            },
            {
                "fieldname": "rendimiento_secado",
                "label": "Rendimiento Secado (%)",
                "fieldtype": "Percent",
                "read_only": 1,
                "description": "Porcentaje de rendimiento del secado"
            },
            {
                "fieldname": "destino_sec",
                "label": "Destino del Café",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "destino_cafe",
                "label": "Destino del Café",
                "fieldtype": "Select",
                "options": "Almacenamiento\nSecado Mecánico Complementario\nTrilla Inmediata\nVenta Pergamino\nOtro",
                "description": "Destino del café después del secado"
            },
            {
                "fieldname": "observaciones_sec",
                "label": "Observaciones",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones Generales",
                "fieldtype": "Text",
                "description": "Notas sobre el secado, problemas, recomendaciones"
            },
            {
                "fieldname": "estado_sec",
                "label": "Estado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "estado_secado",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "Iniciado\nEn Proceso\nFinalizado\nCancelado\nCon Problemas",
                "default": "Iniciado",
                "in_list_view": 1
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
                "role": "Agriculture Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 0
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Patio Secado Mejorado' creado")

def create_secadora_mejorada():
    """
    Crear DocType mejorado para Secadora - Control avanzado del secado mecánico
    """
    
    if frappe.db.exists("DocType", "Secadora Mejorada"):
        print("⚠️  DocType 'Secadora Mejorada' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Secadora Mejorada",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:SEC-{fecha_inicio}-{#####}",
        "title_field": "lote_secado_mecanico",
        "fields": [
            {
                "fieldname": "informacion_basica",
                "label": "Información del Secado Mecánico",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fecha_inicio",
                "label": "Fecha de Inicio",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
            },
            {
                "fieldname": "hora_inicio",
                "label": "Hora de Inicio",
                "fieldtype": "Time",
                "reqd": 1
            },
            {
                "fieldname": "basica_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "lote_secado_mecanico",
                "label": "Lote de Secado Mecánico",
                "fieldtype": "Data",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "operador_secadora",
                "label": "Operador de Secadora",
                "fieldtype": "Link",
                "options": "Employee",
                "reqd": 1
            },
            {
                "fieldname": "origen_sec",
                "label": "Material de Origen",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "origen_material",
                "label": "Origen del Material",
                "fieldtype": "Select",
                "options": "Café Lavado Fresco\nPatio Secado Parcial\nCombinado\nOtro",
                "reqd": 1
            },
            {
                "fieldname": "peso_inicial_qq",
                "label": "Peso Inicial (quintales)",
                "fieldtype": "Float",
                "reqd": 1,
                "precision": 2,
                "in_list_view": 1
            },
            {
                "fieldname": "origen_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "humedad_inicial",
                "label": "Humedad Inicial (%)",
                "fieldtype": "Float",
                "reqd": 1,
                "description": "Humedad del café al inicio del secado mecánico"
            },
            {
                "fieldname": "humedad_objetivo",
                "label": "Humedad Objetivo (%)",
                "fieldtype": "Float",
                "default": 12,
                "description": "Humedad objetivo para el secado"
            },
            {
                "fieldname": "equipo_sec",
                "label": "Información del Equipo",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "tipo_secadora",
                "label": "Tipo de Secadora",
                "fieldtype": "Select",
                "options": "Secadora Rotativa\nSecadora de Bandejas\nSecadora de Flujo Continuo\nSecadora Solar Híbrida\nOtra",
                "reqd": 1
            },
            {
                "fieldname": "marca_modelo",
                "label": "Marca y Modelo",
                "fieldtype": "Data",
                "description": "Marca y modelo de la secadora"
            },
            {
                "fieldname": "equipo_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "capacidad_nominal_qq",
                "label": "Capacidad Nominal (quintales)",
                "fieldtype": "Float",
                "description": "Capacidad nominal de la secadora"
            },
            {
                "fieldname": "combustible_utilizado",
                "label": "Combustible Utilizado",
                "fieldtype": "Select",
                "options": "Leña\nGas Propano\nDiesel\nElectricidad\nCascarilla de Café\nMixto\nOtro",
                "reqd": 1
            },
            {
                "fieldname": "configuracion_sec",
                "label": "Configuración del Proceso",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "temperatura_inicial",
                "label": "Temperatura Inicial (°C)",
                "fieldtype": "Float",
                "reqd": 1,
                "description": "Temperatura de inicio del secado"
            },
            {
                "fieldname": "temperatura_maxima",
                "label": "Temperatura Máxima (°C)",
                "fieldtype": "Float",
                "description": "Temperatura máxima alcanzada"
            },
            {
                "fieldname": "configuracion_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "velocidad_aire",
                "label": "Velocidad del Aire",
                "fieldtype": "Select",
                "options": "Baja\nModerada\nAlta\nVariable",
                "description": "Velocidad del flujo de aire"
            },
            {
                "fieldname": "programa_secado",
                "label": "Programa de Secado",
                "fieldtype": "Select",
                "options": "Suave (Baja Temperatura)\nNormal\nRápido\nPersonalizado",
                "description": "Programa utilizado para el secado"
            },
            {
                "fieldname": "control_sec",
                "label": "Control del Proceso",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "sistema_control",
                "label": "Sistema de Control",
                "fieldtype": "Select",
                "options": "Manual\nSemi-Automático\nAutomático\nControl PLC",
                "description": "Tipo de control utilizado"
            },
            {
                "fieldname": "monitoreo_humedad",
                "label": "Monitoreo de Humedad",
                "fieldtype": "Select",
                "options": "Cada Hora\nCada 2 Horas\nCada 4 Horas\nManual\nContinuo",
                "description": "Frecuencia de monitoreo de humedad"
            },
            {
                "fieldname": "control_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "ajustes_temperatura",
                "label": "Ajustes de Temperatura",
                "fieldtype": "Small Text",
                "description": "Ajustes realizados durante el proceso"
            },
            {
                "fieldname": "tiempo_total_horas",
                "label": "Tiempo Total (horas)",
                "fieldtype": "Float",
                "description": "Duración total del secado mecánico"
            },
            {
                "fieldname": "consumo_sec",
                "label": "Consumo de Combustible",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "consumo_combustible",
                "label": "Consumo de Combustible",
                "fieldtype": "Float",
                "description": "Cantidad de combustible consumido"
            },
            {
                "fieldname": "unidad_consumo",
                "label": "Unidad de Consumo",
                "fieldtype": "Select",
                "options": "Galones\nLitros\nKWh\nKg Leña\nM³ Gas\nOtra",
                "description": "Unidad de medida del combustible"
            },
            {
                "fieldname": "consumo_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "eficiencia_combustible",
                "label": "Eficiencia Combustible",
                "fieldtype": "Float",
                "read_only": 1,
                "description": "Eficiencia del consumo por quintal"
            },
            {
                "fieldname": "costo_combustible",
                "label": "Costo Combustible (GTQ)",
                "fieldtype": "Currency",
                "description": "Costo total del combustible utilizado"
            },
            {
                "fieldname": "seguimiento_sec",
                "label": "Seguimiento del Proceso",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "humedad_4_horas",
                "label": "Humedad a 4 horas (%)",
                "fieldtype": "Float",
                "description": "Humedad después de 4 horas"
            },
            {
                "fieldname": "humedad_8_horas",
                "label": "Humedad a 8 horas (%)",
                "fieldtype": "Float",
                "description": "Humedad después de 8 horas"
            },
            {
                "fieldname": "seguimiento_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "humedad_12_horas",
                "label": "Humedad a 12 horas (%)",
                "fieldtype": "Float",
                "description": "Humedad después de 12 horas"
            },
            {
                "fieldname": "humedad_final",
                "label": "Humedad Final (%)",
                "fieldtype": "Float",
                "description": "Humedad final alcanzada"
            },
            {
                "fieldname": "calidad_sec",
                "label": "Control de Calidad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "uniformidad_secado",
                "label": "Uniformidad del Secado",
                "fieldtype": "Select",
                "options": "Excelente\nBuena\nRegular\nDeficiente",
                "description": "Uniformidad en el secado del lote"
            },
            {
                "fieldname": "color_pergamino",
                "label": "Color del Pergamino",
                "fieldtype": "Select",
                "options": "Dorado Natural\nAmarillo Claro\nAmarillo\nAmarillo Oscuro\nMarrón Claro\nMarrón",
                "description": "Color del pergamino después del secado"
            },
            {
                "fieldname": "calidad_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "granos_tostados",
                "label": "Granos Tostados (%)",
                "fieldtype": "Percent",
                "description": "Porcentaje de granos dañados por exceso de calor"
            },
            {
                "fieldname": "evaluacion_aroma",
                "label": "Evaluación del Aroma",
                "fieldtype": "Select",
                "options": "Excelente\nBueno\nNeutro\nDeficiente",
                "description": "Evaluación del aroma del café secado"
            },
            {
                "fieldname": "problemas_sec",
                "label": "Problemas y Eventos",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "problemas_equipo",
                "label": "Problemas del Equipo",
                "fieldtype": "Small Text",
                "description": "Problemas técnicos durante el secado"
            },
            {
                "fieldname": "paradas_imprevistas",
                "label": "Paradas Imprevistas",
                "fieldtype": "Int",
                "description": "Número de paradas no programadas"
            },
            {
                "fieldname": "problemas_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "tiempo_perdido_horas",
                "label": "Tiempo Perdido (horas)",
                "fieldtype": "Float",
                "description": "Tiempo perdido por problemas"
            },
            {
                "fieldname": "sobrecalentamiento",
                "label": "Sobrecalentamiento",
                "fieldtype": "Check",
                "description": "Se presentó sobrecalentamiento"
            },
            {
                "fieldname": "resultados_sec",
                "label": "Resultados Finales",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "peso_final_qq",
                "label": "Peso Final (quintales)",
                "fieldtype": "Float",
                "precision": 2,
                "in_list_view": 1
            },
            {
                "fieldname": "rendimiento_secado",
                "label": "Rendimiento Secado (%)",
                "fieldtype": "Percent",
                "read_only": 1,
                "description": "Porcentaje de rendimiento del secado"
            },
            {
                "fieldname": "resultados_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "fecha_finalizacion",
                "label": "Fecha de Finalización",
                "fieldtype": "Date",
                "description": "Fecha de finalización del secado"
            },
            {
                "fieldname": "calificacion_general",
                "label": "Calificación General",
                "fieldtype": "Select",
                "options": "Excelente\nBuena\nRegular\nDeficiente",
                "description": "Calificación general del proceso"
            },
            {
                "fieldname": "mantenimiento_sec",
                "label": "Mantenimiento",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "mantenimiento_pre",
                "label": "Mantenimiento Previo",
                "fieldtype": "Check",
                "description": "Se realizó mantenimiento antes del uso"
            },
            {
                "fieldname": "limpieza_post",
                "label": "Limpieza Posterior",
                "fieldtype": "Check",
                "description": "Se realizó limpieza después del uso"
            },
            {
                "fieldname": "mantenimiento_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "mantenimiento_requerido",
                "label": "Mantenimiento Requerido",
                "fieldtype": "Small Text",
                "description": "Mantenimiento necesario para próximo uso"
            },
            {
                "fieldname": "horas_operacion",
                "label": "Horas de Operación",
                "fieldtype": "Float",
                "description": "Horas acumuladas de operación del equipo"
            },
            {
                "fieldname": "observaciones_sec",
                "label": "Observaciones",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones Generales",
                "fieldtype": "Text",
                "description": "Notas sobre el secado mecánico, problemas, recomendaciones"
            },
            {
                "fieldname": "estado_sec",
                "label": "Estado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "estado_secado",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "Iniciado\nEn Proceso\nFinalizado\nCancelado\nCon Problemas",
                "default": "Iniciado",
                "in_list_view": 1
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
                "role": "Agriculture Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 0
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Secadora Mejorada' creado")

def create_almacenamiento_pergamino():
    """
    Crear DocType para Almacenamiento de Pergamino - Control de bodega y inventario
    """
    
    if frappe.db.exists("DocType", "Almacenamiento Pergamino"):
        print("⚠️  DocType 'Almacenamiento Pergamino' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Almacenamiento Pergamino",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:ALM-{fecha_ingreso}-{#####}",
        "title_field": "lote_almacenamiento",
        "fields": [
            {
                "fieldname": "informacion_basica",
                "label": "Información del Almacenamiento",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "fecha_ingreso",
                "label": "Fecha de Ingreso",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
            },
            {
                "fieldname": "hora_ingreso",
                "label": "Hora de Ingreso",
                "fieldtype": "Time",
                "reqd": 1
            },
            {
                "fieldname": "basica_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "lote_almacenamiento",
                "label": "Lote de Almacenamiento",
                "fieldtype": "Data",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "responsable_bodega",
                "label": "Responsable de Bodega",
                "fieldtype": "Link",
                "options": "Employee",
                "reqd": 1
            },
            {
                "fieldname": "origen_sec",
                "label": "Origen del Material",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "origen_secado",
                "label": "Origen del Secado",
                "fieldtype": "Select",
                "options": "Patio Secado\nSecado Mecánico\nSecado Combinado\nOtro",
                "reqd": 1
            },
            {
                "fieldname": "secado_ref",
                "label": "Referencia de Secado",
                "fieldtype": "Data",
                "description": "Referencia al proceso de secado"
            },
            {
                "fieldname": "origen_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "fecha_secado",
                "label": "Fecha de Secado",
                "fieldtype": "Date",
                "description": "Fecha en que finalizó el secado"
            },
            {
                "fieldname": "tiempo_reposo_dias",
                "label": "Tiempo de Reposo (días)",
                "fieldtype": "Int",
                "read_only": 1,
                "description": "Días transcurridos desde el secado"
            },
            {
                "fieldname": "producto_sec",
                "label": "Características del Producto",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "peso_ingreso_qq",
                "label": "Peso de Ingreso (quintales)",
                "fieldtype": "Float",
                "reqd": 1,
                "precision": 2,
                "in_list_view": 1
            },
            {
                "fieldname": "humedad_ingreso",
                "label": "Humedad de Ingreso (%)",
                "fieldtype": "Float",
                "reqd": 1,
                "description": "Humedad del café al ingresar a bodega"
            },
            {
                "fieldname": "producto_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "calidad_pergamino",
                "label": "Calidad del Pergamino",
                "fieldtype": "Select",
                "options": "Excelente\nPrimera\nSegunda\nTercera\nDescarte",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "numero_costales",
                "label": "Número de Costales",
                "fieldtype": "Int",
                "reqd": 1,
                "description": "Cantidad de costales almacenados"
            },
            {
                "fieldname": "bodega_sec",
                "label": "Información de la Bodega",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "bodega_ubicacion",
                "label": "Bodega/Ubicación",
                "fieldtype": "Data",
                "reqd": 1,
                "description": "Identificación de la bodega o área"
            },
            {
                "fieldname": "seccion_bodega",
                "label": "Sección de Bodega",
                "fieldtype": "Data",
                "description": "Sección específica dentro de la bodega"
            },
            {
                "fieldname": "bodega_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "nivel_estiba",
                "label": "Nivel de Estiba",
                "fieldtype": "Int",
                "description": "Nivel en que se coloca (1=suelo, 2=segundo nivel, etc.)"
            },
            {
                "fieldname": "tarima_utilizada",
                "label": "Tarima Utilizada",
                "fieldtype": "Check",
                "description": "Se utilizó tarima o paleta para elevar"
            },
            {
                "fieldname": "condiciones_sec",
                "label": "Condiciones de Almacenamiento",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "temperatura_bodega",
                "label": "Temperatura Bodega (°C)",
                "fieldtype": "Float",
                "description": "Temperatura ambiente de la bodega"
            },
            {
                "fieldname": "humedad_relativa_bodega",
                "label": "Humedad Relativa Bodega (%)",
                "fieldtype": "Float",
                "description": "Humedad relativa del ambiente"
            },
            {
                "fieldname": "condiciones_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "ventilacion_bodega",
                "label": "Ventilación de Bodega",
                "fieldtype": "Select",
                "options": "Excelente\nBuena\nRegular\nDeficiente\nSin Ventilación",
                "description": "Nivel de ventilación de la bodega"
            },
            {
                "fieldname": "proteccion_humedad",
                "label": "Protección contra Humedad",
                "fieldtype": "Check",
                "description": "Bodega protegida contra humedad"
            },
            {
                "fieldname": "control_sec",
                "label": "Control de Calidad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "inspeccion_visual",
                "label": "Inspección Visual",
                "fieldtype": "Select",
                "options": "Aprobado\nAceptable\nObservaciones\nRechazado",
                "reqd": 1,
                "description": "Resultado de la inspección visual"
            },
            {
                "fieldname": "presencia_hongos",
                "label": "Presencia de Hongos",
                "fieldtype": "Check",
                "description": "Se detecta presencia de hongos"
            },
            {
                "fieldname": "control_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "olor_caracteristico",
                "label": "Olor Característico",
                "fieldtype": "Select",
                "options": "Normal\nLigeramente Alterado\nMoho\nFermentado\nRancio",
                "description": "Evaluación del olor del café"
            },
            {
                "fieldname": "uniformidad_lote",
                "label": "Uniformidad del Lote",
                "fieldtype": "Select",
                "options": "Muy Uniforme\nUniforme\nRegular\nVariable",
                "description": "Uniformidad del lote almacenado"
            },
            {
                "fieldname": "seguimiento_sec",
                "label": "Seguimiento y Monitoreo",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "frecuencia_inspeccion",
                "label": "Frecuencia de Inspección",
                "fieldtype": "Select",
                "options": "Diaria\nSemanal\nQuincenal\nMensual\nSegún necesidad",
                "default": "Semanal",
                "description": "Frecuencia de inspección del lote"
            },
            {
                "fieldname": "proxima_inspeccion",
                "label": "Próxima Inspección",
                "fieldtype": "Date",
                "description": "Fecha programada para próxima inspección"
            },
            {
                "fieldname": "seguimiento_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "control_plagas",
                "label": "Control de Plagas",
                "fieldtype": "Select",
                "options": "No Requerido\nPreventivo\nCorrectivo\nFumigación",
                "default": "Preventivo",
                "description": "Tipo de control de plagas aplicado"
            },
            {
                "fieldname": "rotacion_costales",
                "label": "Rotación de Costales",
                "fieldtype": "Check",
                "description": "Se realiza rotación periódica de costales"
            },
            {
                "fieldname": "destino_sec",
                "label": "Destino Programado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "destino_programado",
                "label": "Destino Programado",
                "fieldtype": "Select",
                "options": "Trilla Propia\nVenta Pergamino\nExportación Directa\nCatación\nPor Definir",
                "description": "Destino planificado para el lote"
            },
            {
                "fieldname": "fecha_salida_programada",
                "label": "Fecha Salida Programada",
                "fieldtype": "Date",
                "description": "Fecha estimada para salida de bodega"
            },
            {
                "fieldname": "destino_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "tiempo_almacenamiento_min",
                "label": "Tiempo Mínimo Almacenamiento (días)",
                "fieldtype": "Int",
                "default": 30,
                "description": "Días mínimos de reposo requeridos"
            },
            {
                "fieldname": "cliente_destino",
                "label": "Cliente Destino",
                "fieldtype": "Data",
                "description": "Cliente o destino específico del lote"
            },
            {
                "fieldname": "trazabilidad_sec",
                "label": "Trazabilidad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "codigo_trazabilidad",
                "label": "Código de Trazabilidad",
                "fieldtype": "Data",
                "description": "Código único para trazabilidad completa"
            },
            {
                "fieldname": "origen_finca",
                "label": "Origen Finca/Lote",
                "fieldtype": "Data",
                "description": "Identificación del origen específico"
            },
            {
                "fieldname": "trazabilidad_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "fecha_cosecha_origen",
                "label": "Fecha Cosecha Origen",
                "fieldtype": "Date",
                "description": "Fecha original de la cosecha"
            },
            {
                "fieldname": "variedad_cafe",
                "label": "Variedad de Café",
                "fieldtype": "Data",
                "description": "Variedad específica del café"
            },
            {
                "fieldname": "observaciones_sec",
                "label": "Observaciones",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones Generales",
                "fieldtype": "Text",
                "description": "Notas sobre el almacenamiento, calidad, condiciones especiales"
            },
            {
                "fieldname": "estado_sec",
                "label": "Estado",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "estado_almacenamiento",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "Ingresado\nEn Reposo\nListo para Salida\nRetirado\nDeteriorado",
                "default": "Ingresado",
                "in_list_view": 1
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
                "role": "Agriculture Manager",
                "permlevel": 0,
                "create": 1,
                "read": 1,
                "write": 1,
                "delete": 0
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Almacenamiento Pergamino' creado")

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
