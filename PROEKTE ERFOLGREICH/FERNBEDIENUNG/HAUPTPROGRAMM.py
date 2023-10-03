# ______________________________________________________[IMPORTE]______________________________________________________
# Erstellen von Benutzeroberfläche (tk= tkinter)
import tkinter as tk

# Interaktion mit dem OS
import sys

# Importiere Klasse
from Fernbedienung import RC

# ____________________________________________________[FUNKTIONEN]_____________________________________________________
def next_sender():
    # Den Text im Anzeigefeld ändern in die Return Ausgabe der Klasse
    anzeige_feld.config(text=RC.pfeil_oben())


def last_sender():
    # Den Text im Anzeigefeld ändern in die Return Ausgabe der Klasse
    anzeige_feld.config(text=RC.pfeil_unten())


def eingabe():
    # Den Text im Anzeigefeld ändern in die Return Ausgabe der Klasse
    anzeige_feld.config(text=RC.schalten(eingabe_feld.get()))


def volumen_plus():
    anzeige_feld.config(text=RC.vol_plus())


def volumen_minus():
    anzeige_feld.config(text=RC.vol_minus())


def prog_speichern():
    anzeige_feld.config(text=RC.set(eingabe_feld.get()))


# ___________________________________________________[HAUPTPROGRAMM]___________________________________________________
# Ein Dialogfenster Erstellen mit entsprechenden Eigenschaften
window = tk.Tk()
window.title("Fernbedienung")
window.geometry("300x700")
window.config(background="black")


# Eingabefenster erstellen und mit pack() ins Fester einfügen, für die Ausgabe.
anzeige_feld = tk.Label(window, width=30, height=10, text="TV", font=("Arial", 18), foreground="red")
anzeige_feld.pack(side="top", padx=3, fill="y")


# Button: Programm weiter schalten
pfeil_hoch = tk.Button(window, width=15, height=1, text="CH+", command=next_sender, background="skyblue")
pfeil_hoch.pack(side="top", padx=3, fill="x")

# Button: Zum Absenden der Eingabe, und mit pack() ins Fenster einfügen. command=Funktion ausführen
enter = tk.Button(window,width=10, height=1, text="ENTER", command=eingabe, background="red")
enter.pack(side="top", padx=3, fill="x")

# Button: Programm zurück schalten
pfeil_runter = tk.Button(window, width=15, height=1, text="CH-", command=last_sender, background="skyblue")
pfeil_runter.pack(side="top", padx=3, fill="x")

# Eingabefenster erstellen und mit pack() ins Fester einfügen, für die gezielte Sender wahl.
eingabe_feld = tk.Entry(window, width=20)
eingabe_feld.pack(side="top", padx=3)

# Button: Lautstärkeregler
vol_plus = tk.Button(window, width=10, height=1, text="Vol+", background="skyblue", command=volumen_plus)
vol_plus.pack(side="right", padx=3, fill="x")

# Button: Lautstärkeregler
vol_minus = tk.Button(window, width=10, height=1, text="Vol-", background="skyblue", command=volumen_minus)
vol_minus.pack(side="left", padx=3, fill="x")

prog_set = tk.Button(window,  width=10, height=1, text="Speichern", background="skyblue", command=prog_speichern)
prog_set.pack(side="top", padx=1, fill="x")


# ______________________________[Sobald das Fenster geschlossen wird Programm beenden]_________________________________
try:
    sys.exit(window.mainloop())
except KeyboardInterrupt:
    sys.exit("Programm beendet")