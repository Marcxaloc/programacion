nota=int(input("dime una nota: "))
if nota>10 or nota<0:
    print("La nota que has introducido no está entre 0 y 10")
elif nota>=5:
    print("has sacado un",nota," y has aprobado")
else:
    print("Has sacado un",nota," y has suspendido")
    
