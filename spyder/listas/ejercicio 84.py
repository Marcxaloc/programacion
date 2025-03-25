#84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las 
#palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la 
#palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra. 
import random
listapalabras=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
listaletras=[]
listadesorden=[]
palabra= random.choice(listapalabras)
for recorrer in palabra:
    listaletras.append(recorrer)
random.shuffle(listaletras)
palabradesorden="".join(listaletras)
print("adivina la palabra",palabradesorden)
usuario=input("introduce la palabra: ")
while usuario!=palabra:
    print("error no es correcto")
    usuario=input("introduce la palabra: ")
else:
    print("has adivinado")