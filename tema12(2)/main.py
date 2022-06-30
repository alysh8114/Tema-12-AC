num1 = int(input("Introduce primer valor: "))
num2 = int(input("Introduce segundo valor: "))
num3 = int(input("Introduce tercer valor: "))
if num1 > num2 > num3:
    print("El primer valor es mayor")
elif num1 < num2 > num3:
    print("El segundo valor es mayor")
elif num1 == num2 == num3:
    print("Los tres valores son iguales")
else:
    print("El tercer valor es mayor")
