# Format Ausgabe Modul.
import AFA

# Das vorher definite Modul importieren, um Verbindung zu DB aufzubauen.
import VERBINDUNG

# Das zurückgegebene Objekt in Var. Speichern
VERBINDUNG = VERBINDUNG.verbindung_herstellen()

# Formatierung: Das zurückgegebene Objekt in Var. Speichern
F = AFA


# Funktion für Anweisungsangabe:
def sql_befehl(befehl):
    """
    :befehl: ALS PAR. wird ein SQL BEFEHL als string übergeben
    """
    cursor = VERBINDUNG.cursor()
    print("Cursor erstellt.")

    cursor.execute(befehl)
    print(cursor)

    F.auto_format_ausgabe_titel("DATENBANKEN")
    for i in cursor:
        print(i)
    cursor.close()
    F.auto_format_ausgabe_titel("ENDE")
