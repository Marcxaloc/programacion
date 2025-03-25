# 73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están 
#repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se 
#repiten y cuales no
lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]

repetidos=[]
norepetidos=[]

for element in lista1:
        if element in lista2:
            repetidos.append(element)
        elif element not in lista2:
            norepetidos.append(element)


print(f"Están repetidos: {repetidos}")
print(f"No están repetidos: {norepetidos}")
