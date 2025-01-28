#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior 
#haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
#cuando la suma acumulada sea inferior a 50 o la suma acumulada sea par. Con While
total=0
operaciones=0
par=0
while total<50 or par==0:
    numero1=int(input("dime el primer numero: "))
    numero2=int(input("dime otro numero: "))
    suma=numero1+numero2
    print("la suma de los numeros enteros es",suma)
    total=total+suma
    operaciones=operaciones+1
    par=total%2
    if operaciones==1:
        print("la suma total es",total,"y llevas",operaciones,"operacion realizada")
    else:
        print("la suma total es",total,"y llevas",operaciones,"operaciones realizadas")
print("programa acabado")