#creando una lista con list
lista = list(['hola','agus',23])
lista2 = list([21,22,23,24,25,75,12,11,88,1,2023,True,False])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append('caceres')

#agregando un elemento a la lista en un indice especifico
lista.insert(2,'como estas')

#agregamos varios elementos de una lista a otra lista 
lista.extend([True,'pepe'])

#eliminando un elemento de la lista (por su indice)
lista.pop(0) # -1 para eliminar el ultimo -2 penultimo etc

#removemos un elemento de la lista por su valor
lista.remove(23)

#eliminando todos los elementos de la lista 
# ->  lista.clear()

#ordena una lista de forma acendente ( para decreciente lista2.sort(reverse=True))
lista2.sort()

#invirtiendo los elementos de una lista
lista2.reverse()

print(lista2)