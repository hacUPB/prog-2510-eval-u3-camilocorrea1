altitud_inicial = float(input("Ingrese la altitud inicial del satelite(en km): "))
coe_arrastre = float(input("Ingrese el coeficiente de arrastre inicial: "))
alt_min = float(input("Ingrese la altitud minima segura(en Km): "))
cont = 1
estabilizado = 0.01
while altitud_inicial > alt_min:
    altitud_perdida = coe_arrastre*altitud_inicial
    coe_arrastre += 0.0001
    if altitud_perdida < estabilizado:
        print(f"el satélite se estabiliza en órbita a {altitud_inicial}km después de {cont} órbitas.")
        break   
    altitud_inicial -= altitud_perdida
    print(f"Órbita {cont}: Altitud actual = {altitud_inicial} km, Coeficiente de arrastre = {coe_arrastre}")
    cont += 1
cont -=1
print(f"El satélite ha reingresado en la atmósfera terrestre después de {cont} órbitas.")
    