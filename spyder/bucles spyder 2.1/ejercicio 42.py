#42. Imprima el siguiente patrón con el ciclo for. 
cadena=""
for contador in range(0,5):
    cadena=cadena+"*"
    print(cadena)
longitud=len(cadena)
for contador in range (0,5):
    cadena=cadena[0:longitud-contador-1]
    print(cadena)
    
 