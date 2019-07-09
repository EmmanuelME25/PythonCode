#funcion una variable
def sh(nombre):
	print('hola {0}'.format(nombre))

sh('andres')

#funcion dos variables
def sum(a,b):
	x=a+b
	return x

print('pruea ', sum(2,3))

#funcion + ciclo
for i in range (0,10):
	print(sum(2,i))

total=sum(2.5,5)
print(total, type(total))
