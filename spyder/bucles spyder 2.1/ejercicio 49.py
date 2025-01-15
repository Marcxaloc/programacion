#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.
var=input("introduzca la palabra: ")

var1=input("dime una letra: ")
contador=0
for k in var:
    contador+=1
    if k==var1:
        print(f"la letra {var1} se encuentra en la posicion",contador)