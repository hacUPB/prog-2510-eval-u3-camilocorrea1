# Análisis código

Este código simula la desintegración de la órbita de un satélite debido al arrastre atmosférico. Evalúa la disminución de altitud en cada órbita y ajusta el coeficiente de arrastre con un incremento constante hasta que el satélite alcance una altitud mínima segura o se estabilice en una órbita estable.

[Código satelite](satelite.py)

# Variables de entrada

- **altitud_inicial**: El usuario ingresa la altitud inicial del satélite en kilómetros.

- **coe_arrastre**: El usuario ingresa el coeficiente de arrastre inicial.

- **alt_min**: El usuario ingresa la altitud mínima segura en kilómetros.

# Variables de salida

- **print()**: Mensajes mostrados en pantalla

    - Estado del satélite en cada órbita.

    - Si el satélite se estabiliza.

    - Si el satélite reingresa en la atmósfera.

# Otras variables y bucles

- **cont**: Es el contador de órbitas (inicia en 1).

- **estabilizado**: Referencia de la pérdida de altitud para determinar si el satélite se estabiliza (0.01 km).

- **altitud_perdida**: Pérdida de altitud en cada órbita.

- **while**: Mientras la altitud del satélite sea mayor que el límite mínimo, el bucle seguirá ejecutándose.

# Pseudocodigo

```
Inicio  
Escribir "Ingrese la altitud inicial del satelite(en km): "
Escribir "Ingrese el coeficiente de arrastre inicial: "
Escribir "Ingrese la altitud minima segura(en Km): "
Leer altitud_inicial, coe_arrastre, alt_min    
      
cont = 1    
estabilizado = 0.01  

Mientras altitud_inicial > alt_min  
    altitud_perdida = coe_arrastre * altitud_inicial  
    coe_arrastre = coe_arrastre + 0.0001  

    Si altitud_perdida < estabilizado   
        Escribir "El satélite se estabiliza en órbita a ", altitud_inicial, " km después de ", cont, " órbitas."  
        Terminar  

    altitud_inicial = altitud_inicial - altitud_perdida  
    Escribir "Órbita {cont}: Altitud actual = {altitud_inicial} km, Coeficiente de arrastre = {coe_arrastre}"  
    cont = cont + 1  
      
cont = cont - 1  
Escribir "El satélite ha reingresado en la atmósfera terrestre después de {cont} órbitas."  
Fin
```
