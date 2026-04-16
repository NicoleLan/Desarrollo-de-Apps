'''
1. Carga de Catálogo
Pide el nombre de 3 productos y su categoría. Guarda cada par como una tupla dentro de una lista llamada productos.
'''

productos = []
for i in range (3):
    nombreP = str(input(f"¿Qué producto queres ingresar?"))
    categoria = str(input(f"¿Qué categoría tiene el prodcuto {nombreP}?"))
    tupla= (nombreP, categoria)
    productos.append (tupla)

'''
2. Carga de Stock
Pide la cantidad actual para cada producto y guárdalas en una lista llamada stock. Los índices deben coincidir con la lista anterior.
3. Actualización
Busca un producto por nombre para sumar una "donación" recibida a su cantidad en la lista de stock.
'''
stock = []

for i in range (3):
    cantidad = int(input(f"¿Cuanto stock hay de {productos[i][0]}?"))
    stock.append (cantidad)


nombreBuscado = str(input("¿Qué producto recibió una donación? "))
donacion = int(input(f"¿Cuántas unidades se donaron? "))

for i in range(3):
    if productos[i][0] == nombreBuscado:
        stock[i] += donacion
        print(f"El stock de {nombreBuscado} actualizado a {stock[i]} unidades.")
    else:
        print("Producto no encontrado.")

'''
4. Simulación de Consumo
El equipo de cocina consumió todo el stock del segundo producto (índice 1). Modifica su valor a 0.
'''
stock[1] = 0

'''
5. Informe Final
Recorre ambas listas en paralelo y muestra:
"Producto: [Nombre] - Categoría: [Categoría] - Cantidad: [Cantidad]"
'''
for i in range(3):
    print(f"Producto: {productos[i][0]} - Categoría: {productos[i][1]} - Cantidad: {stock[i]}")

