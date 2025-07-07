import time
import random
class Personaje:

    def __init__(self, name, life, attack, defense, coins, sword):
        self.nombre = name
        self.vida = life
        self.ataque = attack
        self.defensa = defense
        self.monedas = coins
        self.casco = ""
        self.armadura = ""
        self.guantes = ""
        self.botas = ""
        self.espada = sword

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

    def encontrar_obj(self, lista, inventario_total):
        lista_temp = random.choice(lista)
        inventario_total.objetos.append(lista_temp)
        print(f"usted ha ganado {lista_temp.name}")
        return inventario_total

    def encontrar_enemigo(self, enemigos_lista):
        return random.choice(enemigos_lista)


    def equipar(self, equipo):
        if equipo.name.rfind("casco") == 0:
            if self.casco == "":
                self.casco = equipo
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
            else:
                casco_temp = self.casco
                self.casco = equipo
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
                self.vida -= casco_temp.life
                self.ataque -= casco_temp.attack
                self.defensa -= casco_temp.defense
                return casco_temp
        elif equipo.name.rfind("armadura") == 0:
            if self.armadura == "":
                self.armadura = equipo
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
            else:
                armadura_temp = self.armadura
                self.armadura = equipo
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
                self.vida -= armadura_temp.life
                self.ataque -= armadura_temp.attack
                self.defensa -= armadura_temp.defense
                return armadura_temp
        elif equipo.name.rfind("guantes") == 0:
            if self.guantes == "":
                self.guantes = equipo
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
            else:
                guantes_temp = self.guantes
                self.guantes = equipo
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
                self.vida -= guantes_temp.life
                self.ataque -= guantes_temp.attack
                self.defensa -= guantes_temp.defense
                return guantes_temp
        elif equipo.name.rfind("botas") == 0:
            if self.botas == "":
                self.botas = equipo
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
            else:
                botas_temp = self.botas
                self.botas = equipo
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
                self.vida -= botas_temp.life
                self.ataque -= botas_temp.attack
                self.defensa -= botas_temp.defense
                return  botas_temp
        elif equipo.name.rfind("espada") == 0:
            if self.espada == "":
                self.espada = equipo
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
            else:
                espada_temp = self.espada
                self.espada = equipo
                self.vida += equipo.life
                self.ataque += equipo.attack
                self.defensa += equipo.defense
                self.vida -= espada_temp.life
                self.ataque -= espada_temp.attack
                self.defensa -= espada_temp.defense
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

    def anadir_objeto(self, obj):
        self.objetos.append(obj)
    def retirar_objeto(self, obj):
        self.objetos.remove(obj)

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


