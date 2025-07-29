# ERPCafe - Copilot Instructions

ERPCafe is a specialized ERPNext v15 system for Guatemalan coffee farms, automating operations from cultivation to international export while ensuring compliance with local regulations (ANACAFE, MAGA, BANGUAT).

## Architecture Overview

**Framework**: ERPNext v15 on Frappe v15 with Guatemala-specific customizations
- **Core Pattern**: DocType-driven metadata architecture with Python controllers
- **Database**: MariaDB 10.6+ with Guatemala-optimized configurations
- **Stack**: Ubuntu 22.04, Python 3.11+, Node.js 18 LTS, Redis 7
- **Deployment**: Docker Compose with monitoring (Prometheus/Grafana)

## Critical Coffee Workflow

The system models Guatemala's coffee processing chain:
```
Campo (Actividad de Campo) → Fermentación → Patio Secado → Secadora → Bodega
```

Each stage creates **DocTypes** with automatic lot tracking using format: `{fecha}-{unidad}-{sequential}`

## Key DocTypes and Business Logic

### Core DocTypes (see `erpnext_setup_finca_completo.py`)
- **`Unidad de Trabajo`**: Land parcels using Guatemalan measurements (varas to meters conversion)
- **`Actividad de Campo`**: Field activities with automatic salary minimum verification 
- **`Adelantos y Prestamos`**: Employee advances/loans with legal compliance tracking
- **`Fermentacion`**: Coffee fermentation control (pH, temperature, timing)
- **`Patio Secado`**: Sun drying with humidity control
- **`Secadora`**: Mechanical drying with temperature limits

### Critical Business Rules
1. **Salary Compliance**: Every payment must meet Guatemala's minimum wage (Q112.99/day CE2)
2. **Traceability**: Automatic lot ID generation preserves farm-to-export tracking
3. **Guatemala Measurements**: Land measured in "cuerdas" (25x25 or 40x40 varas), auto-converted to m²
4. **ANACAFE Integration**: Lot codes follow `GT-YYYY-FFFF-LLLL` format for export compliance

## Development Patterns

### DocType Creation Pattern
```python
# Standard pattern in setup scripts
if frappe.db.exists("DocType", "DocType Name"):
    print("⚠️  DocType already exists")
    return

doc = frappe.get_doc({
    "doctype": "DocType",
    "name": "DocType Name",
    "module": "Custom",
    "custom": 1,
    "naming_rule": "Expression (old style)",
    "autoname": "format:PREFIX-{field}-{#####}",
    "fields": [...]
})
doc.insert()
```

### ERPNext v15 Field Types
Use new v15 field types for enhanced functionality:
- `Duration`: For fermentation/drying times
- `JSON`: For quality control data  
- `Rating`: For coffee quality scores (1-5 stars)
- `Geolocation`: For farm locations
- `Barcode`: For traceability codes

### Guatemala-Specific Calculations
```python
# Vara to meter conversion (1 vara = 0.835 meters)
if doc.area_varas2:
    doc.area_metros2 = doc.area_varas2 * (0.835 ** 2)

# Salary minimum verification
if doc.pago_generado < SALARIO_MINIMO_DIARIO:
    doc.complemento_salarial = SALARIO_MINIMO_DIARIO - doc.pago_generado
```

## Installation and Setup

### Development Setup
```bash
# Full installation
chmod +x scripts/install.sh
sudo ./scripts/install.sh

# ERPNext v15 configuration
python3 scripts/erpnext_v15_config.py

# Apply coffee farm setup
bench --site erpcafe.local execute erpnext_setup_finca_completo.py
```

### Docker Development
```bash
cp .env.example .env
docker-compose up -d
# Access: http://localhost:8000
```

## Project Structure

```
src/erpnext_finca_cafe/     # Main app module
├── doctypes/               # Custom DocType definitions
├── dashboards/             # Coffee-specific dashboards  
├── reports/               # Guatemala export reports
└── integrations/          # ANACAFE/MAGA API connections

mobile_app/                # Flutter 3.x mobile app (prepared)
scripts/                   # Installation and config scripts
docs/                     # Technical documentation
```

## Critical Configuration Files

- **`package.json`**: Frappe v15 hooks, custom JS/CSS includes
- **`requirements.txt`**: Python 3.11+ dependencies for coffee analytics
- **`docker-compose.yml`**: Full production stack with monitoring
- **`.env.example`**: Guatemala-specific environment variables

## Testing Key Workflows

1. **Employee Payment Flow**: Create `Actividad de Campo` → verify automatic salary minimum calculation
2. **Coffee Processing**: Test complete fermentation → drying → storage chain with lot tracking
3. **ANACAFE Compliance**: Verify lot code generation and contribution calculations (Q1.00 + Q0.15/quintal)
4. **Mobile Sync**: Test offline data collection and synchronization

## Debugging Common Issues

- **DocType Creation Fails**: Always check `frappe.db.exists()` before creation
- **Salary Calculation Errors**: Verify Guatemala salary constants in environment
- **Lot Tracking Breaks**: Check server scripts for automatic lote_id generation
- **ANACAFE Integration**: Validate API credentials and format compliance

Use `bench logs` to monitor Frappe errors and `docker-compose logs erpnext` for container issues.
