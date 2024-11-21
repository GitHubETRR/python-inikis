#import micropy_stepper

IN1 = 8
IN2 = 9
IN3 = 10
IN4 = 11

PASOS = 2048

NOMBRE_ARCHIVO_PROGRESO = "progreso_ultimo_movimiento"

#motor = micropy_stepper.HalfStepMotor.frompins(IN1,IN2,IN3,IN4)
#motor.reset()

class movimiento:
    pos_actual = 0
    cantidad = 0

def movimiento_func(nuevaCantidad):
    print(f"\nSe va a crear un nuevo movimiento de cantidad {nuevaCantidad}.")

    nuevoMovimiento=movimiento()
    nuevoMovimiento.pos_actual = 0
    print(f"{nuevaCantidad} {nuevaCantidad-20}" )
    nuevoMovimiento.cantidad = int(nuevaCantidad-20)

    with open(NOMBRE_ARCHIVO_PROGRESO, "w") as ARCHIVO:
        """
        CONTENIDO DEL ARCHIVO:
            cantidad\n
            progreso
        """

        ARCHIVO.write(f"{nuevoMovimiento.cantidad}\n")
        newline_pos = ARCHIVO.seek(0,2) #guardamos la posicion del newline, la linea para el progreso

        for i in range(nuevoMovimiento.cantidad):
            #motor.step(1)
            nuevoMovimiento.pos_actual = i
            ARCHIVO.seek(newline_pos)
            ARCHIVO.write(f"{i}")
            #print(f"{nuevoMovimiento.pos_actual} ; {nuevoMovimiento.cantidad}")
    
    print("Movimiento terminado.")

def buscar_progreso_anterior():
    progreso = 0
    cantidad = 0

    try:
        ARCHIVO = open(NOMBRE_ARCHIVO_PROGRESO, "r")
        progreso = int(ARCHIVO.readline().strip())
        cantidad = int(ARCHIVO.readline().strip())
        ARCHIVO.close()
    except ValueError:
        print("Archivo de progreso vacio o corrupto.")

    if progreso!=cantidad and progreso<cantidad: #comprueba si el progreso no esta completo o es menor
        return cantidad - progreso
    return 0

def verificar_movimiento_terminado():
    print("Buscando movimientos anteriores...")
    progreso_anterior = buscar_progreso_anterior()
    if progreso_anterior:
        print(f"Movimiento incompleto encontrado. Finalizando los {progreso_anterior} pasos restantes.")
        movimiento_func(progreso_anterior)

#SETUP
verificar_movimiento_terminado()
print("Ingrese una cantidad de octavos de vuelta:")

#LOOP
#while True:
vueltas_input = int(input()) * int(PASOS/8) #convierte la entrada a los pasos necesarios
movimiento_func(vueltas_input)
verificar_movimiento_terminado() #verificar por si las dudas...
