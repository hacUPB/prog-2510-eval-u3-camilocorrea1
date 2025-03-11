num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

while True:
    print("S. suma\nR. resta\nD. division\nM. multiplicacion\nE. salir")
    opcion = input("Elija una opcion: ").upper()
    if opcion == 'S':
        suma = num1 +num2
        print(suma)
    elif opcion == 'R':
        resta = num1 - num2
        print(resta)
    elif opcion == 'D':
        if num2 == 0:
            print("No es posible dividir por 0")
        else:
            division = num1/num2
            print(division)
    elif opcion == 'M':
        multiplicacion = num1 * num2
        print(multiplicacion)
    elif opcion == 'E':
        print("Saliendo del programa")
        break
    else:
        print("Opcion no válida.")
        
