#creando un conjunto con set

conjunto = set(['dato1','dato2'])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(['dato1','dato2'])
conjunto2 = {conjunto1,'dato3'}

#print(conjunto2)

#teoria de conjuntos

conjunto1 = {1,2,3,4}
conjunto2 = {1,2,3}

#verificar si es un subconjunto
#resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= (conjunto1)

#verificar si es un superconjunto
#resultado1 = conjunto2.issuperset(conjunto1)
resultado1 = conjunto2 > (conjunto1)

#verificar si no hay algun resultado en comun (si hay un numero en comun da falso, si no hay ninguno en comun da verdadero)
resultado2 = conjunto2.isdisjoint(conjunto1)

print(resultado2)