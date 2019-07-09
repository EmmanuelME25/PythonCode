#arreglos
num=[1,2,3,4,5]
fru=['Naranjas','Uvas','Peras','Manzana']

print (num,fru)

#tamano del arreglo
print(len(fru))


#agragar al arreglo
fru.append('Mango')
print(fru)

#ciclo
for i in range(0,4):
	print(fru[i])

fru.remove('Uvas')
print (fru)

fru.insert(2,'Pina')
print (fru)

fru.pop(2)
print(fru)

fru.reverse()
print(fru)

fru.sort()
print(fru)
