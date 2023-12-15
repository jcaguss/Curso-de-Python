# a) Pedirle al usuario que diga cualquier texto real y:
#       -Calcular cuanto tardaria en decir esa frase
#       -Cuantas palabras dijo?

# b) Si se tarda mas de 1 minuto:
#       -decirle:'Para flaco tampoco te pedi un testamento'

# c) Dalto habla un 30% mas rapido:  
#       -Cuanto tardara en decirlo?

frase = input('Decime una frase y te calculo cuanto tardaria si tuviera que decirla: ')
palabras_separadas = frase.split(' ')
cantidad_de_palabras = len(palabras_separadas)

if cantidad_de_palabras > 120:
    print('Para flaco tampoco te pedi un testamento')


print(f'Dijiste {cantidad_de_palabras} palabras en {cantidad_de_palabras * 100 //2 * 1.3 / 100} segundos')
print(f'Dalto lo diria en {cantidad_de_palabras/2} segundos')
