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