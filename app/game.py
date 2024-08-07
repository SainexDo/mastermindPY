from colorama import Fore
from time import sleep
import random

class Game:
    def __init__(self, rojo, azul, verde, amarillo, reset):
        self.rojo = rojo
        self.azul = azul
        self.verde = verde
        self.amarillo = amarillo
        self.reset = reset
        self.pistas = [' ⬜ ', ' ⬜ ', ' ⬜ ', ' ⬜ ']
        self.secuencia = []
        self.intentoDeAdivinarSecuencia = []
        self.color_a_verificar = ['🟡', '🟢', '🔴', '🔵']
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
                        self.eleccionAzar()
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
        print("".join(self.secuencia))

    def eleccionAzar(self):
        posiblesOpciones = [self.rojo, self.azul, self.amarillo, self.verde]
        intentos = 0
        while True:
            if intentos == 12:
                print(f"La computadora no ha podido adivinar. ¡Has ganado!")
                break
            else:
                sleep(1)
                intentos += 1
                print(f"Intento: {intentos}")
                eleccionComputadora = [random.choice(posiblesOpciones) for _ in range(4)]
                print('La elección de la computadora es: ', "|" + ''.join(eleccionComputadora) + Fore.RESET, ''.join(self.generarPistas(eleccionComputadora)))

                if eleccionComputadora == self.secuencia:
                    print("¡La computadora ha ganado!")
                    print(''.join(eleccionComputadora) + self.reset)
                    break

    def eleccionJugador(self):
        intentos = 1
        while True:
            if intentos > 12:
                print("Número máximo de intentos alcanzado. Perdiste.")
                break
            print(f"Ronda: {intentos}")
            eleccionJugador = []

            while len(eleccionJugador) < 4:
                opcion = input("Elige los colores de tu secuencia (r/b/y/g). Para terminar la secuencia: ").strip().lower()

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

                print("|", "".join(eleccionJugador) + self.reset, "|")
            if eleccionJugador == self.secuencia:
                print("¡Felicidades, has ganado!")
                break
            else:
                pistas = self.generarPistas(eleccionJugador)
                print(f"Pistas: {''.join(pistas)}")
                eleccionJugador = []
                intentos += 1

    def generarPistas(self, secuencia=None):
        if secuencia is None:
            secuencia = self.secuencia
        
        self.pistas = [' ⬜ ', ' ⬜ ', ' ⬜ ', ' ⬜ ']  # Reinicia las pistas a blanco por defecto

        for i in range(len(secuencia)):
            if secuencia[i] == self.secuencia[i]:
                self.pistas[i] = ' 🟩 '
            elif secuencia[i] in self.secuencia:
                self.pistas[i] = ' 🟨 '

        return self.pistas

    def fuerzaBruta(self):
        # ¡Oh no, hermano, oh no, hermano!
        pass
        

def main():
    Juego = Game(azul=" 🔵 ", rojo=" 🔴 ", amarillo=" 🟡 ", verde=" 🟢 ", reset=Fore.RESET)
    Juego.elegirModo()

if __name__ == "__main__":
    main()