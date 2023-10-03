import sys
import erkennung
import maus

# Koordinaten der Farbe erfassen
koordinaten = erkennung.erkennung()
if not koordinaten:
    sys.exit("Nicht erkannt")

else:
    # koordinaten an die Maussteuerung übergeben
    maus.anvisieren(koordinaten[0], koordinaten[1])