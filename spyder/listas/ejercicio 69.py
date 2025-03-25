#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
#irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
#ordenados de menor a mayor.
lista=[]
numero=int(input("cuantos numeros quieres: "))
for x in range (0,numero):
    x=int(input("dime los numeros: "))
    lista.append(x)
lista.sort()
print(lista)
