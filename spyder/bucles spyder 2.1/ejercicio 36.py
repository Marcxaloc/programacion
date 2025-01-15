#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.
n=int(input("introduce el valor de ´n`: "))
var1=0
for contador in range (0,n+1):
    var1=var1+contador
print("La suma total de números naturales es:",var1)