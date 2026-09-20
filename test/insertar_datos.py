import sqlite3
from pathlib import Path

def cargar_datos_iniciales():
 
    directorio_actual = Path(__file__).parent
    
   
    ruta_db = directorio_actual.parent / 'data' / 'farmacia_conciliacion.db'
    

    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    
    # 1: INSERTAR DATOS
    # chequear lo del porcentaje porque no recuerdo
    try:
        cursor.execute('''
        INSERT INTO obras_sociales (nombre, porcentaje_comision) 
        VALUES ('OSDEPYM', 0.15)
        ''')
        conexion.commit()
        print("Obra social agregada con éxito.\n")
    except sqlite3.IntegrityError:
        print("La obra social ya estaba registrada.\n")

    # 2: CONSULTAR DATOS
    cursor.execute('SELECT id, nombre, porcentaje_comision FROM obras_sociales')

    obras = cursor.fetchall()

    print("--- LISTA DE OBRAS SOCIALES ---")
    for obra in obras:
      
        print(f"ID: {obra[0]} | Nombre: {obra[1]} | Comisión: {obra[2]*100}%")

    conexion.close()

if __name__ == '__main__':
    cargar_datos_iniciales()