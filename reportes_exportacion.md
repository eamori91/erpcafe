# 📊 Reportes Avanzados para Exportación Internacional

## 🎯 OBJETIVO

Sistema completo de reportes automatizados para cumplir con requisitos internacionales de exportación de café guatemalteco, incluyendo documentación VUPE, certificados fitosanitarios, reportes de trazabilidad y documentos para mercados específicos.

## 📋 ARQUITECTURA DE REPORTES

### Motor de Reportes Dinámicos
```python
# export_reports_engine.py
import frappe
from frappe.utils import flt, get_datetime, now_datetime, cstr
import pandas as pd
from datetime import datetime, timedelta
import json

class ExportReportsEngine:
    """
    Motor principal para generación de reportes de exportación
    """
    
    def __init__(self):
        self.company = frappe.defaults.get_user_default("Company")
        self.fiscal_year = frappe.defaults.get_user_default("fiscal_year")
        self.templates_path = "/assets/report_templates/"
    
    def generate_export_package(self, lote_ids, destino_pais, tipo_mercado="Specialty"):
        """
        Generar paquete completo de documentos para exportación
        
        Args:
            lote_ids: Lista de IDs de lotes para exportar
            destino_pais: País de destino (USA, Germany, Japan, etc.)
            tipo_mercado: Tipo de mercado (Specialty, Commodity, Organic)
        """
        
        # Validar lotes y calcular totales
        lotes_data = self.validate_and_prepare_lotes(lote_ids)
        
        # Generar documentos según destino
        documentos = {
            'VUPE': self.generar_vupe(lotes_data),
            'Certificado_Fitosanitario': self.generar_certificado_fitosanitario(lotes_data, destino_pais),
            'Factura_Comercial': self.generar_factura_comercial(lotes_data, destino_pais),
            'Packing_List': self.generar_packing_list(lotes_data),
            'Certificado_Origen': self.generar_certificado_origen(lotes_data),
            'Trazabilidad_Completa': self.generar_reporte_trazabilidad(lotes_data),
            'Analisis_Calidad': self.generar_analisis_calidad(lotes_data),
            'FAUCA_Consolidado': self.generar_fauca_consolidado(lotes_data)
        }
        
        # Documentos específicos por mercado
        if tipo_mercado == "Organic":
            documentos['Certificado_Organico'] = self.generar_certificado_organico(lotes_data)
        
        if tipo_mercado == "Specialty":
            documentos['Reporte_Catacion'] = self.generar_reporte_catacion(lotes_data)
            documentos['Historia_Productor'] = self.generar_historia_productor(lotes_data)
        
        # Documentos específicos por país
        if destino_pais == "USA":
            documentos['FDA_Prior_Notice'] = self.generar_fda_prior_notice(lotes_data)
        elif destino_pais == "Germany" or destino_pais in ["Netherlands", "Belgium", "France"]:
            documentos['EU_Health_Certificate'] = self.generar_eu_health_certificate(lotes_data)
        elif destino_pais == "Japan":
            documentos['Japan_Import_Notification'] = self.generar_japan_notification(lotes_data)
        
        # Crear ZIP con todos los documentos
        zip_file = self.create_export_package_zip(documentos, lotes_data)
        
        return {
            'export_package_id': self.create_export_record(lotes_data, documentos),
            'zip_file': zip_file,
            'documentos_generados': list(documentos.keys()),
            'resumen': self.get_export_summary(lotes_data)
        }
    
    def validate_and_prepare_lotes(self, lote_ids):
        """
        Validar y preparar datos de lotes para exportación
        """
        lotes = []
        
        for lote_id in lote_ids:
            lote = frappe.get_doc("Lote Cafe", lote_id)
            
            # Validaciones
            if lote.estado_lote != "Listo para Exportación":
                frappe.throw(f"Lote {lote_id} no está listo para exportación")
            
            if not lote.puntaje_catacion or lote.puntaje_catacion < 80:
                frappe.msgprint(f"Advertencia: Lote {lote_id} tiene puntaje bajo ({lote.puntaje_catacion})")
            
            # Preparar datos enriquecidos
            lote_data = {
                'doc': lote,
                'trazabilidad': self.get_detailed_traceability(lote),
                'calidad': self.get_quality_analysis(lote),
                'contribuciones': self.calculate_all_contributions(lote),
                'certificaciones': self.get_all_certifications(lote)
            }
            
            lotes.append(lote_data)
        
        return lotes
```

## 📄 GENERADORES DE DOCUMENTOS ESPECÍFICOS

### 1. VUPE (Volumen Único de Productos Exportables)
```python
def generar_vupe(self, lotes_data):
    """
    Generar documento VUPE para BANGUAT
    """
    
    # Calcular totales
    total_quintales = sum(lote['doc'].cantidad_quintales for lote in lotes_data)
    total_valor_fob = sum(lote['doc'].cantidad_quintales * lote['doc'].precio_base_qq for lote in lotes_data)
    
    vupe_data = {
        'numero_vupe': self.get_next_vupe_number(),
        'fecha_emision': now_datetime().date(),
        'exportador': {
            'razon_social': frappe.db.get_single_value('Company', 'company_name'),
            'nit': frappe.db.get_single_value('Company', 'tax_id'),
            'direccion': frappe.db.get_single_value('Company', 'address_line1'),
            'telefono': frappe.db.get_single_value('Company', 'phone_no'),
            'licencia_anacafe': frappe.conf.get('anacafe_licencia')
        },
        'producto': {
            'descripcion': 'CAFE ORO EN GRANO',
            'clasificacion_arancelaria': '0901.11.00',
            'total_quintales': total_quintales,
            'total_kg': total_quintales * 46,
            'valor_fob_usd': total_valor_fob / 7.8,  # Conversión aproximada
            'precio_promedio_qq': total_valor_fob / total_quintales
        },
        'lotes_detalle': [],
        'resumen_calidad': self.get_quality_summary(lotes_data),
        'contribuciones_pagadas': sum(lote['contribuciones']['total'] for lote in lotes_data)
    }
    
    # Detalle por lote
    for lote in lotes_data:
        vupe_data['lotes_detalle'].append({
            'codigo_anacafe': lote['doc'].codigo_anacafe,
            'cantidad_qq': lote['doc'].cantidad_quintales,
            'region': lote['doc'].region_origen,
            'variedad': lote['doc'].variedad_cafe,
            'calidad': lote['doc'].clasificacion_calidad,
            'humedad': lote['doc'].humedad_porcentaje,
            'puntaje': lote['doc'].puntaje_catacion
        })
    
    # Generar PDF del VUPE
    html_content = self.render_vupe_template(vupe_data)
    pdf_file = self.generate_pdf(html_content, f"VUPE-{vupe_data['numero_vupe']}")
    
    return {
        'file': pdf_file,
        'data': vupe_data,
        'tipo': 'VUPE'
    }

def render_vupe_template(self, data):
    """
    Template HTML para documento VUPE
    """
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>VUPE - {{ data.numero_vupe }}</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 30px; font-size: 11px; }
            .header { text-align: center; margin-bottom: 20px; border: 2px solid #000; padding: 10px; }
            .section { margin: 15px 0; }
            .table { width: 100%; border-collapse: collapse; margin: 10px 0; }
            .table th, .table td { border: 1px solid #333; padding: 5px; text-align: left; font-size: 10px; }
            .table th { background-color: #f0f0f0; font-weight: bold; }
            .total-row { background-color: #e6f2ff; font-weight: bold; }
            .firma-section { margin-top: 40px; }
        </style>
    </head>
    <body>
        <div class="header">
            <h2>BANCO DE GUATEMALA</h2>
            <h3>VOLUMEN ÚNICO DE PRODUCTOS EXPORTABLES (VUPE)</h3>
            <h3>{{ data.numero_vupe }}</h3>
            <p><strong>Fecha:</strong> {{ data.fecha_emision.strftime('%d/%m/%Y') }}</p>
        </div>
        
        <div class="section">
            <h4>DATOS DEL EXPORTADOR</h4>
            <table class="table">
                <tr><td width="25%"><strong>Razón Social:</strong></td><td>{{ data.exportador.razon_social }}</td></tr>
                <tr><td><strong>NIT:</strong></td><td>{{ data.exportador.nit }}</td></tr>
                <tr><td><strong>Dirección:</strong></td><td>{{ data.exportador.direccion }}</td></tr>
                <tr><td><strong>Teléfono:</strong></td><td>{{ data.exportador.telefono }}</td></tr>
                <tr><td><strong>Licencia ANACAFE:</strong></td><td>{{ data.exportador.licencia_anacafe }}</td></tr>
            </table>
        </div>
        
        <div class="section">
            <h4>INFORMACIÓN DEL PRODUCTO</h4>
            <table class="table">
                <tr><td width="30%"><strong>Descripción:</strong></td><td>{{ data.producto.descripcion }}</td></tr>
                <tr><td><strong>Clasificación Arancelaria:</strong></td><td>{{ data.producto.clasificacion_arancelaria }}</td></tr>
                <tr><td><strong>Cantidad Total:</strong></td><td>{{ data.producto.total_quintales }} quintales ({{ data.producto.total_kg }} kg)</td></tr>
                <tr><td><strong>Valor FOB:</strong></td><td>USD {{ "%.2f"|format(data.producto.valor_fob_usd) }}</td></tr>
                <tr><td><strong>Precio Promedio:</strong></td><td>Q {{ "%.2f"|format(data.producto.precio_promedio_qq) }} por quintal</td></tr>
            </table>
        </div>
        
        <div class="section">
            <h4>DETALLE POR LOTES</h4>
            <table class="table">
                <thead>
                    <tr>
                        <th>Código ANACAFE</th>
                        <th>Cantidad (qq)</th>
                        <th>Región</th>
                        <th>Variedad</th>
                        <th>Calidad</th>
                        <th>Humedad %</th>
                        <th>Puntaje</th>
                    </tr>
                </thead>
                <tbody>
                    {% for lote in data.lotes_detalle %}
                    <tr>
                        <td>{{ lote.codigo_anacafe }}</td>
                        <td>{{ lote.cantidad_qq }}</td>
                        <td>{{ lote.region }}</td>
                        <td>{{ lote.variedad }}</td>
                        <td>{{ lote.calidad }}</td>
                        <td>{{ lote.humedad }}%</td>
                        <td>{{ lote.puntaje }}</td>
                    </tr>
                    {% endfor %}
                    <tr class="total-row">
                        <td><strong>TOTAL</strong></td>
                        <td><strong>{{ data.producto.total_quintales }}</strong></td>
                        <td colspan="5"></td>
                    </tr>
                </tbody>
            </table>
        </div>
        
        <div class="section">
            <h4>CONTRIBUCIONES PAGADAS</h4>
            <table class="table">
                <tr><td width="30%"><strong>Total Contribuciones ANACAFE:</strong></td><td>Q {{ "%.2f"|format(data.contribuciones_pagadas) }}</td></tr>
            </table>
        </div>
        
        <div class="firma-section">
            <table width="100%">
                <tr>
                    <td width="50%">
                        <br><br><br>
                        <p>_________________________________</p>
                        <p><strong>Firma del Exportador</strong></p>
                        <p>{{ data.exportador.razon_social }}</p>
                    </td>
                    <td width="50%">
                        <br><br><br>
                        <p>_________________________________</p>
                        <p><strong>Sello de la Empresa</strong></p>
                    </td>
                </tr>
            </table>
        </div>
    </body>
    </html>
    """
    
    from jinja2 import Template
    template_obj = Template(template)
    return template_obj.render(data=data)
```

### 2. Certificado Fitosanitario
```python
def generar_certificado_fitosanitario(self, lotes_data, destino_pais):
    """
    Generar Certificado Fitosanitario para MAGA
    """
    
    certificado_data = {
        'numero_certificado': self.get_next_fitosanitario_number(),
        'fecha_emision': now_datetime().date(),
        'destino': {
            'pais': destino_pais,
            'puerto_entrada': self.get_puerto_entrada(destino_pais),
            'codigo_pais': self.get_country_code(destino_pais)
        },
        'exportador': {
            'nombre': frappe.db.get_single_value('Company', 'company_name'),
            'direccion': frappe.db.get_single_value('Company', 'address_line1'),
            'codigo_exportador': frappe.conf.get('maga_codigo_exportador')
        },
        'producto': {
            'nombre_cientifico': 'Coffea arabica L.',
            'nombre_comun': 'Café en grano oro',
            'descripcion': 'Granos de café pergamino seco, procesado húmedo',
            'cantidad_total': sum(lote['doc'].cantidad_quintales for lote in lotes_data),
            'peso_neto': sum(lote['doc'].peso_kg for lote in lotes_data),
            'origen': 'Guatemala - Regiones cafetaleras certificadas'
        },
        'inspecciones': self.get_inspection_data(lotes_data),
        'declaracion_fitosanitaria': {
            'libre_plagas': True,
            'cumple_requisitos': True,
            'tratamientos_aplicados': self.get_treatments_applied(lotes_data),
            'inspector_maga': frappe.conf.get('maga_inspector_certificado')
        },
        'lotes_incluidos': [lote['doc'].codigo_anacafe for lote in lotes_data]
    }
    
    # Generar PDF del certificado
    html_content = self.render_fitosanitario_template(certificado_data)
    pdf_file = self.generate_pdf(html_content, f"Fitosanitario-{certificado_data['numero_certificado']}")
    
    return {
        'file': pdf_file,
        'data': certificado_data,
        'tipo': 'Certificado_Fitosanitario'
    }

def get_inspection_data(self, lotes_data):
    """
    Obtener datos de inspecciones realizadas
    """
    inspecciones = []
    
    for lote in lotes_data:
        # Buscar registros de inspección de calidad
        inspecciones_lote = frappe.db.sql("""
            SELECT fecha, inspector, resultado, observaciones
            FROM `tabInspeccion Calidad`
            WHERE lote_cafe = %s
            ORDER BY fecha DESC
            LIMIT 1
        """, (lote['doc'].name,), as_dict=True)
        
        if inspecciones_lote:
            inspecciones.append({
                'lote': lote['doc'].codigo_anacafe,
                'fecha_inspeccion': inspecciones_lote[0].fecha,
                'inspector': inspecciones_lote[0].inspector,
                'resultado': inspecciones_lote[0].resultado,
                'observaciones': inspecciones_lote[0].observaciones
            })
    
    return inspecciones

def get_treatments_applied(self, lotes_data):
    """
    Obtener tratamientos fitosanitarios aplicados
    """
    tratamientos = [
        "Almacenamiento en ambiente controlado",
        "Control de humedad < 12.5%",
        "Inspección visual de granos",
        "Control de temperatura de almacenamiento"
    ]
    
    # Verificar si hay tratamientos orgánicos
    for lote in lotes_data:
        if lote['doc'].organico:
            tratamientos.append("Procesamiento orgánico certificado")
            break
    
    return tratamientos
```

### 3. Reporte de Trazabilidad Completa
```python
def generar_reporte_trazabilidad(self, lotes_data):
    """
    Generar reporte completo de trazabilidad
    """
    
    trazabilidad_data = {
        'reporte_id': f"TRAZ-{now_datetime().strftime('%Y%m%d%H%M')}",
        'fecha_generacion': now_datetime(),
        'lotes_incluidos': len(lotes_data),
        'cadena_custodia': [],
        'actividades_campo': [],
        'procesamiento': [],
        'almacenamiento': [],
        'calidad_controles': [],
        'empleados_involucrados': set(),
        'equipos_utilizados': set()
    }
    
    for lote in lotes_data:
        # Cadena de custodia del lote
        cadena = self.build_custody_chain(lote)
        trazabilidad_data['cadena_custodia'].append(cadena)
        
        # Actividades de campo
        actividades = self.get_field_activities_detail(lote)
        trazabilidad_data['actividades_campo'].extend(actividades)
        
        # Procesamiento
        procesamiento = self.get_processing_steps(lote)
        trazabilidad_data['procesamiento'].extend(procesamiento)
        
        # Controles de calidad
        controles = self.get_quality_controls(lote)
        trazabilidad_data['calidad_controles'].extend(controles)
        
        # Empleados y equipos
        empleados, equipos = self.get_resources_used(lote)
        trazabilidad_data['empleados_involucrados'].update(empleados)
        trazabilidad_data['equipos_utilizados'].update(equipos)
    
    # Convertir sets a listas para serialización
    trazabilidad_data['empleados_involucrados'] = list(trazabilidad_data['empleados_involucrados'])
    trazabilidad_data['equipos_utilizados'] = list(trazabilidad_data['equipos_utilizados'])
    
    # Generar reporte Excel detallado
    excel_file = self.generate_traceability_excel(trazabilidad_data)
    
    # Generar PDF resumen
    pdf_file = self.generate_traceability_pdf(trazabilidad_data)
    
    return {
        'excel_file': excel_file,
        'pdf_file': pdf_file,
        'data': trazabilidad_data,
        'tipo': 'Trazabilidad_Completa'
    }

def build_custody_chain(self, lote):
    """
    Construir cadena de custodia completa del lote
    """
    cadena = {
        'lote_id': lote['doc'].codigo_anacafe,
        'etapas': []
    }
    
    # Etapa 1: Cultivo y Cosecha
    etapas_cultivo = frappe.db.sql("""
        SELECT ac.fecha, ac.empleado, ut.nombre as cuerda, ac.tipo_trabajo, ac.cantidad_jornal
        FROM `tabActividad de Campo` ac
        JOIN `tabUnidad de Trabajo` ut ON ac.unidad_trabajo = ut.name
        WHERE ut.name IN (
            SELECT DISTINCT unidad_trabajo 
            FROM `tabLote Cafe Actividad` 
            WHERE parent = %s
        )
        ORDER BY ac.fecha
    """, (lote['doc'].name,), as_dict=True)
    
    for etapa in etapas_cultivo:
        cadena['etapas'].append({
            'fase': 'Cultivo y Cosecha',
            'fecha': etapa.fecha,
            'responsable': etapa.empleado,
            'ubicacion': etapa.cuerda,
            'actividad': etapa.tipo_trabajo,
            'detalle': f"Jornales: {etapa.cantidad_jornal}"
        })
    
    # Etapa 2: Beneficiado Húmedo
    if frappe.db.exists("Fermentacion", {"lote_cafe": lote['doc'].name}):
        fermentacion = frappe.get_doc("Fermentacion", {"lote_cafe": lote['doc'].name})
        cadena['etapas'].append({
            'fase': 'Fermentación',
            'fecha': fermentacion.fecha_inicio,
            'responsable': fermentacion.responsable_proceso,
            'ubicacion': 'Tanques de Fermentación',
            'actividad': 'Fermentación Controlada',
            'detalle': f"Tiempo: {fermentacion.tiempo_fermentacion_horas}h, pH: {fermentacion.ph_final}"
        })
    
    # Etapa 3: Secado
    secado_records = frappe.db.sql("""
        SELECT fecha_inicio, fecha_fin, responsable_secado, tipo_secado, humedad_inicial, humedad_final
        FROM `tabPatio Secado`
        WHERE lote_cafe = %s
        UNION ALL
        SELECT fecha_inicio, fecha_fin, operador as responsable_secado, 'Secadora Mecánica' as tipo_secado, 
               humedad_inicial, humedad_final
        FROM `tabSecadora`
        WHERE lote_cafe = %s
        ORDER BY fecha_inicio
    """, (lote['doc'].name, lote['doc'].name), as_dict=True)
    
    for secado in secado_records:
        cadena['etapas'].append({
            'fase': 'Secado',
            'fecha': secado.fecha_inicio,
            'responsable': secado.responsable_secado,
            'ubicacion': 'Área de Secado',
            'actividad': secado.tipo_secado,
            'detalle': f"Humedad: {secado.humedad_inicial}% → {secado.humedad_final}%"
        })
    
    # Etapa 4: Almacenamiento
    cadena['etapas'].append({
        'fase': 'Almacenamiento',
        'fecha': lote['doc'].fecha_creacion,
        'responsable': 'Bodeguero Principal',
        'ubicacion': 'Bodega de Café Oro',
        'actividad': 'Almacenamiento Controlado',
        'detalle': f"Humedad final: {lote['doc'].humedad_porcentaje}%"
    })
    
    return cadena
```

### 4. Documentos Específicos por País

#### FDA Prior Notice (USA)
```python
def generar_fda_prior_notice(self, lotes_data):
    """
    Generar FDA Prior Notice para exportaciones a USA
    """
    
    fda_data = {
        'submission_id': f"FDA-{now_datetime().strftime('%Y%m%d%H%M%S')}",
        'arrival_date': (now_datetime() + timedelta(days=14)).date(),
        'arrival_time': '08:00',
        'port_of_arrival': 'New York, NY',
        'transmitter': {
            'name': frappe.db.get_single_value('Company', 'company_name'),
            'fda_registration': frappe.conf.get('fda_registration_number'),
            'address': frappe.db.get_single_value('Company', 'address_line1'),
            'country': 'Guatemala',
            'phone': frappe.db.get_single_value('Company', 'phone_no')
        },
        'manufacturer': {
            'name': frappe.db.get_single_value('Company', 'company_name'),
            'fda_registration': frappe.conf.get('fda_food_facility_number'),
            'address': frappe.db.get_single_value('Company', 'address_line1'),
            'country': 'Guatemala'
        },
        'product_info': {
            'product_description': 'Green Coffee Beans (Washed Arabica)',
            'fda_product_code': 'Coffee, Green Beans',
            'food_category': 'Coffee and Tea',
            'quantity': sum(lote['doc'].peso_kg for lote in lotes_data),
            'unit': 'KG',
            'lot_numbers': [lote['doc'].codigo_anacafe for lote in lotes_data]
        },
        'shipper': {
            'name': 'Coffee Export Guatemala S.A.',
            'address': 'Guatemala City, Guatemala',
            'country': 'Guatemala'
        }
    }
    
    # Generar archivo JSON para FDA
    json_file = self.generate_fda_json(fda_data)
    
    # Generar PDF de respaldo
    pdf_file = self.generate_fda_pdf(fda_data)
    
    return {
        'json_file': json_file,
        'pdf_file': pdf_file,
        'data': fda_data,
        'tipo': 'FDA_Prior_Notice'
    }
```

#### EU Health Certificate
```python
def generar_eu_health_certificate(self, lotes_data):
    """
    Generar Certificado de Salud para Unión Europea
    """
    
    eu_cert_data = {
        'certificate_number': f"EU-{now_datetime().strftime('%Y')}-GT-{now_datetime().strftime('%m%d%H%M')}",
        'issue_date': now_datetime().date(),
        'competent_authority': 'Ministerio de Agricultura, Ganadería y Alimentación (MAGA)',
        'official_veterinarian': frappe.conf.get('maga_veterinario_oficial'),
        'exporter': {
            'name': frappe.db.get_single_value('Company', 'company_name'),
            'address': frappe.db.get_single_value('Company', 'address_line1'),
            'approval_number': frappe.conf.get('eu_approval_number'),
            'authorization_date': frappe.conf.get('eu_authorization_date')
        },
        'destination': {
            'country': 'European Union',
            'establishment': 'Coffee Import Facility',
            'border_inspection_post': 'Hamburg, Germany'
        },
        'product_details': {
            'description': 'Green Coffee Beans (Coffea arabica)',
            'nature_packaging': 'Jute Sacks - 60kg each',
            'number_packages': len(lotes_data),
            'net_weight': sum(lote['doc'].peso_kg for lote in lotes_data),
            'identification_marks': [lote['doc'].codigo_anacafe for lote in lotes_data]
        },
        'health_attestation': {
            'origin_statement': True,
            'health_certificate': True,
            'residue_monitoring': True,
            'haccp_compliance': True,
            'contaminant_levels': self.get_contaminant_analysis(lotes_data)
        }
    }
    
    # Generar PDF del certificado
    html_content = self.render_eu_certificate_template(eu_cert_data)
    pdf_file = self.generate_pdf(html_content, f"EU-Health-Cert-{eu_cert_data['certificate_number']}")
    
    return {
        'file': pdf_file,
        'data': eu_cert_data,
        'tipo': 'EU_Health_Certificate'
    }
```

## 📊 DASHBOARD DE EXPORTACIONES

### Panel de Control para Exportaciones
```python
def create_export_dashboard():
    """
    Crear dashboard especializado para exportaciones
    """
    
    dashboard_config = {
        'name': 'Export Control Dashboard',
        'charts': [
            {
                'chart_name': 'Exportaciones por País',
                'chart_type': 'donut',
                'data_source': 'Custom',
                'custom_options': {
                    'type': 'donut',
                    'height': 300,
                    'colors': ['#7cd6fd', '#5e64ff', '#743ee2', '#ff5858', '#ffa00a']
                }
            },
            {
                'chart_name': 'Volumen Mensual de Exportación',
                'chart_type': 'line',
                'data_source': 'Custom',
                'custom_options': {
                    'type': 'line',
                    'height': 300,
                    'colors': ['#7cd6fd']
                }
            },
            {
                'chart_name': 'Calidad Promedio por Región',
                'chart_type': 'bar',
                'data_source': 'Custom',
                'custom_options': {
                    'type': 'bar',
                    'height': 300,
                    'colors': ['#5e64ff']
                }
            }
        ],
        'cards': [
            {
                'card_name': 'Total Exportado (Año Actual)',
                'source_type': 'Custom',
                'function_name': 'get_yearly_export_total'
            },
            {
                'card_name': 'Contribuciones ANACAFE Pagadas',
                'source_type': 'Custom',
                'function_name': 'get_anacafe_contributions_paid'
            },
            {
                'card_name': 'Certificados Vigentes',
                'source_type': 'Custom',
                'function_name': 'get_active_certificates'
            },
            {
                'card_name': 'Próximos Vencimientos',
                'source_type': 'Custom',
                'function_name': 'get_upcoming_expirations'
            }
        ]
    }
    
    return dashboard_config

# Funciones para los cards del dashboard
@frappe.whitelist()
def get_yearly_export_total():
    current_year = datetime.now().year
    
    total = frappe.db.sql("""
        SELECT SUM(cantidad_quintales) as total_qq
        FROM `tabLote Cafe`
        WHERE estado_lote = 'Exportado'
        AND YEAR(fecha_creacion) = %s
    """, (current_year,), as_dict=True)
    
    return {
        'value': total[0].total_qq or 0,
        'description': f'Quintales exportados en {current_year}'
    }

@frappe.whitelist()
def get_anacafe_contributions_paid():
    current_year = datetime.now().year
    
    total = frappe.db.sql("""
        SELECT SUM(contribucion_anacafe + contribucion_municipal) as total_contrib
        FROM `tabLote Cafe`
        WHERE estado_lote = 'Exportado'
        AND YEAR(fecha_creacion) = %s
    """, (current_year,), as_dict=True)
    
    return {
        'value': f"Q{total[0].total_contrib or 0:.2f}",
        'description': 'Contribuciones pagadas este año'
    }
```

## 🔄 AUTOMATIZACIÓN DE REPORTES

### Scheduler para Reportes Automáticos
```python
# scheduler_events.py
from frappe import _

def daily():
    """Tareas diarias de exportación"""
    
    # Verificar licencias próximas a vencer
    check_expiring_licenses()
    
    # Actualizar precios de referencia ANACAFE
    update_anacafe_reference_prices()
    
    # Generar reportes automáticos si hay exportaciones programadas
    generate_scheduled_export_reports()

def check_expiring_licenses():
    """
    Verificar licencias que vencen en los próximos 30 días
    """
    from datetime import datetime, timedelta
    
    expiry_date = datetime.now().date() + timedelta(days=30)
    
    expiring_licenses = frappe.db.sql("""
        SELECT numero_licencia, fecha_vencimiento, tipo_licencia
        FROM `tabLicencia ANACAFE`
        WHERE fecha_vencimiento <= %s
        AND estado = 'Vigente'
    """, (expiry_date,), as_dict=True)
    
    if expiring_licenses:
        # Enviar notificación por email
        recipients = ['administracion@finca.com', 'exportaciones@finca.com']
        
        message = "Las siguientes licencias vencen pronto:\n\n"
        for license in expiring_licenses:
            message += f"- {license.numero_licencia} ({license.tipo_licencia}): {license.fecha_vencimiento}\n"
        
        frappe.sendmail(
            recipients=recipients,
            subject='⚠️ Licencias ANACAFE próximas a vencer',
            message=message
        )

def generate_scheduled_export_reports():
    """
    Generar reportes para exportaciones programadas
    """
    
    # Buscar lotes listos para exportación que tengan fecha programada
    lotes_programados = frappe.db.sql("""
        SELECT name, codigo_anacafe, fecha_exportacion_programada
        FROM `tabLote Cafe`
        WHERE estado_lote = 'Listo para Exportación'
        AND fecha_exportacion_programada = CURDATE()
    """, as_dict=True)
    
    if lotes_programados:
        for lote in lotes_programados:
            # Generar paquete de documentos automáticamente
            export_engine = ExportReportsEngine()
            try:
                package = export_engine.generate_export_package(
                    lote_ids=[lote.name],
                    destino_pais='USA',  # Por defecto, debería ser configurable
                    tipo_mercado='Specialty'
                )
                
                # Notificar que los documentos están listos
                frappe.sendmail(
                    recipients=['exportaciones@finca.com'],
                    subject=f'📄 Documentos listos: {lote.codigo_anacafe}',
                    message=f'Los documentos de exportación para el lote {lote.codigo_anacafe} han sido generados automáticamente.',
                    attachments=[package['zip_file']]
                )
                
            except Exception as e:
                frappe.log_error(f"Error generando documentos para lote {lote.name}: {str(e)}")
```

Este sistema completo de reportes para exportación automatiza toda la documentación requerida para el comercio internacional de café guatemalteco, cumpliendo con los estándares de ANACAFE, MAGA, FDA, Unión Europea y otros mercados internacionales.
