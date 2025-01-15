#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado 
#o suspendido.
notas=int(input("Introduce el número de notas que deseas introducir: "))
for contador in range (0,notas):
    var1=float(input("nota:"))
    if var1>=5:
        print("has aprobado")
    if var1<5:
        print("has suspendido")