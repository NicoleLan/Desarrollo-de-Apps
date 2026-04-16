def suma (a, b):
    return a + b

def statistics (a, b):
    return a/b

def greet():
    print ("¡Hola!")
    return str(input("¿Cuál es tu nombre, capitán?"))


def getData():
    cargaBase = int(input("¿Cuánto es la carga base?"))
    reserva = int(input("¿Cuánto es la reserva?"))
    return cargaBase, reserva

def checkFuel(reserva, cargaBase):
    if reserva < 50:
        reserva = 50 
        print ("La reserva fue reescrita a 50u por razones de seguridad.")
        resultado = suma (cargaBase, reserva)
    else:
        resultado = suma (cargaBase, reserva)
        print (resultado)
    return resultado

def checkComponents():
    cantComponentes = int(input("Cuántos componentes vas a checkear?"))
    operativo = 0
    fallido = 0
    while (cantComponentes > 0):
        nombreComponente = str(input("Ingrese nombre del componente:")) 
        nivelEnergia = int(input("¿Qué nivel de energía tiene? (0-100)"))
        funciona = checkComponent(nombreComponente, nivelEnergia)
        if (funciona) :
            operativo += 1
        else:
            fallido += 1
        
        cantComponentes -= 1
    return operativo, fallido


def checkComponent(nombre, energia):
    if energia >= 70:
        print (f"{nombre} OPERATIVO")
        return True

    else:
        print (f"{nombre} FALLIDO")
        return False


    
