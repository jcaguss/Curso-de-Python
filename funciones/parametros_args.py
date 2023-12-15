#Parametro args 
def sumar(nombre,*nums): #el parametro args (*variable)
    return f"{nombre}, la suma de tus numeros son:{sum(nums)} "
    
res = sumar('AGUS',234,5,2,234,23,43,3,3,3,5,2,52)
print(res)

#Forma optima de sumar valores
def suma_total(nums):
    return sum([*nums])
res2 = suma_total([2,3,4,5,6,7,8,9,1])
print(res2)