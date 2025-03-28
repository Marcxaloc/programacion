#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un 
#notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota 
#introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
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