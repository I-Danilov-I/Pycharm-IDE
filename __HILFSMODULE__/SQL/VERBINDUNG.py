# Modul einbinden, um die DB-Zugriffe zu ermöglichen
import mysql.connector

# Modul mit den festgelegten Login Daten importieren
import LOGIN as LOG


# LOGIN DATEN VERDECKT, von Tupel in String konvertiert
HOST = "".join(LOG.host)
USER = "".join(LOG.user)
PASSWORD = "".join(LOG.password)
DATENBANK = "". join(LOG.datenbank)


# Funktionsdefinition um die Verbindung zu Datenbank herzustellen
def verbindung_herstellen():
    """
    _________________________________________________________________________________________________________________
    Zunächst müssen wir eine Verbindung aufbauen, dazu benötigen wir die nachfolgenden Informationen:
        - Servername,
        - Benutzername,
        - Passwort
    Diese Login Daten habe ich aus Datenschutzgründen in einem separaten Modul definiert.

    :verbindung: Verbindung aufbauen - connection-Objekt erstellen und als Rückgabewerten wiedergeben.
    :return: Ausgabe des Hashwertes des initialisierten Objektes.
    :except: Database Errors in der Var.errors speichern und den Wert wiedergeben.
    _________________________________________________________________________________________________________________
    """
    try:
        verbindung = mysql.connector.connect(host=HOST,
                                             user=USER,
                                             password=PASSWORD,
                                             database=DATENBANK)
        if verbindung is None:
            print("Verbindungsfehler!")
        else:
            print("Erfolgreich verbunden!")
        return verbindung

    except mysql.connector.errors.DatabaseError as error:
        return error

