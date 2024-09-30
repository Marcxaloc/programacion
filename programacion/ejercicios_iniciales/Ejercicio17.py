peso = float(input("Introduce su peso en Kg: "))
estatura = float(input("Introduce su estatura en metros: "))
var2=estatura**2
var1= peso/var2
if var1<25:
    print("Si pesas",peso,"y mides",estatura,",tu IMC es:",round(var1,2))
else:
    print("Si pesas",peso,"y mides",estatura,",tu IMC es:",round(var1,2),". Hay sobrepeso")
