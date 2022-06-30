respuesta = "s"
while respuesta == "s":
    print("***************BIENVENIDO***************")
    num1 = float(input("Introduce primer valor: "))
    num2 = float(input("Introduce segundo valor: "))
    if print(" "):
        print("La suma de los valores es: ", num1 + num2)
    elif num1 + num2:
        print("La suma de los valores es:", num1 + num2)
    else :
        print("")
        respuesta = input()
    print("_____________________________________________________________________")