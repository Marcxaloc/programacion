#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en 
#caso de introducir un número, aparezca un aviso por pantalla
numero=input("dime una letra: ")
if numero.isupper()==True:
    print("la letra es mayúscula")
elif numero.islower()==True:
    print("la letra es minuscula")
elif numero.isnumeric()==True:
    print("el valor introduccido es un numero")
else:
    print("la letra es mayuscula¿?")
