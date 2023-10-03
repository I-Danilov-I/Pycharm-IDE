# Fakultät iterativ berechnen
def fakultet_iterativ(wert):
	f = 1
	for i in range(wert, 1, -1):
		f *= i
	return f


zahl = int(input("Bitte geben Sie ine Zahl ein, um die Fakultät zu berechnen: "))
fakultet = fakultet_iterativ(zahl)
print("Die Fakultät der Zahl", zahl, "ist:", fakultet)


# Fakultät rekursiv berechnen(Kürzer und Kompakter, braucht aber viele Ressourcen, weil er zwischenspeichern muss)
def fakultet_rekursiv(wert):
	if wert > 1:
		f = wert * fakultet_rekursiv(wert-1)
	else:
		f = 1
	return f


print(fakultet_rekursiv(1))
