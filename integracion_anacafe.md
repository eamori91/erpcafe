# 🏛️ Integración Completa con ANACAFE

## 🎯 OBJETIVO

Automatizar completamente el cumplimiento de los requisitos ANACAFE para:
- Licencias de exportación
- Contribuciones obligatorias por quintal
- Documentación FAUCA
- Trazabilidad para certificaciones
- Reportes automáticos al sistema ANACAFE

## 📋 ARQUITECTURA DE INTEGRACIÓN

### Sistema de Documentos ANACAFE en ERPNext
```python
# anacafe_integration.py
import frappe
from frappe.model.document import Document
from frappe.utils import flt, get_datetime, now_datetime

class ANACAFEIntegration:
    """
    Clase principal para manejo de integración ANACAFE
    """
    
    def __init__(self):
        self.base_url = frappe.conf.get('anacafe_api_url', 'https://api.anacafe.org')
        self.api_key = frappe.conf.get('anacafe_api_key')
        self.licencia_exportador = frappe.conf.get('anacafe_licencia')
    
    def calcular_contribuciones(self, quintales_cafe):
        """
        Calcular contribuciones obligatorias por quintal exportado
        """
        contribuciones = {
            'anacafe_q1_00': quintales_cafe * 1.00,  # Q1.00 por quintal
            'municipalidades_q0_15': quintales_cafe * 0.15,  # Q0.15 por quintal
            'total': quintales_cafe * 1.15
        }
        
        return contribuciones
    
    def generar_codigo_lote_anacafe(self, lote_interno):
        """
        Generar código de lote compatible con ANACAFE
        Formato: GT-YYYY-FFFF-LLLL
        GT = Guatemala
        YYYY = Año
        FFFF = Código de finca (4 dígitos)
        LLLL = Número de lote secuencial
        """
        year = now_datetime().year
        finca_code = frappe.conf.get('anacafe_codigo_finca', '0001')
        
        # Obtener último número de lote del año
        ultimo_lote = frappe.db.sql("""
            SELECT MAX(CAST(SUBSTRING(codigo_anacafe, -4) AS UNSIGNED)) as max_lote
            FROM `tabLote Cafe`
            WHERE YEAR(fecha_creacion) = %s
            AND codigo_anacafe LIKE 'GT-%s-%s-%%'
        """, (year, year, finca_code))
        
        nuevo_numero = (ultimo_lote[0][0] or 0) + 1
        codigo_anacafe = f"GT-{year}-{finca_code}-{nuevo_numero:04d}"
        
        return codigo_anacafe
```

## 🗃️ DOCTYPES ESPECÍFICOS ANACAFE

### 1. Licencia ANACAFE
```python
def create_licencia_anacafe_doctype():
    """
    DocType para gestionar licencias ANACAFE
    """
    
    if frappe.db.exists("DocType", "Licencia ANACAFE"):
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Licencia ANACAFE",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "By fieldname",
        "autoname": "field:numero_licencia",
        "fields": [
            {
                "fieldname": "informacion_licencia",
                "label": "Información de la Licencia",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "numero_licencia",
                "label": "Número de Licencia",
                "fieldtype": "Data",
                "reqd": 1,
                "in_list_view": 1,
                "description": "Número asignado por ANACAFE"
            },
            {
                "fieldname": "tipo_licencia",
                "label": "Tipo de Licencia",
                "fieldtype": "Select",
                "options": "Productor-Exportador\nComprador-Exportador\nComprador-Exportador Tostado",
                "reqd": 1,
                "in_list_view": 1
            },
            {
                "fieldname": "licencia_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "fecha_emision",
                "label": "Fecha de Emisión",
                "fieldtype": "Date",
                "reqd": 1
            },
            {
                "fieldname": "fecha_vencimiento",
                "label": "Fecha de Vencimiento",
                "fieldtype": "Date",
                "reqd": 1
            },
            {
                "fieldname": "estado",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "Vigente\nPor Vencer\nVencida\nSuspendida",
                "default": "Vigente",
                "in_list_view": 1
            },
            {
                "fieldname": "titular_sec",
                "label": "Datos del Titular",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "razon_social",
                "label": "Razón Social",
                "fieldtype": "Data",
                "reqd": 1
            },
            {
                "fieldname": "nit",
                "label": "NIT",
                "fieldtype": "Data",
                "reqd": 1
            },
            {
                "fieldname": "titular_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "representante_legal",
                "label": "Representante Legal",
                "fieldtype": "Data"
            },
            {
                "fieldname": "direccion",
                "label": "Dirección",
                "fieldtype": "Small Text"
            },
            {
                "fieldname": "operaciones_sec",
                "label": "Operaciones Permitidas",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "puede_comprar",
                "label": "Puede Comprar",
                "fieldtype": "Check",
                "default": 0
            },
            {
                "fieldname": "puede_exportar",
                "label": "Puede Exportar",
                "fieldtype": "Check",
                "default": 1
            },
            {
                "fieldname": "operaciones_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "puede_procesar",
                "label": "Puede Procesar (Tostar)",
                "fieldtype": "Check",
                "default": 0
            },
            {
                "fieldname": "volumen_maximo",
                "label": "Volumen Máximo (qq/año)",
                "fieldtype": "Float",
                "description": "Límite de quintales por año si aplica"
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
    print("✅ DocType 'Licencia ANACAFE' creado")
```

### 2. Lote de Café para Exportación
```python
def create_lote_cafe_doctype():
    """
    DocType para lotes de café con códigos ANACAFE
    """
    
    if frappe.db.exists("DocType", "Lote Cafe"):
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Lote Cafe",
        "module": "Custom",
        "custom": 1,
        "naming_rule": "By fieldname",
        "autoname": "field:codigo_anacafe",
        "title_field": "codigo_anacafe",
        "fields": [
            {
                "fieldname": "identificacion_sec",
                "label": "Identificación del Lote",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "codigo_anacafe",
                "label": "Código ANACAFE",
                "fieldtype": "Data",
                "reqd": 1,
                "in_list_view": 1,
                "description": "Formato: GT-YYYY-FFFF-LLLL"
            },
            {
                "fieldname": "codigo_interno",
                "label": "Código Interno",
                "fieldtype": "Data",
                "description": "Referencia interna de la finca"
            },
            {
                "fieldname": "identificacion_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "fecha_creacion",
                "label": "Fecha de Creación",
                "fieldtype": "Date",
                "reqd": 1,
                "default": "Today"
            },
            {
                "fieldname": "estado_lote",
                "label": "Estado",
                "fieldtype": "Select",
                "options": "En Formación\nCompleto\nEn Proceso\nListo para Exportación\nExportado",
                "default": "En Formación",
                "in_list_view": 1
            },
            {
                "fieldname": "produccion_sec",
                "label": "Información de Producción",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "region_origen",
                "label": "Región de Origen",
                "fieldtype": "Select",
                "options": "Antigua\nAtitlán\nCobán\nFraijanes\nHuehuetenango\nNuevo Oriente\nSan Marcos\nAcatenango",
                "reqd": 1
            },
            {
                "fieldname": "finca_origen",
                "label": "Finca de Origen",
                "fieldtype": "Data",
                "reqd": 1
            },
            {
                "fieldname": "produccion_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "variedad_cafe",
                "label": "Variedad Principal",
                "fieldtype": "Select",
                "options": "Typica\nBourbon\nCaturra\nCatuaí\nAnacafé 14\nPache\nVilla Sarchí\nMezcla",
                "reqd": 1
            },
            {
                "fieldname": "altitud_cultivo",
                "label": "Altitud de Cultivo (msnm)",
                "fieldtype": "Int",
                "reqd": 1
            },
            {
                "fieldname": "cantidad_sec",
                "label": "Cantidad y Calidad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "cantidad_quintales",
                "label": "Cantidad (Quintales)",
                "fieldtype": "Float",
                "reqd": 1,
                "in_list_view": 1,
                "precision": 2
            },
            {
                "fieldname": "peso_kg",
                "label": "Peso (Kg)",
                "fieldtype": "Float",
                "read_only": 1,
                "description": "Cálculo automático: quintales × 46"
            },
            {
                "fieldname": "cantidad_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "humedad_porcentaje",
                "label": "Humedad (%)",
                "fieldtype": "Percent",
                "default": 12
            },
            {
                "fieldname": "puntaje_catacion",
                "label": "Puntaje de Catación",
                "fieldtype": "Float",
                "precision": 1,
                "description": "Escala 0-100"
            },
            {
                "fieldname": "clasificacion_calidad",
                "label": "Clasificación de Calidad",
                "fieldtype": "Select",
                "options": "Estrictamente Duro\nDuro\nSemi Duro\nExtra Prime\nPrime\nExtra Good Washed\nGood Washed"
            },
            {
                "fieldname": "certificaciones_sec",
                "label": "Certificaciones",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "organico",
                "label": "Orgánico Certificado",
                "fieldtype": "Check",
                "default": 0
            },
            {
                "fieldname": "rainforest",
                "label": "Rainforest Alliance",
                "fieldtype": "Check",
                "default": 0
            },
            {
                "fieldname": "cert_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "fair_trade",
                "label": "Fair Trade",
                "fieldtype": "Check",
                "default": 0
            },
            {
                "fieldname": "utz",
                "label": "UTZ Certified",
                "fieldtype": "Check",
                "default": 0
            },
            {
                "fieldname": "financiero_sec",
                "label": "Información Financiera",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "precio_base_qq",
                "label": "Precio Base (Q/qq)",
                "fieldtype": "Currency"
            },
            {
                "fieldname": "premio_calidad",
                "label": "Premio por Calidad",
                "fieldtype": "Currency",
                "description": "Premio adicional por calidad especial"
            },
            {
                "fieldname": "financiero_col",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "contribucion_anacafe",
                "label": "Contribución ANACAFE",
                "fieldtype": "Currency",
                "read_only": 1,
                "description": "Q1.00 por quintal"
            },
            {
                "fieldname": "contribucion_municipal",
                "label": "Contribución Municipal",
                "fieldtype": "Currency",
                "read_only": 1,
                "description": "Q0.15 por quintal"
            },
            {
                "fieldname": "trazabilidad_sec",
                "label": "Trazabilidad",
                "fieldtype": "Section Break"
            },
            {
                "fieldname": "actividades_origen",
                "label": "Actividades de Origen",
                "fieldtype": "Table",
                "options": "Lote Cafe Actividad"
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
    print("✅ DocType 'Lote Cafe' creado")
```

### 3. Tabla Hijo para Trazabilidad
```python
def create_lote_cafe_actividad_doctype():
    """
    DocType hijo para trazabilidad de actividades en el lote
    """
    
    if frappe.db.exists("DocType", "Lote Cafe Actividad"):
        return
    
    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Lote Cafe Actividad",
        "module": "Custom",
        "custom": 1,
        "istable": 1,
        "fields": [
            {
                "fieldname": "actividad_campo",
                "label": "Actividad de Campo",
                "fieldtype": "Link",
                "options": "Actividad de Campo",
                "in_list_view": 1
            },
            {
                "fieldname": "empleado",
                "label": "Empleado",
                "fieldtype": "Data",
                "in_list_view": 1,
                "read_only": 1
            },
            {
                "fieldname": "unidad_trabajo",
                "label": "Cuerda",
                "fieldtype": "Data",
                "in_list_view": 1,
                "read_only": 1
            },
            {
                "fieldname": "fecha",
                "label": "Fecha",
                "fieldtype": "Date",
                "in_list_view": 1,
                "read_only": 1
            },
            {
                "fieldname": "cantidad_contribuida",
                "label": "Cantidad (lbs)",
                "fieldtype": "Float",
                "in_list_view": 1,
                "precision": 2
            }
        ]
    })
    
    doc.insert()
    print("✅ DocType 'Lote Cafe Actividad' creado")
```

## 📄 DOCUMENTACIÓN AUTOMÁTICA FAUCA

### Generador de Formularios ANACAFE
```python
class FAUCAGenerator:
    """
    Generador automático de documentos FAUCA para ANACAFE
    """
    
    def generar_fauca(self, lote_cafe_id):
        """
        Generar documento FAUCA automáticamente
        """
        lote = frappe.get_doc("Lote Cafe", lote_cafe_id)
        
        # Datos básicos del FAUCA
        fauca_data = {
            'numero_fauca': self.get_next_fauca_number(),
            'fecha_emision': now_datetime().date(),
            'exportador': {
                'razon_social': frappe.db.get_single_value('Company', 'company_name'),
                'nit': frappe.db.get_single_value('Company', 'tax_id'),
                'licencia_anacafe': frappe.conf.get('anacafe_licencia'),
                'direccion': frappe.db.get_single_value('Company', 'address_line1')
            },
            'producto': {
                'codigo_lote': lote.codigo_anacafe,
                'cantidad_quintales': lote.cantidad_quintales,
                'peso_kg': lote.peso_kg,
                'variedad': lote.variedad_cafe,
                'region_origen': lote.region_origen,
                'clasificacion': lote.clasificacion_calidad,
                'humedad': lote.humedad_porcentaje
            },
            'contribuciones': {
                'anacafe': lote.contribucion_anacafe,
                'municipal': lote.contribucion_municipal,
                'total': lote.contribucion_anacafe + lote.contribucion_municipal
            },
            'certificaciones': self.get_certificaciones(lote),
            'trazabilidad': self.get_trazabilidad_completa(lote)
        }
        
        # Generar PDF del FAUCA
        html_content = self.render_fauca_template(fauca_data)
        pdf_file = self.generate_pdf(html_content, f"FAUCA-{fauca_data['numero_fauca']}")
        
        return {
            'fauca_number': fauca_data['numero_fauca'],
            'pdf_file': pdf_file,
            'data': fauca_data
        }
    
    def get_next_fauca_number(self):
        """
        Obtener siguiente número FAUCA del año
        """
        year = now_datetime().year
        last_number = frappe.db.sql("""
            SELECT MAX(CAST(SUBSTRING(numero_fauca, -4) AS UNSIGNED)) as last_num
            FROM `tabFAUCA`
            WHERE YEAR(fecha_emision) = %s
        """, (year,))
        
        next_number = (last_number[0][0] or 0) + 1
        return f"FAUCA-{year}-{next_number:04d}"
    
    def get_certificaciones(self, lote):
        """
        Obtener certificaciones del lote
        """
        certificaciones = []
        
        if lote.organico:
            certificaciones.append("Orgánico Certificado")
        if lote.rainforest:
            certificaciones.append("Rainforest Alliance")
        if lote.fair_trade:
            certificaciones.append("Fair Trade")
        if lote.utz:
            certificaciones.append("UTZ Certified")
            
        return certificaciones
    
    def get_trazabilidad_completa(self, lote):
        """
        Obtener trazabilidad completa del lote
        """
        trazabilidad = []
        
        for actividad in lote.actividades_origen:
            act_doc = frappe.get_doc("Actividad de Campo", actividad.actividad_campo)
            
            trazabilidad.append({
                'fecha': act_doc.fecha,
                'empleado': act_doc.empleado,
                'cuerda': act_doc.unidad_trabajo,
                'cantidad_lbs': actividad.cantidad_contribuida,
                'tipo_trabajo': act_doc.tipo_trabajo
            })
        
        return trazabilidad
    
    def render_fauca_template(self, data):
        """
        Renderizar template HTML del FAUCA
        """
        template = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>FAUCA - {{ data.numero_fauca }}</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .header { text-align: center; margin-bottom: 30px; }
                .section { margin: 20px 0; }
                .table { width: 100%; border-collapse: collapse; margin: 10px 0; }
                .table th, .table td { border: 1px solid #ccc; padding: 8px; text-align: left; }
                .table th { background-color: #f5f5f5; }
                .logo { max-width: 200px; }
            </style>
        </head>
        <body>
            <div class="header">
                <img src="/assets/anacafe_logo.png" alt="ANACAFE" class="logo">
                <h1>FORMULARIO ÚNICO DE CAFÉ (FAUCA)</h1>
                <h2>{{ data.numero_fauca }}</h2>
                <p>Fecha de Emisión: {{ data.fecha_emision.strftime('%d/%m/%Y') }}</p>
            </div>
            
            <div class="section">
                <h3>DATOS DEL EXPORTADOR</h3>
                <table class="table">
                    <tr><td><strong>Razón Social:</strong></td><td>{{ data.exportador.razon_social }}</td></tr>
                    <tr><td><strong>NIT:</strong></td><td>{{ data.exportador.nit }}</td></tr>
                    <tr><td><strong>Licencia ANACAFE:</strong></td><td>{{ data.exportador.licencia_anacafe }}</td></tr>
                    <tr><td><strong>Dirección:</strong></td><td>{{ data.exportador.direccion }}</td></tr>
                </table>
            </div>
            
            <div class="section">
                <h3>INFORMACIÓN DEL PRODUCTO</h3>
                <table class="table">
                    <tr><td><strong>Código de Lote:</strong></td><td>{{ data.producto.codigo_lote }}</td></tr>
                    <tr><td><strong>Cantidad:</strong></td><td>{{ data.producto.cantidad_quintales }} quintales ({{ data.producto.peso_kg }} kg)</td></tr>
                    <tr><td><strong>Variedad:</strong></td><td>{{ data.producto.variedad }}</td></tr>
                    <tr><td><strong>Región de Origen:</strong></td><td>{{ data.producto.region_origen }}</td></tr>
                    <tr><td><strong>Clasificación:</strong></td><td>{{ data.producto.clasificacion }}</td></tr>
                    <tr><td><strong>Humedad:</strong></td><td>{{ data.producto.humedad }}%</td></tr>
                </table>
            </div>
            
            <div class="section">
                <h3>CONTRIBUCIONES PAGADAS</h3>
                <table class="table">
                    <tr><td><strong>Contribución ANACAFE:</strong></td><td>Q{{ "%.2f"|format(data.contribuciones.anacafe) }}</td></tr>
                    <tr><td><strong>Contribución Municipal:</strong></td><td>Q{{ "%.2f"|format(data.contribuciones.municipal) }}</td></tr>
                    <tr><td><strong>TOTAL:</strong></td><td><strong>Q{{ "%.2f"|format(data.contribuciones.total) }}</strong></td></tr>
                </table>
            </div>
            
            {% if data.certificaciones %}
            <div class="section">
                <h3>CERTIFICACIONES</h3>
                <ul>
                {% for cert in data.certificaciones %}
                    <li>{{ cert }}</li>
                {% endfor %}
                </ul>
            </div>
            {% endif %}
            
            <div class="section">
                <h3>TRAZABILIDAD</h3>
                <table class="table">
                    <thead>
                        <tr>
                            <th>Fecha</th>
                            <th>Empleado</th>
                            <th>Cuerda</th>
                            <th>Cantidad (lbs)</th>
                            <th>Actividad</th>
                        </tr>
                    </thead>
                    <tbody>
                    {% for item in data.trazabilidad %}
                        <tr>
                            <td>{{ item.fecha.strftime('%d/%m/%Y') }}</td>
                            <td>{{ item.empleado }}</td>
                            <td>{{ item.cuerda }}</td>
                            <td>{{ item.cantidad_lbs }}</td>
                            <td>{{ item.tipo_trabajo }}</td>
                        </tr>
                    {% endfor %}
                    </tbody>
                </table>
            </div>
            
            <div class="section" style="margin-top: 50px;">
                <p><strong>Fecha de Emisión:</strong> {{ data.fecha_emision.strftime('%d de %B de %Y') }}</p>
                <br><br>
                <p>_______________________________</p>
                <p>Firma del Exportador</p>
            </div>
        </body>
        </html>
        """
        
        from jinja2 import Template
        template_obj = Template(template)
        return template_obj.render(data=data)
```

## 🔄 AUTOMATIZACIÓN DE REPORTES

### Reportes Automáticos a ANACAFE
```python
class ANACAFEReports:
    """
    Generación automática de reportes para ANACAFE
    """
    
    def reporte_mensual_exportaciones(self, mes, año):
        """
        Reporte mensual de exportaciones
        """
        lotes_exportados = frappe.db.sql("""
            SELECT 
                codigo_anacafe,
                cantidad_quintales,
                region_origen,
                variedad_cafe,
                precio_base_qq,
                contribucion_anacafe + contribucion_municipal as contribuciones_pagadas
            FROM `tabLote Cafe`
            WHERE estado_lote = 'Exportado'
            AND MONTH(fecha_creacion) = %s
            AND YEAR(fecha_creacion) = %s
        """, (mes, año), as_dict=True)
        
        resumen = {
            'total_lotes': len(lotes_exportados),
            'total_quintales': sum(lote.cantidad_quintales for lote in lotes_exportados),
            'total_contribuciones': sum(lote.contribuciones_pagadas for lote in lotes_exportados),
            'por_region': {},
            'por_variedad': {}
        }
        
        # Agrupar por región
        for lote in lotes_exportados:
            region = lote.region_origen
            if region not in resumen['por_region']:
                resumen['por_region'][region] = {'lotes': 0, 'quintales': 0}
            
            resumen['por_region'][region]['lotes'] += 1
            resumen['por_region'][region]['quintales'] += lote.cantidad_quintales
        
        # Generar archivo Excel para ANACAFE
        self.generar_excel_anacafe(resumen, lotes_exportados, mes, año)
        
        return resumen
    
    def generar_excel_anacafe(self, resumen, detalle_lotes, mes, año):
        """
        Generar archivo Excel con formato ANACAFE
        """
        import xlsxwriter
        from io import BytesIO
        
        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        
        # Hoja 1: Resumen
        worksheet_resumen = workbook.add_worksheet('Resumen')
        
        # Formatos
        header_format = workbook.add_format({
            'bold': True,
            'bg_color': '#8B4513',
            'font_color': 'white',
            'align': 'center'
        })
        
        # Encabezados
        worksheet_resumen.write('A1', f'REPORTE MENSUAL - {mes:02d}/{año}', header_format)
        worksheet_resumen.write('A3', 'RESUMEN GENERAL', header_format)
        
        # Datos del resumen
        row = 4
        worksheet_resumen.write(row, 0, 'Total de Lotes:')
        worksheet_resumen.write(row, 1, resumen['total_lotes'])
        
        row += 1
        worksheet_resumen.write(row, 0, 'Total Quintales:')
        worksheet_resumen.write(row, 1, resumen['total_quintales'])
        
        row += 1
        worksheet_resumen.write(row, 0, 'Total Contribuciones:')
        worksheet_resumen.write(row, 1, f"Q{resumen['total_contribuciones']:.2f}")
        
        # Hoja 2: Detalle por lote
        worksheet_detalle = workbook.add_worksheet('Detalle Lotes')
        
        headers = ['Código ANACAFE', 'Quintales', 'Región', 'Variedad', 'Precio Base', 'Contribuciones']
        for col, header in enumerate(headers):
            worksheet_detalle.write(0, col, header, header_format)
        
        for row, lote in enumerate(detalle_lotes, 1):
            worksheet_detalle.write(row, 0, lote.codigo_anacafe)
            worksheet_detalle.write(row, 1, lote.cantidad_quintales)
            worksheet_detalle.write(row, 2, lote.region_origen)
            worksheet_detalle.write(row, 3, lote.variedad_cafe)
            worksheet_detalle.write(row, 4, lote.precio_base_qq)
            worksheet_detalle.write(row, 5, lote.contribuciones_pagadas)
        
        workbook.close()
        output.seek(0)
        
        # Guardar archivo
        file_name = f"Reporte_ANACAFE_{año}_{mes:02d}.xlsx"
        frappe.get_doc({
            "doctype": "File",
            "file_name": file_name,
            "content": output.getvalue(),
            "is_private": 1
        }).save()
        
        return file_name
```

## 🌐 API INTEGRATION CON SISTEMA ANACAFE

### Cliente API para Sistema ANACAFE
```python
class ANACAFEAPIClient:
    """
    Cliente para integración con API de ANACAFE
    """
    
    def __init__(self):
        self.base_url = frappe.conf.get('anacafe_api_url')
        self.api_token = frappe.conf.get('anacafe_api_token')
        self.session = self.create_session()
    
    def create_session(self):
        """
        Crear sesión autenticada con ANACAFE
        """
        import requests
        session = requests.Session()
        session.headers.update({
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json',
            'User-Agent': 'ERPNext-FincaCafe/1.0'
        })
        return session
    
    def registrar_lote(self, lote_data):
        """
        Registrar lote en sistema ANACAFE
        """
        endpoint = f"{self.base_url}/api/v1/lotes"
        
        payload = {
            'codigo_lote': lote_data.codigo_anacafe,
            'exportador_licencia': frappe.conf.get('anacafe_licencia'),
            'cantidad_quintales': lote_data.cantidad_quintales,
            'region_origen': lote_data.region_origen,
            'variedad': lote_data.variedad_cafe,
            'altitud': lote_data.altitud_cultivo,
            'humedad': lote_data.humedad_porcentaje,
            'certificaciones': self.get_certificaciones_array(lote_data),
            'fecha_registro': lote_data.fecha_creacion.isoformat()
        }
        
        try:
            response = self.session.post(endpoint, json=payload)
            response.raise_for_status()
            
            return {
                'success': True,
                'anacafe_id': response.json().get('id'),
                'message': 'Lote registrado exitosamente en ANACAFE'
            }
            
        except Exception as e:
            frappe.log_error(f"Error registrando lote en ANACAFE: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def consultar_precios_referencia(self):
        """
        Consultar precios de referencia de ANACAFE
        """
        endpoint = f"{self.base_url}/api/v1/precios"
        
        try:
            response = self.session.get(endpoint)
            response.raise_for_status()
            
            precios = response.json()
            
            # Guardar en cache local
            frappe.cache().set_value('anacafe_precios', precios, expires_in_sec=3600)
            
            return precios
            
        except Exception as e:
            # Si falla, usar cache local
            cached_prices = frappe.cache().get_value('anacafe_precios')
            if cached_prices:
                return cached_prices
            
            frappe.log_error(f"Error consultando precios ANACAFE: {str(e)}")
            return None
    
    def validar_licencia(self, numero_licencia):
        """
        Validar vigencia de licencia ANACAFE
        """
        endpoint = f"{self.base_url}/api/v1/licencias/{numero_licencia}"
        
        try:
            response = self.session.get(endpoint)
            response.raise_for_status()
            
            licencia_info = response.json()
            
            return {
                'vigente': licencia_info.get('estado') == 'Vigente',
                'fecha_vencimiento': licencia_info.get('fecha_vencimiento'),
                'tipo': licencia_info.get('tipo'),
                'titular': licencia_info.get('titular')
            }
            
        except Exception as e:
            frappe.log_error(f"Error validando licencia ANACAFE: {str(e)}")
            return None
```

Esta integración completa con ANACAFE automatiza todos los procesos requeridos para el cumplimiento legal y la exportación de café guatemalteco, desde el registro de lotes hasta la generación automática de documentos FAUCA.
