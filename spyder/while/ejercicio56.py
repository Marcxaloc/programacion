#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
#compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
#dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
#visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
#realización de un pedido, si quiere gestionar otro. 
#El establecimiento contempla los siguientes descuentos:
#Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
#Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%
#Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:
#• El número de pedidos realizados
#• Total a pagar.
#• Total con IVA (10%)
#• Total con el descuento aplicado.
print("""
MENÚ
1. Bocadillo de calamares- 9 €"
2. Bocadillo de chistorra - 4.5 €
3. Bikini de jamón - 2.5 €"

ACOMPAÑAMIENTO
1. Patatas finas - 1.5 €
2. Patatas gruesas - 1.75 €
3. Patatas rústicas - 2 €

BEBIDAS
1. Coca cola - 2 €"
2. Acuarius - 1.5 €
3. Agua - 1 €"
""")
totaldec=0
descuento=0
precio=0
pedido=0
bocadillos=0
repetir="si"
while repetir=="si":
    pedido=pedido+1
    bocata=int(input("que bocata quieres? [1/2/3]:"))
    patatas=int(input("que patatas quieres?[1/2/3]:"))
    bebidas=int(input("que bebida quieres?[1/2/3]:"))
    if bocata==1:
        precio=precio+9
    elif bocata==2:
        precio=precio+4.5
    else:
        precio=precio+2.5
    if patatas==1:
        precio=precio+1.5
    elif patatas==2:
        precio=precio+1.75
    else:
        precio=precio+2
    if bebidas==1:
        precio=precio+2
    elif bebidas==2:
        precio=precio+1.5
    else:
        precio=precio+1
    repetir=input("quieres otro menu?[si/no]:")
iva=precio*0.1
totaliv=precio+iva
if totaliv<=30 and totaliv>=20:
    descuento=totaliv*0.05
    totaldesc=totaliv-descuento
    print("te añadimos un 5% de descuento porque el precio esta entre 20 y 30 el total es",totaldesc)
elif totaliv>30:
    descuento1=totaliv*0.15
    totaldesc1=totaliv-descuento1
    print("te añadimos un 15% de descuento porque el precio es mayor a 30 el total es",totaldesc1)
print("el numero de pedidos que has pedido son",pedido)
print("el total a pagar son",precio)
print("el total a pagar con iva es",totaliv)
print("fin")

    
    