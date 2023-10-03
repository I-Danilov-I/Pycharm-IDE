import erkennung
import maus

koordinaten = erkennung.erkennung()
# print(type(koordinaten), koordinaten)

maus.anvisieren(koordinaten[0], koordinaten[1])
