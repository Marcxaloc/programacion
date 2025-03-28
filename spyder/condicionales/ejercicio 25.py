#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
nota=float(input("dime una nota: "))
if nota>10 or nota<0:
    print("La nota que has introducido no está entre 0 y 10")
elif nota>=8.5:
    print("tu nota es",nota," y has sacado un excelente")
elif nota>=6.5 and nota<8.5:
    print("tu nota es",nota," y has sacado un notable")
elif nota>=5 and nota<6.5:
    print("tu nota es",nota," y has sacado un suficiente")
else:
    print("Has sacado un",nota," y has suspendido")

