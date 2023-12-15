#creando las listas
frutas = ['banana','pera','manzana','ciruela','naranja','durazno','kigui']
cadena = "Hola Agustin"
numeros = [2,5,8,10]

for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'Me voy a comer una {fruta}')

print('---------------------------------')
#evitar que el bucle siga ejecutandose (el else tampoco se ejecuta cuando termina)
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == 'ciruela':
        break
print(f'despues de comer la ciruela me dolio la panza')

#recorrer una cadena de texto
for letra in cadena:
    print(letra)

#for en una sola lista de codigos (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
