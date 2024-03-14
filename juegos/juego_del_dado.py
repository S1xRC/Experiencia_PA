import random
import time


def juego_del_dado():
    print("\n\nEn este juego compites contra la computadora, el primero en llegar a 30 lanzando un dado de 6 caras gana.\n")
    puntaje_jugador = 0
    puntaje_computadora = 0
    while True:
        print("Turno del jugador:\n")
        puntaje = input("¡Lanza el dado!\n\n")
        time.sleep(0.5)
        puntaje = random.randint(1, 6)
        print(f"\n¡Obtuviste {puntaje} puntos!\n")
        time.sleep(0.5)
        puntaje_jugador += puntaje
        if puntaje_jugador >= 30:
            print("¡El jugador gano! :DD")
            break
        time.sleep(0.5)
        print("Turno de la computadora:\n")
        time.sleep(0.5)
        puntaje = random.randint(1, 6)
        print(f"La computadora lanzo y obtuvo {puntaje} puntos\n")
        time.sleep(0.5)
        puntaje_computadora += puntaje
        if puntaje_computadora >= 30:
            print("La computadora gano :(((")
            break
        print(
            f"Puntajes:\n\n| Jugador: {puntaje_jugador} | Computadora: {puntaje_computadora} |\n")
        time.sleep(0.5)


juego_del_dado()