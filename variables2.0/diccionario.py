#creando diccionario con dict()

diccionario = dict(nombre='Agustin',apellido='Caceres')

#mostrando diccionario

print(diccionario)

#las listas no pueden ser claves
diccionario = {('agus','cace'):'jajaja'} #la tupla si pueden ser claves
#diccionario = {['agus','cace']:'jajaja'} #en listas no se puede
#diccionario = {{'agus','cace'}:'jajaja'} #tampoco se puede hacer con conjuntos
diccionario = {frozenset(['agus','cace']):'jajaja'} #si se puede en conjuntos con frozenset

print(diccionario)

#creando diccionario con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(['nombre','apellido','edad'])
print(diccionario)
print(diccionario['apellido'])

#creando diccionarios con fromkeys() valor por defecto: no se
diccionario = dict.fromkeys(['nombre','apellido','edad'],'No se')

print(diccionario)
print(diccionario['apellido'])


