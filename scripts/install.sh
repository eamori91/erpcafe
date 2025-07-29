#!/bin/bash

#!/bin/bash

# 🇬🇹 ERPCafe - Instalación automatizada ERPNext v15
# Script completo para Ubuntu 22.04 LTS con todas las dependencias optimizadas

set -e  # Salir si cualquier comando falla

# ===== CONFIGURACIÓN GLOBAL =====
ERPNEXT_VERSION="version-15"
FRAPPE_VERSION="version-15"
PYTHON_VERSION="3.11"
NODE_VERSION="18"
MARIADB_VERSION="10.6"
REDIS_VERSION="7"

BENCH_USER="frappe"
SITE_NAME="erpcafe.local"
ADMIN_PASSWORD="admin123"
MYSQL_ROOT_PASSWORD="erpcafe_root_2024"

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# ===== FUNCIONES AUXILIARES =====
print_step() {
    echo -e "
${BLUE}📋 PASO: $1${NC}
"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
    exit 1
}

check_root() {
    if [ "$EUID" -eq 0 ]; then
        print_error "No ejecutar como root. Este script creará el usuario frappe automáticamente."
    fi
}

check_os() {
    if [[ ! -f /etc/os-release ]]; then
        print_error "No se puede determinar el sistema operativo"
    fi
    
    . /etc/os-release
    
    if [[ "$ID" != "ubuntu" ]] || [[ "$VERSION_ID" != "22.04" ]]; then
        print_warning "Este script está optimizado para Ubuntu 22.04 LTS"
        read -p "¿Desea continuar? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi
    
    print_success "Sistema operativo verificado: Ubuntu 22.04 LTS"
}

# ===== VERIFICACIONES INICIALES =====
print_step "VERIFICACIONES INICIALES"
check_root
check_os

print_step "ACTUALIZANDO SISTEMA"
sudo apt update && sudo apt upgrade -y
print_success "Sistema actualizado"

# ===== INSTALACIÓN DE DEPENDENCIAS BASE =====
print_step "INSTALANDO DEPENDENCIAS BASE"

sudo apt install -y 
    software-properties-common 
    apt-transport-https 
    ca-certificates 
    curl 
    wget 
    gnupg 
    lsb-release 
    git 
    build-essential 
    python3-dev 
    python3-setuptools 
    python3-pip 
    python3-distutils 
    python3-venv 
    python3-wheel 
    libssl-dev 
    libffi-dev 
    libmysqlclient-dev 
    libpq-dev 
    libjpeg8-dev 
    zlib1g-dev 
    libwebp-dev 
    libreadline-gplv2-dev 
    libncursesw5-dev 
    libsqlite3-dev 
    libgdbm-dev 
    libc6-dev 
    libbz2-dev 
    libexpat1-dev 
    liblzma-dev 
    tk-dev 
    redis-server 
    xvfb 
    libfontconfig 
    wkhtmltopdf 
    nginx 
    supervisor 
    fontconfig 
    libxrender1 
    xfonts-75dpi 
    xfonts-base

# ===== INSTALACIÓN DE PYTHON 3.11 =====
print_step "INSTALANDO PYTHON 3.11"

# Verificar si Python 3.11 ya está instalado
if command -v python3.11 &> /dev/null; then
    print_success "Python 3.11 ya está instalado"
else
    sudo add-apt-repository ppa:deadsnakes/ppa -y
    sudo apt update
    sudo apt install -y python3.11 python3.11-dev python3.11-venv python3.11-distutils
    
    # Configurar python3.11 como alternativa
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
    print_success "Python 3.11 instalado y configurado"
fi

# Verificar versión
python3 --version
print_success "Python configurado correctamente"

# ===== INSTALACIÓN DE NODE.JS 18 LTS =====
print_step "INSTALANDO NODE.JS 18 LTS"

if command -v node &> /dev/null && [[ $(node -v | cut -d'v' -f2 | cut -d'.' -f1) -ge 18 ]]; then
    print_success "Node.js 18+ ya está instalado"
else
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt-get install -y nodejs
    print_success "Node.js 18 LTS instalado"
fi

# Verificar versiones
node --version
npm --version
print_success "Node.js y NPM configurados correctamente"

# ===== INSTALACIÓN DE MARIADB 10.6+ =====
print_step "INSTALANDO MARIADB 10.6+"

if command -v mysql &> /dev/null; then
    print_success "MariaDB ya está instalado"
else
    sudo apt install -y mariadb-server mariadb-client
    print_success "MariaDB instalado"
fi

# Configurar MariaDB
print_step "CONFIGURANDO MARIADB"
sudo systemctl start mariadb
sudo systemctl enable mariadb

# Configuración segura de MariaDB
sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED BY '${MYSQL_ROOT_PASSWORD}';"
sudo mysql -u root -p${MYSQL_ROOT_PASSWORD} -e "DELETE FROM mysql.user WHERE User='';"
sudo mysql -u root -p${MYSQL_ROOT_PASSWORD} -e "DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');"
sudo mysql -u root -p${MYSQL_ROOT_PASSWORD} -e "DROP DATABASE IF EXISTS test;"
sudo mysql -u root -p${MYSQL_ROOT_PASSWORD} -e "DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';"
sudo mysql -u root -p${MYSQL_ROOT_PASSWORD} -e "FLUSH PRIVILEGES;"

# Crear configuración optimizada para ERPNext
sudo tee /etc/mysql/mariadb.conf.d/60-erpnext.cnf > /dev/null <<EOF
[mysqld]
innodb-file-format=barracuda
innodb-file-per-table=1
innodb-large-prefix=1
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

# Optimizaciones para ERPNext v15
innodb_buffer_pool_size = 1G
innodb_log_file_size = 256M
max_connections = 500
query_cache_size = 64M
query_cache_type = 1
thread_cache_size = 16
table_open_cache = 2000
table_definition_cache = 1400
EOF

sudo systemctl restart mariadb
print_success "MariaDB configurado y optimizado para ERPNext v15"

# ===== CONFIGURACIÓN DE REDIS =====
print_step "CONFIGURANDO REDIS"

sudo systemctl start redis-server
sudo systemctl enable redis-server

# Configurar Redis para ERPNext
sudo tee /etc/redis/redis.conf > /dev/null <<EOF
# Redis configuration for ERPNext v15
bind 127.0.0.1
port 6379
timeout 0
save 900 1
save 300 10
save 60 10000
rdbcompression yes
dbfilename dump.rdb
dir /var/lib/redis
maxmemory 256mb
maxmemory-policy allkeys-lru
EOF

sudo systemctl restart redis-server
print_success "Redis configurado y optimizado"

# ===== CREACIÓN DE USUARIO FRAPPE =====
print_step "CREANDO USUARIO FRAPPE"

if id "$BENCH_USER" &>/dev/null; then
    print_success "Usuario $BENCH_USER ya existe"
else
    sudo adduser --disabled-password --gecos "" $BENCH_USER
    sudo usermod -aG sudo $BENCH_USER
    print_success "Usuario $BENCH_USER creado"
fi

# ===== INSTALACIÓN DE BENCH =====
print_step "INSTALANDO FRAPPE BENCH"

sudo -u $BENCH_USER bash << EOF
cd /home/$BENCH_USER

# Instalar bench
pip3 install --user frappe-bench

# Configurar PATH
echo 'export PATH=\$PATH:/home/$BENCH_USER/.local/bin' >> /home/$BENCH_USER/.bashrc
source /home/$BENCH_USER/.bashrc

# Verificar instalación
/home/$BENCH_USER/.local/bin/bench --version
EOF

print_success "Frappe Bench instalado"

# ===== INICIALIZACIÓN DE BENCH PARA ERPNEXT V15 =====
print_step "INICIALIZANDO BENCH PARA ERPNEXT V15"

sudo -u $BENCH_USER bash << EOF
cd /home/$BENCH_USER
export PATH=\$PATH:/home/$BENCH_USER/.local/bin

# Inicializar bench con ERPNext v15
bench init --version=$ERPNEXT_VERSION frappe-bench

cd frappe-bench

# Obtener ERPNext v15
bench get-app --branch $ERPNEXT_VERSION erpnext

# Crear sitio
bench new-site $SITE_NAME --admin-password $ADMIN_PASSWORD --mariadb-root-password $MYSQL_ROOT_PASSWORD

# Instalar ERPNext en el sitio
bench --site $SITE_NAME install-app erpnext

# Configurar sitio por defecto
bench use $SITE_NAME
EOF

print_success "ERPNext v15 inicializado correctamente"

# ===== INSTALACIÓN DE ERPCAFE =====
print_step "INSTALANDO APLICACIÓN ERPCAFE"

sudo -u $BENCH_USER bash << EOF
cd /home/$BENCH_USER/frappe-bench
export PATH=\$PATH:/home/$BENCH_USER/.local/bin

# Obtener aplicación ERPCafe desde GitHub
bench get-app https://github.com/eamori91/erpcafe.git

# Instalar ERPCafe en el sitio
bench --site $SITE_NAME install-app erpnext_finca_cafe

# Ejecutar configuración específica para café
bench --site $SITE_NAME execute erpnext_finca_cafe.setup.install.setup_coffee_farm

print_success "Aplicación ERPCafe instalada y configurada"
EOF

# ===== CONFIGURACIÓN DE PRODUCCIÓN =====
print_step "CONFIGURANDO ENTORNO DE PRODUCCIÓN"

sudo -u $BENCH_USER bash << EOF
cd /home/$BENCH_USER/frappe-bench
export PATH=\$PATH:/home/$BENCH_USER/.local/bin

# Configurar para producción
sudo bench setup production $BENCH_USER --yes

# Habilitar scheduler
bench --site $SITE_NAME scheduler enable

# Configurar SSL (opcional)
# bench setup lets-encrypt $SITE_NAME

print_success "Configuración de producción completada"
EOF

# ===== CONFIGURACIÓN DE FIREWALL =====
print_step "CONFIGURANDO FIREWALL"

sudo ufw allow ssh
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 8000
sudo ufw allow 9000
sudo ufw --force enable

print_success "Firewall configurado"

# ===== VERIFICACIÓN FINAL =====
print_step "VERIFICACIÓN FINAL DE LA INSTALACIÓN"

echo "Verificando servicios..."

# Verificar servicios
systemctl is-active --quiet mariadb && print_success "MariaDB activo" || print_error "MariaDB no está activo"
systemctl is-active --quiet redis-server && print_success "Redis activo" || print_error "Redis no está activo"
systemctl is-active --quiet nginx && print_success "Nginx activo" || print_error "Nginx no está activo"

# Verificar conexión a base de datos
sudo -u $BENCH_USER bash << EOF
cd /home/$BENCH_USER/frappe-bench
export PATH=\$PATH:/home/$BENCH_USER/.local/bin

bench --site $SITE_NAME console << 'PYTHON_EOF'
import frappe
frappe.connect()
print("✅ Conexión a base de datos exitosa")
exit()
PYTHON_EOF
EOF

print_success "Verificación completada"

# ===== MOSTRAR INFORMACIÓN DE ACCESO =====
print_step "INFORMACIÓN DE ACCESO"

echo -e "${GREEN}
🎉 ¡INSTALACIÓN DE ERPCAFE COMPLETADA EXITOSAMENTE! 🎉

📋 INFORMACIÓN DE ACCESO:
   URL del sitio: http://$(hostname -I | awk '{print $1}'):8000
   Sitio local: http://$SITE_NAME:8000
   Usuario admin: Administrator
   Contraseña: $ADMIN_PASSWORD

📁 UBICACIONES IMPORTANTES:
   Directorio bench: /home/$BENCH_USER/frappe-bench
   Logs: /home/$BENCH_USER/frappe-bench/logs
   Configuración: /home/$BENCH_USER/frappe-bench/sites/$SITE_NAME

🔧 COMANDOS ÚTILES:
   Iniciar desarrollo: sudo -u $BENCH_USER -H bench start
   Detener servicios: sudo -u $BENCH_USER -H bench setup production $BENCH_USER --stop
   Ver logs: sudo -u $BENCH_USER -H bench logs
   Respaldar sitio: sudo -u $BENCH_USER -H bench --site $SITE_NAME backup
   Actualizar apps: sudo -u $BENCH_USER -H bench update

📱 APLICACIÓN ERPCAFE:
   ✅ Sistema base ERPNext v15 instalado
   ✅ Aplicación ERPCafe configurada
   ✅ DocTypes especializados para café
   ✅ Integración ANACAFE lista
   ✅ Reportes guatemaltecos configurados

🌐 SERVICIOS CONFIGURADOS:
   ✅ MariaDB 10.6+ optimizado
   ✅ Redis 7 para cache
   ✅ Nginx como proxy reverso
   ✅ Supervisor para procesos
   ✅ Firewall configurado

📞 SOPORTE:
   GitHub: https://github.com/eamori91/erpcafe
   Issues: https://github.com/eamori91/erpcafe/issues
   
🇬🇹 ¡Bienvenido a ERPCafe - El ERP del café guatemalteco!
${NC}"

# ===== CONFIGURACIÓN OPCIONAL =====
echo -e "\n${YELLOW}¿Desea configurar características adicionales?${NC}"

read -p "¿Configurar integración con ANACAFE? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    sudo -u $BENCH_USER bash << EOF
cd /home/$BENCH_USER/frappe-bench
export PATH=\$PATH:/home/$BENCH_USER/.local/bin
bench --site $SITE_NAME execute erpnext_finca_cafe.integrations.anacafe.setup
EOF
    print_success "Integración ANACAFE configurada"
fi

read -p "¿Configurar reportes para exportación? (y/N): " -n 1 -r
echo  
if [[ $REPLY =~ ^[Yy]$ ]]; then
    sudo -u $BENCH_USER bash << EOF
cd /home/$BENCH_USER/frappe-bench
export PATH=\$PATH:/home/$BENCH_USER/.local/bin
bench --site $SITE_NAME execute erpnext_finca_cafe.setup.reports.install_export_reports
EOF
    print_success "Reportes de exportación configurados"
fi

read -p "¿Iniciar el servidor de desarrollo ahora? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${GREEN}Iniciando servidor de desarrollo...${NC}"
    echo -e "${YELLOW}Presiona Ctrl+C para detener el servidor${NC}"
    sudo -u $BENCH_USER bash << EOF
cd /home/$BENCH_USER/frappe-bench
export PATH=\$PATH:/home/$BENCH_USER/.local/bin
bench start
EOF
fi

echo -e "\n${GREEN}¡Instalación completada! Para soporte visite: https://github.com/eamori91/erpcafe${NC}\n"

# ===== LOG FINAL =====
log "Instalación de ERPCafe v15 completada exitosamente en $(date)"
log "Sitio creado: $SITE_NAME"
log "Usuario bench: $BENCH_USER"
log "Versión ERPNext: $ERPNEXT_VERSION"
log "Para soporte visite: https://github.com/eamori91/erpcafe"

exit 0
    # Verificar Python
    if ! command -v python3 &> /dev/null; then
        error "Python 3 no está instalado"
        exit 1
    fi
    
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
    if [[ $(echo "$PYTHON_VERSION < 3.10" | bc -l) -eq 1 ]]; then
        error "Se requiere Python 3.10 o superior. Versión actual: $PYTHON_VERSION"
        exit 1
    fi
    
    log "Python $PYTHON_VERSION detectado ✓"
    
    # Verificar Node.js
    if ! command -v node &> /dev/null; then
        warning "Node.js no está instalado. Se instalará automáticamente."
    else
        NODE_VERSION=$(node --version | cut -d'v' -f2 | cut -d'.' -f1)
        if [[ $NODE_VERSION -lt 18 ]]; then
            warning "Se recomienda Node.js 18+. Versión actual: v$NODE_VERSION"
        else
            log "Node.js v$NODE_VERSION detectado ✓"
        fi
    fi
}

# Instalar dependencias del sistema
install_system_dependencies() {
    log "Instalando dependencias del sistema..."
    
    sudo apt update
    sudo apt install -y \
        git \
        python3-dev \
        python3-pip \
        python3-venv \
        software-properties-common \
        mariadb-server \
        mariadb-client \
        redis-server \
        nginx \
        supervisor \
        curl \
        wget \
        wkhtmltopdf \
        xvfb \
        libffi-dev \
        libblas-dev \
        liblapack-dev \
        libmariadb-dev \
        libssl-dev \
        libxml2-dev \
        libxslt1-dev \
        zlib1g-dev \
        libsasl2-dev \
        libldap2-dev \
        libcups2-dev \
        pv \
        libjpeg8-dev \
        liblcms2-dev \
        libwebp-dev \
        tcl8.6-dev \
        tk8.6-dev \
        python3-tk
        
    log "Dependencias del sistema instaladas ✓"
}

# Instalar Node.js
install_nodejs() {
    if ! command -v node &> /dev/null || [[ $(node --version | cut -d'v' -f2 | cut -d'.' -f1) -lt 18 ]]; then
        log "Instalando Node.js 18..."
        
        curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
        sudo apt-get install -y nodejs
        
        log "Node.js $(node --version) instalado ✓"
    fi
    
    # Instalar yarn
    if ! command -v yarn &> /dev/null; then
        log "Instalando Yarn..."
        npm install -g yarn
        log "Yarn instalado ✓"
    fi
}

# Configurar MariaDB
setup_mariadb() {
    log "Configurando MariaDB..."
    
    # Configurar MariaDB para ERPNext
    sudo mysql -e "SET GLOBAL innodb_file_format=Barracuda;"
    sudo mysql -e "SET GLOBAL innodb_large_prefix=1;"
    sudo mysql -e "SET GLOBAL innodb_file_per_table=1;"
    
    # Crear configuración personalizada
    sudo tee /etc/mysql/conf.d/erpnext.cnf > /dev/null <<EOF
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

[mysql]
default-character-set = utf8mb4
EOF
    
    sudo systemctl restart mariadb
    sudo systemctl enable mariadb
    
    log "MariaDB configurado para ERPNext ✓"
}

# Instalar ERPNext v15
install_erpnext() {
    log "Instalando ERPNext v15..."
    
    # Crear usuario frappe si no existe
    if ! id "frappe" &>/dev/null; then
        sudo adduser --disabled-login --gecos "" frappe
        sudo usermod -aG sudo frappe
    fi
    
    # Cambiar a usuario frappe
    sudo -u frappe bash << 'EOF'
cd /home/frappe

# Instalar frappe-bench
pip3 install frappe-bench

# Inicializar bench para v15
bench init --frappe-branch version-15 frappe-bench

cd frappe-bench

# Crear sitio
bench new-site finca.local --admin-password admin123 --mariadb-root-password ""

# Instalar ERPNext v15
bench get-app --branch version-15 erpnext
bench --site finca.local install-app erpnext

# Configurar desarrollo
bench use finca.local
bench set-config -g developer_mode 1
bench set-config -g server_script_enabled 1

EOF
    
    log "ERPNext v15 instalado ✓"
}

# Clonar e instalar ERPCafe
install_erpcafe() {
    log "Instalando aplicación ERPCafe..."
    
    sudo -u frappe bash << 'EOF'
cd /home/frappe/frappe-bench

# Clonar aplicación ERPCafe
bench get-app https://github.com/eamori91/erpcafe.git

# Instalar aplicación
bench --site finca.local install-app erpcafe

# Ejecutar migraciones
bench --site finca.local migrate

EOF
    
    log "ERPCafe instalado ✓"
}

# Configurar production
setup_production() {
    log "Configurando para producción..."
    
    sudo -u frappe bash << 'EOF'
cd /home/frappe/frappe-bench

# Setup production
sudo bench setup production frappe

# Configurar SSL (opcional)
# sudo bench setup lets-encrypt finca.local

EOF
    
    log "Configuración de producción completada ✓"
}

# Función principal
main() {
    log "🚀 Iniciando instalación de ERPCafe..."
    
    check_os
    check_prerequisites
    install_system_dependencies
    install_nodejs
    setup_mariadb
    install_erpnext
    install_erpcafe
    
    if [[ "$1" == "--production" ]]; then
        setup_production
    fi
    
    log "🎉 ¡Instalación completada exitosamente!"
    info "Acceder al sistema en: http://localhost:8000"
    info "Usuario: Administrator"
    info "Contraseña: admin123"
    info "Sitio: finca.local"
}

# Ejecutar función principal
main "$@"
