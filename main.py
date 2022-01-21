"""
Ejercicio 6
Enunciado: Crea una función que convierta un password (entre 6 y 12 caracteres) en una cadena de texto alfanumérica
de 32 caracteres. La función SIEMPRE debe devolver el mismo resultado para la misma entrada.
Objetivo:
    - Aprender a manejar los bucles y las cadena de texto.
    - Mejorar la capacidad algorítmica.

@author Rafael
"""

def cifrado(contrasenya):
    i=0
    newContrasenya=""
    contador=0


    while i < len(contrasenya):
        tamanyo = len(contrasenya)
        posicion = i + 3
        if i+3 >= len(contrasenya):
            a = ((i+3)-len(contrasenya))
            newContrasenya = newContrasenya + contrasenya[a] + str(contador)
        else:
            newContrasenya = newContrasenya + contrasenya[i+3] + str(contador)

        i=i+1
        contador = contador + 1
    return newContrasenya

def aumentarTamanyo(newContrasenya):

    i=0
    newContrasenya2=newContrasenya
    tamanyoPassword=len(newContrasenya)

    while tamanyoPassword < 32:
        lenNewContrasenya=len(newContrasenya)
        if i >= len(newContrasenya):
            a = i - len(newContrasenya)
            newContrasenya2 = newContrasenya2 + newContrasenya[a]
        else:
            newContrasenya2 = newContrasenya2 + newContrasenya[i]

        i = i + 1
        tamanyoPassword=tamanyoPassword+1
    return newContrasenya2

contrasenya = input("Introduce la contraseña (Entre 6 y 12 caracteres): ")
condicion = True
tamanyo = len(contrasenya)

while condicion:
    if tamanyo>12 or tamanyo<6:
        print("La contraseña ha de contener entre 6 y 12 caracteres y usted ha utilizado " + str(tamanyo)
              + ".\nIntenelo de nuevo.")
        contrasenya = input("Introduce la contraseña (Entre 6 y 12 caracteres): ")
        tamanyo = len(contrasenya)
    else: 
        condicion=False
        contrasenya = cifrado(contrasenya)
        print("La contraseña despues de la 1º codificacion es: " + contrasenya)
        contrasenya2 = aumentarTamanyo(contrasenya)
        print("La contraseña despues de la 2º codificacion es: " + contrasenya2 + " su tamanyo es: "
              + (str)(len(contrasenya2)))
