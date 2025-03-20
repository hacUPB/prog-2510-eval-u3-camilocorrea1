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