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


if len(password)>=6 and len(password)<=8:
    Errorlongitud=""
    
    if password[0].isnumeric():
        if int(password[0])>=1 and int(password[0])<=5:
            Error0= ""
    
    if password[1].islower():
        Error1= ""
    
    if password[2].isupper():
        Error2= ""
    
    if password[3]=="*" or password[3]=="_" or password[3]=="@":
        Error3= ""
        
    if password[4].islower():
        Error4= ""
        
    if password[5].isnumeric():
        if int(password[5])>=6 and int(password[5])<=9:
            Error5= ""
    if len(password)>=7:    
        if password[6]=="&" or password[6]=="/" or password[6]=="#":
            Error6= ""
    else:
        Error6= ""
        
    if len(password)>=8:
        if password[7].isnumeric():
            if int(password[7])<=5:
                Error7= "" 
    else:
        Error7=""            
            
    
Errores= Error0 + Error1 + Error2 + Error3 + Error4 + Error5 + Error6 + Error7

if Errores=="" and Errorlongitud=="":
    print ("El format del PASSWORD és correcte")
elif Errorlongitud=="":    
    print (Errores)
else:
    print (Errorlongitud)