# ______________________________________________________[IMPORTE]______________________________________________________
# Erstellen von Benutzeroberfläche (tk= tkinter)
import tkinter as tk

# Interaktion mit dem OS
import sys

# Importiere die Klasse Bruchrechner
from back import Bruch

# ____________________________________________________[FUNKTIONEN]_____________________________________________________
def info_pack():
    """
    :expand:
        − wenn es auf „true“ gesetzt ist, wird das Widget erweitert, um jeden Platz zu füllen, der nicht anderweitig
        im übergeordneten Element des Widgets verwendet wird.

    :fill:
        − legt fest, ob das Widget zusätzlichen Platz ausfüllt, der ihm vom Packer zugewiesen wurde, oder ob es seine
        eigenen minimalen Abmessungen beibehält: NONE (Standard), X (nur horizontal füllen), Y (nur vertikal füllen)
        oder BOTH (sowohl horizontal als auch vertikal füllen).

    :side:
        − legt fest, gegen welche Seite des übergeordneten Widgets gepackt wird: OBEN (Standard), UNTEN, LINKS oder RECHTS
    """
    pass


def eingabe_annahme():
    """
    _____________________________________[Die Funktion erledigt folgende Ausgaben]_____________________________________
        - Eingabe annehmen
        - Eingabe an die Klasse weiterleiten
        - Zurück gegeben Wert aus der Klasse ins Fenster einschließen.

    :display.config: = ändere den Text im Label Display in eing.get().
    :eing.get(): = Wert aus der Eingabe nehmen.
    :return: Wert zu weiterverarbeitung wiedergeben.
    _______________________________________________________[ENDE]______________________________________________________
    """
    # Bruch 1: Wert aus dem Feld 1.
    z = int(eing_z.get())
    # Wert aus dem Feld 2
    n = int(eing_n.get())

    # Bruch 2: Wert aus dem Feld 1.
    z2 = int(eing_z2.get())
    # Wert aus dem Feld 2
    n2 = int(eing_n2.get())

    # Eingabe vom Operator Entry (Eingabefeld) in Var. Speichern.
    operator = operator_eingabe.get()

    # Bedienung für die Rechenartauswahl.
    if operator == "+":
        ergebnis = Bruch(z, n) + Bruch(z2, n2)
        # Text aus dem Anzeigefeld ändern und als return speichern um wiederzuverwenden.
        return display.config(text=f"Ergebnis: {ergebnis}")

    elif operator == "-":
        # Return-wert aus der Klasse (Also das Ergebnis).
        ergebnis = Bruch(z, n) - Bruch(z2, n2)
        # Text aus dem Anzeigefeld ändern und als return speichern um wiederzuverwenden.
        return display.config(text=f"Ergebnis: {ergebnis}")

    elif operator == "*":
        # Return-wert aus der Klasse (Also das Ergebnis).
        ergebnis = Bruch(z, n) * Bruch(z2, n2)
        # Text aus dem Anzeigefeld ändern und als return speichern um wiederzuverwenden.
        return display.config(text=f"Ergebnis: {ergebnis}")

    elif operator == "/" or ":" :
         ergebnis = Bruch(z, n) / Bruch(z2, n2)
         # Text aus dem Anzeigefeld ändern und als return speichern um wiederzuverwenden.
         return display.config(text=f"Ergebnis: {ergebnis}")


# ___________________________________________________[HAUPTPROGRAMM]___________________________________________________
# Hauptanzeigefeld
win = tk.Tk()               # Object initialisieren
win.title("BRUCH-RECHNER")  # Fenstertitel festlegen
win.geometry("400x300")     # Hauptfenster Größe Festlegen (Par.1 = Breite, Par2 = ""Höhe)
win.maxsize(400, 300)       # Max. Größe Festlegen (Par.1 = Breite, Par2 = ""Höhe)
win.minsize(400, 300)       # Min.e Größe Festlegen (Par.1 = Breite, Par2 = ""Höhe)
win.resizable(True, True)   # Fenster größe Blockieren (Par.1 = Breite, Par2 = ""Höhe)


# Anzeigefeld: Par1: in welchen Fenster. Rest Eigenschaften.
display = tk.Label(win, width=25,height=5,background="black",foreground="red",text="WIllKOMMEN",
                   font=("arial", 20))
display.pack(side="top", fill="both", expand=True)

# Eingabefeld für den Zähler.
eing_z = tk.Entry(win,width=2, background="skyblue", font=("arial black", 20))
eing_z.pack(side="left", expand=False)

# # Eingabefeld für den Nenner.
eing_n = tk.Entry(win, width=2, background="blue", font=("arial black", 20))
eing_n.pack(side="left", expand=False)

# Eingabefeld 2 für den Nenner.
eing_n2 = tk.Entry(win, width=2, background="yellow", font=("arial black", 20))
eing_n2.pack(side="right")

# Eingabefeld 2 für den Zähler.
eing_z2 = tk.Entry(win, width=2, background="red", font=("arial black", 20))
eing_z2.pack(side="right")

# Enter Taste zum absender der eingegebenen Daten.
enter = tk.Button(win, text="BERECHNEN", font=("arial black", 16), background="green", command=eingabe_annahme)
enter.pack(side="bottom")

# Eingabefeld für den Operator.
operator_eingabe = tk.Entry(win, width=1, background="yellow", font=("arial black", 20))
operator_eingabe.pack(side="bottom")


# print(info_pack.__doc__)
# ______________________________[Sobald das Fenster geschlossen wird Programm beenden]_________________________________
try:
    sys.exit(win.mainloop())
except KeyboardInterrupt:
    sys.exit("Programm beendet")