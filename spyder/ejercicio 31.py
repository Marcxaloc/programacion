#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
#Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su 
#índice.
frase= "A quién madruga Dios ayuda"
a=frase.find (input("dime la palabra que quieres buscar: "))
if a>1:
    print("La palabra está en la frase y está en el índice",a)
else:
    print("La palabra no está en la frase")


