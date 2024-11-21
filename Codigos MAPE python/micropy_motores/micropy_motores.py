import machine
import micropy_stepper

INPUTS_MOTORES = [
            [1,2,4,5],
            [6,7,9,10],
            [11,12,14,15],
            [16,17,19,20],
            [34,32,31,29],
            [27,26,25,24]
                ],

PASOS = 2048

motores = []

pin_led1 = Pin(22, Pin.OUT)
pin_led2 = Pin(21, Pin.OUT)

#setup motores
for entradas in INPUTS_MOTORES:
    nuevoMotor = micropy_stepper.HalfStepMotor.frompins(entradas[0],entradas[1],entradas[2],entradas[3])
    nuevoMotor.reset()
    motores.append(nuevoMotor)
    pass

# DIRECCION MOTORES: lista mutable que representa las direcciones en las que deberían moverse los 6 motores
#   estados:
#     1: vuelta clockwise (arriba)
#     0: retener
#    -1: vuelta anti-clockwise (abajo)
#   ej. [1,0,-1,1,0,1,0,1] => [arriba, retener, abajo, arriba, retener, arriba, retener, arriba]
direccionMotores = [0,0,0,0,0,0]

estadosAnteriores = [0,0,1,0,1,0,1,0]

#
# decodificacion de los caracteres, representan los nuevos estados
#
caracterDecodificado = [1,0,1,0,0,1,0,1]

# setup direccion motores
#   se compara los estados anteriores con los nuevos estados del caracter decodificado
#   para determinar la dirección de los motores
for i, estado in enumerate(caracterDecodificado[:-2]):
    if estadosAnteriores[i] == caracterDecodificado[i]:
        direccionMotores[i] = 0
    elif estadosAnteriores[i] == 0 and caracterDecodificado[i] == 1:
        direccionMotores[i] = 1
    elif estadosAnteriores[i] == 1 and caracterDecodificado[i] == 0:
        direccionMotores[i] = -1

# setup leds
pin_led1.value = caracterDecodificado[-2]
pin_led2.value = caracterDecodificado[-1]

for i, valorEntradaMotor in enumerate(direccionMotores): #modificar los motores
    motores[i].step(PASOS*valorEntradaMotor)
