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
        VALUES ('ASI', 0.18),
        ('AVALIAN', 0.05),
        ('ASMEPRIV', 0.21),
        ('BRISTOL MEDICINE', 0.21),
        ('CASA', 0.10),
        ('GALENO', 0.17),
        ('SWISS MEDICAL', 0.17),
        ('OSDE', 0.17),
        ('LUIS PASTEUR', 0.18),
        ('UNION PERSONAL', 0.13),
        ('POLICIA FEDERAL', 0.125),
        ('OSRJA', 0.21),
        ('OSPIHMP', 0.18),
        ('OSPE', 0.18),
        ('OSPA', 0.18),
        ('OSPETELCO', 0.18),
        ('OSDOP', 0.19),
        ('JUBILADOS TELEFONICOS', 0.18),
        ('OSPPCYQ', 0.19),
        ('WILLIAM HOPE', 0.18),
        ('MEDIFE', 0.1),
        ('OSMATA', 0.16),
        ('PODER JUDICIAL', 0.15),
        ('BANCO PROVINCIA', 0.08),
        ('SAMI', 0.18),
        ('OMINT', 0.19),
        ('OSPATCA', 0.15),
        ('RECETARIO SOLIDARIO', 0.1)
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