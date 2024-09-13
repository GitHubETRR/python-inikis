from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment, Color

#definiciones de cada objeto
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

ventas = []
lista = open("ventas.txt",'r').readlines()

#obtenemos los datos
for linea in lista:
    datos = linea.split()

    cant = int(datos[0])

    objeto = objetos[datos[1]] if objetos[datos[1]] else 0
    pago = metodos_pago[datos[2]] if metodos_pago[datos[2]] else 0

    ventas.append((cant,objeto,pago))

    #print("Se compro", objeto.lower(), "| Cantidad:", cant, "| Metodo de pago:", pago.lower())

excel = Workbook()
hoja = excel.active
hoja.title = "Ventas Tortiferia 12-9"

columnas = ("CANTIDAD","OBJETO","PRECIO")
col_anchos = (11.7, 28.9, 13.3) #respectivos a las columnas de arriba

#columnas
for col_index, col in enumerate(hoja.iter_cols(min_row=1, max_col=3)):
    for celda in col:
        celda.value = columnas[col_index]
        celda.font = Font(bold=True, color="FFFFFF")
        celda.alignment = Alignment(horizontal="center")
        celda.fill = PatternFill(fill_type="solid",start_color='000000')
        hoja.column_dimensions[celda.coordinate[0]].width = col_anchos[celda.col_idx-1]

#filas (items)
for fila_idx, fila in enumerate(hoja.iter_rows(min_row=2, max_col=3, max_row=lista.__len__())):
    fila[0].value = ventas[fila_idx][0]
    fila[1].value = ventas[fila_idx][1]
    fila[2].value = ventas[fila_idx][2]
    for celda in fila:
        celda.alignment = Alignment(horizontal="center")

excel.save("ventas_12_9.xlsx")
