from itertools import product
import random
from time import sleep
from colorama import Fore
from random import choice

class Game:
    def __init__(self, rojo, azul, verde, amarillo, reset):
        self.rojo = rojo
        self.azul = azul
        self.verde = verde
        self.amarillo = amarillo
        self.reset = reset
        self.secuencia = []
        self.intentoDeAdivinarSecuencia = []
        self.color_a_verificar = [self.azul, self.amarillo, self.rojo, self.verde]
        self.pistas_actualizadas = self.generarPistas()

    def elegirModo(self):
        while True:
            respuesta = input(f'¿Adivinas o creas la secuencia? (Adivinar / Crear): ').strip().lower()
            if respuesta not in ('adivinar', 'crear'):
                print("Agrega una respuesta correcta.")
            else:
                if respuesta == 'adivinar':
                    self.creaComputadora()
                elif respuesta == 'crear':
                    self.creaJugador()
                break

    def creaJugador(self):
        posiblesOpciones = [self.rojo, self.azul, self.amarillo, self.verde]
        while True:
            opcion = input("Elige los colores de tu secuencia (r/b/y/g): ").strip().lower()
            if len(self.secuencia) < 4:
                match opcion:
                    case "r":
                        self.secuencia.append(posiblesOpciones[0])
                    case "b":
                        self.secuencia.append(posiblesOpciones[1])
                    case "y":
                        self.secuencia.append(posiblesOpciones[2])
                    case "g":
                        self.secuencia.append(posiblesOpciones[3])
                    case _:
                        print("Introduzca una respuesta correcta.")
                print("|", "".join(self.secuencia) + self.reset, "|")
                if len(self.secuencia) == 4:
                    confirm = input(f"¿Confirmar secuencia? (S/N): ").strip().lower()
                    if confirm == "s":
                        self.fuerzaBruta()
                        break
                    else:
                        self.secuencia = []
        return self.secuencia

    def creaComputadora(self):
        posiblesOpciones = [self.rojo, self.azul, self.amarillo, self.verde]
        while True:
            self.secuencia = [random.choice(posiblesOpciones) for _ in range(4)]
            self.eleccionJugador()
            break
        print("".join(self.secuencia) + self.reset)

    def eleccionJugador(self):
        intentos = 0
        print("Elige los colores de tu secuencia (r/b/y/g). Para terminar la secuencia: ")
        while True:
            if intentos == 12:
                print("Número máximo de intentos alcanzado. Perdiste.")
                break
            eleccionJugador = []
            while len(eleccionJugador) < 4:
                opcion = input().strip().lower()
                match opcion:
                    case "r":
                        eleccionJugador.append(self.rojo)
                        self.generarPistas()
                    case "b":
                        eleccionJugador.append(self.azul)
                        self.generarPistas()
                    case "y":
                        eleccionJugador.append(self.amarillo)
                        self.generarPistas()
                    case "g":
                        eleccionJugador.append(self.verde)
                        self.generarPistas()
                    case _:
                        print("Introduzca una respuesta correcta.")
            if eleccionJugador == self.secuencia:
                print("¡Felicidades, has ganado!")
                break
            else:
                pistas = self.generarPistas(eleccionJugador)
                print(f"Intento {intentos + 1}: | {"".join(eleccionJugador) + self.reset} | {''.join(pistas) + self.reset}")
                eleccionJugador = []

    def generarPistas(self, secuencia=None):
        ORANGE = '\033[38;5;208m'
        if secuencia is None:
            secuencia = self.secuencia
        self.pistas = [' o ', ' o ', ' o ', ' o ']
        for i in range(len(secuencia)):
            if secuencia[i] == self.secuencia[i]:
                self.pistas[i] = (Fore.GREEN + ' o ' + self.reset)
            elif secuencia[i] in self.secuencia:
                self.pistas[i] = (ORANGE + ' o ' + self.reset)
        return self.pistas

    def fuerzaBruta(self):
        colores = [self.rojo, self.azul, self.amarillo, self.verde]
        posiblesCombinaciones = list(product(colores, repeat=4))
        secuencia = [None] * 4
        intentos = 0
        while intentos < 12 and posiblesCombinaciones:
            sleep(1)
            intento = choice(posiblesCombinaciones)
            posiblesCombinaciones.remove(intento)
            pistas = self.generarPistas(list(intento))
            print(f"Intento {intentos + 1}: | {''.join(intento) + self.reset} | {''.join(pistas) + self.reset}")
            if all(pista == (Fore.GREEN + ' o ' + self.reset) for pista in pistas):
                print("¡La secuencia ha sido adivinada!")
                break
            for i in range(4):
                if pistas[i] == (Fore.GREEN + ' o ' + self.reset):
                    secuencia[i] = intento[i]
                else:
                    posiblesCombinaciones = [comb for comb in posiblesCombinaciones if comb[i] != intento[i] or secuencia[i] == intento[i]]
            intentos += 1

def main():
    Juego = Game(azul=(Fore.BLUE + ' O '), rojo=(Fore.RED + ' O '), amarillo=(Fore.YELLOW + ' O '), verde=(Fore.GREEN + ' O '), reset=Fore.RESET)
    Juego.elegirModo()
    
if __name__ == "__main__":
    main()