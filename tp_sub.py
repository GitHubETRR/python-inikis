"""
tengo un servidor en casa donde guardo pelis y series y las transmito mediante la aplicacion Plex

la serie que descargue (Twin Peaks) venia con la siguiente similiar estructura en una de sus temporadas:

Twin Peaks S02:
  - Episodio1.mp4
  - Episodio2.mp4
  - Episodio3.mp4
     ...
  - Episodio22.mp4

  Subtitulos:
     Episodio1:
        - English.srt
     Episodio2:
        - English.srt
     Episodio3:
        - English.srt
       ...
     Episodio22:
        - English.srt

debido a esta estructura Plex no podia detectar los subtitulos, porque en vez
de estar en la carpeta 'Subtitulos', estaban en sub carpetas creadas para cada Episodio.

escribi este script de python para que me los reacomodara a la carpeta 'Subtitulos'
y ademas les cambie el nombre, porque si no todos se llamarían 'English.srt' y
eso causaría conflictos de nombre, por lo que a cada subitutlo les puse el nombre
de su episodio correspondiente, ademas esto facilitaba la deteccion automatica de subtitulos
de Plex.
"""

import os
import sys
import shutil

serie_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
subs_dir = "/home/nacho/plexmedia/Series/Twin Peaks/Twin.Peaks.S03.1080p.BluRay.x265-RARBG/Subs/"

for carpeta in os.scandir(subs_dir):
    print(carpeta.name)
    print("Accediendo a:", carpeta.name)

    for sub in os.scandir(subs_dir+carpeta.name):
        print("\tMoviendo", os.path.realpath(sub), "a", subs_dir + carpeta.name + ".srt")
        shutil.move(os.path.realpath(sub), (subs_dir + carpeta.name + ".srt"))
