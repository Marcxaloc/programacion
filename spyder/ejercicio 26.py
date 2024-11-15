#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
#está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición
numero=input("dime una letra: ")
if numero.isupper()==True:
    print("la letra es mayúscula")
if numero.islower()==True:
    print("la letra es minuscula")
else:
    print("la letra es mayuscula¿?")