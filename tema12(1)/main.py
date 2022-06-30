n1 = float(input("Introduce tu primer número: "))
n2 = float(input("Introduce tu segundo número: "))
while True:
    print("***********************************************")
    print("Dime, ¿qué funcion quieres hacer?")
    print("1) Sumar los dos números")
    print("2) Restar los dos números")
    print("3) Multiplicar los dos números")
    print("4) Dividir los dos números")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de los 2 numero es: ", n1 + n2)
    elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta de los 2 numero es: ", n1 - n2)
    elif opcion == 3:
        print(" ")
        print("RESULTADO: La multiplicaion de los 2 numero es: ", n1 * n2)
    elif opcion == 4:
        print(" ")
        print("RESULTADO: La division de los 2 numero es: ", n1 / n2)

    else:
        print("Opción incorrecta")