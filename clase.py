class usuario:

	def __init__(self,name,email,age):
		self.name=name
		self.email=email
		self.age=age
	
	def saludos(self):
		return 'me llamo {0} y tengo {1}'.format(self.name,self.age)
	
	def teno_cumplo(self):
		 self.age+=1
		

Emmanuel = usuario('EmmanuelME','medina@gmail',17)

print(type(Emmanuel))
print(Emmanuel.name)
print(Emmanuel.saludos())
#print(Emmanuel.teno_cumplo())

class cliente(usuario):

	def __init__(self,name,email,age):
		self.name=name
		self. email=email
		self. age=age
		self. saldo=0
	
	def defsaldo(saldo):
		saldo=self.saldo
	def salsal(self):
		return 'me llamo {0} y tengo saldo:{1},edad: {2}'.format(self.name,self.saldo,self.age)

Emmanuelc=cliente('EmmanuelMEC','@med',18)
print('-----------')
Emmanuelc.defsaldo(500)
print(Emmanuelc.salsal())
