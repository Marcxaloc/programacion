#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales
var1=int(input("introduce un numero: "))
var2= int(input("introduce otro numero: "))
if var1>var2:
    print("el numero",var1,"es mayor que",var2)
elif var2>var1:
    print("el numero",var2,"es mayor que",var1)
else:
    print("ambos numeros son iguales")
