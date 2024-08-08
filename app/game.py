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
            respuesta = input(f'¡Bienvenido a Mastermind! \n1. Adivinar. \n2. Crear secuencia.\n').strip().lower()
            if respuesta not in ('1', '2'):
                print("Agrega una respuesta correcta.")
            else:
                if respuesta == '1':
                    self.creaComputadora()
                elif respuesta == '2':
                    self.creaJugador()
                break

    def creaJugador(self):
        posiblesOpciones = {'r': self.rojo, 'b': self.azul, 'y': self.amarillo, 'g': self.verde}
        while True:
            opcion = input("Elige los colores de tu secuencia ( r / b / y / g ): ").strip().lower()
            
            if len(opcion) != 4 or any(i not in posiblesOpciones for i in opcion):
                print("Introduzca una secuencia válida.")
            
            self.secuencia = [posiblesOpciones[i] for i in opcion]
            print("|", "".join(self.secuencia) + self.reset, "|")
            
            confirm = input(f"¿Confirmar secuencia? (S/N): ").strip().lower()
            if confirm == "s":
                self.fuerzaBruta()
                break
            else:
                self.secuencia = []


    def creaComputadora(self):
        posiblesOpciones = [self.rojo, self.azul, self.amarillo, self.verde]
        while True:
            self.secuencia = [random.choice(posiblesOpciones) for _ in range(4)]
            self.eleccionJugador()
            break
        print("".join(self.secuencia) + self.reset)

    def eleccionJugador(self):
        posiblesOpciones = {'r': self.rojo, 'b': self.azul, 'y': self.amarillo, 'g': self.verde}
        intentos = 0
        print("Introduce tu secuencia de 4 colores ( r / b / y / g ): ")

        while True:
            if intentos == 12:
                print("Número máximo de intentos alcanzado. Perdiste.")
            opcion = input().strip().lower()
            if len(opcion) != 4 or any(i not in posiblesOpciones for i in opcion):
                print("Introduzca una secuencia válida.")
            eleccionJugador = [posiblesOpciones[i] for i in opcion]
            if eleccionJugador == self.secuencia:
                print("¡Felicidades, has ganado!")
                break
            else:
                pistas = self.generarPistas(eleccionJugador)
                print(f"Intento {intentos + 1}: | {''.join(eleccionJugador) + self.reset} | {''.join(pistas) + self.reset}")
                intentos += 1


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