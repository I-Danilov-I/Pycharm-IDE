# Variablen
startkapital = 100
zinssatz = 0.02


# Berechnung ohne Funktion
ergebnis = startkapital + startkapital * zinssatz
print("Ergebnis:", ergebnis, "EUR")


# Berechnung mit standard Funktion
def zinssatz_berechnen(kapital, zins):
    return kapital * zins + kapital
print("Ergebnis mit Funktion:", zinssatz_berechnen(100, 0.02), "EUR")


# Berechnung mit Lamda Funktion
lamda_function = lambda k, z: k * z + k
print("Ergebnis mit lamda Funktion:", lamda_function(100, 0.02), "EUR")


# Funktion mit List Compression
LISTE_ZAHLEN = [7, 18, 11, 12, 14]
print("Liste vor dem Rechnen:", LISTE_ZAHLEN)
LISTE_ZAHLEN = [werte * 2 for werte in LISTE_ZAHLEN]
print("Liste nach dem Rechnen:", list(LISTE_ZAHLEN))
