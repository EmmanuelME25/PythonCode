#crear clase
class usuario:
	def __init__(self,numeroa,ac,age,name):
		self.numeroa=numeroa
		self.ac=ac
		self.age=age
		self.name=name

#"base de datos"
ac=[200,150,300,201,230,100,250,0,100,350]
name=['A1','A2','A3','A4','A5','A6','A7','A8','A9','B1']
ed=[15,16,17,18,19,20,14,15,16,17]

print(len(ac),len(name),len(ed))

#definir usuarios
user=[]
import lib
from lib import pase

for i in range (0,10):
	user[i]=usuario((i+1),ac[i],ed[i],'name[i]')	
	
miArchivo =open('Resultados.txt','w')
for i in range(0,11):
	Resultados.write(pase(u[i]))
