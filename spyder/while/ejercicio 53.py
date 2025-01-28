#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
#sumas y el número de repeticiones. Con While
repetir="si"
total=0
while repetir=="si":
    numero1=int(input("dime el primer numero: "))
    numero2=int(input("dime otro numero: "))
    suma=numero1+numero2
    print("la suma de los numeros enteros es",suma)
    repetir=input("quieres repetir: ")
    total=total+suma
print("la suma total es",total)