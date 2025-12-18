import mysql.connector

config= {
    'user':'root',
    'password':'cuentodeaventura123',
    'host' : 'localhost',
    'database' : 'shrekdb',
    'raise_on_warnings' : True
}
"""try:
    conexion= mysql.connector.Connect(**config)
    print("conexion exitosa")
    
    cursor= conexion.cursor()

    
    # cursor.execute("SELECT * FROM objeto")
    #resultados = cursor.fetchall()
    #for fila in resultados:
     
     #   print(fila)
except mysql.connector.Error as err:
    print(f"error: {err}")"""
conexion = None
cursor = None
def close_db():
    global conexion, cursor
    if conexion is not None and conexion.is_connected():
        cursor.close()
        conexion.close()
        print("conexion cerrada")

def reconectar_db():
    global conexion, cursor
    try:
        if conexion is not None and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("conexion cerrada, reconectando...")
        conexion= mysql.connector.Connect(**config)
        cursor= conexion.cursor()

    
    # cursor.execute("SELECT * FROM objeto")
    #resultados = cursor.fetchall()
    #for fila in resultados:
     
     #   print(fila)
    except mysql.connector.Error as err:
        print(f"error: {err}")
def conectar_db():
    global conexion, cursor
    try:
        conexion= mysql.connector.Connect(**config)
        cursor= conexion.cursor()
    except mysql.connector.Error as err:
        print(f"error: {err}")
def verificar_conexion_db():
    global conexion
    if conexion is None:
        print("sin conexion")
    try:
        if conexion.is_connected():
            print("conexion activa")
        else:
            print("cnexion inactiva")
    except:
        print("error verificando conexion")
