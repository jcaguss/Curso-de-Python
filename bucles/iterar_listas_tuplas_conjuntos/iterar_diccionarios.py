diccionario = {
    'nombre': 'Agustin',
    'apellido': 'Caceres',
    'edad': 23
}
#iteramos diccionarios
for datos in diccionario.items():
    print(datos) # trae una tupla
    key = datos[0]
    value = datos[1]
    print(f'la clave es: {key} y el valor es: {value}')