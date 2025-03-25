cifras=int(input("cuantas cifras quieres: "))
suma=0
for contador in range (0,cifras):
    numero=int(input("dime un numero: "))
    suma=suma+numero
print("resultado es:",suma)