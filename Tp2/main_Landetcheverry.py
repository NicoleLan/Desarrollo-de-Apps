from funciones_Landet import *

print ("¡Hola!")
nombre = str(input("Cuál es tu nombre, capitán?"))

cargaBase = int(input("¿Cuánto es la carga base?"))
reserva = int(input("¿Cuánto es la reserva?"))


""" Cálculo de Combustible"""
if reserva < 50:
    reserva = 50 
    print ("La reserva fue re-escrita a 50u por razsones de seguridad.")
    resultado = suma (cargaBase, reserva)
    
else:
    resultado = suma (cargaBase, reserva)

print (resultado)


"""Chequeo de Sistema: """
cantComponentes = int(input("Cuántos componentes vas a checkear?"))
operativo = 0
fallido = 0

while (cantComponentes > 0):
    nombreComponente = str(input("Ingrese nombre del componente:")) 
    nivelEnergia = int(input("Qué nivel de energía tiene? (0-100)"))

    if nivelEnergia >= 70:
        print ("OPERATIVO")
        operativo += 1

    else:
        print ("FALLIDO")
        fallido += 1
    
    cantComponentes -= 1

"""Cálculo de Estadísticas"""
print (fallido, operativo)

porcentaje = (statistics (operativo, (fallido + operativo))) * 100

print (f"Siendo la cantidad de componentes revisados igual a {(fallido) + (operativo)}, el porcentaje de aprobados es: {porcentaje}")
print (f"Chau {nombre}")