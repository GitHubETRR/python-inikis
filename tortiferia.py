objetos = {
    "TF": "Tortafrita",
    "MED": "Medialuna",
    "CAFE": "Cafe",
    "TOST": "Tostado",
    "OFERTA": "Oferta Cafe y 2 Medialunas",
    "TO(OFERTA)": "Oferta Cafe y 2 Tostados"
}
metodos_pago = {
    "EF": "Efectivo",
    "MP": "Transferencia",
}

lista = open("ventas.txt",'r').readlines()

for linea in lista:
    datos = linea.split()

    cant = int(datos[0])

    objeto = objetos[datos[1]] if objetos[datos[1]] else 0
    pago = metodos_pago[datos[2]] if metodos_pago[datos[2]] else 0

    print("Se compro", objeto.lower(), "| Cantidad:", cant, "| Metodo de pago:", pago.lower())
