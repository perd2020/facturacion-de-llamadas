# facturacion-de-llamadas
programa para calcular el descuento a aplicar en facturas telefónicas con python
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
