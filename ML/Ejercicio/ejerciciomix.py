#crear clase
class usuario:
	def __init__ (self,numeroa,ac,age,name):
		self.numeroa=numeroa
		self.ac=ac
		self.age=age
		self.name=name

#"base de datos"
#ac=[200,150,300,201,230,100,250,0,100,350]
#name=['A1','A2','A3','A4','A5','A6','A7','A8','A9','B1']
#age=[15,16,17,18,19,20,14,15,16,17]

#print(len(ac),len(name),len(age))

#definir usuarios
#user=[]
import lib
from lib import pase

#abrir archivo
miArchivo =open('Resultados.txt','w')


#for i in range (0,9):
user=usuario((1),150,17,'A1')	
miArchivo.write(pase(user,'150','17'))
