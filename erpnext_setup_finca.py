#!/usr/bin/env python3
"""
Script para configurar ERPNext para una finca de café en Guatemala
Crea los Doctypes necesarios para control de trabajadores, pagos y trazabilidad
"""

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def setup_finca_cafe():
    """Configuración principal para la finca de café"""
    
    print("🌱 Iniciando configuración de ERPNext para Finca de Café...")
    
    # 1. Crear Doctypes personalizados
    create_adelantos_prestamos()
    create_pago_quincenal()
    create_unidad_trabajo()
    create_actividad_campo()
    create_fermentacion()
    create_patio_secado()
    create_secadora()
    
    print("✅ Configuración completada exitosamente!")

def create_adelantos_prestamos():
    """Crear Doctype para Adelantos y Préstamos"""
    
    if frappe.db.exists("DocType", "Adelantos y Prestamos"):
        print("⚠️  DocType 'Adelantos y Prestamos' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Adelantos y Prestamos",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "By fieldname",
        "autoname": "field:empleado",
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
                "options": "Adelanto\nPrestamo",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "monto",
                "label": "Monto",
                "fieldtype": "Currency",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "estado",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "Pendiente\nAplicado",
                "default": "Pendiente",
                "in_list_view": 1
            },
            {
                "fieldname": "nota",
                "label": "Nota",
                "fieldtype": "Small Text"
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
    print("✅ DocType 'Adelantos y Prestamos' creado")

def create_pago_quincenal():
    """Crear Doctype para Pago Quincenal"""
    
    if frappe.db.exists("DocType", "Pago Quincenal"):
        print("⚠️  DocType 'Pago Quincenal' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Pago Quincenal",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "By fieldname",
        "autoname": "field:empleado",
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
                "fieldname": "fecha_inicio",
                "label": "Fecha Inicio",
                "fieldtype": "Date",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "fecha_fin",
                "label": "Fecha Fin",
                "fieldtype": "Date",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "total_producido",
                "label": "Total Producido",
                "fieldtype": "Currency",
                "reqd": 1
            },
            {
                "fieldname": "adelantos_aplicados",
                "label": "Adelantos Aplicados",
                "fieldtype": "Currency",
                "default": 0
            },
            {
                "fieldname": "pago_neto",
                "label": "Pago Neto",
                "fieldtype": "Currency",
                "read_only": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "estado",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "Borrador\nPagado",
                "default": "Borrador",
                "in_list_view": 1
            },
            {
                "fieldname": "notas",
                "label": "Notas",
                "fieldtype": "Text"
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
    print("✅ DocType 'Pago Quincenal' creado")

def create_unidad_trabajo():
    """Crear Doctype para Unidad de Trabajo (Cuerdas)"""
    
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
        "fields": [
            {
                "fieldname": "codigo",
                "label": "Código",
                "fieldtype": "Data",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "ubicacion",
                "label": "Ubicación",
                "fieldtype": "Data",
                "in_list_view": 1
            },
            {
                "fieldname": "tamano",
                "label": "Tamaño",
                "fieldtype": "Data",
                "default": "25x25 metros",
                "read_only": 1
            },
            {
                "fieldname": "cultivo_actual",
                "label": "Cultivo Actual",
                "fieldtype": "Link",
                "options": "Item",
                "in_list_view": 1
            },
            {
                "fieldname": "cantidad_arboles",
                "label": "Cantidad de Árboles",
                "fieldtype": "Int",
                "default": 0
            },
            {
                "fieldname": "notas",
                "label": "Notas",
                "fieldtype": "Text"
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
    """Crear Doctype para Actividad de Campo"""
    
    if frappe.db.exists("DocType", "Actividad de Campo"):
        print("⚠️  DocType 'Actividad de Campo' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Actividad de Campo",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:ACT-{empleado}-{#####}",
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
                "fieldname": "unidad_trabajo",
                "label": "Unidad de Trabajo",
                "fieldtype": "Link",
                "options": "Unidad de Trabajo",
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
                "fieldname": "tipo_trabajo",
                "label": "Tipo de Trabajo",
                "fieldtype": "Select",
                "options": "Recolección\nPoda\nLimpieza\nAplicación\nSiembra\nCosecha",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "medida",
                "label": "Medida",
                "fieldtype": "Select",
                "options": "Libras\nUnidades\nMetros\nDía",
                "reqd": 1
            },
            {
                "fieldname": "cantidad",
                "label": "Cantidad",
                "fieldtype": "Float",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "tarifa_unidad",
                "label": "Tarifa por Unidad",
                "fieldtype": "Currency",
                "reqd": 1
            },
            {
                "fieldname": "pago_generado",
                "label": "Pago Generado",
                "fieldtype": "Currency",
                "read_only": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "es_pago_inmediato",
                "label": "Es Pago Inmediato (Domingo)",
                "fieldtype": "Check",
                "default": 0
            },
            {
                "fieldname": "lote_id",
                "label": "Lote ID",
                "fieldtype": "Data",
                "description": "ID para trazabilidad del producto"
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
    """Crear Doctype para proceso de Fermentación"""
    
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
        "fields": [
            {
                "fieldname": "fecha",
                "label": "Fecha",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
            },
            {
                "fieldname": "producto",
                "label": "Producto",
                "fieldtype": "Link",
                "options": "Item",
                "reqd": 1,
                "default": "Café Cereza"
            },
            {
                "fieldname": "cantidad",
                "label": "Cantidad (lbs)",
                "fieldtype": "Float",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "pileta",
                "label": "Pileta",
                "fieldtype": "Data",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "tiempo_estimado",
                "label": "Tiempo Estimado (horas)",
                "fieldtype": "Float",
                "default": 24
            },
            {
                "fieldname": "responsable",
                "label": "Responsable",
                "fieldtype": "Link",
                "options": "Employee"
            },
            {
                "fieldname": "estado",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "En Proceso\nListo\nTerminado",
                "default": "En Proceso",
                "in_list_view": 1
            },
            {
                "fieldname": "lote_origen",
                "label": "Lote de Origen",
                "fieldtype": "Data",
                "description": "Referencia al lote de recolección"
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones",
                "fieldtype": "Text"
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

def create_patio_secado():
    """Crear Doctype para Patio de Secado"""
    
    if frappe.db.exists("DocType", "Patio Secado"):
        print("⚠️  DocType 'Patio Secado' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Patio Secado",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:PATIO-{fecha}-{patio}",
        "fields": [
            {
                "fieldname": "fecha_ingreso",
                "label": "Fecha de Ingreso",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
            },
            {
                "fieldname": "producto",
                "label": "Producto",
                "fieldtype": "Link",
                "options": "Item",
                "reqd": 1,
                "default": "Café Fermentado"
            },
            {
                "fieldname": "cantidad",
                "label": "Cantidad (lbs)",
                "fieldtype": "Float",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "patio",
                "label": "Patio",
                "fieldtype": "Data",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "dias_secado",
                "label": "Días de Secado",
                "fieldtype": "Int",
                "default": 0
            },
            {
                "fieldname": "humedad_estimada",
                "label": "% Humedad Estimada",
                "fieldtype": "Percent",
                "default": 0
            },
            {
                "fieldname": "estado",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "En Secado\nListo\nPasado a Secadora",
                "default": "En Secado",
                "in_list_view": 1
            },
            {
                "fieldname": "lote_origen",
                "label": "Lote de Origen",
                "fieldtype": "Data",
                "description": "Referencia al lote de fermentación"
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones",
                "fieldtype": "Text"
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
    print("✅ DocType 'Patio Secado' creado")

def create_secadora():
    """Crear Doctype para Secadora Mecánica"""
    
    if frappe.db.exists("DocType", "Secadora"):
        print("⚠️  DocType 'Secadora' ya existe")
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Secadora",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "Expression (old style)",
        "autoname": "format:SEC-{fecha}-{operario}",
        "fields": [
            {
                "fieldname": "fecha_ingreso",
                "label": "Fecha de Ingreso",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today",
                "in_list_view": 1
            },
            {
                "fieldname": "producto_entrada",
                "label": "Producto de Entrada",
                "fieldtype": "Link",
                "options": "Item",
                "reqd": 1,
                "default": "Café Semiseco"
            },
            {
                "fieldname": "cantidad_entrada",
                "label": "Cantidad Entrada (lbs)",
                "fieldtype": "Float",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "tiempo_secado",
                "label": "Tiempo en Máquina (horas)",
                "fieldtype": "Float",
                "reqd": 1
            },
            {
                "fieldname": "temperatura",
                "label": "Temperatura",
                "fieldtype": "Data"
            },
            {
                "fieldname": "operario",
                "label": "Operario",
                "fieldtype": "Link",
                "options": "Employee",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "producto_salida",
                "label": "Producto de Salida",
                "fieldtype": "Link",
                "options": "Item",
                "default": "Café Pergamino"
            },
            {
                "fieldname": "cantidad_salida",
                "label": "Cantidad Salida (lbs)",
                "fieldtype": "Float",
                "in_list_view": 1
            },
            {
                "fieldname": "estado",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "En Proceso\nTerminado\nPasado a Bodega",
                "default": "En Proceso",
                "in_list_view": 1
            },
            {
                "fieldname": "lote_origen",
                "label": "Lote de Origen",
                "fieldtype": "Data",
                "description": "Referencia al lote de patio"
            },
            {
                "fieldname": "observaciones",
                "label": "Observaciones",
                "fieldtype": "Text"
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
    print("✅ DocType 'Secadora' creado")

if __name__ == "__main__":
    setup_finca_cafe()
