# 🇬🇹 ERPCafe - Dockerfile para ERPNext v15
# Imagen Docker optimizada para sistema de gestión de fincas cafetaleras

FROM ubuntu:22.04

# Metadata
LABEL maintainer="ERPNext Guatemala Coffee Solutions <info@erpcafe.gt>"
LABEL version="3.0.0"
LABEL description="ERPNext v15 para gestión integral de fincas cafetaleras guatemaltecas"
LABEL vendor="ERPCafe Guatemala"

# Variables de entorno
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV TZ=America/Guatemala

# Configuración específica ERPNext v15
ENV ERPNEXT_VERSION=15
ENV FRAPPE_VERSION=15
ENV PYTHON_VERSION=3.11
ENV NODE_VERSION=18
ENV MARIADB_VERSION=10.6

# Directorio de trabajo
WORKDIR /home/frappe

# Actualizar sistema y instalar dependencias base
RUN apt-get update && apt-get install -y \
    # Dependencias del sistema
    software-properties-common \
    ca-certificates \
    curl \
    wget \
    gnupg \
    lsb-release \
    apt-transport-https \
    # Herramientas de desarrollo
    git \
    build-essential \
    python3.11 \
    python3.11-dev \
    python3.11-venv \
    python3-pip \
    # Dependencias de base de datos
    mariadb-client \
    libmariadb-dev \
    # Dependencias de Redis
    redis-tools \
    # Dependencias web
    nginx \
    supervisor \
    # Dependencias de archivos
    libffi-dev \
    libjpeg-dev \
    libpng-dev \
    libwebp-dev \
    libzip-dev \
    # Dependencias de sistema
    cron \
    vim \
    nano \
    htop \
    tmux \
    # Limpiar cache
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar Node.js 18 LTS
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

# Verificar versiones instaladas
RUN python3.11 --version \
    && node --version \
    && npm --version

# Crear usuario frappe
RUN useradd -m -s /bin/bash frappe \
    && usermod -aG sudo frappe \
    && echo "frappe ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Cambiar a usuario frappe
USER frappe

# Instalar bench (ERPNext CLI)
RUN pip3 install --user frappe-bench

# Configurar PATH para frappe
ENV PATH="/home/frappe/.local/bin:$PATH"

# Inicializar bench para ERPNext v15
RUN bench init --version=version-15 frappe-bench \
    && cd frappe-bench \
    && bench get-app --branch version-15 erpnext

# Configurar directorio de trabajo
WORKDIR /home/frappe/frappe-bench

# Copiar archivos de configuración
COPY --chown=frappe:frappe requirements.txt .
COPY --chown=frappe:frappe package.json .
COPY --chown=frappe:frappe scripts/ ./scripts/
COPY --chown=frappe:frappe src/ ./apps/erpnext_finca_cafe/

# Instalar dependencias de Python
RUN pip3 install -r requirements.txt

# Instalar aplicación ERPCafe
RUN bench get-app erpnext_finca_cafe ./apps/erpnext_finca_cafe

# Configurar sitio
ARG SITE_NAME=erpcafe.local
ENV SITE_NAME=${SITE_NAME}

# Crear sitio ERPNext
RUN bench new-site ${SITE_NAME} \
    --admin-password=admin123 \
    --mariadb-root-password=root123 \
    --install-app erpnext \
    --install-app erpnext_finca_cafe

# Configurar desarrollo
RUN bench use ${SITE_NAME} \
    && bench set-config developer_mode 1 \
    && bench set-config server_script_enabled 1

# Configurar puertos
EXPOSE 8000 9000

# Configurar volúmenes
VOLUME ["/home/frappe/frappe-bench/sites", "/home/frappe/frappe-bench/logs"]

# Configurar supervisor
COPY --chown=frappe:frappe docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Script de inicio
COPY --chown=frappe:frappe docker/start.sh /home/frappe/start.sh
RUN chmod +x /home/frappe/start.sh

# Comando por defecto
CMD ["/home/frappe/start.sh"]

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8000 || exit 1

# Labels adicionales
LABEL org.opencontainers.image.title="ERPCafe Guatemala"
LABEL org.opencontainers.image.description="Sistema ERPNext v15 para fincas cafetaleras guatemaltecas"
LABEL org.opencontainers.image.version="3.0.0"
LABEL org.opencontainers.image.created="2025-07-XX"
LABEL org.opencontainers.image.source="https://github.com/eamori91/erpcafe"
LABEL org.opencontainers.image.licenses="MIT"
