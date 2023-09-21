"""
Author: Jeimilitza Sainz Lopez
"""

from abc import ABC, abstractmethod
import random
import matplotlib.pyplot as plt
import numpy as np

class Statistics: # Clase para mostrar las estadisticas
    __x = np.array(["Piedra", "Papel", "Tijera"]) # Las dos variables privadas
    __y = np.array([35.4, 35, 29.6]) #Porcientos sacados de estudios sobre el juego, esta en las referencias
    
    def showGraph(self): # Metodo para hacer la grafica de barra
        width = 0.5
        fig, ax = plt.subplots()

        pps = ax.bar(self.__x, self.__y, width, align='center', color= "green")

        for p in pps: # Para mostrar los porcentajes en la grafica
            height = p.get_height()
            ax.text(x=p.get_x() + p.get_width() / 2, y=height+.10, s="{}%".format(height), ha='center')
        
        plt.title("Opciones mas jugadas")
        plt.ylabel("Porcentaje")
        plt.ylim(25, 40)
        plt.show() # Mostrando la grafica de barra

class Validation: # Clase para verificar toda variable insertada por el usuario
    @staticmethod
    def wantToPlay_validation(WTP): # Metodo estatico que verifica la respuesta a querer jugar
        try: # Esta sobre cargado, sino es entero el error va a ser detectado
            WTP = int(WTP)
            if WTP == 1 or WTP == 2: # verificando que este dentro del rango de respuestas
                return WTP
            else:
                print()
                print("Respuesta invalida, por favor intente de nuevo.")
                return Game.wantToPlay()
        except: # si no es entero, la funcion muestra un mensaje diferente
            print()
            print("La respuesta debe ser un numero entero, por favor intente de nuevo.")
            return Game.wantToPlay()
    
    @staticmethod
    def option_validation(OPT): # Metodo estatico que verifica la opcion a jugar
        try: # Esta sobre cargado, sino es entero el error va a ser detectado
            OPT = int(OPT)
            if OPT == 1 or OPT == 2 or OPT == 3: # verificando que este dentro del rango de respuestas
                return OPT
            else:
                print()
                print("Respuesta invalida, por favor intente de nuevo.")
                return Player.getOption()
        except: # si no es entero, la funcion muestra un mensaje diferente
            print()
            print("La respuesta debe ser un numero entero, por favor intente de nuevo.")
            return Player.getOption()
        
class Template(ABC): # Clase abstracta para usar metodo de plantilla
    @abstractmethod
    def getOption(self):
        pass
    
class Player(Template): # Clase donde se asigna la decision del jugador
    player_option = 0 # variable de clase para la opcion del jugador
    
    @classmethod
    def getOption(cls): # Metodo de clase donde el jugador decide su opcion
        cls.player_option = input("Haga su eleccion:\n Precione 1 para piedra\n Precione 2 para papel\n Precione 3 para tijera\n")
        cls.player_option = Validation.option_validation(cls.player_option)
        if cls.player_option == 1:
            cls.player_option = "piedra"
        elif cls.player_option == 2:
            cls.player_option = "papel"
        else:
            cls.player_option = "tijera"
            
class Computer(Template): # Clase donde se asigna la opcion de la computadora
    computer_option = 0 # variable de clase para la opcion de la computadora
    
    @classmethod
    def getOption(cls): # Metodo de clase donde se elige aleatoriamente por la computadora
        cls.computer_option = random.randint(1, 3)
        if cls.computer_option == 1:
            cls.computer_option = "piedra"
        elif cls.computer_option == 2:
            cls.computer_option = "papel"
        else:
            cls.computer_option = "tijera"
            
class Game(Player, Computer): # Clase para comenzar el juego y decidir el ganador
    def __init__(self): # Constructor inicializa variable de instancia winner
        self.winner = "Aun no hay ganador"
        
    @staticmethod
    def wantToPlay(): # Metodo estatico decide si el juego comienza
        choice = input("Quiere jugar piedra, papel o tijera?\n Si(1)\n No(2)\n")
        choice = Validation.wantToPlay_validation(choice)
        return choice
        
    def Winner(self): # Metodo de instancia decide ganador segun las reglas del juego
        if Computer.computer_option == Player.player_option:
            self.winner = "Es un empate"
            print(self.winner)
        elif (Computer.computer_option == "papel" and Player.player_option == "piedra") or (Computer.computer_option == "tijera" and Player.player_option == "papel") or (Computer.computer_option == "piedra" and Player.player_option == "tijera"):
            self.winner = "Has perdido"
            print(self.winner)
        else:
            self.winner = "Has Ganado!"
            print(self.winner)
# Creando todos los objetos
G = Game()
P = Player()
C = Computer()
S = Statistics()

S.showGraph() # Muestro la grafica al comienzo
print() # Bienvenida y mostrando las reglas
print("Bienvenid@!,\nEstas son las reglas de juego:\n Piedra vs Tijera - Piedra gana\n Papel vs Piedra - Papel gana\n Tijera vs Papel - Tijera gana")

WTP = G.wantToPlay() # Usuario decide si quiere jugar
while WTP == 1: # Mientras la respuesta siga siendo si, el juego continua
    P.getOption() # Se eligen las opciones
    C.getOption()
    print()
    print("Eleccion del usuarion: ", P.player_option) # Se muestran al jugador
    print("Computadora a elegido: ", C.computer_option)
    print()
    G.Winner() # Se muestra el ganador
    WTP = G.wantToPlay() # se pregunta si quiere jugar de nuevo

print() # Fin del programa
print("Fin del Juego")