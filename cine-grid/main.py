import random

MAYUSCULA = ["A","B","C"]
MINUSCULA = ["x","y","z"]
NUMERO = ["0","1","2"]

TEMAS = [MAYUSCULA, MINUSCULA, NUMERO]

combinaciones = {}

cant_combinaciones = 0

for item1 in TEMAS[0]:
    for item2 in TEMAS[1]:
        for item3 in TEMAS[2]:
            nuevaCombinacion = item1+item2+item3
            combinaciones[nuevaCombinacion] = random.randint(0,1)
            #print(f"{nuevaCombinacion}, {combinaciones[nuevaCombinacion]}")
            cant_combinaciones += 1

#print(cant_combinaciones)

opcion_x, opcion_y, opcion_z = random.sample(range(0, len(TEMAS)), 3)
tema_x, tema_y, tema_z = TEMAS[opcion_x], TEMAS[opcion_y], TEMAS[opcion_z]

grilla = [
    [" ",tema_x[0],tema_x[1],tema_x[2]],
    [tema_y[0],"0","0","0"],
    [tema_y[1],"0","0","0"],
    [tema_y[2],"0","0","0"],
]

for fila in grilla:
    print(fila)
"""
coord_x_usuario = input("Ingresar una coordenada X: ")
coord_y_usuario = input("Ingresar una coordenada Y: ")
coord_usuario = (int(coord_x_usuario)-1,int(coord_y_usuario)-1)

grilla[coord_usuario[1]+1][coord_usuario[0]+1] = tema_x[coord_usuario[0]] + tema_y[coord_usuario[1]]
"""
input_usuario = str(input(f"Elija uno de los siguientes valores: {tema_z[0],tema_z[1],tema_z[2]}"))

for combinacion in combinaciones:
    print(combinacion)

for fila in grilla:
    print(fila)
