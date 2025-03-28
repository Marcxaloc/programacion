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
error=False

if len(password)<6 or len(password)>8:
    print("Error, el password té una longitud de",len(password)," caràcters i no compleix els requisits")
else:
    if not password[0].isnumeric():
        print("Error en el caràcter 1")
        error=True
    elif int(password[0])<1 or int(password[0])>5:
        print("Error en el caràcter 1")
        error=True
    if not password[1].islower():
        print("Error en el caràcter 2")
        error=True
    if not password[2].isupper():
        print("Error en el caràcter 3")  
        error=True
    if not password[3]=="*" and not password[3]=="_" and not password[3]=="@":
        print("Error en el caràcter 4")  
        error=True
    if not password[4].islower():
        print("Error en el caràcter 5")  
        error=True
    if not password[5].isnumeric():
        print("Error en el caràcter 6") 
        error=True
    elif int(password[5])<6 or int(password[5])>9:
        print("Error en el caràcter 6") 
        error=True
    if len(password)>=7:    
        if not password[6]=="&" and not password[6]=="/" and not password[6]=="#":
            print("Error en el caràcter 7")  
            error=True
    if len(password)>=8:
        if not password[7].isnumeric():
            print("Error en el caràcter 8") 
            error=True
        elif int(password[7])>5:
            print("Error en el caràcter 8")  
            error=True
    if not error:
        print("El format del PASSWORD és correcte")
