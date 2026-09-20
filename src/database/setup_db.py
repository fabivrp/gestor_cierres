import sqlite3

def inicializar_base_datos():
    conexion = sqlite3.connect('farmacia_conciliacion.db')
    cursor = conexion.cursor()

    # Tabla 1: Obras Sociales 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS obras_sociales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL,
            porcentaje_comision REAL NOT NULL
        )
    ''')

    # Tabla 2: Alias
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alias_obras_sociales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            obra_social_id INTEGER,
            alias TEXT NOT NULL,
            FOREIGN KEY (obra_social_id) REFERENCES obras_sociales (id)
        )
    ''')

    # Tabla 3: Cierres 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cierres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            obra_social_id INTEGER,
            fecha_cierre DATE, 
            periodo TEXT, 
            numero_presentacion TEXT,
            monto_total REAL,
            monto_obra_social REAL,
            pago_esperado REAL,
            estado TEXT DEFAULT 'Pendiente',
            FOREIGN KEY (obra_social_id) REFERENCES obras_sociales (id)
        )
    ''')

    # Tabla 4: Pagos 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pagos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cierre_id INTEGER,
            monto_recibido REAL,
            fecha_recibido DATE,
            origen_pago TEXT,
            tipo_documento TEXT,
            FOREIGN KEY (cierre_id) REFERENCES cierres (id)
        )
    ''')

    conexion.commit()
    conexion.close()
    print("Base de datos y tablas creadas exitosamente")

if __name__ == '__main__':
    inicializar_base_datos()