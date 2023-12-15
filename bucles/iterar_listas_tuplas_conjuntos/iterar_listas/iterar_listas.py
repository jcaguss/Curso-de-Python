animales = ['perro','gato','loro','cocodrilo','mono']
numeros = [2,3,4,5,6]
#recorriendo la lista de animales
for animal in animales:
    print(f'Ahora la variable es igual a: {animal}')
#recorriendo a la lista de numeros y multiplicandolos por 10
for numero in numeros:
    print(f'{numero} multiplicado por 10 da {numero * 10}')
#recorriendo dos listas del mismo tamaño con zip()
for numero,animal in zip(animales,numeros):
    print(f'recorriendo lista1: {numero}')
    print(f'recorriendo lista2: {animal}')
    
#forma no optima de recorrer una lista con su indice
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    print(num)#lo devuelve como tupla
    indice = num[0]
    valor = num[1]
    print(f'el indice es : {indice} y el valor es: {valor}')
#Usando el for/else
for num in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {num}')
else:
    print('el bucle termino')