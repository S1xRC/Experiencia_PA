import random
import time


def memoria():
    puntaje = 0
    print("Debes memorizar 10 números entre el 1 y 10 en 10 segundos.\n")
    adivinar = []
    asd = ""
    for x in range(10):
        numero = random.randint(1, 10)
        adivinar.append(str(numero))
    asd = " ".join(adivinar)
    print("¡Memoriza! \n\n" + asd)
    time.sleep(10)
    print("#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n")

    print("¡Adivina!\n")

    for i in range(10):
        intento = input(f"{i + 1}) ")
        if intento == adivinar[i]:
            puntaje += 1
    print(f"¡Obtuviste {puntaje} puntos!\n\n Gracias por jugar :D")

memoria()