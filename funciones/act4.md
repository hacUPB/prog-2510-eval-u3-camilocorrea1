# Ejercicio de clase

```
def mcd(num,den):
    if num<= den:
        menor = num
    else:
        menor = den

    for divisor in range(menor,0,-1):
        if num % divisor == 0 and den % divisor == 0:
            max_cm_divisor = divisor
            break
    return max_cm_divisor

def imprime_fraccion(num, den, mc):
    numerador = num/mc
    denominador = den/mc
    fraccion = print(f'{num}/{den} = {numerador}/{denominador}')
    
    

def main():
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))
    maximo = mcd(numerador, denominador)
    print(f"MCD = {maximo}")
    fraccion = imprime_fraccion(numerador,denominador,maximo)
if __name__ == "__main__":
    main()
```

# Conversion de puntos

```
def convertir_puntuacion(puntuacion: int):
    if puntuacion > 100 or puntuacion < 0:
        print("Puntuacion invalida")
    elif 90 <= puntuacion <= 100:
        nota = "A"
    elif puntuacion >= 80:
        nota = "B"
    elif puntuacion >=70:
        nota = "C"
    elif puntuacion >= 60:
        nota = "D"
    elif puntuacion >= 0:
        nota = "F"
    return nota

def main():
    puntuacion = int(input("Ingrese la puntuacion a convertir: "))
    nota = convertir_puntuacion(puntuacion)
    print(nota)
    
    
if __name__ == "__main__":
    main()
```

# Determinar dia

```
def determinar_dia(num: int):
    if num > 7 or num < 1:
        print("Número de día inválido")
    else:
        if num == 1:
            dia = "Lunes"
        elif num == 2:
            dia = "Martes"
        elif num == 3:
            dia = "Miercoles"
        elif num == 4:
            dia = "Jueves"
        elif num == 5:
            dia = "Viernes"
        elif num == 6:
            dia = "Sabado"
        elif num == 7:
            dia = "Domingo"
        return dia

def main():
    num = int(input("Ingrese un numero entero del 1 al 7: "))
    dia = determinar_dia(num)
    print(dia)
     
    
if __name__ == "__main__":
    main()
```

