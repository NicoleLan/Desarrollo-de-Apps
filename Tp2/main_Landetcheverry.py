nombre = greet()
cargaBase, reserva = getData()

checkFuel(reserva, cargaBase)

operativo, fallido = checkComponents()

"""Cálculo de Estadísticas"""
print (fallido, operativo)

porcentaje = (statistics (operativo, (fallido + operativo))) * 100

print (f"Siendo la cantidad de componentes revisados igual a {(fallido) + (operativo)}, el porcentaje de aprobados es: {porcentaje}")
print (f"Chau {nombre}")
