cadena1 = 'Hola soy Agus'
cadena2 = 'Bienvenido Loco'
numeros = '112341234'
cadena3 = 'abcdefoz'

#convierte a Maysculas
mayusc = cadena1.upper()

#convierte a minuscula
minusc = cadena1.lower()

#Primeta letra en Mayuscula
pri_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra si no encuentra nada devuelve -1
busqueda_find = cadena1.find('a')


#buscamos una cadena en otra cadena si no lo encuentra devuelve una exepcion
busqueda_idex = cadena1.index('a')

#si es numerico devuelve true sino false

num = numeros.isnumeric()

#si es alfanumerico devolvemos true sino false
es_alfanumerico = cadena3.isalpha()

#buscamos una cadena en otra cadena, devuelve cuantas veces coinciden
contar_coincidencias = cadena1.count('ola')

#contamos las coincidencias de una cadena dentro de una cadena, devuelve la cantidad de coincidencias
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith('H')

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith('gus')

#remplaza un pedazo de la cadena dada por otra dada, si existe se la coincidencia se ejecuta
cadena_nueva = cadena2.replace('Loco','loca')

#Separa por el parametro dado
cadena_separada = cadena1.split(' ')

print(cadena_separada)
print(cadena_separada[2])