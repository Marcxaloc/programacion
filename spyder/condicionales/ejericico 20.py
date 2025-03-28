#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
var1=int(input("introduce un numero entre 0 y 10: "))
var2= int(input("introduce otro numero entre 0 y 10: "))
if var1>=0 and var1<=10 and var2>=0 and var2<=10:
    if var1>var2:
        print("el numero",var1,"es mayor que",var2)
    elif var2>var1:
        print("el numero",var2,"es mayor que",var1)
    else:
        print("ambos numeros son iguales")
else:
    print("Los numeros introducidos no estan dentro de los parametros")
          
