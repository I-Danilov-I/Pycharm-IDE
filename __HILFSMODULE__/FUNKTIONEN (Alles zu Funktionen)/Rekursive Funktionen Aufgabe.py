# ---------------------------------------------[Importierte Module]---------------------------------------------------
import time
import random


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[Aufgabe Nr. 1: Countdown]<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
# Es ist eine Funktion zu definieren, die durch Aufruf der Funktion selbst von einem Startwert
# bis 0 herunterzählt und diese Werte auf der Konsole ausgibt.
# --------------------------------------------------------------------------------------------------------------------


def countdown(startzeit):
	"""
	--- Rekursive Funktionen ---
	Die Idee eines rekursiven Algorithmus ist, einen Algorithmus durch sich selbst zu beschreiben der
	Algorithmus muss an einer definierten Stelle beendet werden, sonst ist der Algorithmus unendlich
	
	:param startzeit:
	:return:
	"""
	startzeit -= 1
	if startzeit == 0:
		return startzeit
	else:
		print(startzeit)
		time.sleep(1)
		return countdown(startzeit)


# Funktionsaufruf: Beschreibung der Funktion ausgeben
print(countdown.__doc__)

# Funktionsaufruf: Countdown
print(countdown(10))


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[Aufgabe Nr. 2: Messreihe]<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
# Aus einer Messreihe wurden 100 ganzzahlige Werte in einer Liste gespeichert. Für die
# Messwerte sollen verschiedene statistische Kenndaten ermittelt werden:
# --------------------------------------------------------------------------------------------------------------------

# Erzeuge 100 zufällige Zahlen in dem umkreis von 0 -1000 = Liste
messwerte = random.choices(range(0, 1000), k=100)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[Funktionen]<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Information
def info():
	# Ausgabe der Messwerte mit Info
	print("Messwerte:", messwerte, "\n" "Datentyp:", type(messwerte), "\n"
		  "Elementen anzahl:", len(messwerte))
	print("----------------------------------------------------------------------------------------------------------")


# a, b) Berechnung des Min/Max der Messwerte
def berechnung_min_max():
	# Minimalen und Maximalen wert aus der Liste ermitteln und ausgeben
	return min(messwerte), max(messwerte)


# c) Berechnung des Medians (Mittelwert/Durchschnitt)
def berechnung_mittelwert():
	return min(messwerte) + max(messwerte) / 2


# d) Berechnung der Spannweite der Messwerte
def berechne_spannweite():
	return max(messwerte) - min(messwerte)


# e) Berechnung der mittleren Abweichung der Messwerte
def berechne_mittle_abweichung_berechnen():
	
	# Liste zum Speichern der zwischenwerte
	zwischen_speicher = []
	
	# Schleife: einzelnen Messwert in dem wiedergegebenen Wert von erzeuge_zuf_zahlen() (Type:Liste)
	for MESSWERT in messwerte:
		
		# Rechne immer den größeren Wert von den kleiner ab, um nur positive zahlen wiederzugeben
		if MESSWERT < berechnung_mittelwert():
			zwischen_speicher.append(berechnung_mittelwert() - MESSWERT)
			
		elif MESSWERT > berechnung_mittelwert():
			zwischen_speicher.append(MESSWERT - berechnung_mittelwert())
			
	# Diesen Wert wiedergeben. Alle werte der Liste summieren und / 100 Teilen.
	return sum(zwischen_speicher) / 100


# f) Berechnung des Wertes, der am häufigsten vorkommt
def berechne_haufigsten_wer():
	# Rechne wie oft ein gleicher wert vorkommt
	return max(set(messwerte), key=messwerte.count)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[Hauptprogramm]<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

info()

print("a) Minimaler Messwert:", berechnung_min_max()[0], "\n"
	  "b) Maximaler Messwert:", berechnung_min_max()[1])

print("c) Mittelwert:", berechnung_mittelwert())

print("d) Spannweite der Messwerte", berechne_spannweite())

print("e) Mittlere Abweichung:", berechne_mittle_abweichung_berechnen())

print("f) Häufigster Wert:", berechne_haufigsten_wer())

# -------------------------------------------------------[ENDE]--------------------------------------------------------
