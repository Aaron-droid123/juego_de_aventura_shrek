# contraseña: cuentodeaventura123
# usuario: root
import random
import time
import sys
import conexion_DB
from cuento_de_Aventura_Shrek import Personaje, Objeto, Inventario, Enemigo
from cuento_de_aventura_equipos import equipos_explorar, equipos_tienda
"""conexion_DB.cursor.execute("SELECT * FROM objeto")
resultados = conexion_DB.cursor.fetchall()
for fila in resultados:
    print(fila)
conexion_DB.close_db()"""
# nombre = input("ingresar nombre de tu personaje")
# while len(nombre) < 2:
#    nombre = input("ingresar nombre de tu personaje")
personaje_principal = ""
enemigos_lista = ""
vida_total = 150
ataque_total = 15
defensa_total = 6

tienda = equipos_tienda().equipo()
def validar_input_cadenas(message):
    while True:
        mensaje = input(message)
        if not len(mensaje) < 2:
            print("cadena valido")
            return mensaje
        else:
            print("cadena incorrecta o vacia")
def validar_input_opcion(max_opc):
    while True:
        opcion = input("ingrese una opcion")
        if not opcion:
            print("no se permite entrada vacia")
            continue
        if not opcion.isdigit():
            print("solo se permiten numeros enteros")
            continue
        opcion = int(opcion)
        if 1 <= opcion <= max_opc:
            print("numero valido")
            return opcion
        else: 
            print("numero fuera de rango") 
def elegir_personaje(): 
    global personaje_principal
    print("<<<<BIENVENIDO AL JUEGO>>>>") 
    print("1. CREAR PERSONAJE") 
    print("2. USAR PERSONAJE") 
    opcion = validar_input_opcion(2) 
    if opcion == 1: 
       personaje_principal = crear_personaje()
    if opcion == 2:
       personaje_principal = usar_personaje()

def crear_personaje():
    quary= """SELECT * FROM inventario ORDER BY inventario DESC LIMIT 1""" 
    
    conexion_DB.conectar_db()
    conexion_DB.cursor.execute(quary)
    resultados = conexion_DB.cursor.fetchall()
    quary= """INSERT INTO inventario(inventario, objetoID) VALUES(%s, %s)"""
    valores= (resultados[0][1] + 1,1)
    conexion_DB.conectar_db()
    conexion_DB.cursor.execute(quary, valores)
    conexion_DB.conexion.commit()
    # IDinventario = conexion_DB.cursor.lastrowid
    nombre = validar_input_cadenas("ingresar nombre de tu personaje")
    stick = Objeto("espada stick", 2, 4, 1, "comun","equipos", 5)
    quary = """INSERT INTO personaje(nombre, ataque, defensa, vida, monedas, casco, armadura, guantes, botas, espada, inventarioID) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    valores = (nombre, ataque_total, defensa_total, vida_total, 100, 0, 0, 0, 0, 1, resultados[0][1]+ 1)
    conexion_DB.cursor.execute(quary, valores)
    conexion_DB.conexion.commit()
    conexion_DB.close_db()
    personaje_principal = Personaje(nombre, vida_total, ataque_total, defensa_total,100, stick, resultados[0][1]+ 1)
    return personaje_principal

def usar_personaje():
    print("<<<<<PERSONAJES>>>>")
    conexion_DB.conectar_db()
    conexion_DB.cursor.execute("SELECT * FROM personaje")
    resultados = conexion_DB.cursor.fetchall()
    personaje_principal = ""
    for fila in resultados:
        print(f"nombre: {fila[1]}", end=' - ')
        print(f"dano: {fila[2]}")
    # conexion_DB.close_db()
    pregunta = validar_input_cadenas("ingrese el nombre del jugador que usara")
    for personaje in resultados:
        if personaje[1] == pregunta:
            conexion_DB.cursor.execute("SELECT * FROM objeto")
            resultados = conexion_DB.cursor.fetchall()
            conexion_DB.close_db()
            stick = ""
            for lit in resultados:
                if int(lit[0]) == personaje[10]:
                    stick = Objeto(lit[1], lit[2], lit[3], lit[4], lit[5], lit[6], lit[7])
            personaje_principal = Personaje(personaje[1], personaje[4], personaje[2], personaje[3],personaje[5], stick, personaje[11])
    if personaje_principal == "":
        print("ingrese un personaje correcto")
        personaje_principal = usar_personaje()

    return personaje_principal

def iniciar_juego():
    menu_principal()
    opcion = validar_input_opcion(7)
    if opcion == 1:
        enemigo = personaje_principal.encontrar_enemigo(enemigos_lista)
        menu_explorar(enemigo)
    elif opcion == 2:
        REVISAR_ESTADO()
    elif opcion == 3:
        menu_tienda()
    elif opcion == 4:
        menu_inventario()
    elif opcion == 5:
        personaje_principal.curar_vida(vida_total)
        guardar_datos()
        print(personaje_principal)
        iniciar_juego()


def menu_principal():
    print("")
    print("<<<<BIENVENIDO AL MUNDO DE 'MUY MUY LEJANO'>>>>")
    print("1. EXPLORAR MUNDO")
    print("2. REVISAR ESTADO")
    print("3. TIENDA")
    print("4. INVENTARIO")
    print("5. DESCANSAR")

def menu_explorar(enemigo):

    global personaje_principal
    print(enemigo)
    print()
    print(personaje_principal)
    print("1. PELEAR")
    print("2. ESCAPAR")
    opcion = validar_input_opcion(2)
    if opcion == 1:
        personaje_principal = enemigo.atacar(personaje_principal)
        enemigo = personaje_principal.atacar(enemigo)
        if enemigo.vida <= 0:
            victoria(enemigo)
        elif personaje_principal.vida <= 0:
            derrota()
        menu_explorar(enemigo)
    if opcion == 2:
        iniciar_juego()
def victoria(enemigo):
    print(f"has derrotado {enemigo.nombre}")
    i = 1
    global inventario_total
    rand = random.randrange(1, 10)
    while i < rand:
        inventario_total = personaje_principal.encontrar_obj(comidas_lista, inventario_total, personaje_principal.inventario)
        i += 1
    inventario_total = personaje_principal.encontrar_obj(equipos_lista, inventario_total, personaje_principal.inventario)
    if enemigo.nombre == "Aldeano":
        personaje_principal.monedas += 10
        print("ganaste 10 monedas")
    elif enemigo.nombre == "Caballero":
        personaje_principal.monedas += 20
        print("ganaste 20 monedas")
    elif enemigo.nombre == "lord Farquaad":
        personaje_principal.monedas += 600
        print("ganaste 600 monedas")
    elif enemigo.nombre == "Dragona":
        personaje_principal.monedas += 3000
        print("ganaste 3000 monedas")
    elif enemigo.nombre == "Oso":
        personaje_principal.monedas += 50
        print("ganaste 50 monedas")

    enemigos_lista.remove(enemigo)
    guardar_datos()
    del enemigo




    iniciar_juego()
def derrota():
    print("el juego ha terminado")
    sys.exit()

def menu_tienda():
    print("<<<<BIENVENIDO A LA TIENDA DEL REINO 'MUY MUY LEJANO'>>>>")
    print("1. COMPRAR OBJETO")
    print("2. VENDER OBJETO")
    print("3. SALIR DE LA TIENDA")
    opcion = validar_input_opcion(3)
    if opcion == 1:
        comprar()
    if opcion == 2:
        vender()
    if opcion == 3:
        salir_tienda()

def vender():
    imprimir_inventario()
    confirma = "no"
    nombre_objeto = ""
    calidad_comida = ""
    while confirma == "no":


        while True:
            nombre_objeto = input("escriba el nombre de el objeto que quiera vender")
            if nombre_objeto.isdigit():
                print("no se permiten numeros, solo cadenas")
                continue
            if len(nombre_objeto) < 2:
                print("no se permiten entradas vacias o menor de 2 letras")
            else:
                break

        for list in inventario_total.objetos:
            if list.name == nombre_objeto:
                if list.type == "comida":
                    calidad_comida = input("ingrese la calidad de la comida")
                    break

        while True:
            confirma = input(f"esta seguro que escribio y desea vender {nombre_objeto}: (si/no/cancelar)")
            if confirma.isdigit():
                print("no se permiten numeros, solo cadenas")
                continue
            if len(confirma) < 2:
                print("cadena vacia o incompleta")
            else:
                print("cadena valida")
                break


        if confirma == "cancelar":
            menu_tienda()    
            break
        if confirma != "no" and confirma != "si":
            menu_tienda()
            break
    for list in inventario_total.objetos:
        if list.name == nombre_objeto and calidad_comida == list.quality or list.type == "equipos" and list.name == nombre_objeto:
            nombre_objeto = list
    if isinstance(nombre_objeto, str):
        print("el objeto que busca no se encuentra en el inventario")
        menu_tienda()
    indice = inventario_total.objetos.index(nombre_objeto)
    # corregir el bug 'nombre_objeto no encontrado' para la siguiente clase
    item = inventario_total.objetos.pop(indice)
    item.vender_objeto(personaje_principal)
    del item

    print(personaje_principal)
    menu_tienda()



def imprimir_inventario():
    contador_comida = 0
    contador_equipo = 0
    print("comidas:")
    for list in inventario_total.objetos:
        if list.type == "comida":
            contador_comida += 1
            print(f"{list.name}({list.quality}) | ", end=' ')
            if contador_comida % 3 == 0:
                print()
    print()
    print("equipos:")
    for list in inventario_total.objetos:
        if list.type == "equipos":
            contador_equipo += 1
            print(f"{list.name}({list.quality}) | ", end=' ')
            if contador_equipo % 3 == 0:
                print()
    print()

def imprimir_tienda():
    contador_equipo = 0
    print()
    print("<<<<BIENVENIDO A LA TIENDA>>>>")
    for list in tienda:
        contador_equipo += 1
        print(f"{list.name}({list.quality}) | ", end=' ')
        if contador_equipo % 3 == 0:
            print()
    print()
def comprar():
    imprimir_tienda()
    print("1. DETALLES DE OBJETO")
    print("2. COMPRAR OBJETO DEFINITIVAMENTE")
    print("3. SALIR DE LA TIENDA")
    opcion = validar_input_opcion(3)
    if opcion == 1:
        objeto = validar_input_cadenas("ingrese el nombre del objeto")
        for list in tienda:
            if list.name == objeto:
                print(list)
        comprar()
    if opcion == 2:
        # solucionar el bug de restar monedas al comprar
        objeto_a_comprar = validar_input_cadenas("ingresar nombre del objeto que desea comprar")
        if objeto_a_comprar == "cancelar":
            menu_tienda()
        objeto_comprado = ""
        while True:
            for list in tienda:
                if objeto_a_comprar == list.name:
                    objeto_comprado = list
                    break
            if objeto_comprado == "":
                objeto_a_comprar = validar_input_cadenas("ingresar nombre del objeto que desea comprar")
                if objeto_a_comprar == "cancelar":
                    menu_tienda()
            else:
                break
        if personaje_principal.monedas >= objeto_comprado.price:
            
            objeto_comprado.comprar_objeto(personaje_principal)
            inventario_total.objetos.append(objeto_comprado)
            guardar_datos()



            quary = """SELECT * FROM objeto WHERE nombre = %s"""
            conexion_DB.conectar_db()
            conexion_DB.cursor.execute(quary, (objeto_comprado.name, ))
            resultado = conexion_DB.cursor.fetchall()

            existe = len(resultado) > 0
            if existe:
                quary = """INSERT INTO inventario(inventario, objetoID) VALUES (%s, %s)"""
                valores = (personaje_principal.inventario, resultado[0][0])
                conexion_DB.conectar_db()
                conexion_DB.cursor.execute(quary, valores)
                conexion_DB.conexion.commit()
                print(len(resultado))

            else:
                quary = """INSERT INTO objeto(nombre, vida, ataque, defensa, calidad, tipo, precio) VALUES (%s, %s, %s ,%s , %s, %s, %s)"""
                valores = (objeto_comprado.name, objeto_comprado.life, objeto_comprado.attack, objeto_comprado.defense, objeto_comprado.quality, objeto_comprado.type, objeto_comprado.price)
                conexion_DB.conectar_db()
                conexion_DB.cursor.execute(quary, valores)
                conexion_DB.conexion.commit()
                IDitem = conexion_DB.cursor.lastrowid
                
                quary = """INSERT INTO inventario(inventario, objetoID) VALUES (%s, %s)"""
                valores = (personaje_principal.inventario, IDitem)
                conexion_DB.conectar_db()
                conexion_DB.cursor.execute(quary, valores)
                conexion_DB.conexion.commit()
            # continuar la implementacion de las quary's
            print("<<<<SU COMPRA HA SIDO EXITOSA>>>>")
            print()
            menu_tienda()
        else:
            print("monedas insuficientes para la compra")
            menu_tienda()


    if opcion == 3:
        iniciar_juego()
def salir_tienda():
    iniciar_juego()

def menu_inventario():
    print("")
    print("<<<<BIENVENIDO A TU INVENTARIO>>>>")
    print("1. MOSTRAR OBJETO")
    print("2. SALIR DEL INVENTARIO")
    opcion = validar_input_opcion(2)
    if opcion == 1:
        menu_mostrar_objeto()
    if opcion == 2:
        iniciar_juego()


def menu_mostrar_objeto():
    print("<<<<MOSTRAR OBJETO>>>>>")
    imprimir_inventario()
    print("1. EQUIPAR OBJETO")
    print("2. DETALLES DEL OBJETO")
    print("3. MEJORAR COMIDA")
    print("4. CONSUMIR COMIDA")
    print("5. SALIR INVENTARIO")
    opcion = validar_input_opcion(5)

    if opcion == 1:
        if not personaje_principal.vida == vida_total:
            print("<<<<ANTES DE EQUIPAR VAYA A 'DESCANSO'>>>")
            iniciar_juego()
        else:
            equipar_objeto()
    if opcion == 2:
        detalles_objeto = input("ingresar objeto para revisar")
        calidad_objeto = input("ingresar calidad del objeto para revisar")
        for list in inventario_total.objetos:
            if detalles_objeto == list.name and calidad_objeto == list.quality:
                print(list)
                break
        menu_mostrar_objeto()

    if opcion == 3:
        mejorar_comida()

    if opcion == 4:

        consumir_comida = input("ingrese el nombre de la comida que desea comer")
        calidad_comida = input("ingrese la calidad de la comida que desea comer")
        for list in inventario_total.objetos:
            if list.name == consumir_comida and list.quality == calidad_comida:
                list.comer_objeto(personaje_principal)
                inventario_total.objetos.remove(list)
                print(f"la comida {list.name} ha sido consumida por el jugador")
                break
        menu_mostrar_objeto()
    if opcion == 5:
        iniciar_juego()

def equipar_objeto():

    equipo_nombre = input("ingresar nombre del equipo")
    equipo_ant = ""
    equipo = ""

    for list in inventario_total.objetos:
        if list.name == equipo_nombre and list.type == "equipos":
            equipo = list
    if equipo == "":
        print(f"no se ha encontrado el equipo {equipo_nombre}")
        menu_mostrar_objeto()
    inventario_total.retirar_objeto(equipo, personaje_principal.inventario)
    equipo_ant = personaje_principal.equipar(equipo)
    # tomar en cuenta la quary de update para equipar()
    global vida_total
    vida_total += equipo.life
    global ataque_total
    ataque_total += equipo.attack
    global defensa_total
    defensa_total += equipo.defense
    if not equipo_ant is None:
        vida_total -= equipo_ant.life
        ataque_total -= equipo_ant.attack
        defensa_total -= equipo_ant.defense
        inventario_total.anadir_objeto(equipo_ant, personaje_principal.inventario)
        # tomar en cuenta la quary para insertar en anadir_objeto()
    menu_mostrar_objeto()
    
def mejorar_comida():
    mejora = input("que comida desea mejorar")
    calidad = input("ingrese la calidad de la comida que desea mejorar")
    contador = 0
    comida1 = ""
    comida2 = ""
    for list in inventario_total.objetos:
        if mejora == list.name and calidad  == list.quality:
            contador += 1
            if contador == 1:
                comida1 = list
            elif contador == 2:
                comida2 = list
                break
    if contador <= 1:
        print("comida insuficiente para mejorarla")
        menu_mostrar_objeto()
    inventario_total.objetos.remove(comida1)
    inventario_total.objetos.remove(comida2)
    del comida2
    if comida1.quality == "Leyenda":
        print("no se puede mejorar la calidad 'Leyenda'")
        menu_mostrar_objeto()
    else:
        comida1.combinar_objeto()
    inventario_total.objetos.append(comida1)
    menu_mostrar_objeto()
def REVISAR_ESTADO():
    # implementar el guardado de datos
    print("ESTADO ACTUAL:")
    print(personaje_principal)
    print("--------ITEMS--------")
    if not personaje_principal.casco == "":
        print("")
        print(f"el nombre del obj. es {personaje_principal.casco.name}")
        print(f"la vida del obj. es {personaje_principal.casco.life}")
        print(f"el ataque del obj. es {personaje_principal.casco.attack}")
        print(f"la defensa del obj es {personaje_principal.casco.defense}")

    if not personaje_principal.armadura == "":
        print("")
        print(f"el nombre del obj. es {personaje_principal.armadura.name}")
        print(f"la vida del obj. es {personaje_principal.armadura.life}")
        print(f"el ataque del obj. es {personaje_principal.armadura.attack}")
        print(f"la defensa del obj es {personaje_principal.armadura.defense}")
    if not personaje_principal.guantes == "":
        print("")
        print(f"el nombre del obj. es {personaje_principal.guantes.name}")
        print(f"la vida del obj. es {personaje_principal.guantes.life}")
        print(f"el ataque del obj. es {personaje_principal.guantes.attack}")
        print(f"la defensa del obj es {personaje_principal.guantes.defense}")
    if not personaje_principal.botas == "":
        print("")
        print(f"el nombre del obj. es {personaje_principal.botas.name}")
        print(f"la vida del obj. es {personaje_principal.botas.life}")
        print(f"el ataque del obj. es {personaje_principal.botas.attack}")
        print(f"la defensa del obj es {personaje_principal.botas.defense}")
    if not personaje_principal.espada == "":
        print("")
        print(f"el nombre del obj. es {personaje_principal.espada.name}")
        print(f"la vida del obj. es {personaje_principal.espada.life}")
        print(f"el ataque del obj. es {personaje_principal.espada.attack}")
        print(f"la defensa del obj es {personaje_principal.espada.defense}")
    print("----------------")
    guardar_datos()
    iniciar_juego()
def guardar_datos():
    # obtener el ID de los objetos cuando asignamos a personaje principal, para poder guardar esos IDS junto con los datos de personaje_principal
    conexion_DB.reconectar_db()
    curse = conexion_DB.conexion.cursor(dictionary= True)
    curse.execute("SELECT * FROM personaje WHERE nombre = %s", (personaje_principal.nombre,))
    resultados = curse.fetchone()
    if not resultados:
        print("sin resultados")
    query = "UPDATE personaje SET ataque = %s,defensa = %s,vida = %s, monedas = %s WHERE nombre = %s"
    curse.execute(query,(personaje_principal.ataque, personaje_principal.defensa, personaje_principal.vida, personaje_principal.monedas, personaje_principal.nombre))
    conexion_DB.conexion.commit()
    print("personaje actualizado correctamente")






    print("GUARDADO EXITOSO")
def crear_equipos():
    objeto_equipos = equipos_explorar().equipo()
    return objeto_equipos
def crear_comidas():
    comidas = []
    i = 0
    while i < random.randrange(100, 1000): comidas.append(Objeto("Carne", 5, 0, 1, "comun", "comida", 10)); i += 1
    #100 - 1000
    i = 0
    while i < random.randrange(90, 900): comidas.append(Objeto("Sandia", 5, 0, 2, "comun","comida",12)); i += 1
    #90 - 900
    i = 0
    while i < random.randrange(70, 600): comidas.append(Objeto("Pastel de zanahoria", 10, 3, 3, "Raro","comida",20)); i += 1
    #70 - 600
    i = 0
    while i < random.randrange(40, 480): comidas.append(Objeto("Pizza", 10, 5, 5, "Excepcional","comida", 25)); i += 1
    #40 - 480
    i = 0
    while i < random.randrange(20, 200): comidas.append(Objeto("hamburguesa", 15,10,10,"Mitico","comida",30)); i += 1
    #20 - 200
    i = 0
    while i < random.randrange(5, 100): comidas.append(Objeto("plato Gourmet",30,20,20,"Leyenda","comida", 40)); i += 1
    #5 - 100
    return comidas
def crear_enemigos():
    enemigos = []
    i = 0
    while i < random.randrange(50,300):enemigos.append(Enemigo("Aldeano",5,5,100)); i += 1
    i = 0

    while i < random.randrange(50,250):enemigos.append(Enemigo("Caballero",10,10,190)); i += 1
    i = 0
    enemigos.append(Enemigo("lord Farquaad",7,7,70))

    enemigos.append(Enemigo("Dragona",40,32,720))

    while i < random.randrange(50,300):enemigos.append(Enemigo("Oso",15,10,200)); i += 1
    return enemigos

def construir_objs(lista):
    var = []
    for list in lista:
        var.append(Objeto(list[1], list[2], list[3], list[4], list[5],list[6],list[7]))
    return var
def obtener_inv():
    quary= f"""SELECT i.objetoID, i.nombre, i.vida, i.ataque, i.defensa, i.calidad, i.tipo, i.precio FROM inventario inv JOIN objeto i ON inv.objetoID = i.objetoID WHERE inv.inventario = {personaje_principal.inventario}""" 
    conexion_DB.conectar_db()
    conexion_DB.cursor.execute(quary)
    resultados = conexion_DB.cursor.fetchall()
    resultados = construir_objs(resultados)

    return resultados
elegir_personaje()
enemigos_lista = crear_enemigos()
comidas_lista = crear_comidas()
equipos_lista = crear_equipos()
inventario_total = Inventario()
inventario_total.objetos = obtener_inv()
iniciar_juego()
# global inventario_total
# global comidas_lista
# global enemigos_lista
inventario_total.anadir_objeto(stick)
inventario_total.anadir_objeto(Objeto("espada de plata", 5, 15, 8, "Raro","equipos", 1))
inventario_total.anadir_objeto(Objeto("espada de madera", 0, 5, 4, "comun","equipos", 2))
inventario_total.anadir_objeto(Objeto("espada de hierro", 15, 35, 18, "Excepcional","equipos", 3))

# personaje_principal = crear_personaje() 


