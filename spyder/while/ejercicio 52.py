#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
#pantalla. El programa preguntará si deseas o no repetir la operación. Con While
repetir="si"
while repetir=="si":
    numero1=int(input("dime el primer numero: "))
    numero2=int(input("dime otro numero: "))
    suma=numero1+numero2
    print("la suma de los numeros enteros es",suma)
    repetir=input("quieres repetir: ")
