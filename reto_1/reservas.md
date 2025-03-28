# Analisis codigo

Este código permite al usuario reservar un boleto de avión con base en la ciudad de origen y destino, el día de la semana, la fecha y la preferencia de asiento. Por ultimo, asigna un precio y un asiento.

# Variables de entrada

- **nombre**: El usuario ingresa nombre y apellido.

- **titulo**: El usuario indica si es "Sr." o "Sra.".

- **origen**: El usuario ingresa la ciudad de origen del vuelo (Medellín, Bogotá, Cartagena).

- **destino**: El usuario ingresa la Ciudad de destino del vuelo (Medellín, Bogotá, Cartagena).

- **semana**: El usuario ingresa  el día de la semana en que se realizará el vuelo.

- **dia**: El usuario ingresa el día del mes (1-30).

- **preferencia**: El usuario ingresa la preferencia de asiento (pasillo, ventana, sin preferencia).

# Variables de salida

- **precio**: Se muestra el precio del boleto determinado por la distancia y el día de la semana.

- **asiento**: Se muestra el número y letra del asiento asignado.

# Otras variables

- **distancia**: Es la distancia entre la ciudad de origen y la de destino. Esta sirve para determinar el precio.

- **let_asiento**: Es la letra del asiento según la preferencia del usuario.

    - **"A"**: Ventana

    - **"B"**: Sin preferencia

    - **"C"**: Pasillo

- **num_asiento**: Es el número aleatorio entre 1 y 29 asignado al asiento.

# Pseudocodigo

```
Inicio  

Escribir "Ingrese su nombre y apellido: "    
Escribir "Ingrese su título 'Sr' o 'Sra': "  
Leer nombre, titulo    
    
Si titulo es "sr"  
    Escribir "Sr. ", nombre, " ¡Bienvenido a FastFast Airlines!"  
Sino
    Si titulo es "sra"  
        Escribir "Sra. ", nombre, " ¡Bienvenida a FastFast Airlines!"  
    Sino  
        Escribir "Título no reconocido. Ingrese 'Sr' o 'Sra'"  
    
Escribir "Seleccione una ciudad de origen (Medellin, Bogota, Cartagena): "       
Escribir "Seleccione una ciudad de destino (Medellin, Bogota, Cartagena): "    
Escribir "Ingrese el día de la semana: "  
Escribir "Ingrese el día del mes (1-30): "  
Leer origen, destino, semana, dia  
      
Si (origen es "medellin" Y destino es "bogota") O (origen es "bogota" Y destino es "medellin")  
    distancia = 240  
Sino
    Si (origen es "medellin" Y destino es "cartagena") O (origen es "cartagena" Y destino es "medellin")  
        distancia = 461  
    Sino
        Si (origen es "cartagena" Y destino es "bogota") O (origen es "bogota" Y destino es "cartagena")  
            distancia = 657  
        Sino  
            Escribir "Origen o destino no reconocido. Ingrese (Medellin, Bogota, Cartagena)"  
 
Si distancia < 400  
    Si semana es ("lunes", "martes", "miércoles", "jueves")  
            precio = 79900  
    Sino
        Si semana es ("viernes", "sábado", "domingo")  
            precio = 119900  
        Sino  
            Escribir "Ingrese un día de la semana correcto"  
Sino
    Si distancia >= 400  
        Si semana es ("lunes", "martes", "miércoles", "jueves")  
            precio = 156900  
        Sino
            Si semana es ("viernes", "sábado", "domingo")  
                precio = 213000  
            Sino  
                Escribir "Ingrese un día de la semana correcto"  
      
  
Escribir "¿Qué preferencia de asiento tiene? (pasillo, ventana, sin preferencia): "  
Leer preferencia  
 
Si preferencia es "pasillo"  
        let_asiento = 'C'  
Sino
    Si preferencia es "ventana"  
        let_asiento = 'A'  
    Sino
        Si preferencia es "sin preferencia"  
            let_asiento = 'B'  
        Sino  
            Escribir "Ingrese una preferencia adecuada"  
 
num_asiento = numero_aleatorio(1, 29)  
asiento = {num_asiento}{let_asiento}  

Escribir "Tu vuelo de ", origen, " a ", destino, " del ", semana, " ", dia, " está reservado."  
Escribir "Precio del boleto: ", precio  
Escribir "Tu asiento es: ", asiento  

Fin
```
