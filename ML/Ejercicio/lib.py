import re
def pase(usuario,ac,age):
	if ac>=200 and age>=15 and age<=18 and ac<=300:
		print('ACEPTADO')
	else:
		print('Aciertos: {0}'.format(ac))
