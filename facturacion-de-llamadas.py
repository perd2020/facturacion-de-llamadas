##### REGLAS Y CONDICIONES
# Si la duracion de la llamada es menor a 5 minutos, se cobraran 3 centavos por cada segundo.
# Ejemplo:
# 00:01:07 --> 67seg * 3 = 201 centavos

# Si la duracion de la llamada dura 5 minutos o mas, se cobrara 150 centavos por cada minuto.
# Se redondeara el minuto inmediato superior en el caso de que la llamada no sea exacta en minutos.
# Ejemplo:

# 5 minutos en adelante: 150 centavos/Minuto
#	00:05:00 --> 5min * 150cent = 750 cent
#	00:05:01 --> 6min * 150cent = 900 cent  ---> Se redondea a una llamada de 6 minutos
#   00:05:33 --> 6min * 150cent = 900 cent  ---> Se redondea a una llamada de 6 minutos

# La Persona con la llamada mas larga, todas sus llamadas son gratis.
# Si hay empate, se aplicara el descuento al telefono con el numero mas chico. 

##### Ejemplos de registros de llamadas:

### Registros: 

# registros = '00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090'

# Se realizaron llamadas desde 2 numeros:
# 400-234-090
# 701-080-080


# El numero 400-234-090 suma un total de duracion de llamadas de 367 segundos ( Primer llamada de 67 segundos + Segunda llamada de 300 segundos)
# El numero 701-080-080 suma un total de duracion de llamadas de 301 segundos ( Una sola llamada de 301 segundos)


# Primer llamada asociada al numero 400-234-090 tiene una duracion de 67 segundos --> 67 (segundos) * 3 = 201   ( REGLA 1 - Menor a 5 minutos )
# Segunda llamada asociada al numero 701-080-080 tiene una duracion de 301 segundos --> 6 (minutos) * 150 = 900 ( REGLA 2 - Mayor a 5 minutos)
# Tercer llamada asociada al numero 400-234-090 tiene una duracion de 300 segundos --> 5 (minutos) * 150 = 750  ( REGLA 2 - Igual a 5 minutos)

# El numero 400-234-090 factura por un monto de: 951 ( 201 + 750 = 951 )
# El numero 701-080-080 factura por un monto de: 900

# El subtotal es de 951 + 900 = 1851

# Aplicando el descuento al numero 400-234-090 ( Ya que posee la duracion total mas larga):
# 1851 - 951 = 900

# Costo final de facturacion: 900

registros = '00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090'

registros2 = '00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090\n00:06:07,800-234-090\n00:01:00,999-234-090'

registros3 = '00:01:07,400-234-090\n00:05:01,701-080-080'

registros4 = ''

def dic_duracion(registros):
    """

    Toma como entrada todas las llamadas y te devuelve un diccionario con cada valor asociada a un numero de telefono y
    y su clave es la cantidad total de segundos de todas las llamadas de ese telefono

    """
    
    # Aca creamos una lista separando cada registro individual en duracion y en su numero asociado
    # La separacion de cada llamada esta dada por '\n'
    # Cada elemento de esta lista es una llamada
    registros_dividos = registros.split('\n')
    # Creamos un diccionario vacio
    dic = {}

    # Creamos una variable que represente la cantidad total de llamadas
    cantidad_de_llamadas = len(registros_dividos)
    
    # Iteramos para acceder a cada una de las llamadas
    for llamada in range(cantidad_de_llamadas):
        # Seleccionamos los primeros 8 caracteres que brindan informacion respecto a la duracion de la llamada
        # en cuestion
        # String
        duracion = registros_dividos[llamada][0:8]
        

        # Separamos la duracion en horas, minutos y segundos
        # Lista
        duracion_sep = duracion.split(':')
        
        # Definimos horas, minutos y segundos
        hora = int(duracion_sep[0])
        minutos = int(duracion_sep[1])
        segundos = int(duracion_sep[2])
        
        # Convertimos todo a segundos
        hora_a_seg = hora*60*60
        minutos_a_seg = minutos * 60

        # Calculamos la duracion total en segundos
        # Int
        duracion_total = hora_a_seg + minutos_a_seg + segundos
        

        # Registramos el numero del telefono asociado al registro
        # String 
        numero_telefono = registros_dividos[llamada][9:]
        
        # Corroboramos si existe un ya un registro del numero en cuestion
        if not numero_telefono in dic.keys():
            # Si no existe una clave asociada al numero, la creamos
            # Y le asociamos la duracion total en segundos de esa llamada
            dic[numero_telefono] = duracion_total
        else:
            # Si ya existe una clave asociada al numero, le sumamos la duracion de la llamada
            dic[numero_telefono] += duracion_total # dic[numero_telefono] = dic[numero_telefono] + duracion_total

    return dic

def dic_costo(registros):
    """

    Toma como entrada todas las llamadas y te devuelve un diccionario con cada valor asociada a un numero de telefono y
    y su clave es el costo total de todas las llamadas de ese telefono
    
    """

    # Aca creamos una lista separando cada registro individual en duracion y en su numero asociado
    # La separacion de cada llamada esta dada por '\n'
    # Cada elemento de esta lista es una llamada
    registros_dividos = registros.split('\n')
    # Creamos un diccionario vacio
    dic = {}

    # Creamos una variable que represente la cantidad total de llamadas
    cantidad_de_llamadas = len(registros_dividos)
    
    #print('todas las llamadas: ',registros_dividos)
    #print('llamada deseada: ',registros_dividos[1])
    #print('Seleccion de interes: ',registros_dividos[1][:8])
    
    # Iteramos para acceder a cada una de las llamadas
    for llamada in range(cantidad_de_llamadas):
        # Seleccionamos los primeros 8 caracteres que brindan informacion respecto a la duracion de la llamada
        # en cuestion
        # String
        duracion = registros_dividos[llamada][0:8]
        
        # Separamos la duracion en horas, minutos y segundos
        # Lista
        duracion_sep = duracion.split(':')

        # Definimos horas, minutos y segundos
        hora = int(duracion_sep[0])
        minutos = int(duracion_sep[1])
        segundos = int(duracion_sep[2])
        
        # Convertimos todo a segundos
        hora_a_seg = hora*60*60
        minutos_a_seg = minutos * 60

        # Calculamos la duracion total en segundos
        # Int
        duracion_total = hora_a_seg + minutos_a_seg + segundos

        # Registramos el numero del telefono asociado al registro
        # String 
        numero_telefono = registros_dividos[llamada][9:]

        # Chequeamos si la duracion es menor a 300 segundos
        if duracion_total < 300:
            # El costo total sera la duracion total en segundos multiplicado por 3 (3 centavos por segundo)
            costo_total = duracion_total * 3 
        else:
            # Si es 300 segundos o mas, se cobrara la cantidad de minutos multiplicado por 150 (150 centavos el minuto)
            # Se redondea en segundos hacia arriba, es decir:
            # una llamada de 5 minutos y 10 segundos, cuenta como una llamada de 6 minutos
            if duracion_total // 60 != duracion_total / 60:
                costo_total = ((duracion_total//60)+1)*150
            else:
                costo_total = (duracion_total/60)*150
        
        
        ######### Asignacion de numeros de telefonos al diccionario con su correspondiente costo en centavos.

        # Corroboramos si existe un ya un registro del numero en cuestion 
        if not numero_telefono in dic.keys():
            # Si no existe la clave en cuestion, la creamos y le asociamos el costo total en centavos asociado a la llamada en cuestion
            dic[numero_telefono] = costo_total
        else:
            # Si ya existe una clave asociada al numero en cuestion, le sumamos el costo total de la llamada en cuestion al previo
            dic[numero_telefono] += costo_total

    return dic

def sub_total(registros):
    """

    Toma como entrada registros de llamadas
    Devuelve el subtotal de todas las llamadas de todos los numeros con todos los costos    

    """
    
    # Creamos la variable la cual contendra el costo total de todas las llamadas de todos los numeros
    subtotal = 0

    # Llamamos a la funcion dic_costo, la evaluamos en registros para acceder al diccionario de costos de las llamadas
    diccionario_de_costos = dic_costo(registros)
    
    # Iteramos sobre todos los costos para poder acceder a cada uno de ellos
    for costo in diccionario_de_costos.values():
        # Sumamos cada costo al subtotal
        subtotal += costo # subtotal = subtotal + costo
    # Devolvemos el subtotal
    return subtotal
    
def aplicar_descuento_y_total(registros):
    """

    Toma como entrada registros de llamadas
    Devuelve el total con el descuento aplicado al numero correspondiente 

    """

    ## Chequeamos si hay mas de un numero con igual cantidad de duracion
    
    # Creamos un diccionario en donde asociamos los numeros potenciales de aplicacion del descuento 
    # A su mismo numero pero en otro formato para poder comparar cual es el menor de todos ellos.
    telefonos_promocion_aplicables = {}

    # Llamamos la funcion dic_duracion que nos devuelve el diccionario con los numeros de telefono y sus
    # duraciones totales asociadas
    diccionario_de_duracion = dic_duracion(registros)

    # Creamos la variable asociada a la duracion total mas grande
    maxima_duracion = max(diccionario_de_duracion.values())
    
    # Iteramos sobre el diccionario de duracion para poder acceder a todos los numeros con su correspondiente duracion
    # Para corroborar a cuantos numeros de telefono se le puede aplicar el descuento
    # Y los agregamos al diccionario con su valor transformado a INT 
    for numero_telefono , duracion in diccionario_de_duracion.items():
        
        # Si la duracion total de ese telefono coincide con la maxima duracion
        if duracion == maxima_duracion:
            # Creamos una lista con las partes que estaban separadas por un '-'
            # Lista
            numero_en_partes = numero_telefono.split('-')
            
            # Creamos el numero transformado, sumando las partes individuales
            numero_sin_transformar = numero_en_partes[0] + numero_en_partes[1] + numero_en_partes[2]
            
            # Transformamos el string en un INT para poder comparar posteriormente
            numero_transformado = int(numero_sin_transformar)

            # Creamos la clave asociada al numero de telefono y el valor asociado al mismo transformado para
            # Comparar posteriormente
            telefonos_promocion_aplicables[numero_telefono] = numero_transformado
    
    # Contamos la cantidad de numeros que se le puede aplicar el descuento
    cantidad_telefonos_promocion_aplicables = len(telefonos_promocion_aplicables)
    
    
    # Llamamos a la funcion subtotal previamente creada para calcular el subtotal
    
    subtotal = sub_total(registros)
    
    # Llamamos a la funcion asociada al diccionario de costos
    
    diccionario_de_costos = dic_costo(registros)

    
    # Si solo hay UN numero para aplicar el descuento
    if cantidad_telefonos_promocion_aplicables < 2:
        # Accedemos al telefono con la mayor duracion
        
        telefono_con_descuento = max(diccionario_de_duracion, key=diccionario_de_duracion.get)
        
        # Restamos al total el costo del numero de telefono que se le aplico el descuento
        
        total = subtotal - diccionario_de_costos[telefono_con_descuento] 
        
        

    # Si hay mas de un numero con mayor duracion
    else:
        telefono_con_descuento_final = min(telefonos_promocion_aplicables)

        total = subtotal - diccionario_de_costos[telefono_con_descuento_final]

    return total

def final(registros):
    """
    Corroboramos que el registro contenga llamadas previamente, y luego utilizamos la funcion:
    aplicar_descuento_y_total en la variable que contiene las llamadas (En este caso, seria la variable 'registros')
    """
    
    # Corroboramos que el registro no se encuentre vacio
    if len(registros) != 0:
        return aplicar_descuento_y_total(registros)
    else:
        return 'El registro se encuentra vacio, sin llamadas.'
    
factura_total_1 = final(registros)
factura_total_2 = final(registros2)
factura_total_3 = final(registros3)
factura_total_4 = final(registros4)

print('El total de la factura 1 es:',factura_total_1)
print('El total de la factura 2 es:',factura_total_2)
print('El total de la factura 3 es:',factura_total_3)
print('El total de la factura 4 es:',factura_total_4)
