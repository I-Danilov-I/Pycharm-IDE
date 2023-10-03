print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[Beispiel 1]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# Syntax: lambda argumente(Werte die übergeben werden): algorythm (Was passieren soll).
# Dabei kann die Anzahl der Argumente beliebig sein. Es darf aber nur ein Ausdruck vorhanden sein.
# Betrachten wir als Nächstes eine einfache Funktion. Es sollen lediglich zwei Werte multipliziert werden:
# ____________________________________________________________________________________________________________________
def multiply_values(a, b):
    return a * b
print("Standard Funktion:", multiply_values(2, 2))

# ___________________________________________________________________________________________________________________
# Mit einer Lambda-Funktion würde dies wie im folgenden Beispiel aussehen. Der Rückgabewert der Lambda-Funktion wird
# hier der Variablen multiply_values zugewiesen.
# ____________________________________________________________________________________________________________________
multiply_values = lambda x, y: x * y
print("Lamda Funktion:", multiply_values(2, 2))


print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[Beispiel 2]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# Im zweiten Beispiel soll jedes Element einer Liste mit dem Wert 2 multipliziert werden. Hierbei nutze ich die Built-
# In-Funktionen range() und len().[2]
# ____________________________________________________________________________________________________________________
LISTE_ZAHLEN = [6, 8, 10, 12, 14]
print("Liste vor dem Rechnen:", LISTE_ZAHLEN)
for i in range(len(LISTE_ZAHLEN)):
    LISTE_ZAHLEN[i] *= 2
print("Liste nach dem Rechnen:", LISTE_ZAHLEN)

# ____________________________________________________________________________________________________________________
# Als Variante zur for-Schleife kommt nun map() zum Einsatz. Diese Funktion erwartet als ersten Parameter eine Funktion
# und als zweiten Parameter eine Sequenz. Als Argumente werden ihr die Lambda-Funktion und
# die Liste my_values (eine Sequenz) übergeben.

# An diesem Beispiel wird deutlich, welchen Vorteil eine Lambda-Funktion hat: Der Code läßt sich (hier zu einem
# Einzeiler) verkürzen. Freilich kann man sich aber darüber streiten, ob dies auf Kosten der Lesbarkeit geht.
# Außerdem mag – gerade bei Einsteigern – eine Lambda-Funktion große Konfusion auslösen.
# ____________________________________________________________________________________________________________________
LISTE_ZAHLEN = [6, 8, 10, 12, 14]
print("Liste vor dem Rechnen:", LISTE_ZAHLEN)
LISTE_ZAHLEN_new = map(lambda a: a * 2, LISTE_ZAHLEN)
print("Liste nach dem Rechnen:", list(LISTE_ZAHLEN))
print("Gespeichert in einer neun Liste:", list(LISTE_ZAHLEN_new))


print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[Beispiel 3]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# Der Vollständigkeit halber sei erwähnt, dass man als Variante auch eine list comprehension verwenden könnte:
# Wie Ihr den Beispielen entnehmen könnt, führen – wie so häufig – mehrere Wege zum Ziel. Ob man in der Praxis auf eine
# Lambda-Funktion zurückgreift, wird dabei häufig Geschmacksache sein.
# ____________________________________________________________________________________________________________________
LISTE_ZAHLEN = [7, 18, 11, 12, 14]
print("Liste vor dem Rechnen:", LISTE_ZAHLEN)
LISTE_ZAHLEN = [werte * 2 for werte in LISTE_ZAHLEN]
print("Liste nach dem Rechnen:", list(LISTE_ZAHLEN))
