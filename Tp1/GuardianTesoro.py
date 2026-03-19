
print("¡Bienvenido/a!")
nombre = str(input("¿Cómo te llamas?").lower())

if nombre == "nicole":
    print ("¡Bienvenido, creador! El tesoro es tuyo sin preguntas.")
else:
    valentia = int(input("¿Qué valor de valentía tenés? (Ingresá un número del 1-10)"))
    cantOro = int(input("¿Cuántas monedas de oro llevas en tu mochila?"))
    regalo = cantOro + 15 
    print("Te regalo 15 monedas, ahora tenes {regalo}")

    if (valentia > 7):
        print ("Eres digno, ¡puedes pasar!")

        edad = int(input("¿Qué edad tenes?"))

        if (edad > 18 and regalo > 100):
            print ("¡Cofre abierto!")
        else:
            print ("Acceso denegado.")
                  
    elif (valentia < 7 and valentia > 4):
        print ("Me servís como guardia, pero no para el tesoro.")
    else:
        print ("¡Corré antes de que sea tarde!")




