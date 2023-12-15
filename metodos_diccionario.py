diccionario = {
    'nombre' : 'Agus',
    'apellido' : 'Caceres',
    'subs' : 1000
}

#devuelve las claves del diccionario 
claves = diccionario.keys()

#tambien podemos traer los valores de este modo
valor = diccionario.get('nombre') #si no lo encuentra devuelve none y el programa continua
valor1 = diccionario['apellido'] #devuelve una expcion si no lo encuentra y para el programa

#eliminando elementos de un diccionario
diccionario.pop('subs')

#opteniendo un elemento dict_item iterable
diccionario_iterable = diccionario.items()

#eliminando todo del diccionario
#diccionario.clear()

print(diccionario_iterable)