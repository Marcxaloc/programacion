#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza 
#elif.

numero=input("dime una letra: ")
if numero.isupper()==True:
    print("la letra es mayúscula")
elif numero.islower()==True:
    print("la letra es minuscula")
elif numero.isnumeric()==True:
    print("el valor introduccido es un numero")
else:
    print("El valor introducido es un símbolo")


