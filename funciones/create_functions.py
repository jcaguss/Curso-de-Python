#creando una funcion simple
def saludar():
    print('Hola Agus, como estas?')
    
#llamando a la funcion
saludar()

#creando una funcion con parametros
def saludarr(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adj = "Reina"
    elif (sexo == "hombre"):
        adj = "Titan"
    else:
        adj = "Compi"

    print(f"Hola {nombre}, mi {adj}, como estas?")

saludarr("Agustin","hombre")

#crear una funcion que retorna multiples valores
def crear_contra(num):
    chars = "abcdefghijk"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num -2
    c2 = num
    c3 = num -5
    contra = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contra,num_entero

#desempaquetando la funcion
password,num = crear_contra(99991)
#mostrando los resultados optenidos y los datos utilizados para obtenerlo
print(f"Tu contra es {password}")
print(f"El numero que se utilizo fue {num}")