#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
#notas inferiores a 0 y superiores a 10
notas=int(input("Introduce el número de notas que deseas introducir: "))
for contador in range (0,notas):
    var1=int(input("nota:"))
    if var1>=0 and var1<=10:
        if var1>=5:
            print("has aprobado")
        if var1<5:
            print("has suspendido")
    else:
        print("Has introducido una nota equivocada")
