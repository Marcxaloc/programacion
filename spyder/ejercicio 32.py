#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
#no distinguir entre mayúsculas y minúsculas

frase= "A quién madruga Dios ayuda"
c=input("dime la palabra que quieres buscar: ")
a=frase.find(c)
frase=frase.lower()
b=frase.find(c)
if a>1:
    print("La palabra está en la frase y está en el índice",a)
elif b>1:
    print("La palabra está en la frase y está en el índice",b)
else:
    print("La palabra no está en la frase")