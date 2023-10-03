# ________________________________________________[ FUNKTIONALITÄTEN ]_________________________________________________
# Definition der Klasse Bruch für die Berechnung von Brüchen
class Bruch:
    # Mag-Methode: Konstruktor.
    def __init__(self, z, n):
        # Zähler
        self.z = z
        # Nenner
        self.n = n

    # Mag-Methode: für die Ausgabe.
    def __str__(self):
        return f"{self.z} / {self.n}"

    # Mag-Methode-Addition:
    def __add__(self, other):
        print("-----------[ Aufruf der Mag-Methode Addition ]-----------")
        # Bruchaddition nach der Standardformel.
        z = (self.z * other.n) + (other.z * self.n)
        n = self.n * other.n
        # Ausgabe auf die Konsole zum Verständnis
        print(f"Berechne: {Bruch(self.z, self.n)} + {Bruch(other.z, other.n)} = ")
        return Bruch(z, n)

    # Mag-Methode-Subtrahieren:
    def __sub__(self, other):
        print("-----------[ Aufruf der Mag-Methode Subtrahieren ]-----------")
        # Gemeinsamen Zähler finden und Subtrahieren
        z = (self.z * other.n) - (other.z * self.n)
        n = self.n * other.n
        # Ausgabe auf die Konsole zum Verständnis
        print(f"Berechne: {Bruch(self.z, self.n)} - {Bruch(other.z, other.n)} = ")
        return Bruch(z, n)

    # Mag-Methode-Multiplikation:
    def __mul__(self, other):
        print("-----------[ Aufruf der Mag-Methode Multiplizieren ]-----------")
        # Bruchmultiplikation nach der Standardformel.
        z = self.z * other.z
        n = self.n * other.n
        # Ausgabe auf die Konsole zum Verständnis
        print(f"Berechne: {Bruch(self.z, self.n)} * {Bruch(other.z, other.n)} = ")
        return Bruch(z, n)

    # Mag-Methode-Division:
    def __truediv__(self, other):
        print("-----------[ Aufruf der Mag-Methode Dividieren ]-----------")
        # Bruchdivision nach der Standardformel.
        z = self.z * other.n
        n = self.n * other.z
        # Ausgabe auf die Konsole zum Verständnis
        print(f"Berechne: {Bruch(self.z, self.n)} : {Bruch(other.z, other.n)} = ")
        return Bruch(z, n)

    # Mag-Methode-Gleichheit:
    def __eq__(self, other):
        print("-----------[ Aufruf der Mag-Methode Gleichheit ]-----------")
        return None

# ___________________________________________________[ HAUPTPROGRAMM ]_________________________________________________
# Instanziieren, Erzeugen eines Objektes der Klasse Bruch.
# bruch = Bruch(5, 6)

# # Addiere Klasse (Bruch)
# r = A + C
# print("Ergebnisse:", r)
#
# # Subtrahiere Klasse (Bruch)
# r = A - C
# print("Ergebnisse:", r)
#
# # Multiplizieren Klasse (Bruch)
# r = A * C
# print("Ergebnisse:", r)
#
# # Dividieren Klasse (Bruch)
# r = A / C
# print("Ergebnisse:", r)
#
# r = A == C
# print("Ergebnisse:", r)
