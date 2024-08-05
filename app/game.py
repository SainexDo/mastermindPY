from colorama import Fore
from time import sleep
import keyboard
import random

class Game:
    #Juego, dividido en sus respectivas clases y métodos.
    def __init__(self, rojo, azul, verde, amarillo, reset):
        #Declaramos variables privadas.
        self.rojo = rojo
        self.azul = azul
        self.verde = verde
        self.amarillo = amarillo
        self.reset = reset
        self.secuencia = []
        self.intentoDeAdivinarSecuencia = []

    def elegirModo(self):
        while True:
            respuesta = input(f'¿Adivinas o creas la secuencia? (Adivinar / Crear): ').strip().lower()
            if respuesta not in ('adivinar', 'crear'):
                print("Agrega una respuesta correcta.")
            else:
                break

    def creaJugador(self):
        print("ga")

    def creaComputadora(self):
        while True:
            posiblesOpciones = (self.rojo, self.azul, self.amarillo, self.verde)
            self.secuencia.insert(1, random.choice(posiblesOpciones) + self.reset)
            if len(self.secuencia) == 4:
                print(''.join(self.secuencia) + self.reset)
                break

        intentos = []
        # while True:
        #     print("Manejo")
        #     break

def main():
    Juego = Game(azul=(Fore.BLUE + " O "), rojo=(Fore.RED + " O "), amarillo=(Fore.YELLOW + " O "), verde=(Fore.GREEN + " O "), reset=Fore.RESET)
    Juego.elegirModo()

if __name__ == "__main__":
    # Inicializador del archivo.
    main()