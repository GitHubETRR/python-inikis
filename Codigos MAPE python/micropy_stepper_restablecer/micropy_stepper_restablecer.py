import micropy_stepper

IN1 = 8
IN2 = 9
IN3 = 10
IN4 = 11

PASOS = 2048

motor = micropy_stepper.HalfStepMotor.frompins(IN1,IN2,IN3,IN4)

motor.reset()
steps_input=0

print("Ingrese una cantidad de pasos en la terminal.")

while True:
    steps_input = int(input())
    cantidad = steps_input*PASOS
    print(f"Moviendo {cantidad} pasos.")
    motor.step(cantidad)
    print("Listo.")
