from database import connect_db
import csv
import os

UPLOAD_FOLDER = "logs"

def process_csv(file_path):
    """Lee un archivo CSV e inserta los datos en la base de datos."""
    if not os.path.exists(file_path):
        print("El archivo no existe.")
        return

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("USE capstone_db")  # Usar la base de datos correcta

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Saltar encabezado si tiene
        for row in reader:
            cursor.execute("""
                INSERT INTO incidents (source_ip, destination_ip, protocol, action_taken)
                VALUES (%s, %s, %s, %s)
            """, row)

    conn.commit()
    conn.close()
    print("Datos insertados en la base de datos.")

if __name__ == "__main__":
    file_name = input("Ingresa el nombre del archivo CSV dentro de 'logs/': ")
    file_path = os.path.join(UPLOAD_FOLDER, file_name)
    process_csv(file_path)