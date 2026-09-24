############## TP Listas  ##############

### Ejercicio 1
print("=====================================")
print("Ejercicio 1")
print("=====================================")
notas= [7, 8, 6, 9, 10, 5, 8, 7, 9, 6]

print("Lista de notas: ")
for nota in notas:
    print(nota)

promedio = sum(notas) / len(notas)

print("Promedio: ", promedio)

print("Nota mas alta:", max(notas))
print("Nota mas baja:", min(notas))


### Ejercicio 2
print("=====================================")
print("Ejercicio 2")
print("=====================================")
productos= []

for i in range(5):
    producto= input("Ingrese un producto a la lista: ")
    productos.append(producto)

print("Productos ordenados alfabeticamente: ")
productos_ordenados = sorted(productos)

for producto in productos_ordenados:
    print(producto)

eliminar = input(" Que producto quiere eliminar? ")

if eliminar in productos:
    productos.remove(eliminar)
    print("Producto eliminado correctamente")
else:
    print("El producto no se encuentra en la lista")

print("Lista actualizada: ")
for producto in productos:
    print(producto)


### Ejercicio 3
print("=====================================")
print("Ejercicio 3")
print("=====================================")


import random

numeros = []

for i in range(15):
    numeros.append(random.randint(1, 100))

pares= []

impares= []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print("=====================================")
print(" Numeros generados: ")
print("=====================================")
for numero in numeros: 
    print(numero)
print("=====================================")
print(" Numeros pares: ")
print("=====================================")
for numero in pares:
    print(numero)
print("=====================================")
print(" cantidad de pares:", len(pares))
print("=====================================")
print(" numeros impares: ")
print("=====================================")
for numero in impares:
    print(numero)
print("=====================================")
print(" Cantidad de impares: ", len(impares))
print("=====================================")


### Ejercicio 4
print("=====================================")
print(" Ejercicio 4 ")
print("=====================================")

numeros = [4, 7, 2, 4, 9, 7, 2, 10, 4, 9]

sin_repetir = []

for valor in numeros:
    if valor not in sin_repetir:
        sin_repetir.append(valor)

print(" Lista original: ")
for valor in numeros:
    print(valor)

print(" Lista sin numeros repetidos: ")
for valor in sin_repetir:
    print(valor)


### Ejercicio 5
print("=====================================")
print("Ejercicio 5")
print("=====================================")

listado = [
    "juan",
    "carolina",
    "naylea",
    "gertrudis",
    "dionisio",
    "hermes",
    "simon",
    "martina"
    ]

print("Estudiantes presentes: ")
for alumno in listado:
    print(alumno)

opcion = input(" Desea agregar o eliminar un estudiante de la lista? ").lower()

if opcion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo alumno: ")
    listado.append(nuevo)
    print("Alumno agregado con exito")

elif opcion == "eliminar":
    eliminar = input("Ingrese el nombre del alumno que desea eliminar: ")

    if eliminar in listado:
        listado.remove(eliminar)
        print("Estudiante eliminado. ")

    else:
        print("El estudiante no se encuentra en la lista ")

print(" Lista final: ")
for alumno in listado:
    print(alumno)




###  Ejercicio 6
print("=====================================")
print("Ejercicio 6")
print("=====================================")


lista = [24, 3, 5, 8, 15, 80, 2]

print("Lista original: ")
for numero in lista:
    print(numero)

ultimo = lista[-1]
    ## toma el ultimo valor de la lista

lista = [ultimo] + lista[:-1]
    ## propone el ultimo valor como primero y le suma a la derecha el resto de la lista

print(" Lista reordenada: ")
for numero in lista:
    print(numero)


### Ejercicio 7
print("=====================================")
print("Ejercicio 7")
print("=====================================")

temperaturas = [
    [10, 20],
    [12, 25],
    [8, 20],
    [15, 28],
    [11, 24],
    [9, 19],
    [13, 26]
]

dias = [
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado",
    "Domingo"
    ]

suma_minimas = 0
suma_maximas = 0

mayor_amplitud = 0
dia_mayor_amplitud = ""

print(" Temperaturas de la semana: ")
print("========================================")
for i in range(len(temperaturas)):
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]

    print(dias[i], "minima: ", minima, "maxima: ", maxima)

    print("-------------------------------------")

    suma_minimas += minima
    suma_maximas += maxima 

    amplitud = maxima - minima

    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias[i]

promedio_minimas = suma_minimas / len(temperaturas)
promedio_maximas = suma_maximas / len(temperaturas)
print("========================================")
print(f" Promedio de minimas: {promedio_minimas:.2f}")
print(f" Promedio de maximas: {promedio_maximas:.2f}")
print(" Mayor amplitud termica: ", mayor_amplitud)
print(" Dia con mayor amplitud: ", dia_mayor_amplitud)
print("========================================")


### Ejercicio 8 
print("=====================================")
print("Ejercicio 8")
print("=====================================")

notas = [
    [8, 7, 9],
    [6, 8, 7],
    [10, 9, 10],
    [7, 6, 8],
    [9, 8, 7]
]

nombres = ["Ana", "Juan", "Sofía", "Pedro", "Lucía"]

materias = ["Matematica", "Programacion 1", "Organizacion Empresarial"]

for i in range(len(notas)):
    ##Len(notas) nos permite expresar cuantas filas tiene la matriz
    promedio = sum(notas[i]) / len(notas[i])
    ##sum(notas[x]) nos permite sumar los elementos de esa fila
    ##y con len(notas[x]) cuenta cuantos elmentos hay en esa fila y divide el producto antertior
    print(nombres[i], ":", promedio)

print(" Promedio de cada materia: ")

for columna in range(3):
    suma= 0 

    for fila in range(5):
        suma+= notas[fila][columna]

    promedio = suma / 5

    print(materias[columna], ":", promedio)


### Ejercicio 9:
print("=====================================")
print("Ejercicio 9")
print("=====================================")
tablero= [
["-", "-", "-"],
["-", "-", "-"],
["-", "-", "-"]
]

def mostrar_tablero():
    ## Creamos lña funcion mostrar_tablero para llamarla cada vez que querramos usarla.
    print(" tablero:")
    for fila in tablero:
        for elemento in fila:
            print(elemento, end= " ")
        print()

turno = 0
    ### usamos while para que solo las jugadas validas cuenten como turno.
while turno < 9:
    if turno % 2 == 0:
        jugador = "X"
    else:
        jugador = "O"

    mostrar_tablero()

    print("Turno del jugador", jugador)

    fila = input("Ingrese la fila del 1 al 3: ")
    columna = input("Ingrese la columna del 1 al 3: ")

    if not fila.isdigit() or not columna.isdigit():
        print("Debe ingresar numeros.")
        continue

    fila = int(fila) - 1
    columna = int(columna) - 1
       ### le restamos 1 a los valores asi coinciden con la base 0 de las listas.
    if 0 <= fila < 3 and 0 <= columna < 3:
        if tablero[fila][columna] == "-":
            tablero[fila][columna] = jugador
            turno += 1

        else:
            print("La casilla esta ocupada.")
            continue

    else:
        print("Posicion invalida.")
        continue

mostrar_tablero()


### Ejercicio 10
print("=====================================")
print("Ejercicio 10")
print("=====================================")


ventas = [
    [10, 15, 20, 12, 18, 25, 20],  # puerro
    [20, 18, 15, 22, 25, 30, 28],  # Choclo
    [8, 12, 10, 15, 13, 17, 14],   # hormigon
    [15, 20, 18, 16, 22, 24, 19]   # lentes de sol
]


productos = [
    "Puerro",
    "Choclo",
    "hormigon",
    "lentes de sol"
]

totales_productos = []

for i in range(len(ventas)):
    total = sum(ventas[i])
    totales_productos.append(total)

print(" Total vendido por productos: ")

for i in range(len(productos)):
    print(productos[i], ":", totales_productos[i])

### ventas por dia

totales_dias = []

for dia in range(7):
    total = 0

    for producto in range (4):
        total += ventas[producto][dia]


    totales_dias.append(total)


mayor_venta_dia = max(totales_dias)

dia_mayor_venta =totales_dias.index(mayor_venta_dia)

print(" Dia con mayores ventas: ")
print(f" Dia {dia_mayor_venta + 1} con  {mayor_venta_dia} unidades.")

## mas vendido

mayor_producto = max(totales_productos)
posicion_producto = totales_productos.index(mayor_producto)

print(" Producto mas vendido: ")
print(productos[posicion_producto], "con", mayor_producto, "unidades.")


### Ejercicio 11
print("=====================================")
print("Ejercicio 11")
print("=====================================")


alumnos =  [
    "juan",
    "carlos",
    "camila", 
    "mara",
    "candra",
    "uriel",
    "leonel",
    "tamara",
    "cristobal",
    "yanella"
]

nombre = input("Escriba el nombre que desea buscar en la lista: ").lower()


if nombre in alumnos:
    posicion = alumnos.index(nombre)

    print("El alumno se encuentra en la lista. ")
    print(" Posicion:", posicion + 1)

else:
    print("El alumno no se encuentra en la lista. ")
    
    

### Ejercicio 12
print("=====================================")
print("Ejercicio 12")
print("=====================================")

lista_numeros = []

for i in range(8):
    numero = int(input("Ingrese un numero: "))
    lista_numeros.append(numero)

## imprimimos la lista original: 
print("Lista original: ")
for numero in lista_numeros:
    print(numero)
### damos uso de sorted() que nos odena los numeros de menor a mayor:
lista_ascendente = sorted(lista_numeros)

print("lista ordenada de menor a mayor: ")
for numero in lista_ascendente:
    print(numero)
### y con reverse invertimos ese orden para tener la lista de mayor a menor:
lista_descendente = sorted(lista_numeros, reverse=True)

print("Lista ordenada de mayor a menor: ")
for numero in lista_descendente:
    print(numero)


### Ejercicio 13:
print("=====================================")
print("Ejercicio 13")
print("=====================================")

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

print("=====================================")
print("Los puntajes en la partida fueron: ")

for numero in puntajes:
    print(numero)
print("=====================================")
print("Puntaje mas alto:", max(puntajes))
print("Puntaje mas bajo:", min(puntajes))

ranking = sorted(puntajes, reverse=True)
print("=====================================")
print("Ranking de esta partida:")
for numero in ranking:
    print(numero)

posicion = ranking.index(990)
print("=====================================")
print(f"El jugador con 990 puntos se encuentra en la posicion {posicion + 1} !!")
print("=====================================")
