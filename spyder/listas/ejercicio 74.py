lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]

repetidos=[]
norepetidos=[]

for element in lista1:
        if element in lista2:
            repetidos.append(element)
        elif element not in lista2:
            norepetidos.append(element)
for element in lista2:
        if element not in lista1:
            norepetidos.append(element)
print(f"Están repetidos: {repetidos}")
print(f"No están repetidos: {norepetidos}")