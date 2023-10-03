def auto_format_ausgabe_titel(schrift):
    """
    Formatiert automatisch überschriften.
    :param schrift: Hier wird der Text übergeben der Formatiert ausgegeben werden soll.
    """

    # Zeichenanzahl berechnung um den Text immer mittig zu halten
    lang = len(schrift)
    lang = int(lang)
    seitlich = (100 - lang - 4) / 2
    seitlich = int(seitlich)

    # Maßen ausgaben (Nur bei änderungen Nötig)
    # print("Mitte Länge:", lang, seitlich, "Pro seite")

    # Zeichen die für die Formatierung verwendet werden
    a = "_"
    b = "_"
    c = "_"
    kl = "["
    kr = "]"

    # Ausgabe
    print(f"{a*seitlich}{kl} {schrift:{lang}} {kr}{b*seitlich}")
