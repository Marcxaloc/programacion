var=input("introduzca la palabra: ")
for i in range (len(var)):
    var1=input("dime una letra: ")
    if var1 in var:
        print("existe")
    else:
        print("letra no existe")