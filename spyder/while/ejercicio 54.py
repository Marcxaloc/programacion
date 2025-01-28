#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
#de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
#preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
#operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural.. . Con While
total=0
operaciones=0
while total<50:
    numero1=int(input("dime el primer numero: "))
    numero2=int(input("dime otro numero: "))
    suma=numero1+numero2
    print("la suma de los numeros enteros es",suma)
    total=total+suma
    operaciones=operaciones+1
    if operaciones==1:
        print("la suma total es",total,"y llevas",operaciones,"operacion realizada")
    else:
        print("la suma total es",total,"y llevas",operaciones,"operaciones realizadas")
    