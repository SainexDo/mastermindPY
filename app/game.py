from colorama import Fore
from time import sleep
import keyboard


class Game:
    #Juego, dividido en sus respectivas clases y métodos.
    def __init__(self):
        #Declaramos variables privadas.
        self.secuencia = []
        self.intentoDeSecuencia = []



    def elegirModo(self):
        while True:
            print(f'¿Adivinas o creas la secuencia? (Adivinar / Crear)')
            respuesta = input().strip().lower()
            if respuesta not in ('adivinar', 'crear'):
                print("Agrega una respuesta correcta.")
            else:
                if respuesta == 'adivinar':
                    self.creaComputadora()
                elif respuesta == 'crear':
                    self.creaJugador()
                break

    def creaJugador(self):
        print(Fore.GREEN + "FRAFRA" + Fore.RESET)

    def creaComputadora(self):
        print("Crea Jugador.")


def main():
    Juego = Game()
    Juego.elegirModo()



if __name__ == "__main__":
    # Inicializador del archivo.
    main()