import time
import random
import conexion_DB
class Personaje:

    def __init__(self, name, life, attack, defense, coins, hat, armor, gloves, boots, sword, inventarioo):
        self.nombre = name
        self.vida = life
        self.ataque = attack
        self.defensa = defense
        self.monedas = coins
        self.casco = hat
        self.armadura = armor
        self.guantes = gloves
        self.botas = boots
        self.espada = sword
        self.inventario = inventarioo
    def __str__(self):
        return f"las estadisticas del jugador son:\n el ataque del personaje principal es {self.ataque},\n la defensa del personaje principal {self.defensa},\n la vida del personaje principal es {self.vida},\n y las monedas {self.monedas}"
    def atacar(self, enemigo):
        dano_personaje = self.ataque / (1 + enemigo.defensa / 100)
        enemigo.vida = round(enemigo.vida - dano_personaje, 3)
        return enemigo

    def curar_vida(self, vida_total):
        print("usted esta ingresando a la zona de descanso")
        tiempo = 5
        vida = vida_total - self.vida
        while True:
            print("descansando...")
            time.sleep(tiempo)
            self.vida += 10
            if self.vida >= vida_total:
                self.vida = vida_total
                break

    def encontrar_obj(self, lista, inventario_total, Personaje_inventario):
        item_temp = random.choice(lista)
        quary= """SELECT * FROM objeto WHERE nombre = %s AND calidad = %s"""
        conexion_DB.conectar_db()
        conexion_DB.cursor.execute(quary, (item_temp.name, item_temp.quality))
        resultado = conexion_DB.cursor.fetchall()
        # if not resultado:
        #    resultado = 0
        existe = len(resultado) > 0
        if existe:
            quary= """INSERT INTO inventario(inventario, objetoID) VALUES(%s, %s)"""
            valores= (Personaje_inventario, resultado[0][0])
            conexion_DB.conectar_db()
            conexion_DB.cursor.execute(quary, valores)
            conexion_DB.conexion.commit()
        else:
            
            quary= """INSERT INTO objeto(nombre, vida, ataque, defensa, calidad, tipo, precio) VALUES(%s, %s, %s, %s, %s, %s, %s)"""
            valores= (item_temp.name,item_temp.life, item_temp.attack, item_temp.defense, item_temp.quality, item_temp.type, item_temp.price)
            conexion_DB.conectar_db()
            conexion_DB.cursor.execute(quary, valores)
            conexion_DB.conexion.commit()
            IDitem = conexion_DB.cursor.lastrowid

            # aqui va el codigo de guardar en inventario los objetos no-repetidos
            quary = """INSERT INTO inventario(inventario, objetoID) VALUES(%s, %s)"""
            valores = (Personaje_inventario, IDitem)
            conexion_DB.conectar_db()
            conexion_DB.cursor.execute(quary, valores)
            conexion_DB.conexion.commit()
        inventario_total.objetos.append(item_temp)
        print(f"usted ha ganado {item_temp.name}")
        return inventario_total

    def encontrar_enemigo(self, enemigos_lista):
        return random.choice(enemigos_lista)


    def equipar(self, equipo, objID):

        if equipo.name.rfind("casco") == 0:
            if self.casco == "" or int(self.casco) == 0:
                self.casco = objID
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
            else:
                casco_temp = self.casco
                quary = """SELECT * FROM objeto WHERE objetoID = %s"""
                conexion_DB.conectar_db()
                conexion_DB.cursor.execute(quary, (casco_temp, ))
                resultado = conexion_DB.cursor.fetchall()
                self.casco = objID
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
                self.vida -= resultado[0][2]
                self.ataque -= resultado[0][3]
                self.defensa -= resultado[0][4]
                casco_temp = Objeto(resultado[0][1], resultado[0][2], resultado[0][3], resultado[0][4], resultado[0][5], resultado[0][6], resultado[0][7])
                return casco_temp
        elif equipo.name.rfind("armadura") == 0:

            if self.armadura == "" or int(self.armadura) == 0:
                self.armadura = objID
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
            else:
                armadura_temp = self.armadura
                quary = """SELECT * FROM objeto WHERE objetoID = %s"""
                conexion_DB.conectar_db()
                conexion_DB.cursor.execute(quary, (armadura_temp, ))
                resultado = conexion_DB.cursor.fetchall()
                self.armadura = objID
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
                self.vida -= resultado[0][2]
                self.ataque -= resultado[0][3]
                self.defensa -= resultado[0][4]
                # reconstruir armadura_temp a un obj.
                armadura_temp = Objeto(resultado[0][1], resultado[0][2], resultado[0][3], resultado[0][4], resultado[0][5], resultado[0][6], resultado[0][7])
                return armadura_temp
        elif equipo.name.rfind("guantes") == 0:
            if self.guantes == "" or int(self.guantes) == 0:
                self.guantes = objID
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
            else:
                guantes_temp = self.guantes
                quary = """SELECT * FROM objeto WHERE objetoID = %s"""
                conexion_DB.conectar_db()
                conexion_DB.cursor.execute(quary, (guantes_temp, ))
                resultado = conexion_DB.cursor.fetchall()
                self.guantes = objID
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
                self.vida -= resultado[0][2]
                self.ataque -= resultado[0][3]
                self.defensa -= resultado[0][4]
                guantes_temp = Objeto(resultado[0][1], resultado[0][2], resultado[0][3], resultado[0][4], resultado[0][5], resultado[0][6], resultado[0][7])
                return guantes_temp
        elif equipo.name.rfind("botas") == 0:
            if self.botas == "" or int(self.botas) == 0:
                self.botas = objID
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
            else:
                botas_temp = self.botas
                quary = """SELECT * FROM objeto WHERE objetoID = %s"""
                conexion_DB.conectar_db()
                conexion_DB.cursor.execute(quary, (botas_temp, ))
                resultado = conexion_DB.cursor.fetchall()
                self.botas = objID
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
                self.vida -= resultado[0][2]
                self.ataque -= resultado[0][3]
                self.defensa -= resultado[0][4]
                botas_temp = Objeto(resultado[0][1], resultado[0][2], resultado[0][3], resultado[0][4], resultado[0][5], resultado[0][6], resultado[0][7])
                return  botas_temp
        elif equipo.name.rfind("espada") == 0:
            if self.espada == "" or int(self.espada) == 0:
                self.espada = objID
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
            else:
                espada_temp = self.espada
                quary = """SELECT * FROM objeto WHERE objetoID = %s"""
                conexion_DB.conectar_db()
                conexion_DB.cursor.execute(quary, (espada_temp, ))
                resultado = conexion_DB.cursor.fetchall()
                self.espada = objID
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
                self.vida -= resultado[0][2]
                self.ataque -= resultado[0][3]
                self.defensa -= resultado[0][4]
                espada_temp = Objeto(resultado[0][1], resultado[0][2], resultado[0][3], resultado[0][4], resultado[0][5], resultado[0][6], resultado[0][7])
                return espada_temp



class Objeto:

    def __init__(self, nombre, vida, ataque, defensa, calidad, tipo, precio):

        self.name = nombre
        self.life = vida
        self.attack = ataque
        self.defense = defensa
        self.quality = calidad
        self.type = tipo
        self.price = precio

    def __str__(self):
        return f"{self.name} tiene {self.life} de vida,\n tiene {self.attack} de ataque,\n tiene {self.defense} de defensa,\n la calidad es {self.quality}, y el precio es {self.price}"
    def comer_objeto(self, personaje_principal):
        personaje_principal.vida += self.life
        personaje_principal.ataque += self.attack
        personaje_principal.defensa += self.defense

    def combinar_objeto(self):
        self.life += int(self.life * 1.5)
        self.attack += int(self.attack * 1.5)
        self.defense += int(self.defense * 1.5)
        mejora_calidad = {
            'comun': "Raro",
            'Raro': "Excepcional",
            'Excepcional': "Mitico",
            'Mitico': "Leyenda"
        }
        self.quality = mejora_calidad.get(self.quality)
    def vender_objeto(self, personaje_principal):
        precios_calidad = {
            'comun': 10,
            'Raro': 15,
            'Excepcional': 50,
            'Mitico': 150,
            'Leyenda': 300
        }
        mi_moneda = precios_calidad.get(self.quality, 0)

        personaje_principal.monedas += mi_moneda
        print(f"el personaje gano {mi_moneda} monedas")

    def comprar_objeto(self, personaje_principal):
        personaje_principal.monedas -= self.price
        


class Inventario:

    def __init__(self):
        self.objetos = []

    def anadir_objeto(self, obj, inventario):
        self.objetos.append(obj)
        quary = """SELECT * FROM objeto WHERE nombre = %s"""
        conexion_DB.conectar_db()
        conexion_DB.cursor.execute(quary, (obj.name, ))
        resultados = conexion_DB.cursor.fetchall()

        query = """INSERT INTO inventario(inventario, objetoID) VALUES(%s, %s)"""
        conexion_DB.conectar_db()
        conexion_DB.cursor.execute(query, (inventario, resultados[0][0]))
        conexion_DB.conexion.commit()

    def retirar_objeto(self, obj, inventariooo):
        self.objetos.remove(obj)
        quary= """SELECT * FROM objeto WHERE nombre = %s""" 
        conexion_DB.conectar_db()
        conexion_DB.cursor.execute(quary, (obj.name, ))
        resultados = conexion_DB.cursor.fetchall()

        query = """DELETE FROM inventario WHERE inventario = %s AND objetoID = %s"""
        conexion_DB.conectar_db()
        objID = resultados[0][0]
        conexion_DB.cursor.execute(query, (inventariooo, objID))
        conexion_DB.conexion.commit()
        return objID
class Enemigo:
    def __init__(self, name, attack, defense, life):
        self.nombre = name
        self.ataque = attack
        self.defensa = defense
        self.vida = life
    def __str__(self):
        return f"las estadisticas del enemigo son:\n nombre:{self.nombre},\n ataque:{self.ataque}, \n defensa: {self.defensa}, \n y la vida: {self.vida}"
    def atacar(self, personaje_principal):
        dano_enemigo = self.ataque / (1 + personaje_principal.defensa / 100)
        personaje_principal.vida = round(personaje_principal.vida - dano_enemigo, 3)
        return personaje_principal


