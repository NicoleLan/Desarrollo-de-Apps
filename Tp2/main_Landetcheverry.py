from funciones_Landet import *

nombre = greet()
cargaBase, reserva = getData()

checkFuel()

operativo, fallido = checkComponents()

"""Cálculo de Estadísticas"""
print (fallido, operativo)

porcentaje = (statistics (operativo, (fallido + operativo))) * 100

print (f"Siendo la cantidad de componentes revisados igual a {(fallido) + (operativo)}, el porcentaje de aprobados es: {porcentaje}")
print (f"Chau {nombre}")
