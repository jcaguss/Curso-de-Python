#creando una fucnion de 3 parametros
#def frase (nombre,apellido,adj):
#    return f"Hola {nombre} {apellido}, sos muy {adj}"
#utulizando keyword arguments
#frase_res = frase(adj= 'genio', apellido= 'Caceres', nombre= 'Agus')
#print(frase_res)
#creando la misma funcion con un parametro opcional y un valor por defecto
def frase2(nombre,apellido,adj = 'Pancho'):
    return f"Hola {nombre} {apellido}, sos muy {adj}"
frase_res2 = frase2('agus','caceres','Genio')
print(frase_res2)