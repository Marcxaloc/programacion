#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
#no deben almacenarse en la lista
lista=[]
vocales_a=["a","á","à","A","Á","À"]
vocales_e=["e","è","é","E","É","È"]
vocales_i=["i","ì","í","I","Ì","Í"]
vocales_o=["o","ò","ó","O","Ò","Ó"]
vocales_u=["u","ù","ú","U","Ù","Ú"]
lista=[]
repetir=input("deseas emezar s/n: ")
while repetir=="s":
    letra=input("introduce una letra: ")
    if letra in vocales_a:
        letra="a"
    if letra in vocales_e:
        letra="e"
    if letra in vocales_i:
        letra="i"
    if letra in vocales_o:
        letra="o"
    if letra in vocales_u:
        letras="u"
    lista.append(letra)
    repetir=input("deseas repetir: ")
print(set(lista))