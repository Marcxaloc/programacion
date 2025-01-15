#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por 
#pantalla el número total de positivos, negativos y número de 0
numeros=int(input("dime cuantos numeros quieres: "))
var0=0
var1=0
var2=0
for contador in range (0,numeros):
    var3=int(input("numero:"))
    if var3>0:
        var1=var1+1
    elif var3<0:
        var2=var2+1
    else:
        var0=var0+1
print("La cantidad de números positivos es: ",var1)
print("La cantidad de números negativos es: ",var2)
print("La cantidad de números ceros es: ",var0)