#falto el profe y los pibes arman la clase
#pedir el nombre y la edad de los compas que vinieron a clase hoy

#funcion para obtener al asistente y al profesor segun la edad
def get_compas(cantidad):
    
    #creando la liste de los compas
    compas = []
    
    #ejecutando un for para pedir informacion de cada compa
    for i in range(cantidad):
        nombre = input("ingrese el nombre del compa: ")
        edad = int(input("ingrese el edad del compa: "))
        compa = (nombre,edad)
        
        #agregando la informacion a la lista
        compas.append(compa)
        #ordenandolos de menor a mayor segun su edad
    compas.sort(key=lambda x:x[1])
    #compas[x] devuelve una tupla con (nombre,edad) y despues accedemos a l nombre
    #para definir al asistente y al profesor
    asistente = compas[0][0]
    profesor = compas[-1][0]

#retornamos una tupla
    return asistente,profesor
#desempaquetamos lo que nos retorna la funcion
asistente,profesor = get_compas(5)
print(f"El profesor es: {profesor} y su asistente es {asistente}")
