# 🌱 Sistema ERPNext Completo para Finca de Café Guatemalteca

## 📋 VERSIÓN 2.0 - INTEGRADO CON INVESTIGACIÓN TÉCNICA

Este proyecto ahora incluye **documentación técnica especializada** basada en investigación profunda sobre:

- ✅ **Variedades de café guatemaltecas** (Typica, Bourbon, Caturra, Anacafé 14)
- ✅ **Proceso completo de beneficiado** (fermentación → patios → secadora → bodega)
- ✅ **Marco legal guatemalteco** (Código de Trabajo, ANACAFE, MAGA)
- ✅ **Arquitectura ERPNext especializada** para agricultura
- ✅ **KPIs y métricas agrícolas** específicas
- ✅ **Integración tecnológica** y aplicaciones móviles

## 🆕 NUEVAS CARACTERÍSTICAS

### 🌿 **Productos Específicos del Café**
```
- Café Cereza (materia prima)
- Café Fermentado (proceso)
- Café Semiseco (proceso)
- Café Pergamino (producto final)
- Variedades: Typica, Bourbon, Caturra, Anacafé 14
```

### 📏 **Unidades de Medida Guatemaltecas**
```
- Cuerdas: 25x25 varas (625 varas²) = 437 m²
- Cuerdas: 40x40 varas (1,600 varas²) = 1,118 m²
- Conversión automática: varas → metros → hectáreas
- Densidad de siembra automática
```

### 👥 **Sistema Laboral Guatemalteco Completo**
```
- Adelantos y préstamos con control legal
- Pago por producción (libras, unidades, metros)
- Verificación automática de salario mínimo
- Trabajo dominical "a ganar"
- Cumplimiento del Código de Trabajo
```

### ☕ **Proceso de Beneficiado Integrado**
```
Recolección → Fermentación → Patio Secado → Secadora → Bodega
↓             ↓              ↓              ↓         ↓
Café Cereza   Café Ferment.  Café Semiseco  Café Pergamino
```

### 📊 **Trazabilidad Completa**
```
Lote ID: 2025-07-29-A-01
├── Recolección: Juan (40 lbs), María (50 lbs)
├── Fermentación: Pileta #3, 24 horas
├── Patio: Patio #2, 5 días
├── Secadora: 8 horas, 60°C
└── Producto Final: 85 lbs Café Pergamino
```

## 🚀 INSTALACIÓN

### Opción 1: Script Completo (Recomendado)

```bash
# En tu servidor ERPNext
cd /home/frappe/frappe-bench
bench --site [tu-sitio] execute /root/erpnext_setup_finca_completo.py
```

### Opción 2: Instalación Manual

1. **Crear Productos del Café**
   - Ve a Stock > Item > New
   - Crear: Café Cereza, Café Fermentado, Café Semiseco, Café Pergamino
   - Crear variedades: Typica, Bourbon, Caturra, Anacafé 14

2. **Crear Almacenes**
   ```
   - Campo (para recolección)
   - Fermentación 
   - Patio de Secado
   - Secadora
   - Bodega Central
   ```

3. **Ejecutar Doctypes Individuales**
   - Usar los scripts de la documentación original
   - Crear uno por uno desde la interfaz

## 📊 NUEVOS DOCTYPES PRINCIPALES

### 1. **Unidad de Trabajo** (Cuerdas)
- Código de cuerda (A-01, B-05)
- Medidas guatemaltecas (25x25 o 40x40 varas)
- Conversión automática a metros/hectáreas
- Variedad de café plantada
- Cantidad de árboles y densidad

### 2. **Actividad de Campo** (Trabajo Diario)
- Modalidades de pago completas
- Verificación de salario mínimo
- Generación automática de lote ID
- Control de calidad del trabajo

### 3. **Fermentación** (Proceso de Beneficiado)
- Control de piletas
- Tiempo real vs planificado
- Control de pH y temperatura
- Cálculo automático de mermas

### 4. **Adelantos y Préstamos** (Legal)
- Tipos: quincenal, personal, emergencia
- Métodos de descuento
- Estado de aplicación en nómina
- Aprobaciones requeridas

## 📈 REPORTES ESPECIALIZADOS

### 🎯 **Productividad por Empleado**
- Días trabajados
- Total producido
- Promedio diario
- Pago total generado

### 📍 **Rendimiento por Cuerda**
- Producción por hectárea
- Comparación entre variedades
- Eficiencia por unidad de trabajo

### 💰 **Control de Pagos**
- Adelantos pendientes
- Verificación de salario mínimo
- Pagos inmediatos vs quincenales

## 🔄 FLUJOS AUTOMATIZADOS

### ⚡ **Cálculos Automáticos**
```python
# Pago por producción
pago = cantidad × tarifa_por_unidad

# Verificación salario mínimo
if pago < salario_minimo_diario:
    pago = salario_minimo_diario

# Conversión de medidas
metros² = varas² × (0.835)²
hectáreas = metros² / 10,000
```

### 🏷️ **Generación de Lote ID**
```
Formato: YYYY-MM-DD-UNIDAD
Ejemplo: 2025-07-29-A-01
```

### 📊 **Control de Mermas**
```
merma% = (cantidad_entrada - cantidad_salida) / cantidad_entrada × 100
```

## 🌍 CUMPLIMIENTO LEGAL GUATEMALTECO

### ⚖️ **Código de Trabajo**
- Salario mínimo agrícola: Q90.16/día
- Verificación automática en cada pago
- Control de jornadas laborales
- Registro de horas extras

### 🏛️ **ANACAFE**
- Estructura para licencias de exportación
- Control de contribuciones (Q1.00 + Q0.15 por quintal)
- Trazabilidad para certificaciones

### 📋 **MAGA/SAT**
- Preparación para documentación VUPE
- Estructura para certificados fitosanitarios
- Control de inventarios para exportación

## 🎯 CASOS DE USO IMPLEMENTADOS

### 🌱 **Caso 1: Recolección Diaria**
```
1. Trabajador registra: 45 lbs de Café Cereza
2. Sistema calcula: 45 × Q1.25 = Q56.25
3. Verifica salario mínimo: ✅ (> Q90.16 en jornada completa)
4. Genera lote: 2025-07-29-A-01
5. Actualiza inventario: +45 lbs en "Campo"
```

### ⚗️ **Caso 2: Proceso de Fermentación**
```
1. Ingreso: 500 lbs Café Cereza a Pileta P-03
2. Control: 24 horas, pH inicial 6.2
3. Finalización: pH final 4.8, merma 2%
4. Salida: 490 lbs Café Fermentado
5. Trazabilidad: Lote 2025-07-29-A-01-F3
```

### 💰 **Caso 3: Pago Quincenal**
```
1. Sistema suma actividades: 15 días × promedio
2. Resta adelantos: Q150 pendientes
3. Verifica mínimo: Q90.16 × 15 = Q1,352.40
4. Genera pago neto: Total - adelantos
5. Estado: Listo para pago
```

## 🛠️ PRÓXIMOS PASOS

### Fase 1: Configuración Básica
- [x] Ejecutar script de instalación
- [ ] Crear empleados y cuerdas
- [ ] Configurar tarifas de pago
- [ ] Capacitar usuarios básicos

### Fase 2: Operación Piloto
- [ ] Registrar actividades diarias (1 semana)
- [ ] Probar proceso de fermentación
- [ ] Generar primer pago quincenal
- [ ] Validar trazabilidad completa

### Fase 3: Expansión
- [ ] Integrar aplicación móvil
- [ ] Conectar sensores IoT
- [ ] Implementar BI/Dashboards
- [ ] Automatizar reportes ANACAFE

## 📞 SOPORTE

**Desarrollado para**: Finca de Café, Guatemala  
**Basado en**: Documentación técnica especializada  
**Versión ERPNext**: Compatible con v13+  
**Fecha**: Julio 2025

---

### 🎯 **DIFERENCIAS CLAVE vs VERSIÓN 1.0**

| Aspecto | Versión 1.0 | Versión 2.0 |
|---------|-------------|-------------|
| **Productos** | Genéricos | Específicos del café guatemalteco |
| **Medidas** | Métricas | Cuerdas guatemaltecas con conversión |
| **Legal** | Básico | Cumplimiento completo Código de Trabajo |
| **Proceso** | Simple | Beneficiado completo con trazabilidad |
| **Pago** | Por producción | Múltiples modalidades + salario mínimo |
| **Calidad** | No incluida | Control de calidad en cada etapa |
| **Reportes** | Básicos | Especializados para café |

La **Versión 2.0** es un sistema completo y especializado, listo para implementación en fincas reales de café en Guatemala.
