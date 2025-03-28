#printeamos las instrucciones 
print("""
Instrucciones 
1. la longitud del password té que tenir una longitud d’entre 6 i 8 caràcters
2. Forçar els valors segons la posició indicada:
    posición 1 un número major o igual que 1 i menos o igual que 5
    posición 2 una lletra minúscula 
    posición 3 una lletra majúscula 
    posición 4 un dels següents símbols *,_,@
    posición 5 una lletra minúscula 
    posición 6 un número major o igual que 6 i menor o igual que 9
    posición 7 un dels següents símbols &,/,#
    posición 8 un número menor o igual que 5
""")
#primero todas las variables las ponemos como error y usamos el str para poder usar la longitud del password como letras 
password=input("Introduce una palabra clave: ")
Errorlongitud="Error, el password té una longitud de " + str(len(password)) + " caràcters i no compleix els requisits"
Error0=" Error en el caràcter 1."
Error1=" Error en el caràcter 2."
Error2=" Error en el caràcter 3."
Error3=" Error en el caràcter 4."
Error4=" Error en el caràcter 5."
Error5=" Error en el caràcter 6."
Error6=" Error en el caràcter 7."
Error7=" Error en el caràcter 8."
# esta varialble concadena todas las otras para sumar los errores para seber si el password es correcte 
errores=""
#primero de todo hacemos que la longitud del password sea entre 6 y 8
if len(password)>=6 and len(password)<=8:
    Errorlongitud=""   
# despues hacemos que el primer caracter sea un numero y si es un numero y es ,ayor o igual que uno y menor o igual que 5 quitamos el error
    if password[0].isnumeric():
        if int(password[0])>=1 and int(password[0])<=5:
            Error0= ""
# el siguiente tiene que ser una letra minuscula a si que usmos un islower para saber si la letra es minuscula si es estonces quitamos el error
    if password[1].islower():
        Error1= ""
#el siguiente tiene que ser una letra mayuscula a si que usmos un isupper para saber si la letra es mayuscula si es estonces quitamos el error
    if password[2].isupper():
        Error2= ""
#el siguiente usamos el doble igual para comparar y decir que hay que usar uno de estos simbulos/signos.
    if password[3]=="*" or password[3]=="_" or password[3]=="@":
        Error3= ""
# el siguiente tiene que ser una letra minuscula a si que usmos un islower para saber si la letra es minuscula si es estonces quitamos el error
    if password[4].islower():
        Error4= ""
# despues hacemos que el primer caracter sea un numero y si es un numero y es ,ayor o igual que 6 y menor o igual que 9 quitamos el error
    if password[5].isnumeric():
        if int(password[5])>=6 and int(password[5])<=9:
            Error5= ""
#si la lonjitud del password es mas o igua que 7 que haga los sigienetes pasos si no quitamos el error
    if len(password)>=7:         
        if password[6]=="&" or password[6]=="/" or password[6]=="#":
            Error6= ""
    else:
        Error6= ""
#si la lonjitud del password es mas o igua que 8 que haga los sigienetes pasos si no quitamos el error
    if len(password)>=8:
        if password[7].isnumeric():
            if int(password[7])<=5:
                Error7= "" 
    else:
        Error7=""            
            
# sumamos todos los errores y si no hay ninguno ponemos el password es correcte y sihay un error se printea el error.
Errores= Error0 + Error1 + Error2 + Error3 + Error4 + Error5 + Error6 + Error7

if Errores=="" and Errorlongitud=="":
    print ("El format del PASSWORD és correcte")
elif Errorlongitud=="":    
    print (Errores)
else:
    print (Errorlongitud)