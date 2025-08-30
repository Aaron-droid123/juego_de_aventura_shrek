import mysql.connector

config= {
    'user':'root',
    'password':'cuentodeaventura123',
    'host' : 'localhost',
    'database' : 'shrekdb',
    'raise_on_warnings' : True
}
try:
    conexion= mysql.connector.Connect(**config)
    print("conexion exitosa")
    
    cursor= conexion.cursor()

    
    # cursor.execute("SELECT * FROM objeto")
    #resultados = cursor.fetchall()
    #for fila in resultados:
     
     #   print(fila)
except mysql.connector.Error as err:
    print(f"error: {err}")
def close_db():
    if conexion is not None and conexion.is_connected():
        cursor.close()
        conexion.close()
        print("conexion cerrada")
