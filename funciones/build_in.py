numeros = [1,4,6,9,0,23,43]

#encontrando el numero mayor de la lista
num_mas_alto = max(numeros)

#encontrando el numero menor de la lista
num_mas_bajo = min(numeros)

#redondiando a 6 decimales
num = round(42.452134, 2)


#retorna false ->, vacio, false, none \ true -> distinto a 0, true, cadena, datos no vacios
res_boll = bool('a')

#retorna True , si todos los valores son verdaderos
res_all = all([123,'True',[234,23]])

#suma todos los valores de un iterable
sum_total = sum(numeros)

print(sum_total)