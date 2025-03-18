# Calculadora menu

```

while True:
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    print("S. suma\nR. resta\nD. division\nM. multiplicacion\nE. salir")
    opcion = input("Elija una opcion: ").upper()

    match opcion:
        case 'S':
            suma = num1 +num2
            print(suma)
        case 'R':
            resta = num1 - num2
            print(resta)
        case 'D':
            if num2 == 0:
                print("No es posible dividir por 0")
            else:
                division = num1/num2
                print(division)
        case 'M':
            multiplicacion = num1 * num2
            print(multiplicacion)
        case 'E':
            print("Saliendo del programa")
            break
        case _:
            print("Opcion no válida.")
        
```

# Ejercicio 2

Resuelve el siguiente problema usando el condicional simple.

Un almacén cobra `$9 000` por costos de envío, pero ofrece el envío a domicilio gratis para compras superiores a `$100 000`. En caso contrario, no hay ningún descuento. Solicite al usuario el valor de la compra y calcule el valor total a pagar.

```
envio = 0
valor_com = float(input("Ingrese el valor de la compra: "))
if valor_com < 100000:
	envio = 9000
total = valor_com + envio
print(f"El total de la compra es {total}")
```

# Ejercicio 3

Determine si un número ingresado por el usuario es par o impar.

```
num = int(input("Ingresa el numero a analizar: "))
r = num%2
if r == 0:
    print(f"{num} es par")
else:
    print(f"{num} es impar")
```

# Ejercicio 4

Ahora tú debes proponer un ejercicio que pueda ser resuelto usando un condicional simple y otro con el condicional doble. Trata que la redacción de cada problema sea la adecuada y verifica que realmente tengan una solución usando el condicional adecuado.

-   Condicional simple
    Una tienda tiene un descuento del 25% a compras mayores de 120000. Solicítele al usuario el valor de la compra para saber si cumple la condición para tener el descuento.
    
-   Condición doble
    Si un estudiante tiene más de 4,5 en el promedio final del semestre recibirá un premio de 100000 pesos, si tiene mas de 4,0 recibirá un premio de 50000 y si es inferior de 4,0 no recibirá nada. Solicítele al estudiante su promedio final para saber que premio recibirá.