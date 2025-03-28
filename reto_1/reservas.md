# Analisis codigo

Este código permite al usuario reservar un boleto de avión con base en la ciudad de origen y destino, el día de la semana, la fecha y la preferencia de asiento. Por ultimo, asigna un precio y un asiento.

# Variables de entrada

- **nombre** = El usuario ingresa nombre y apellido.

- **titulo** = El usuario indica si es "Sr." o "Sra.".

- **origen** = El usuario ingresa la ciudad de origen del vuelo (Medellín, Bogotá, Cartagena).

- **destino** = El usuario ingresa la Ciudad de destino del vuelo (Medellín, Bogotá, Cartagena).

- **semana** = El usuario ingresa  el día de la semana en que se realizará el vuelo.

- **dia** = El usuario ingresa el día del mes (1-30).

- **preferencia** = El usuario ingresa la preferencia de asiento (pasillo, ventana, sin preferencia).

# Variables de salida

- **precio** = Se muestra el precio del boleto determinado por la distancia y el día de la semana.

- **asiento** = Se muestra el número y letra del asiento asignado.

# Otras variables

- **distancia** = Es la distancia entre la ciudad de origen y la de destino. Esta sirve para determinar el precio.

- **let_asiento** = Es la letra del asiento según la preferencia del usuario.

    - **"A"** = Ventana

    - **"B"** = Sin preferencia

    - **"C"** = Pasillo

- **num_asiento** = Es el número aleatorio entre 1 y 29 asignado al asiento.

# Pseudocodigo

```
Inicio  

escribir "Ingrese su nombre y apellido: "    
escribir "Ingrese su título 'Sr' o 'Sra': "  
leer nombre, titulo    
    
si titulo es "sr"  
    escribir "Sr. ", nombre, " ¡Bienvenido a FastFast Airlines!"  
sino
    si titulo es "sra"  
        escribir "Sra. ", nombre, " ¡Bienvenida a FastFast Airlines!"  
    sino  
        escribir "Título no reconocido. Ingrese 'Sr' o 'Sra'"  
    
escribir "Seleccione una ciudad de origen (Medellin, Bogota, Cartagena): "       
escribir "Seleccione una ciudad de destino (Medellin, Bogota, Cartagena): "    
escribir "Ingrese el día de la semana: "  
escribir "Ingrese el día del mes (1-30): "  
leer origen, destino, semana, dia  
      
si (origen es "medellin" Y destino es "bogota") o (origen es "bogota" Y destino es "medellin")  
    distancia = 240  
sino
    si (origen es "medellin" Y destino es "cartagena") o (origen es "cartagena" Y destino es "medellin")  
        distancia = 461  
    sino
        si (origen es "cartagena" Y destino es "bogota") o (origen es "bogota" Y destino es "cartagena")  
            distancia = 657  
        sino  
            escribir "Origen o destino no reconocido. Ingrese (Medellin, Bogota, Cartagena)"  
 
si distancia < 400  
    si semana es ("lunes", "martes", "miércoles", "jueves")  
            precio = 79900  
    sino
        si semana es ("viernes", "sábado", "domingo")  
            precio = 119900  
        sino  
            escribir "Ingrese un día de la semana correcto"  
sino
    si distancia >= 400  
        si semana es ("lunes", "martes", "miércoles", "jueves")  
            precio = 156900  
        sino
            si semana es ("viernes", "sábado", "domingo")  
                precio = 213000  
            sino  
                escribir "Ingrese un día de la semana correcto"  
      
  
escribir "¿Qué preferencia de asiento tiene? (pasillo, ventana, sin preferencia): "  
leer preferencia  
 
si preferencia es "pasillo"  
        let_asiento = 'C'  
sino
    si preferencia es "ventana"  
        let_asiento = 'A'  
    sino
        si preferencia es "sin preferencia"  
            let_asiento = 'B'  
        sino  
            escribir "Ingrese una preferencia adecuada"  
 
num_asiento = numero_aleatorio(1, 29)  
asiento = {num_asiento}{let_asiento}  

escribir "Tu vuelo de ", origen, " a ", destino, " del ", semana, " ", dia, " está reservado."  
escribir "Precio del boleto: ", precio  
escribir "Tu asiento es: ", asiento  

Fin
```
