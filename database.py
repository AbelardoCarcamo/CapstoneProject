import mysql.connector
import os
import csv
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "capstone_db")

def connect_db():
    """Conecta a la base de datos MySQL y devuelve la conexión."""
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return conn

def create_database():
    """Crea la base de datos si no existe."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    conn.commit()
    conn.close()

def create_table():
    """Crea la tabla incidents si no existe."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INT AUTO_INCREMENT PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            source_ip VARCHAR(15),
            destination_ip VARCHAR(15),
            protocol VARCHAR(10),
            action_taken VARCHAR(50)
        )
    """)
    conn.commit()
    conn.close()

def insert_incident(source_ip, destination_ip, protocol, action_taken):
    """Inserta un incidente en la base de datos."""
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()
    query = """
        INSERT INTO incidents (source_ip, destination_ip, protocol, action_taken)
        VALUES (%s, %s, %s, %s)
    """
    values = (source_ip, destination_ip, protocol, action_taken)
    cursor.execute(query, values)
    conn.commit()
    conn.close()

import os
import csv
import mysql.connector
from datetime import datetime

import os
import csv
import mysql.connector
from datetime import datetime

import os
import csv
import mysql.connector
from datetime import datetime

import os
import csv
import mysql.connector
from datetime import datetime

# Función para procesar el CSV
def process_csv(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, mode='r') as file:
                csv_reader = csv.reader(file)
                headers = next(csv_reader)  # Leer los encabezados
                print(f"Encabezados: {headers}")
                
                # Conectar a la base de datos
                connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='Herme0110*',  # Asegúrate de usar la contraseña correcta
                    database='security_db'
                )
                cursor = connection.cursor()

                # Procesar cada fila en el archivo CSV
                for row in csv_reader:
                    print(f"Procesando fila: {row}")
                    # Inserta los datos en la tabla 'incidents'
                    cursor.execute("""
                        INSERT INTO incidents (source_ip, destination_ip, protocol, action_taken)
                        VALUES (%s, %s, %s, %s)
                    """, (row[0], row[1], row[2], row[3]))
                    connection.commit()

                print("Archivo CSV procesado correctamente.")
                
        except Exception as e:
            print(f"Error procesando el archivo CSV: {e}")
        finally:
            # Cerrar la conexión con la base de datos
            cursor.close()
            connection.close()

            # Renombrar el archivo para evitar duplicados, después de cerrar la conexión
            try:
                new_file_name = file_path.replace(".csv", f"_{datetime.now().strftime('%Y%m%d_%H%M%S')}.old")
                os.rename(file_path, new_file_name)
                print(f"Archivo renombrado a: {new_file_name}")
            except Exception as e:
                print(f"Error renombrando el archivo: {e}")
    else:
        print(f"El archivo {file_path} no existe.")

# Llamar a la función con la ruta del archivo CSV
process_csv('logs/incidents.csv')  # Asegúrate de que el archivo CSV esté en la carpeta correcta

# Ejecutar al iniciar
create_database()
create_table()
process_csv('logs/incidents.csv')  # Asegúrate de que el archivo CSV esté en la carpeta correcta