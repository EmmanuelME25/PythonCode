miArchivo = open('miArchivo.txt','w')

print('Name: ',miArchivo.name)
print('Esta cerrado: ',miArchivo.closed)
print('modo abierto: ',miArchivo.mode)
miArchivo.write('Me encanta python')
miArchivo.write(' y root')
miArchivo.close()
miArchivo=open('miArchivo.txt', 'a')
miArchivo.write(' y tambien c++' )

