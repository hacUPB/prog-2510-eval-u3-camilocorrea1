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

# Ejercicio 5

El Ministerio de Salud clasifica las personas según las etapas del ciclo de vida, con el fin de tener una idea sobre su vulnerabilidad. Diseñe un algoritmo que pida al usuario su edad y la clasifique según la etapa del ciclo de vida que le corresponda. Verifique que el usuario no ingrese valores menores a cero. Clasificación etaria de la población colombiana:

- Primera Infancia (0-5 años)
- Infancia (6 - 11 años)
- Adolescencia (12 - 18 años)
- Juventud (14 - 26 años)
- Adultez (27- 59 años)
- Persona Mayor (60 años o más) envejecimiento y vejez

```
edad = int(input("Por favor, ingresa tu edad: "))

if edad >= 0:
    if edad <= 5:
        etapa = "Primera Infancia"
    elif edad <= 11:
        etapa = "Infancia"
    elif edad <= 14:
        etapa = "Adolescencia"
    elif edad <= 18:
        etapa = "Adolecencia y juventud"
    elif edad <= 26:
        etapa = "Juventud"
    elif edad <= 59:
        etapa = "Adultez"
    else:
        etapa = "Persona Mayor (Envejecimiento y Vejez)"
    
    print(f"Tu etapa del ciclo de vida es: {etapa}")
else:
    print("La edad ingresada no es válida.")
```

# Ejercicios adicionales

## Verificar contraseña

- Pide al usuario que ingrese una contraseña.
- Si es correcta, imprimes "Acceso concedido", de lo contrario "Acceso denegado".
- Usa `if-else`.

```
contraseña_correcta = "1234cct"
contraseña = input("Ingrese la contraseña: ")

if contraseña == contraseña_correcta:
    print("Acceso concedido")
else:
    print("Acceso denegado")
```

## Clasificar calificaciones

- Pide al usuario una nota (0 a 5).
- Usa `if-elif-else` para clasificar (por ejemplo, 0-2 "Baja", 3-4 "Media", 5 "Alta").

```
nota = float(input("Ingrese la nota a clasificar(0 a 5): "))

if nota < 3:
    print("Baja")
elif nota < 4:
    print("Basico")
elif nota < 4.5:
    print("Alto")
elif nota <= 5:
    print("Superior")
else:
    print("Nota no valida")
```

## Operación aritmética

- Pide al usuario dos números y una opción: `+`, , , `/`.
- Utiliza `match-case` o `if-elif-else` para realizar la operación y mostrar el resultado.

```
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

print("1. suma(+)\n2. division(/)")
opcion = input("Elija una opcion: ")

match opcion:
        case '1':
            suma = num1 +num2
            print(f"El resultado de la suma es: {suma}")
        case '2':
            if num2 == 0:
                print("No es posible dividir por 0")
            else:
                division = num1/num2
                print(f"El resultado de la division es: {division}")
```
