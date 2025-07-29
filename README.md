# 🌱 Sistema ERPNext para Finca de Café - Guatemala

Este proyecto contiene la configuración completa para implementar ERPNext en una finca de café en Guatemala, adaptado a las necesidades específicas de:

- Control de trabajadores y pagos por producción
- Gestión de unidades de trabajo (cuerdas de 25x25m)
- Trazabilidad completa del proceso del café
- Manejo de adelantos, préstamos y pagos quincenales

## 📋 Características del Sistema

### 🏗️ Doctypes Personalizados

1. **Adelantos y Prestamos** - Control de anticipos financieros
2. **Pago Quincenal** - Cálculo automático de sueldos
3. **Unidad de Trabajo** - Gestión de cuerdas de cultivo
4. **Actividad de Campo** - Registro de trabajo diario
5. **Fermentación** - Control de piletas de fermentación
6. **Patio Secado** - Gestión de patios de secado al sol
7. **Secadora** - Control de secado mecánico

### 🔄 Flujo del Proceso

```
Recolección (Actividad de Campo)
    ↓
Ingreso Inventario (Café Cereza)
    ↓
Fermentación (Piletas)
    ↓
Secado al Sol (Patios)
    ↓
Secadora (Mecánica)
    ↓
Producto Final (Café Pergamino)
    ↓
Bodega
```

### 💰 Sistema de Pagos

- **Pago por producción**: Recolección por libras, unidades, metros
- **Pago por tiempo**: Días completos, quincenas fijas
- **Adelantos y préstamos**: Control y descuento automático
- **Pago inmediato**: Trabajo dominical "a ganar"

## 🚀 Instalación

### Método 1: Script Python (Recomendado)

1. Accede a tu instancia ERPNext via SSH
2. Ejecuta el script de configuración:

```bash
cd /home/frappe/frappe-bench
bench --site [tu-sitio] execute /root/erpnext_setup_finca.py
```

### Método 2: Manual desde la interfaz

1. Ve a **Configuración > Personalización > DocType**
2. Crea cada DocType manualmente usando los campos especificados

## 📊 Casos de Uso

### Ejemplo: Recolección de Café

**Escenario**: 3 empleados recolectan café en 2 unidades diferentes

- Juan Pérez: 40 lbs en Unidad A
- María Gómez: 50 lbs en Unidad A  
- Luis Díaz: 60 lbs en Unidad B
- Tarifa: GTQ 1.25 por libra

**Registros en el sistema**:

1. **Actividad de Campo** (3 registros)
   - Empleado, Unidad, Cantidad, Tarifa
   - Cálculo automático: Pago Generado

2. **Ingreso de Inventario**
   - Total: 150 lbs Café Cereza
   - Origen: Campo → Destino: Fermentación

3. **Pago Quincenal** (al final del período)
   - Suma actividades por empleado
   - Resta adelantos pendientes
   - Genera pago neto

### Trazabilidad del Producto

Cada lote mantiene referencia al origen:

```
Lote: 2025-07-29-A
├── Recolección: Juan (40 lbs), María (50 lbs)
├── Fermentación: Pileta #3, 24 horas
├── Patio: Patio #2, 5 días
├── Secadora: 8 horas, 60°C
└── Producto Final: 85 lbs Café Pergamino
```

## 🔧 Configuración Adicional

### Productos Requeridos

Crear estos Items en ERPNext:

```
- Café Cereza (Materia Prima)
- Café Fermentado (Producto Intermedio)
- Café Semiseco (Producto Intermedio)
- Café Pergamino (Producto Final)
```

### Empleados

Registrar empleados con:
- Método de pago (Producción/Quincenal)
- Tarifa base
- Datos de contacto

### Almacenes

```
- Campo (Virtual - para recolección)
- Fermentación
- Patio de Secado
- Secadora
- Bodega Central
```

## 📈 Reportes Disponibles

1. **Resumen de Actividades por Empleado**
2. **Productividad por Unidad de Trabajo**
3. **Trazabilidad de Lotes**
4. **Control de Adelantos Pendientes**
5. **Análisis de Tiempo de Proceso**

## ⚙️ Próximos Pasos

1. Ejecutar el script de configuración
2. Crear productos e Items necesarios
3. Registrar empleados y unidades de trabajo
4. Configurar tarifas de pago
5. Capacitar al personal en el uso del sistema

## 🆘 Solución de Problemas

### Error de naming_series
Si encuentras errores al crear Doctypes, usa el script Python en lugar de la consola del navegador.

### Permisos de acceso
Asegúrate de tener rol "System Manager" para crear Doctypes personalizados.

### Campos faltantes
Revisa que todos los Items y Empleados estén creados antes de usar los Doctypes personalizados.

---

**Desarrollado para**: Finca de Café, Guatemala  
**Versión ERPNext**: Compatible con v13+  
**Fecha**: Julio 2025
