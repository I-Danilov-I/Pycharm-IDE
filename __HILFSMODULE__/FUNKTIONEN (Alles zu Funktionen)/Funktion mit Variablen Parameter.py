# Funktion mit Variablen Parameter
def addiere(* summanden):
    gesamtsumme = 0

    for s in summanden:
        print(s)
        gesamtsumme += s
        print("Gesammsumme", gesamtsumme)
    return gesamtsumme


addiere(5, 5)
