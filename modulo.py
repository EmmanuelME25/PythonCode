#modulos, importar librerias
import datetime
hoy=datetime.date.today()
print(hoy)

from datetime import date
hoy2=date.today()
print(hoy2)

import time
estampatemporal= time.time()
print(estampatemporal)

import validador

from validador import validate_email
email='@pruebacorreo'

if validate_email(email):	
	print('bien')
else:
	print('mal')
print(len(email))
