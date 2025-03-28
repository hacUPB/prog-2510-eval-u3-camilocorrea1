import random
nombre = input("Ingrese su nombre y apellido: ")
titulo = input("Ingrese su titulo 'Sr' o 'Sra': ").lower()
if titulo == "sr":
    print(f"Sr. {nombre}, ¡Bienvenido a FastFast Airlines! ")
elif titulo == "sra":
    print(f"Sra. {nombre}, ¡Bienvenida a FastFast Airlines! ")
else:
    print("Titulo no reconocido. Ingrese 'Sr' o 'Sra' ")

origen = input("selecione una ciudad de origen (Medellin, Bogota, Cartagena): ").lower()
destino = input("selecione una ciudad de destino (Medellin, Bogota, Cartagena): ").lower()
semana = input("ingrese el dia de la semana: ").lower()
dia = input("ingrese el dia del mes(1-30): ").lower()

if origen == "medellin" and destino == "bogota" or origen == "bogota" and destino == "medellin":
    distancia = 240
elif origen == "medellin" and destino == "cartagena" or origen == "cartagena" and destino == "medellin":
    distancia = 461
elif origen == "cartagena" and destino == "bogota" or origen == "bogota" and destino == "cartagena":
    distancia = 657
else:
    print("Origen o destino no reconocido. Ingrese (Medellin, Bogota, Cartagena)")  

if distancia < 400:
    if semana in ('lunes', 'martes', 'miercoles', 'jueves'):
        precio = 79900
    elif semana in ('viernes', 'sabado', 'domingo'):
        precio = 119900
    else:
        print("Ingrese un dia de la semana correcto")
elif distancia >= 400:
    if semana in ('lunes', 'martes', 'miercoles', 'jueves'):
        precio = 156900
    elif semana in ('viernes', 'sabado', 'domingo'):
        precio = 213000
    else:
        print("Ingrese un dia de la semana correcto")
        
preferencia = input("Que preferencia de asiento tiene (pasillo, ventana , sin preferencia): ").lower().strip()
if preferencia == "pasillo":
    let_asiento = 'C'
elif preferencia == 'ventana':
    let_asiento = 'A'
elif preferencia == 'sin preferencia':
    let_asiento = 'B'
else:
    print("Ingrese una preferencia adecuada")
        
num_asiento = random.randint(1, 29)
asiento = f"{num_asiento}{let_asiento}"

print(f"Tu vuelo de {origen} a {destino} del {semana} {dia} está reservado.\nPrecio del boleto: {precio}\nTu asiento es: {asiento}")