import math

prefix = "py"
print(prefix + "thon")

b=0
while b<10:
    b+=1
    print(b)

print(sorted((10,2,3,40,80)))

#print('C:\d\')

lista_for=[10,40,20,30,60,80]
for i in range(len(lista_for)):
    if lista_for[i] > 60:
        break
    print(i, lista_for[i], lista_for[i]%8)
else:
    print("for terminado")

for n in range(2,10):
    print("N:",n)
    for x in range(2,n):
        print("\tX:",x)
        if x % n == 0:
            print("\t",x,"divisible por",n)
        else:
            print("\t",x,"divisible por",n)

for num in range(2,10):
    if num % 2 == 0:
        print("Encontré un número par", num)
        continue
    print("Encontré un número impar", num)

def fib(lim):
    "Fibonacci sum 'lim' times"
    a,b=0,1
    while a < lim:
        a, b = b, a+b
        print(a)

fib(4)
lista_for.extend(range(2,10))
print(lista_for)

lista_eliminable=[5,10,50,20,3,10]
lista_eliminable.remove(5)
print(lista_eliminable)
#lista_eliminable.remove(40) #error
#if not lista_eliminable.remove(40):
#    print("No se pudo encontrar un elemento 40 de la lista")

print(lista_eliminable.index(10)) #0 porque lista_eliminable despues de remover el 5 es 10, 50, 20, 3
print(lista_eliminable.count(10))

lista_sorteable=[5,6,7,9,10,30,10,5,9,6]
lista_sorteable.sort()
print(lista_sorteable)

print("Is 7 in lista_sorteable?", 7 in lista_sorteable)
a="apalapapa"
print(set(a))

dictionary={'A': 30,'B': 50,'C': 99}
print(dictionary['A'])
print(list(dictionary.keys()))
print('A' in dictionary, 30 in dictionary)

class complejo:
    def __init__(self, real,imaginario):
        self.r = real
        self.i = imaginario
    def modulo(self):
        return int(math.sqrt(self.r + self.i))

miNumeroComplejo=complejo(2,2)
print(miNumeroComplejo.modulo())
format_arg1 = 5
format_arg2 = 10

print("Este string %s est+a %s formateado" %(format_arg1, format_arg2))
print("Este string también {} está {} formateado".format(format_arg1, format_arg2))
print(f"Este otro string también {format_arg1} está {format_arg2} formateado")

Nombre = 'Isi'
Edad = 36
Ocupacion = 'Docente'

msg = (
    f'Nombre: {Nombre}\n'
    f'Edad: {Edad}\n'
    f'Ocupacion: {Ocupacion}'
)
print(msg)

import smtplib

mail = 'dinovelley@gmail.com' #no puedo usar mi mail :(
pw = ''
receiver = 'imena@etrr.edu.ar'
subj = 'Hola'
msg = 'He enviado esto desde Python. Soy un crack'

def enviar_mail():
    try:
        server = smtplib.SMTP_SSL('smtp.gamil.com',465)
        server.ehlo()
        pw=input('Ingresar contraseña: ')
        server.login(mail,pw)
        server.sendmail(mail, receiver, msg)
        server.close()
        print("Email enviado.")
    except:
        print("No se pudo enviar el mail")

import numpy
from matplotlib import pyplot
x = numpy.linspace(0, 2*numpy.pi, 100)
y = numpy.sin(x)

pyplot.plot(x,y)
pyplot.show()
