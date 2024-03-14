import random
def adivinar_par_o_impar():
    Numero=random.randint(0,1)
    Adivinado=input('Adivine si el numero es par o impar, ingresando Par o Impar respectivamente: ')
    if Adivinado=='Par' and Numero==0:
        return(print('Has adivinado correctamente, el numero era par'))
    elif Adivinado=='Impar' and Numero==1:
        return(print('Has adivinado correctamente, el numero era impar'))
    else:
        return(print('Has adivinado incorrectamente'))
adivinar_par_o_impar()