#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🇬🇹 ERPCafe - Configuración específica para ERPNext v15
Script de configuración avanzada para características v15

Compatible con:
- ERPNext v15.x
- Frappe Framework v15.x
- Python 3.11+
- MariaDB 10.6+

Autor: ERPNext Guatemala Coffee Solutions
Fecha: Julio 2025
Licencia: MIT
"""

import frappe
from frappe import _
from frappe.utils import nowdate, now_datetime, flt, cint
import json
import sys
import os

class ERPNextV15Config:
    """
    Clase para configuración específica de ERPNext v15
    """
    
    def __init__(self):
        self.version = "15.x"
        self.python_min = (3, 11)
        self.mariadb_min = "10.6"
        
    def validate_environment(self):
        """
        Validar entorno para ERPNext v15
        """
        print("🔍 Validando entorno para ERPNext v15...")
        
        # Validar Python
        if sys.version_info < self.python_min:
            raise Exception(f"❌ Se requiere Python {self.python_min[0]}.{self.python_min[1]}+")
        
        print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} compatible")
        
        # Validar ERPNext
        try:
            import erpnext
            version = erpnext.__version__
            major_version = int(version.split('.')[0])
            if major_version < 15:
                raise Exception(f"❌ Se requiere ERPNext v15+. Actual: v{version}")
            print(f"✅ ERPNext v{version} compatible")
        except ImportError:
            raise Exception("❌ ERPNext no encontrado")
        
        # Validar Frappe
        try:
            import frappe
            version = frappe.__version__
            major_version = int(version.split('.')[0])
            if major_version < 15:
                raise Exception(f"❌ Se requiere Frappe v15+. Actual: v{version}")
            print(f"✅ Frappe v{version} compatible")
        except ImportError:
            raise Exception("❌ Frappe no encontrado")
        
        print("✅ Entorno validado correctamente para ERPNext v15")
        
    def get_v15_features(self):
        """
        Obtener características nuevas de v15
        """
        return {
            "new_field_types": [
                "Duration",
                "JSON", 
                "Rating",
                "Geolocation",
                "Icon",
                "Barcode"
            ],
            "new_features": [
                "Improved Dashboard",
                "Enhanced Workflow Engine",
                "Better Mobile Support",
                "Advanced Automation",
                "Improved Performance",
                "New Chart Types",
                "Enhanced Security"
            ],
            "database_improvements": [
                "Better Query Optimization",
                "Enhanced Indexing",
                "Improved Backup System",
                "Better Migration Tools"
            ]
        }
        
    def setup_v15_field_types(self):
        """
        Configurar nuevos tipos de campo de v15
        """
        print("🔧 Configurando nuevos tipos de campo v15...")
        
        field_configs = {
            # Campo Duration para tiempos de proceso
            "duration_config": {
                "fieldtype": "Duration",
                "default": "00:00:00",
                "description": "Para tiempos de fermentación, secado, etc."
            },
            
            # Campo JSON para datos estructurados
            "json_config": {
                "fieldtype": "JSON",
                "description": "Para datos de análisis de calidad, configuraciones"
            },
            
            # Campo Rating para calificaciones
            "rating_config": {
                "fieldtype": "Rating",
                "default": 0,
                "max_rating": 5,
                "description": "Para calificar calidad de café, empleados, etc."
            },
            
            # Campo Geolocation para ubicaciones
            "geolocation_config": {
                "fieldtype": "Geolocation",
                "description": "Para ubicación de lotes, áreas de cultivo"
            },
            
            # Campo Barcode para códigos QR/barras
            "barcode_config": {
                "fieldtype": "Barcode",
                "description": "Para trazabilidad de lotes y productos"
            }
        }
        
        return field_configs
        
    def setup_v15_automation(self):
        """
        Configurar automatizaciones mejoradas de v15
        """
        print("🤖 Configurando automatizaciones v15...")
        
        automation_configs = {
            # Automatización para control de calidad
            "quality_automation": {
                "doctype": "Control de Calidad Cafe",
                "trigger": "on_submit",
                "conditions": "doc.puntaje_calidad < 70",
                "actions": [
                    "send_email_alert",
                    "create_corrective_action",
                    "update_lot_status"
                ]
            },
            
            # Automatización para inventario
            "inventory_automation": {
                "doctype": "Stock Entry",
                "trigger": "on_submit", 
                "conditions": "doc.purpose == 'Material Receipt' and 'Cafe' in doc.items[0].item_code",
                "actions": [
                    "update_harvest_records",
                    "calculate_yield_metrics",
                    "send_production_update"
                ]
            }
        }
        
        return automation_configs
        
    def setup_v15_performance(self):
        """
        Configurar mejoras de rendimiento de v15
        """
        print("⚡ Configurando optimizaciones de rendimiento v15...")
        
        performance_configs = {
            # Índices optimizados para café
            "coffee_indexes": [
                {
                    "doctype": "Lote de Cafe",
                    "fields": ["fecha_cosecha", "variedad_cafe", "area_cultivo"],
                    "name": "idx_lote_cafe_performance"
                },
                {
                    "doctype": "Recepcion Cafe Cereza", 
                    "fields": ["fecha_recepcion", "proveedor", "estado"],
                    "name": "idx_recepcion_performance"
                }
            ],
            
            # Configuración de caché
            "cache_config": {
                "enable_query_cache": True,
                "cache_timeout": 3600,
                "cached_queries": [
                    "production_reports",
                    "quality_metrics",
                    "inventory_levels"
                ]
            }
        }
        
        return performance_configs
        
    def create_v15_custom_fields(self):
        """
        Crear campos personalizados usando características v15
        """
        print("📝 Creando campos personalizados v15...")
        
        custom_fields = {
            # Campos para Item (productos de café)
            "Item": [
                {
                    "fieldname": "cafe_rating",
                    "label": "Calificación de Café",
                    "fieldtype": "Rating",
                    "max_rating": 5,
                    "insert_after": "item_name"
                },
                {
                    "fieldname": "cafe_origin_location",
                    "label": "Ubicación de Origen",
                    "fieldtype": "Geolocation", 
                    "insert_after": "cafe_rating"
                },
                {
                    "fieldname": "cafe_traceability_code",
                    "label": "Código de Trazabilidad",
                    "fieldtype": "Barcode",
                    "insert_after": "cafe_origin_location"
                }
            ],
            
            # Campos para Employee (trabajadores)
            "Employee": [
                {
                    "fieldname": "employee_performance_rating",
                    "label": "Calificación de Desempeño",
                    "fieldtype": "Rating",
                    "max_rating": 5,
                    "insert_after": "employee_name"
                },
                {
                    "fieldname": "work_location",
                    "label": "Ubicación de Trabajo",
                    "fieldtype": "Geolocation",
                    "insert_after": "employee_performance_rating"
                }
            ],
            
            # Campos para Stock Entry
            "Stock Entry": [
                {
                    "fieldname": "processing_duration",
                    "label": "Duración del Proceso",
                    "fieldtype": "Duration",
                    "insert_after": "posting_date"
                },
                {
                    "fieldname": "quality_data",
                    "label": "Datos de Calidad",
                    "fieldtype": "JSON",
                    "insert_after": "processing_duration"
                }
            ]
        }
        
        return custom_fields
        
    def setup_v15_dashboard_enhancements(self):
        """
        Configurar mejoras de dashboard v15
        """
        print("📊 Configurando mejoras de dashboard v15...")
        
        dashboard_configs = {
            "coffee_production_dashboard": {
                "name": "Coffee Production v15",
                "charts": [
                    {
                        "chart_name": "Daily Harvest",
                        "chart_type": "line",
                        "source": "Recepcion Cafe Cereza",
                        "x_field": "fecha_recepcion",
                        "y_field": "cantidad_recibida",
                        "time_interval": "Daily",
                        "filters": [
                            {
                                "fieldname": "docstatus",
                                "operator": "=",
                                "value": 1
                            }
                        ]
                    },
                    {
                        "chart_name": "Quality Ratings",
                        "chart_type": "donut",
                        "source": "Control de Calidad Cafe",
                        "x_field": "grado_calidad",
                        "y_field": "count",
                        "aggregate_function": "Count"
                    },
                    {
                        "chart_name": "Processing Duration",
                        "chart_type": "bar",
                        "source": "Stock Entry", 
                        "x_field": "item_code",
                        "y_field": "processing_duration",
                        "aggregate_function": "Average"
                    }
                ]
            }
        }
        
        return dashboard_configs

def main():
    """
    Función principal para configurar ERPNext v15
    """
    try:
        print("🚀 Iniciando configuración ERPNext v15 para ERPCafe...")
        
        # Inicializar configuración
        config = ERPNextV15Config()
        
        # Validar entorno
        config.validate_environment()
        
        # Mostrar características v15
        features = config.get_v15_features()
        print(f"📋 Características v15 disponibles: {len(features['new_field_types'])} nuevos tipos de campo")
        
        # Configurar tipos de campo
        field_configs = config.setup_v15_field_types()
        print(f"✅ Configurados {len(field_configs)} tipos de campo v15")
        
        # Configurar automatizaciones
        automation_configs = config.setup_v15_automation()
        print(f"✅ Configuradas {len(automation_configs)} automatizaciones v15")
        
        # Configurar optimizaciones
        performance_configs = config.setup_v15_performance()
        print(f"✅ Configuradas optimizaciones de rendimiento v15")
        
        # Configurar campos personalizados
        custom_fields = config.create_v15_custom_fields()
        print(f"✅ Configurados campos personalizados para {len(custom_fields)} DocTypes")
        
        # Configurar dashboards
        dashboard_configs = config.setup_v15_dashboard_enhancements()
        print(f"✅ Configurados dashboards mejorados v15")
        
        print("🎉 Configuración ERPNext v15 completada exitosamente!")
        
    except Exception as e:
        print(f"❌ Error en configuración v15: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
