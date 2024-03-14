import random



def adivinar_numero():
    N=random.randint(1,10)
    Adivinado=input('Ingrese un numero: ')
    if int(Adivinado)==N:
        return(print('Has adivinado el numero'))
    else:
        return(print("El numero adivinado es incorrecto, el numero correcto era",str(N)))
    
    
adivinar_numero()
