#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es
#igual, menor o mayor de 11 caracteres. Utiliza elif
frase=input("dime una frase: ")
numeros=len(frase)
if numeros>11:
    print("La frase tiene 11 o más caracteres")
elif numeros<11:
    print("La frase tiene menos de 11 caracteres")
else:
    print("la frase tiene 11 caracteres")