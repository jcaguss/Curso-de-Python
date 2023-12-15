# a) Diferencia en Porcentaje entre el curso actual y:
#       -El mas rapido de otros cursos
#       -El mas lento de otros cursos
#       -El promedio de los cursos

#ej1
print('Ejercicio a)')
print('')

#Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Diferencias de duracion

diferencia_con_min = 100 - (dalto_curso / otros_cursos_min * 100)
diferencia_con_max = 100 - (dalto_curso * 1000 // otros_cursos_max / 10)
diferencia_con_promedio = 100 - (dalto_curso / otros_cursos_promedio * 100)


print('El curso de dalto dura:')
print(f' - El curse de Dalto dura un {diferencia_con_min}% menos que el mas rapdio')
print(f' - El curse de Dalto dura un {diferencia_con_max}% menos que el mas lento')
print(f' - El curse de Dalto dura un {diferencia_con_promedio}% menos que el promedio')


# b) Porcentaje de material inservible que se reducen en:
#       -El promedio de los cursos
#       -El curso actual (este curso)

#Duracion de crudos 
crudo_promedio = 5
crudo_dalto = 3.5 

#Calculando el procentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - (otros_cursos_promedio * 1000 // crudo_promedio / 10)
tiempo_vacio_dalto = 100 - (dalto_curso * 1000 // crudo_dalto / 10)

#espaciado
print('------------------------')
print('Ejercicio b)')
print('')


#Mostrando la cantidad de timpo vacio que se remueven
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimina un {tiempo_vacio_dalto}% de tiempo vacio')


# c) Ver 10 horas de este curso a cuantas de otros cursos equivale?

#espaciado
print('------------------------')
print('Ejercicio c)')
print('')

#Mostrando diferencias si los cursos duraran 10 horas
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_min * 100 // dalto_curso / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este cursos')

print('------------------------')
