# Capstone Project - Ciberseguridad

Este proyecto se enfoca en el procesamiento y almacenamiento de incidentes de seguridad informática relacionados con ataques a una red. Está diseñado para ser una herramienta simple que recibe archivos CSV con registros de incidentes y los almacena en una base de datos MySQL.

## Contenido

- **`app.py`**: Archivo principal que procesa archivos CSV con incidentes de seguridad y los guarda en una base de datos MySQL.
- **`database.py`**: Funciones para la gestión de la base de datos MySQL.
- **`logs/`**: Carpeta que contiene los archivos CSV con los registros de incidentes.
- **`README.md`**: Documentación del proyecto.
- **`requirements.txt`**: Dependencias del proyecto.

## Requisitos

- Python 3.x
- MySQL
- Librerías:
  - `mysql-connector-python`
  - `csv`
  - `os`
  - `datetime`

## Instalación

1. Clona el repositorio:
    git clone https://github.com/AbelardoCarcamo/CapstoneProject.git
2. Instala las dependencias:
    pip install -r requirements.txt
3. Configura tu base de datos MySQL con las tablas necesarias.
4. Coloca tus archivos CSV en la carpeta logs/.
5. Ejecuta el archivo app.py para procesar los incidentes:
    python app.py

Licencia

Este proyecto es de uso personal. Cualquier uso comercial o distribución requiere mi permiso explícito.