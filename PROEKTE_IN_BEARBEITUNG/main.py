import erkennung
import maus

# Koordinaten der Farbe erfassen
koordinaten = erkennung.erkennung()

# koordinaten an die Maussteuerung übergeben
maus.anvisieren(koordinaten[0], koordinaten[1])
