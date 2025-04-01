# Ejercicio 1.

¿Cuál es el rango de datos que se puede representar con 32 bits?

El primer bit representara el signo y el resto de los datos representaran el dato en codigo binario.
Teniendo esto en cuenta calculamos 2^31 = 2 147 483 647

El rango sera entonces desde -2 147 483 648 hasta 2 147 483 647

# Ejercicio 2.

Abre la consola de Python (asegúrate de estar usando la versión 3) y realiza las siguientes operaciones.

```
suma = 2 + 3
multiplicacion = 10 * 5
division = 15 / 3
print(suma)
print(multiplicacion)
print(division)
```

# Ejercicio 3.

Intenta explicar cuál es el error de sintaxis que aparece en este codigo. Luego corrígelo para que se pueda imprimir correctamente la frase: Yo le dije: “cómo estás?”

```
print("Yo le dije: "como estas?" ")
```

El problema de este codigo es el uso doble de  " ", para corregir esto podemos usar unas " " y ' '.

```
print('Yo le dije: "como estas?" ')
```


