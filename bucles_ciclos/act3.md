# Lista con numeros aleatorios

- Crear una lista vacía
- Llenar esa lista con 100 números aleatorios utilizando un bucle

```
import random

lista_num = []
for num in range(100):
    lista_num.append(random.randint(1,100))
print(lista_num)
```

# Tabla de multiplicar

```
num = int(input("Ingrese el numero para hacerle la tabla de multiplicar: "))
print(f"Tabla de multiplicar del {num}")
cont =1

while cont <=10:
    t1 = num*cont
    print(f"{num}*{cont}={t1}")
    cont +=1
```

# Lista de numeros pares

```
num = int(input("Ingresa un numero entero positivo: "))
numeros_pares = []
cont = 0
for i in range(num):
    numeros_pares.append(cont)
    cont +=2
print(f"La lista de los primeros {num} números pares es: {numeros_pares}")
```

# Programa de Conversión de Temperatura

```
print("Tabla de Conversión de Temperatura")
print("-" * 60)
print("Grados Celsius   |   Grados Fahrenheit")
print("-" * 60)

for i in range(0,110,10):
    fa = (i*9/5)+32
    print(f"{i}\t\t | \t\t{fa}")
print("-" * 60)   
```

# Codigo quiz bucles

```
stock = 50
print(f"Bienvenido al sistema de inventario.Stock disponible: {stock}")

while stock != 0:
    compra = int(input("Cuantos productos quieres comprar: "))
    if compra == 0:
        print("Saliendo del inventario")
        break
    elif compra <=50:
        stock -= compra
        
        if stock == 0:
            print(f"Compra realizada. Stock restante: {stock}")  #Esta linea de codigo la coloque dentro del if.
            print("Inventario agotado")
            break
        elif stock < 0:                      # elif añadido para prevenir numeros menores de 0 en la variable stock
            stock += compra
            print("No hay suficientes productos disponibles")

        else:                               # else añadido  
            print(f"Compra realizada. Stock restante: {stock}")
    else:
        print("Ingrese un valor del stock")
```



