#43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra
palabra=input("introduce una palabra: ")
posicion=0
for var in palabra:
    print("en la posicion",posicion,"esta la:",var)
    posicion=posicion+1