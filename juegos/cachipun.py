import random

def cachipun():
    elejido_comp=random.randint(0,2)
    Eleccion=str.lower(input('Elije tu movimiento, Papel, Piedra o Tijera: '))
    Posibles=['piedra','papel','tijera']
    print('La computadora ha elejido:', Posibles[elejido_comp])
    for x in range(2):
        if Eleccion==Posibles[x]:
            Eleccion=x
    if Eleccion==elejido_comp:
        return(print('Has empatado'))
    elif Eleccion==elejido_comp+1:
        return(print('Has ganado'))
    else:
        return(print('Has perdido'))
cachipun()
