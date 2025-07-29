# 📊 Dashboards Especializados para Finca de Café

## 🎯 DASHBOARD EJECUTIVO PRINCIPAL

### Métricas Clave en Tiempo Real
```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  🌱 FINCA LA ESPERANZA - DASHBOARD EJECUTIVO                    📅 29 Jul 2025  │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐              │
│  │ PRODUCCIÓN  │ │   PERSONAL  │ │  CALIDAD    │ │ RENTABILIDAD│              │
│  │             │ │             │ │             │ │             │              │
│  │   2,450     │ │     95%     │ │    4.2★     │ │    85%      │              │
│  │ lbs/día     │ │ asistencia  │ │ promedio    │ │ margen      │              │
│  │ ↗ +12%      │ │ ↗ +5%       │ │ ↗ +0.3      │ │ ↘ -2%       │              │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘              │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │ 📈 PRODUCTIVIDAD POR CUERDA (Últimos 30 días)                          │   │
│  │                                                                         │   │
│  │  A-01 (Caturra)   ████████████████▓▓▓▓ 85 qq/ha                       │   │
│  │  A-02 (Bourbon)   ████████████████████▓ 95 qq/ha                      │   │
│  │  B-01 (Typica)    ████████████▓▓▓▓▓▓▓▓ 65 qq/ha                       │   │
│  │  B-02 (Anacafé)   ████████████████████▓ 92 qq/ha                      │   │
│  │                                                                         │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│  ┌─────────────────────────────┐ ┌─────────────────────────────────────────┐   │
│  │ 🔄 PROCESO DE BENEFICIADO   │ │ 💰 ANÁLISIS FINANCIERO                  │   │
│  │                             │ │                                         │   │
│  │ En Fermentación:   1,200 lbs│ │ Ingresos mes:      Q125,450            │   │
│  │ En Patios:         3,800 lbs│ │ Costos laborales:   Q45,200            │   │
│  │ En Secadora:         950 lbs│ │ Costos insumos:     Q12,300            │   │
│  │ En Bodega:         8,500 lbs│ │ Utilidad neta:      Q67,950            │   │
│  │                             │ │                                         │   │
│  │ ⚠️ Alerta: Pileta P-03      │ │ 📊 ROI mensual:        54.2%           │   │
│  │   28 horas fermentando      │ │                                         │   │
│  └─────────────────────────────┘ └─────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## 📊 DASHBOARD DE PRODUCCIÓN

### Custom Dashboard para ERPNext
```python
# dashboard_produccion.py
import frappe
from frappe import _

def get_dashboard_data():
    """
    Dashboard especializado para producción de café
    """
    
    # Métricas principales
    metricas = {
        'produccion_hoy': get_produccion_hoy(),
        'produccion_semana': get_produccion_semana(),
        'productividad_empleados': get_top_empleados(),
        'rendimiento_cuerdas': get_rendimiento_cuerdas(),
        'proceso_beneficiado': get_estado_beneficiado(),
        'alertas_criticas': get_alertas_criticas()
    }
    
    return metricas

def get_produccion_hoy():
    """Producción del día actual"""
    return frappe.db.sql("""
        SELECT 
            SUM(cantidad) as total_libras,
            COUNT(DISTINCT empleado) as empleados_activos,
            AVG(cantidad) as promedio_empleado,
            COUNT(*) as actividades_registradas
        FROM `tabActividad de Campo` 
        WHERE fecha = CURDATE() 
        AND tipo_trabajo = 'Recolección'
    """, as_dict=True)[0]

def get_rendimiento_cuerdas():
    """Top 10 cuerdas por rendimiento"""
    return frappe.db.sql("""
        SELECT 
            ut.codigo,
            ut.variedad_cafe,
            ut.area_hectareas,
            SUM(ac.cantidad) as total_cosechado,
            SUM(ac.cantidad) / ut.area_hectareas as rendimiento_ha,
            COUNT(ac.name) as dias_cosecha,
            AVG(ac.cantidad) as promedio_diario
        FROM `tabUnidad de Trabajo` ut
        LEFT JOIN `tabActividad de Campo` ac ON ut.name = ac.unidad_trabajo
        WHERE ac.fecha >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
        AND ac.tipo_trabajo = 'Recolección'
        GROUP BY ut.codigo
        ORDER BY rendimiento_ha DESC
        LIMIT 10
    """, as_dict=True)

def get_estado_beneficiado():
    """Estado actual del proceso de beneficiado"""
    return {
        'fermentacion': frappe.db.sql("""
            SELECT COUNT(*) as lotes, SUM(cantidad_entrada) as total_lbs
            FROM `tabFermentacion` 
            WHERE estado = 'En Proceso'
        """, as_dict=True)[0],
        
        'patios': frappe.db.sql("""
            SELECT COUNT(*) as lotes, SUM(cantidad) as total_lbs
            FROM `tabPatio Secado` 
            WHERE estado = 'En Secado'
        """, as_dict=True)[0],
        
        'secadora': frappe.db.sql("""
            SELECT COUNT(*) as lotes, SUM(cantidad_entrada) as total_lbs
            FROM `tabSecadora` 
            WHERE estado = 'En Proceso'
        """, as_dict=True)[0]
    }

# Widgets personalizados para el dashboard
DASHBOARD_CONFIG = {
    "name": "Producción de Café",
    "charts": [
        {
            "name": "Producción Diaria",
            "chart_type": "Line",
            "chart_name": "produccion_diaria",
            "filters_config": {
                "date_range": "30 days"
            }
        },
        {
            "name": "Productividad por Empleado",
            "chart_type": "Bar", 
            "chart_name": "productividad_empleados"
        },
        {
            "name": "Rendimiento por Variedad",
            "chart_type": "Donut",
            "chart_name": "rendimiento_variedad"
        }
    ],
    
    "number_cards": [
        {
            "name": "Producción Hoy",
            "function": "get_produccion_hoy",
            "label": "Libras",
            "color": "Green"
        },
        {
            "name": "Empleados Activos",
            "function": "get_empleados_activos",
            "label": "Trabajadores",
            "color": "Blue"
        },
        {
            "name": "Promedio por Empleado",
            "function": "get_promedio_empleado",
            "label": "lbs/empleado",
            "color": "Orange"
        },
        {
            "name": "Eficiencia General",
            "function": "get_eficiencia_general",
            "label": "%",
            "color": "Purple"
        }
    ]
}
```

## 📈 DASHBOARD DE RECURSOS HUMANOS

### Gestión Laboral Especializada
```html
<!-- dashboard_rrhh.html -->
<div class="dashboard-rrhh">
    <div class="row">
        <!-- Asistencia en tiempo real -->
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h5>👥 Asistencia Hoy</h5>
                </div>
                <div class="card-body">
                    <div class="asistencia-circle">
                        <canvas id="asistencia-chart"></canvas>
                        <div class="center-text">
                            <span class="big-number">23</span>
                            <span class="small-text">de 25</span>
                        </div>
                    </div>
                    
                    <div class="asistencia-details">
                        <div class="row">
                            <div class="col-4">
                                <span class="status-dot present"></span>
                                Presentes: 23
                            </div>
                            <div class="col-4">
                                <span class="status-dot absent"></span>
                                Ausentes: 2
                            </div>
                            <div class="col-4">
                                <span class="status-dot late"></span>
                                Tardías: 1
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Productividad por empleado -->
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h5>🏆 Top Recolectores</h5>
                </div>
                <div class="card-body">
                    <div class="empleado-ranking">
                        <div class="empleado-item gold">
                            <span class="rank">🥇</span>
                            <span class="name">María López</span>
                            <span class="metric">68 lbs</span>
                        </div>
                        <div class="empleado-item silver">
                            <span class="rank">🥈</span>
                            <span class="name">Juan Pérez</span>
                            <span class="metric">62 lbs</span>
                        </div>
                        <div class="empleado-item bronze">
                            <span class="rank">🥉</span>
                            <span class="name">Carlos Ruiz</span>
                            <span class="metric">58 lbs</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Alertas de nómina -->
    <div class="row">
        <div class="col-md-12">
            <div class="card alert-card">
                <div class="card-header">
                    <h5>⚠️ Alertas de Nómina</h5>
                </div>
                <div class="card-body">
                    <div class="alert-list">
                        <div class="alert-item warning">
                            <span class="icon">💰</span>
                            <span class="text">3 empleados por debajo del salario mínimo esta quincena</span>
                            <button class="btn btn-sm btn-warning">Revisar</button>
                        </div>
                        <div class="alert-item info">
                            <span class="icon">📅</span>
                            <span class="text">Pago quincenal programado en 2 días</span>
                            <button class="btn btn-sm btn-info">Preparar</button>
                        </div>
                        <div class="alert-item success">
                            <span class="icon">✅</span>
                            <span class="text">Adelantos por Q1,250 pendientes de aplicar</span>
                            <button class="btn btn-sm btn-success">Aplicar</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

## 📊 DASHBOARD DE CALIDAD

### Control de Calidad Integrado
```javascript
// dashboard_calidad.js
class DashboardCalidad {
    constructor() {
        this.init();
    }
    
    init() {
        this.loadCalidadData();
        this.setupCharts();
        this.setupAlerts();
    }
    
    loadCalidadData() {
        // Datos de calidad por etapa
        frappe.call({
            method: 'finca_cafe.dashboard.get_calidad_data',
            callback: (r) => {
                this.renderCalidadCharts(r.message);
            }
        });
    }
    
    renderCalidadCharts(data) {
        // Gráfico de calidad por proceso
        new Chart(document.getElementById('calidad-proceso'), {
            type: 'radar',
            data: {
                labels: ['Recolección', 'Fermentación', 'Secado', 'Clasificación'],
                datasets: [{
                    label: 'Calidad Promedio',
                    data: data.calidad_por_proceso,
                    backgroundColor: 'rgba(139, 69, 19, 0.2)',
                    borderColor: 'rgba(139, 69, 19, 1)',
                    pointBackgroundColor: 'rgba(139, 69, 19, 1)',
                }]
            },
            options: {
                scale: {
                    ticks: {
                        beginAtZero: true,
                        max: 5
                    }
                }
            }
        });
        
        // Histograma de defectos
        new Chart(document.getElementById('defectos-chart'), {
            type: 'bar',
            data: {
                labels: data.tipos_defectos.map(d => d.tipo),
                datasets: [{
                    label: 'Cantidad de Defectos',
                    data: data.tipos_defectos.map(d => d.cantidad),
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.7)',
                        'rgba(255, 159, 64, 0.7)',
                        'rgba(255, 205, 86, 0.7)',
                        'rgba(75, 192, 192, 0.7)',
                    ]
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    title: {
                        display: true,
                        text: 'Defectos por Tipo'
                    }
                }
            }
        });
    }
    
    setupAlerts() {
        // Alertas automáticas de calidad
        setInterval(() => {
            this.checkCalidadAlerts();
        }, 30000); // Cada 30 segundos
    }
    
    checkCalidadAlerts() {
        frappe.call({
            method: 'finca_cafe.dashboard.get_calidad_alerts',
            callback: (r) => {
                if (r.message.alerts.length > 0) {
                    this.showCalidadAlerts(r.message.alerts);
                }
            }
        });
    }
    
    showCalidadAlerts(alerts) {
        const alertContainer = document.getElementById('calidad-alerts');
        alertContainer.innerHTML = '';
        
        alerts.forEach(alert => {
            const alertDiv = document.createElement('div');
            alertDiv.className = `alert alert-${alert.type}`;
            alertDiv.innerHTML = `
                <strong>${alert.titulo}</strong>
                <p>${alert.mensaje}</p>
                <button class="btn btn-sm btn-primary" onclick="resolveAlert('${alert.id}')">
                    Resolver
                </button>
            `;
            alertContainer.appendChild(alertDiv);
        });
    }
}

// Inicializar dashboard al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    new DashboardCalidad();
});
```

## 📱 DASHBOARD MÓVIL RESPONSIVE

### CSS para dispositivos móviles
```css
/* dashboard_mobile.css */
@media (max-width: 768px) {
    .dashboard-container {
        padding: 10px;
    }
    
    .metric-card {
        width: 100%;
        margin-bottom: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .metric-card .number {
        font-size: 2rem;
        font-weight: bold;
        color: #8B4513;
    }
    
    .metric-card .label {
        font-size: 0.9rem;
        color: #666;
    }
    
    .chart-container {
        height: 250px;
        margin-bottom: 20px;
    }
    
    .empleado-ranking {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    
    .empleado-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px;
        border-radius: 8px;
        background: #f8f9fa;
    }
    
    .empleado-item.gold { border-left: 4px solid #FFD700; }
    .empleado-item.silver { border-left: 4px solid #C0C0C0; }
    .empleado-item.bronze { border-left: 4px solid #CD7F32; }
    
    .alert-item {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 6px;
        background: white;
        border-left: 4px solid;
    }
    
    .alert-item.warning { border-left-color: #ffc107; }
    .alert-item.info { border-left-color: #17a2b8; }
    .alert-item.success { border-left-color: #28a745; }
}
```

## 🔔 SISTEMA DE NOTIFICACIONES

### Alertas en Tiempo Real
```python
# notifications.py
import frappe
from frappe.utils import now_datetime, get_datetime

@frappe.whitelist()
def check_critical_alerts():
    """
    Verificar alertas críticas para dashboards
    """
    alerts = []
    
    # 1. Fermentación que excede tiempo óptimo
    fermentaciones_criticas = frappe.db.sql("""
        SELECT name, pileta, tiempo_planificado, fecha_inicio
        FROM `tabFermentacion`
        WHERE estado = 'En Proceso'
        AND TIMESTAMPDIFF(HOUR, fecha_inicio, NOW()) > tiempo_planificado + 2
    """, as_dict=True)
    
    for ferm in fermentaciones_criticas:
        tiempo_exceso = frappe.db.sql("""
            SELECT TIMESTAMPDIFF(HOUR, %s, NOW()) as horas_transcurridas
        """, (ferm.fecha_inicio,))[0][0]
        
        alerts.append({
            'type': 'critical',
            'module': 'Beneficiado',
            'title': f'Fermentación crítica en {ferm.pileta}',
            'message': f'Lleva {tiempo_exceso} horas, {tiempo_exceso - ferm.tiempo_planificado} horas de exceso',
            'action_url': f'/app/fermentacion/{ferm.name}'
        })
    
    # 2. Empleados por debajo del salario mínimo
    empleados_salario_bajo = frappe.db.sql("""
        SELECT empleado, SUM(pago_generado) as total_quincenal
        FROM `tabActividad de Campo`
        WHERE fecha >= DATE_SUB(CURDATE(), INTERVAL 15 DAY)
        GROUP BY empleado
        HAVING total_quincenal < (90.16 * 15)  -- Salario mínimo × 15 días
    """, as_dict=True)
    
    if empleados_salario_bajo:
        alerts.append({
            'type': 'warning',
            'module': 'RRHH',
            'title': f'{len(empleados_salario_bajo)} empleados bajo salario mínimo',
            'message': 'Requiere ajuste para cumplimiento legal',
            'action_url': '/app/report/Empleados Salario Minimo'
        })
    
    # 3. Baja productividad en cuerdas específicas
    cuerdas_baja_productividad = frappe.db.sql("""
        SELECT ut.codigo, AVG(ac.cantidad / ut.area_hectareas) as rendimiento
        FROM `tabUnidad de Trabajo` ut
        LEFT JOIN `tabActividad de Campo` ac ON ut.name = ac.unidad_trabajo
        WHERE ac.fecha >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
        AND ac.tipo_trabajo = 'Recolección'
        GROUP BY ut.codigo
        HAVING rendimiento < 30  -- Menos de 30 lbs/hectárea promedio
    """, as_dict=True)
    
    for cuerda in cuerdas_baja_productividad:
        alerts.append({
            'type': 'info',
            'module': 'Producción',
            'title': f'Baja productividad en cuerda {cuerda.codigo}',
            'message': f'Rendimiento: {cuerda.rendimiento:.1f} lbs/ha (por debajo del promedio)',
            'action_url': f'/app/unidad-de-trabajo/{cuerda.codigo}'
        })
    
    return alerts

# Webhook para notificaciones push
@frappe.whitelist()
def send_dashboard_notifications():
    """
    Enviar notificaciones push a usuarios suscritos
    """
    alerts = check_critical_alerts()
    
    for alert in alerts:
        # Crear notificación en ERPNext
        notification = frappe.get_doc({
            'doctype': 'Notification Log',
            'subject': alert['title'],
            'email_content': alert['message'],
            'for_user': frappe.session.user,
            'type': 'Alert',
            'document_type': alert['module'],
            'read': 0
        })
        notification.insert(ignore_permissions=True)
        
        # Enviar push notification si está configurado
        if frappe.conf.get('push_notifications_enabled'):
            send_push_notification(alert)

def send_push_notification(alert):
    """
    Enviar notificación push a dispositivos móviles
    """
    import requests
    
    payload = {
        'title': alert['title'],
        'body': alert['message'],
        'data': {
            'action_url': alert['action_url'],
            'type': alert['type']
        }
    }
    
    # Enviar via Firebase Cloud Messaging
    headers = {
        'Authorization': f'key={frappe.conf.get("fcm_server_key")}',
        'Content-Type': 'application/json'
    }
    
    response = requests.post(
        'https://fcm.googleapis.com/fcm/send',
        json=payload,
        headers=headers
    )
    
    return response.status_code == 200
```

Estos dashboards proporcionan una vista completa y en tiempo real de todas las operaciones de la finca, desde la producción hasta la calidad y los recursos humanos, con alertas proactivas para tomar decisiones inmediatas.
