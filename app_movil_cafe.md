# 📱 AgroFinca Café - Aplicación Móvil Especializada

## 🎯 ESPECIFICACIONES TÉCNICAS

### Características Principales
- **Offline-first**: Funciona sin conexión en el campo
- **Geolocalización**: GPS automático para cada registro
- **Códigos QR**: Identificación rápida de cuerdas y empleados
- **Cámara integrada**: Evidencia fotográfica de actividades
- **Sincronización inteligente**: Datos siempre actualizados

## 📋 FUNCIONALIDADES ESPECÍFICAS PARA CAFÉ

### 🌱 Módulo de Recolección
```
┌─────────────────────────────────────┐
│  📱 REGISTRO DE RECOLECCIÓN         │
├─────────────────────────────────────┤
│ Empleado: [Juan Pérez ▼]           │
│ Cuerda: [Escanear QR] [A-01 ▼]     │
│ Variedad: [Caturra]                │
│ Libras: [____] ⚖️                  │
│ Calidad: [⭐⭐⭐⭐⭐]               │
│ Foto: [📷 Capturar]                │
│ Estado: [🟢 Maduro óptimo]         │
│                                     │
│ [💾 Guardar] [📤 Sincronizar]      │
└─────────────────────────────────────┘
```

### ⚗️ Módulo de Beneficiado
```
┌─────────────────────────────────────┐
│  🧪 CONTROL DE FERMENTACIÓN        │
├─────────────────────────────────────┤
│ Pileta: [P-03 ▼]                   │
│ Lote: [2025-07-29-A-01]            │
│ Entrada: [500] lbs                 │
│ pH Inicial: [6.2]                  │
│ Temp: [25°C] 🌡️                   │
│ Estado: [🔄 En proceso]            │
│ Timer: [⏰ 14:30:22]               │
│                                     │
│ [📸 Foto] [⏹️ Finalizar]           │
└─────────────────────────────────────┘
```

### 👥 Módulo de Personal
```
┌─────────────────────────────────────┐
│  👤 GESTIÓN DE EMPLEADOS           │
├─────────────────────────────────────┤
│ Asistencia Hoy: 23/25 ✅           │
│                                     │
│ 🟢 Juan Pérez    | 45 lbs | Q56.25 │
│ 🟢 María López   | 52 lbs | Q65.00 │
│ 🔴 Carlos Ruiz   | Ausente         │
│                                     │
│ Adelantos Pendientes: Q450         │
│ Pago Quincenal: En 3 días         │
│                                     │
│ [➕ Nuevo Adelanto] [📊 Reportes]  │
└─────────────────────────────────────┘
```

## 🔧 ARQUITECTURA TÉCNICA

### Framework: Flutter (Multiplataforma)
```yaml
dependencies:
  flutter: ^3.13.0
  sqflite: ^2.3.0      # Base de datos local
  geolocator: ^9.0.2   # GPS
  camera: ^0.10.5      # Cámara
  qr_code_scanner: ^1.0.1  # QR Scanner
  dio: ^5.3.2          # HTTP Client
  hive: ^2.2.3         # Cache local
```

### Base de Datos Local (SQLite)
```sql
-- Tabla para actividades offline
CREATE TABLE actividades_campo (
    id INTEGER PRIMARY KEY,
    empleado_id TEXT,
    cuerda_id TEXT,
    fecha TEXT,
    tipo_trabajo TEXT,
    cantidad REAL,
    tarifa REAL,
    pago_calculado REAL,
    foto_path TEXT,
    gps_lat REAL,
    gps_lon REAL,
    sincronizado INTEGER DEFAULT 0,
    timestamp_creacion TEXT
);

-- Tabla para empleados (cache)
CREATE TABLE empleados (
    id TEXT PRIMARY KEY,
    nombre TEXT,
    codigo_empleado TEXT,
    activo INTEGER DEFAULT 1,
    ultima_sync TEXT
);

-- Tabla para cuerdas (cache)
CREATE TABLE cuerdas (
    id TEXT PRIMARY KEY,
    codigo TEXT,
    variedad_cafe TEXT,
    area_hectareas REAL,
    qr_code TEXT,
    ultima_sync TEXT
);
```

### API Integration con ERPNext
```dart
class ERPNextAPI {
  static const String baseUrl = 'https://tu-erpnext.com';
  
  // Sincronizar actividades pendientes
  Future<bool> syncActividades() async {
    final pendientes = await db.getActividadesPendientes();
    
    for (var actividad in pendientes) {
      try {
        final response = await dio.post(
          '$baseUrl/api/resource/Actividad de Campo',
          data: {
            'empleado': actividad.empleadoId,
            'unidad_trabajo': actividad.cuerdaId,
            'fecha': actividad.fecha,
            'tipo_trabajo': actividad.tipoTrabajo,
            'cantidad': actividad.cantidad,
            'tarifa_unidad': actividad.tarifa,
            'pago_generado': actividad.pagoCalculado,
          },
        );
        
        if (response.statusCode == 200) {
          await db.marcarSincronizado(actividad.id);
        }
      } catch (e) {
        print('Error sincronizando: $e');
      }
    }
    
    return true;
  }
  
  // Descargar datos maestros
  Future<void> downloadMaestros() async {
    // Empleados
    final empleados = await dio.get(
      '$baseUrl/api/resource/Employee',
      queryParameters: {'filters': '[["status", "=", "Active"]]'}
    );
    await db.insertEmpleados(empleados.data);
    
    // Cuerdas
    final cuerdas = await dio.get(
      '$baseUrl/api/resource/Unidad de Trabajo'
    );
    await db.insertCuerdas(cuerdas.data);
  }
}
```

## 📦 DISTRIBUCIÓN Y DEPLOYMENT

### Android (Play Store Internal)
```yaml
# android/app/build.gradle
android {
    compileSdkVersion 34
    
    defaultConfig {
        applicationId "com.finca.agrocafe"
        minSdkVersion 21
        targetSdkVersion 34
        versionCode 1
        versionName "1.0.0"
    }
    
    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled true
        }
    }
}
```

### iOS (TestFlight)
```yaml
# ios/Runner/Info.plist
<key>NSLocationWhenInUseUsageDescription</key>
<string>Necesario para registrar ubicación de actividades</string>
<key>NSCameraUsageDescription</key>
<string>Tomar fotos de evidencia de trabajo</string>
```

## 📱 MOCKUPS DE PANTALLAS

### Pantalla Principal
```
╔═══════════════════════════════════════╗
║ 🌱 AgroFinca Café        📶🔋100%    ║
║                                       ║
║  Bienvenido, Juan Pérez               ║
║  📍 Finca La Esperanza                ║
║  📅 Lunes, 29 Julio 2025              ║
║                                       ║
║  ┌─────────────────────────────────┐   ║
║  │  🌱 RECOLECCIÓN          [45]   │   ║
║  │  Registrar cosecha diaria       │   ║
║  └─────────────────────────────────┘   ║
║                                       ║
║  ┌─────────────────────────────────┐   ║
║  │  ⚗️ BENEFICIADO          [3]    │   ║
║  │  Control de procesos            │   ║
║  └─────────────────────────────────┘   ║
║                                       ║
║  ┌─────────────────────────────────┐   ║
║  │  👥 PERSONAL             [23]   │   ║
║  │  Asistencia y pagos             │   ║
║  └─────────────────────────────────┘   ║
║                                       ║
║  [📊 Reportes] [⚙️ Config] [📤 Sync]  ║
╚═══════════════════════════════════════╝
```

### Formulario de Recolección
```
╔═══════════════════════════════════════╗
║ ← 🌱 NUEVA RECOLECCIÓN                ║
║                                       ║
║  Trabajador: Juan Pérez ✓             ║
║  ┌─────────────────────────────────┐   ║
║  │ 📷                  📍 GPS OK   │   ║
║  │                                 │   ║
║  │   [Foto del café recolectado]   │   ║
║  │                                 │   ║
║  └─────────────────────────────────┘   ║
║                                       ║
║  Cuerda: [📱 Escanear QR] A-01        ║
║  Variedad: Caturra                    ║
║                                       ║
║  Libras: [_____45_____] ⚖️            ║
║         └─ Deslizar para ajustar ─┘   ║
║                                       ║
║  Calidad: ⭐⭐⭐⭐⭐ (Excelente)       ║
║                                       ║
║  💰 Pago calculado: Q56.25            ║
║                                       ║
║  [❌ Cancelar]    [✅ GUARDAR]        ║
╚═══════════════════════════════════════╝
```

## 🔐 SEGURIDAD Y OFFLINE

### Estrategia Offline-First
```dart
class OfflineManager {
  // Guardar actividad offline
  Future<void> saveActivityOffline(Actividad actividad) async {
    actividad.sincronizado = false;
    actividad.timestampCreacion = DateTime.now().toIso8601String();
    
    await db.insertActividad(actividad);
    
    // Intentar sync inmediato si hay conexión
    if (await NetworkUtils.hasConnection()) {
      await ERPNextAPI().syncActividades();
    }
  }
  
  // Resolver conflictos de sincronización
  Future<void> resolveConflicts() async {
    final conflictos = await db.getConflictos();
    
    for (var conflicto in conflictos) {
      // Estrategia: el timestamp más reciente gana
      if (conflicto.timestampLocal.isAfter(conflicto.timestampServidor)) {
        await ERPNextAPI().updateActividad(conflicto);
      } else {
        await db.updateFromServer(conflicto);
      }
    }
  }
}
```

## 📊 MÉTRICAS Y ANALYTICS

### Dashboard en la App
```dart
class DashboardScreen extends StatelessWidget {
  Widget build(BuildContext context) {
    return Column(
      children: [
        // KPIs del día
        Row(
          children: [
            MetricCard(
              title: "Hoy",
              value: "245 lbs",
              icon: Icons.coffee,
              color: Colors.brown,
            ),
            MetricCard(
              title: "Esta semana", 
              value: "1,850 lbs",
              icon: Icons.trending_up,
              color: Colors.green,
            ),
          ],
        ),
        
        // Gráfico de productividad
        Container(
          height: 200,
          child: LineChart(
            // Datos de los últimos 7 días
            productividadSemanal,
          ),
        ),
        
        // Lista de actividades recientes
        Expanded(
          child: ListView.builder(
            itemBuilder: (context, index) {
              return ActividadCard(actividades[index]);
            },
          ),
        ),
      ],
    );
  }
}
```

Esta app móvil se integra perfectamente con el sistema ERPNext que ya creamos, proporcionando una interfaz intuitiva y robusta para el trabajo de campo.
