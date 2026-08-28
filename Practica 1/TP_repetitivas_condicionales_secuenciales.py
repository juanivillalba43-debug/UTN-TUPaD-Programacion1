

###########             TP_ jUAN iGNACIO VILLALBA            ###########


###   ACTIVIDAD 1:  ###


nombre = input("Ingrese el nombre del cliente: ")

while not nombre.isalpha():
    print("==== ERROR: el nombre debe contener unicamente letras y no puede contener espacios vacios. ===== ")
    nombre = input ("Ingrese el nombre del cliente: ")

cantidad = input("ingrese la cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("==== ERROR: debe ingresar un numero entero pósitivo. ====")
    cantidad = input("iIngrese la cantidad de productos: ")

cantidad = int(cantidad)

total_sin_descuentos = 0
total_con_descuentos = 0

for i in range(cantidad):
    precio = input(f"Producto {i + 1} - Precio: ")

    while not precio.isdigit():
        print("====ERROR: el precio debe ser un numero entero. ====")
        precio= input(f"Producto{i+1} - Precio: ")

    precio= int(precio)

    descuento= input(" Descuento (S/N): ").lower()

    while descuento != "s" and descuento != "n":
        print("====ERROR : ingrese S o N. ====")
        descuento = input(" Descuento (S/N): "). lower()

    total_sin_descuentos += precio

    if descuento == "s":
        precio_con_descuento = precio * 0.90

    else:
        precio_con_descuento = precio

    total_con_descuentos += precio_con_descuento

ahorro = total_sin_descuentos - total_con_descuentos
promedio = float(total_con_descuentos / cantidad)


####Aqui utilizo ":.2f" para aquellos resultados que quiero que se muestren con 2 decimales. 

print()
print("========================================================")
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
print(f"Total sin discuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
print("========================================================")



###   ACTIVIDAD 2:  ###

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3:
    usuario = input(f" Intento{intentos + 1}/3 - Usuario: ")
    clave= input(" Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print(" Acceso concedido.")
        acceso = True
        break

    else:
        print(" Error: credenciales invalidas. ")

    intentos += 1

if not acceso:
    print(" Cuenta bloqueada")

else:
    opcion= ""

    while opcion != "4":
        print()
        print(" 1) Estado.    2) Cambiar clave.    3) Mensaje.    4) Salir.")
    

        opcion = input(" Opcion: ")

        #validamos que sea un numero

        while not opcion.isdigit():
            print(" Error: Ingrese un numero valido. ")
            opcion = input(" Opcion: ")

        #validamos que ese numero este entre 1 y 4

        while int(opcion)< 1 or int(opcion) > 4:
            print( " Error: opcion fuera de rango.")
            opcion = input("Opcion: ")

            while not opcion.isdigit():
                print( " Error: Ingrese un numero valido.")
                opcion = input(" Opcion: ")

        opcion = int(opcion)

        if opcion == 1:
            print(" Estado: Inscripto")

        elif opcion == 2:

            print(" La nueva clave debe tener minimo 6 caracteres.")
            nueva_clave = input(" Nueva calve: ")

            while len(nueva_clave) < 6:
                print( " Error: minimo 6 caracteres.")
                nueva_clave = input( " Nueva clave: ")

            confirmacion = input( " Confirmar clave: ")

            while nueva_clave != confirmacion:
                print(" Error: las claves no coinciden. ")
                confirmacion= input(" Confirmar clave: ")

            clave_correcta = nueva_clave
            print(" La clave se ha cambiado correctamente.")

        elif opcion == 3:
            print("¡Cada vez estamos mas cerca de lograrlo! ")

        elif opcion == 4:
            print(" Sesion finalizada.")


####    ACTIVIDAD 3    #### 

operador = input("Ingerese nombre del operador: ")

while not operador.isalpha():
    print(" Error: Ingrese solo letras. ")
    operador = input("Ingrese nombre del operador: ")


## variables turnos:

lunes1= ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

opcion = ""

while opcion != "5":

    print()
    print("====================================")
    print("          AGENDA DE TURNOS          ")
    print("====================================")
    print()
    print("1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del dia")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")
    print()
    print("====================================")

    opcion = input("Opcion: ")

    ## validar opciones  ##

    while not opcion.isdigit():
        print(" ERROR: ingrese un numero valido. ")
        opcion = input(" Opcion: ")

    while int(opcion) < 1 or int(opcion) > 5:
        print(" Error: opcion fuera de rango. ")
        opcion = input("Opcion: ")

        while not opcion.isdigit(): 
            print(" Error: ingrese un numero valido. ")

    opcion = int(opcion)

    ## reservas

    if opcion == 1:

        dia = input("Seleccione dia (1= lunes, 2=martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print(" ERROR: seleccione 1 o 2.")
            dia= input("Seleccione dia (1= lunes, 2=martes): ")

        dia = int(dia)

        paciente = input ("Nombre del paciente: ")

        while not paciente.isalpha():
            print("Error: ingrese solo letras. ")
            pciente = input(" Nombre del paciente: ")

    ## reserva lunes

        if dia == 1: 

            #varificacion si esta ocupado
            if (paciente == lunes1 or
                paciente == lunes2 or
                paciente == lunes3 or
                paciente == lunes4):

                print("ERROR: el paciente ya tiene un turno el lunes. ")

            #busqueda de un espacio libre

            elif lunes1 == "":
                lunes1 = paciente
                print(" Turno reservado correctamente. Turno 1 - Lunes.")

            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado correctamente. Turno 2 - Lunes.")

            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado correctamente. Turno 3 - Lunes.")

            elif lunes4 == "":
                lunes4 = paciente
                print(" Turno reservado correctamente. Turno 4 - Lunes.")

            else:
                print(" No hay turnos disponibles para el lunes. ")

        ## reserva martes

        elif dia == 2:

            if (paciente == martes1 or
                paciente == martes2 or
                paciente == martes3):

                print(" ERROR: el paciente ya tiene un turno el martes. ")

            elif martes1 == "":
                martes1 = paciente
                print(" Turno reservado correctamente. Turno 1 - Martes. ")

            elif martes2 == "":
                martes2 = paciente
                print(" Turno reservado correctamente. Turno 2 - Martes. ")

            elif martes3 == "":
                martes3 = paciente
                print(" Turno reservado correctamente. Turno 3 - Martes. ")

            else:
                print(" No hay turnos disponibles para el martes. ")


    ### Cancelar turno ###

    elif opcion == 2:

        dia = input(" Seleccione dia (1=Lunes, 2=Martes):  ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print(" ERROR: seleccione 1 o 2. ")
            dia = input(" Seleccione dia (1=Lunes, 2=Martes): ")

        dia = int(dia)

        paciente = input(" Nombre del paciente: ")

        while not paciente.isalpha():
            print(" ERROR: ingrese solo letras. ")
            paciente = input("Nombre del paciente: ")

        ## CANCELACION LUNES ##
        
        if dia == 1:

            if paciente == lunes1:
                lunes1 = ""
                print("Turno cancelado correctamente. ")

            elif paciente == lunes2:
                lunes2 = ""
                print("Turno cancelado correctamente. ")

            elif paciente == lunes3:
                lunes3 = ""
                print("Turno cancelado correctamente. ")

            elif paciente == lunes4:
                lunes4 = ""
                print("Turno cancelado correctamente. ")

            else:
                print(" No se encontro un turno para ese paciente. ")

        ## CANCELACION PARA MARTES ###

        if dia == 2: 

            if paciente == martes1:
                martes1 = ""
                print(" Turno cancelado correctamente. ")

            elif paciente == martes2:
                martes2 = ""
                print(" Turno cancelado correctamente. ")

            elif paciente == martes3:
                martes3 = ""
                print(" Turno cancelado correctamente. ")

            else:
                print("No se encontró un turno para ese paciente.")

    ### agenda del dia ###

    elif opcion == 3:

        dia = input(" Seleccione dia (1= Lunes, 2= Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print(" ERROR: seleccione 1 o 2. ")
            dia = input(" Seleccione dia (1 = lunes, 2 = Martes): ")

        dia = int(dia)

        if dia == 1:

            print("====================================")
            print("           AGENDA LUNES             ")
            print("====================================")

            if lunes1 == "":
                print(" Turno 1: (libre)")
            else:
                print(f"Turno 1: {lunes1}")

            if lunes2 == "":
                print(" Turno 2: (libre)")
            else:
                print(f" Turno 2: {lunes2}")

            if lunes3 == "":
                print(" Turno 3: (libre)")
            else: 
                print(f"Turno 3: {lunes3}")

            if lunes4 == "":
                print(" Turno 4: (libre)")
            else:
                print(f" Turno 4: {lunes4}")

        elif dia == 2:

            print("====================================")
            print("          AGENDA MARTES            ")
            print("====================================")

            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {martes1}")

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {martes2}")

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {martes3}")

    ### RESUMEN GENERAL ###

    elif opcion == 4:

        ocupados_lunes = 0
        ocupados_martes = 0

        ## contador de ocupados lunes ##

        if lunes1 != "":
            ocupados_lunes += 1

        if lunes2 !="":
            ocupados_lunes +=1
        if lunes3 != "":
            ocupados_lunes += 1

        if lunes4 != "":
            ocupados_lunes += 1

        ## contador ocupados martes ##

        if martes1 != "":
            ocupados_martes += 1

        if martes2 != "":
            ocupados_martes += 1

        if martes3 != "":
            ocupados_martes += 1

        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print("================  RESUMEN  ===================")
        print(f" Lunes: {ocupados_lunes} ocupados - {disponibles_lunes} disponibles.")
        print(f" Martes: {ocupados_martes} ocupados - {disponibles_martes} disponibles. ")

        if ocupados_lunes > ocupados_martes:
            print(" Dia con mas turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print(" Dia con mas turnos: Martes")
        else:
            print(" Dia con mas turnos: Empate")


    elif opcion == 5:
        print(" Finalizando sistema...")


### ACTIVIDAD 4 ####

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

print(" Bienvenido a mi escape room agente") 
print(" Quiero probar la seguridad de mi boveda, te molesta hacerlo bajo presion?")
print("intenta abrir una bóveda con 3 cerraduras.")
print("Tenés energía y tiempo limitados.")
print("Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, lograras salir con lo que buscas")
print("De lo contrario...")
print(" Mejor empecemos")

nombre = input("Digame.. cual es su nombre agente? : ")
while not nombre.isalpha():
    nombre = input("Ese no es un nombre, a menos que seas un robot! porfavor ingrese solo letras: ")

print(f"Oh con que.. {nombre}, que lindo nombre.. mm que lastima ")
print("...")
print()
print("ESPERA ESCUHAS ESO? ESTA COMENZANDO!")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:

    print("==============================")
    print("     ESTADO DE LA BÓVEDA")
    print("==============================")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {alarma}")
    print(f"Código parcial: {codigo_parcial}")

    print("¿Qué acción desea realizar?")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Seleccione una opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Opción inválida. Ingrese 1, 2 o 3: ")

    opcion = int(opcion)

    #opcion 1
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        print("Intentando forzar la cerradura...")

        #sist anti.spam,
        if forzar_seguidas == 3:
            print(f"¡La cerradura se trabó {nombre}!")
            print("¡ALARMA ACTIVADA!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            alarma = True

        else:
            # Riesgo de alarma si la energía estaba por debajo de 40
            # Se considera la energía antes de realizar el costo.
            energia_despues = energia

            if energia_despues < 40:
                print("¡La energía es muy baja! Hay riesgo de alarma.")
                numero = input("Elija un número del 1 al 3: ")

                while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                    numero = input(f"Porfavor {nombre}, se nota que no eres un robot. Número inválido. Ingrese un número del 1 al 3: ")

                numero = int(numero)

                if numero == 3:
                    alarma = True
                    print("¡Elegiste 3! que mala suerte, La alarma se activó.")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")

    # pcion 2: hackear panel
    elif opcion == 2:
        forzar_seguidas = 0
        energia -= 10
        tiempo -= 3

        print("Oh se te dan bien las computadortas!")
        print("Iniciando hackeo...")

        for paso in range(1, 5):
            codigo_parcial += "°"
            print(f"Paso {paso}/4... Código: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código completo! Se abrió una cerradura.")
            print(" Bravo!  estoy empezando a dudar si eres una maquina...")
        else:
            print("El código todavía no es suficiente.")

    # OPCIÓN 3: DESCANSAR
    elif opcion == 3:
        forzar_seguidas = 0
            #si al energia supera los 100 vuelve a limitarlo a 100
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma:
            energia -= 10
            print("La alarma está activa: perdés 10 de energía extra.")

        print("Descansaste?..Ya era hora.  ¡CONTINUEMOS!")


    # Bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("¡SISTEMA BLOQUEADO!")
        print("La alarma se activó y queda poco tiempo.")
        print(f"DERROTA: bloqueo de seguridad. quedaste atrapado/a {nombre}")

        break

# final y victoria
if cerraduras_abiertas == 3:
    print("================================")
    print("           ¡VICTORIA!")
    print("================================")
    print(f"Agente {nombre}, abriste las 3 cerraduras! bien jugado.")
    print(" Pero esto no acaba aqui, ya nos encontremos en otras historias")
    print(" Yo con otro nombre, y tu? quien sabe capaz la siguiente vez si seas un robot!")

elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
    print("DERROTA: el sistema quedó bloqueado.")

elif energia <= 0:
    print("Te noto cansado/a, porque no duermes?...")
    print("DERROTA: te quedaste sin energía.")


elif tiempo <= 0:
    print("Para la proxima deberia agregar un reloj de pared en la sala... le dire a mi asistente.")
    print("DERROTA: se acabó el tiempo.")

elif alarma:
    print("aghh.. deberia emepezar a aceptar robots que quieran participar")
    print("DERROTA: la alarma bloqueó la bóveda.")



#### ACTIVIDAD 5 ####

print("--- BIENVENIDO A LA ARENA ---")

# P 1: Nombre del Gladiador
print("Bienvenido a 'La Arena' noble Gladiador")
nombre = input("Digame, Cual es su nombre:  ")

while not nombre.isalpha():
    print()
    print("Mmm.. ese nombre no es muy comun por aqui.. seria peligroso levantar sospechas.")
    print()
    nombre = input("Porfavor inventa un nombre que contenga solo letras guerrero: ")

#### p 2 : info base
vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
danio_enemigo = 12
turno_gladiador = True

print()
print(f"Con que.. {nombre}. Eres el siguiente, prueba tu valor! exitos.")
print()
print("=== INICIO DEL COMBATE ===")

#### P 3: combate
while vida_jugador > 0 and vida_enemigo > 0:

    if turno_gladiador:

        print()
        print(f"{nombre}  HP: {vida_jugador}  vs Enemigo HP: {vida_enemigo}  | Pociones: {pociones}")

        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)

        ### Op 1: Ataque Pesado
        if opcion == 1:

            if vida_enemigo < 20:
                danio = ataque_pesado * 1.5
                print("¡GOLPE CRÍTICO!")
            else:
                danio = ataque_pesado

            vida_enemigo -= danio

            print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

        ### Op 2: Ráfaga Veloz
        elif opcion == 2:

            print(">>> ¡Inicias una ráfaga de golpes!")

            for golpe in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        ### Op 3: Curar
        elif opcion == 3:

            if pociones > 0:
                vida_jugador += 30

                if vida_jugador > 100:
                    vida_jugador = 100

                pociones -= 1

                print("¡Te curaste 30 puntos de vida!")
            else:
                print("¡No quedan pociones!")

        ####Cambio turno
        turno_gladiador = False

    else:

        #### Turno enemigo
        vida_jugador -= danio_enemigo

        print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")

        # Vuelve el turno al Gladiador
        turno_gladiador = True

###### P 4: Final
print()
print("========= FIN DEL COMBATE =========")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate...")