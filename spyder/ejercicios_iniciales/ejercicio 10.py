var1=float (input("dieme un numero: "))
var2=float (input("dime el segundo numero: "))

cociente=var1/var2
print("el cociente es ", cociente)
resto=var1%var2
print("el resto es ", resto)


if resto==0:
    print("par")
else:
    print("impar")
