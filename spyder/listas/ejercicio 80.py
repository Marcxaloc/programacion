#80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no.
lista=[]
numero=""
numero=input("introduce un numero: ")
lista=numero.split(".")
if len(lista)==2:
    if lista[0].isnumeric() and lista[1].isnumeric():
        print("Es un número con decimales")
    else:
        print("no es un numero con decimales")
else:
    print("no es un numero con decimales")