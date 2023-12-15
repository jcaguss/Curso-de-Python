#creando una funcion que nos devuelva los numeros primos
#entre 0 y el argunemto que pasamos

#creando una funcion para verificar si es un numero primo
def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse
    #por nungun numero entero 2 y ese mismo -1
    for i in range(2,num-1):
        #si es divisible por alguno retornamos false y termina el bucle
        if num%i==0: return False
    #si termina el bucle, significa que ni fue divisible entonces es primo
    return True

#creando una funcion que retorne una losta con todos los primos
def primos_hasta(num):
    #creamos la lista con los primos 
    primos = []
    for i in range(3,num+1):
        #verificamos si el valor es primo
        res = es_primo(i)
        #en case de que sea lo agregamos
        if res == True: primos.append(i)
    #devolvemos la lista
    return primos
#creamos el resultado llamando a la funcion y lo mostramos
res = primos_hasta(98)
print(res)