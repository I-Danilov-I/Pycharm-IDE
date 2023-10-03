# map(funktion, liste)
# filter(funktion, liste)


def positiv(wert):
    if wert >= 0:
        return wert
    else:
        return False

# Liste mit zufälligen Zahlen definiert
zahlen_lis = [5, 7, 8, -2, -5, -7, 0]

# Funktion: gibt nur positive Werte zurück
zahlen_pos = list(filter(positiv, zahlen_lis))

# Datentyp und die Liste ausgeben
print("Datentyp:", type(zahlen_pos), list(zahlen_pos))


# Schleife: Gefilterte Werde ausgeben
print("Positive zahlen:")
for i in zahlen_pos:
    print(i, end=" ")
