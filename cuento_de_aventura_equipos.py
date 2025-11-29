import random
from cuento_de_Aventura_Shrek import Objeto


class equipos_explorar:
    def __init__(self):
        self.ITEMS = []

    def equipo(self):
        i = 0
        while i < random.randrange(1, 20):
            #cascos
            self.ITEMS.append(Objeto("casco de tela", 0, 0, 2, "comun","equipos",10))
            self.ITEMS.append(Objeto("armadura de tela", 5, 0, 5, "comun","equipos", 10))
            self.ITEMS.append(Objeto("guantes de tela", 0, 0, 2, "comun","equipos", 10 ))
            self.ITEMS.append(Objeto("botas de tela", 0, 1, 1, "comun","equipos", 11))
            self.ITEMS.append(Objeto("espada de madera", 0, 5, 4, "comun","equipos", 10))
            i += 1
        i = 0
        while i < random.randrange(1, 15):
            self.ITEMS.append(Objeto("casco de cuero", 1, 0, 3, "Raro","equipos", 15))
            self.ITEMS.append(Objeto("armadura de cuero", 10, 0, 8, "Raro","equipos", 16))
            self.ITEMS.append(Objeto("guantes de cuero", 1, 0, 3, "Raro","equipos", 17))
            self.ITEMS.append(Objeto("botas de cuero", 2, 3, 2, "Raro","equipos",19))
            self.ITEMS.append(Objeto("espada de plata", 5, 15, 8, "Raro","equipos",20))
            i += 1
        i = 0
        while i < random.randrange(1, 10):
            self.ITEMS.append(Objeto("casco de hierro", 5, 1, 10, "Excepcional","equipos",25))
            self.ITEMS.append(Objeto("armadura de hierro", 20, 1, 30, "Excepcional","equipos",27))
            self.ITEMS.append(Objeto("guantes de hierro", 5, 1, 10, "Excepcional","equipos", 28))
            self.ITEMS.append(Objeto("botas de hierro", 3, 5, 5, "Excepcional","equipos",29))
            self.ITEMS.append(Objeto("espada de hierro", 15, 35, 18, "Excepcional","equipos",30))
            i += 1
        i = 0
        while i < random.randrange(1,5):
            self.ITEMS.append(Objeto("casco de oro", 20, 8, 25, "Mitico","equipos",30))
            self.ITEMS.append(Objeto("armadura de oro", 50, 8, 55, "Mitico","equipos",30))
            self.ITEMS.append(Objeto("guantes de oro", 20, 8, 25, "Mitico","equipos",32))
            self.ITEMS.append(Objeto("botas de oro", 10, 15, 15, "Mitico","equipos",34))
            self.ITEMS.append(Objeto("espada de oro", 60, 80, 40, "Mitico","equipos",35))
            i += 1
        i = 0
        while i < random.randrange(1, 3):
            self.ITEMS.append(Objeto("casco de diamante", 45, 15, 60, "Leyenda","equipos", 50))
            self.ITEMS.append(Objeto("armadura de diamante", 65, 18, 70, "Leyenda","equipos",52))
            self.ITEMS.append(Objeto("guantes de diamante", 25, 15, 30, "Leyenda","equipos",55))
            self.ITEMS.append(Objeto("botas de diamante", 15, 25, 20, "Leyenda","equipos",57))
            self.ITEMS.append(Objeto("espada de diamante", 150, 120, 90, "Leyenda","equipos",60))
            i += 1
        return self.ITEMS

class equipos_tienda:
    def __init__(self):
        self.ITEMS = []

    def equipo(self):
            #cascos
        self.ITEMS.append(Objeto("casco de camuflaje", 5, 4, 7, "comun","equipos",20))
        self.ITEMS.append(Objeto("armadura de camuflaje", 5, 5, 7, "comun","equipos",20))
        self.ITEMS.append(Objeto("guantes de camuflaje", 7, 7, 8, "comun","equipos",22))
        self.ITEMS.append(Objeto("botas de camuflaje", 10, 9, 9, "comun","equipos",24))
        self.ITEMS.append(Objeto("espada de camuflaje", 15, 10, 10, "comun","equipos",25))

        self.ITEMS.append(Objeto("casco de vikingo", 13, 10, 13, "Raro","equipos", 35))
        self.ITEMS.append(Objeto("armadura de vikingo", 16, 11, 15, "Raro","equipos",36))
        self.ITEMS.append(Objeto("guantes de vikingo", 17, 13, 16, "Raro","equipos",36))
        self.ITEMS.append(Objeto("botas de vikingo", 21, 16, 18, "Raro","equipos",38))
        self.ITEMS.append(Objeto("espada de vikingo", 25, 19, 20, "Raro","equipos",40))

        self.ITEMS.append(Objeto("casco de caballero", 25, 21, 20, "Excepcional","equipos",120))
        self.ITEMS.append(Objeto("armadura de caballero", 26, 23, 23, "Excepcional","equipos",125))
        self.ITEMS.append(Objeto("guantes de caballero", 27, 24, 25, "Excepcional","equipos",130))
        self.ITEMS.append(Objeto("botas de caballero", 33, 26, 27, "Excepcional","equipos",135))
        self.ITEMS.append(Objeto("espada de caballero", 35, 29, 30, "Excepcional","equipos",140))

        self.ITEMS.append(Objeto("Casco de samurai", 32, 31, 32, "Mitico","equipos",250))
        self.ITEMS.append(Objeto("armadura de samurai", 35, 33, 35, "Mitico","equipos",260))
        self.ITEMS.append(Objeto("guantes de samurai", 40, 34, 36, "Mitico","equipos",265))
        self.ITEMS.append(Objeto("botas de samurai", 42, 35, 37, "Mitico","equipos",270))
        self.ITEMS.append(Objeto("espada de samurai", 45, 39, 40, "Mitico","equipos",300))

        self.ITEMS.append(Objeto("casco de troya", 125, 112, 122, "Leyenda","equipos",1000))
        self.ITEMS.append(Objeto("armadura de troya", 155, 118, 130, "Leyenda","equipos",1100))
        self.ITEMS.append(Objeto("guantes de troya", 190, 140, 160, "Leyenda","equipos",1200))
        self.ITEMS.append(Objeto("botas de troya", 240, 199, 199, "Leyenda","equipos",1300))
        self.ITEMS.append(Objeto("espada de troya", 400, 322, 360, "Leyenda","equipos",2500))
        #
        return self.ITEMS
