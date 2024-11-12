# Usamos la imagen de Python 3.9 slim, que es más ligera
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Instalamos las dependencias del sistema necesarias para MariaDB y otros
RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
    gcc \
    libpq-dev \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

# Copiamos el archivo de requerimientos de Python desde la carpeta backend
COPY backend/requirements.txt ./

# Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el archivo supervisord.conf desde la carpeta backend
COPY backend/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Copiamos el resto del proyecto desde la raíz (incluyendo manage.py)
COPY . .

# Exponemos el puerto 8000 para acceder al servidor Django
EXPOSE 8000

# Usamos Supervisor para ejecutar tanto el servidor Django como el procesador de tareas
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"] 

