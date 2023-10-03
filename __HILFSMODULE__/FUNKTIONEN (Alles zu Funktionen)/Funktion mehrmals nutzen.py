# """---[ Import ]---"""
import re
from colorama import Fore, Back, Style

# """---[ Dictionary ]---"""
daten_liste = {}

# """---[ Variablen ]---"""
signal_freigabe = True


# """---[ Funktionen ]---"""
def funktion_prufe_eingabe_of_A_Z(eingabe_buchstaben):
    global signal_freigabe
    if not re.match("^[A-Za-züÖöÜäÄ]*$", eingabe_buchstaben):
        print(f"{Fore.BLACK}{Back.RED}[Der Name darf keine Zahlen oder Sonderzeichen haben!]"
              f"{Style.RESET_ALL}")
    else:
        print("Weiter")
        signal_freigabe_eingabe = False
        return eingabe_buchstaben


def funktion_prufe_eingabe_of_Zahlen(eingabe_zahlen):
    global signal_freigabe
    if eingabe_zahlen < 18 or eingabe_zahlen > 80:
        print(f"{Fore.BLACK}{Back.RED}[Nur alter zwischen 18 - 80 zugeselhasen!]"
              f"{Style.RESET_ALL}")
    else:
        print("Weiter")
        signal_freigabe_eingabe = False
        return eingabe_zahlen


# """---[ Hauptprogramm ]---"""
while signal_freigabe:
    daten_liste["Familienname"] = funktion_prufe_eingabe_of_A_Z(eingabe_buchstaben=str(input("Bitte geben sie ihren "
                                                                                             "Familiennamen ein: ")))
signal_freigabe = True

while signal_freigabe:
    daten_liste["Vorname"] = funktion_prufe_eingabe_of_A_Z(eingabe_buchstaben=str(input("Bitte geben sie ihre"
                                                                                        " Vornamen eingaben: ")))
signal_freigabe = True

while signal_freigabe:
    try:
        daten_liste["Alter"] = funktion_prufe_eingabe_of_Zahlen(eingabe_zahlen=int(input("Bitte geben sie ihr "
                                                                                         "Alter ein: ")))
    except ValueError:
        print(f"{Fore.BLACK}{Back.RED}[Nur Zahlen als Eingabe zugelassen!]"
              f"{Style.RESET_ALL}")
signal_freigabe = True


# """---[ Ausgabe ]---"""
print("\n-------------------------------------------[Ausgabe]--------------------------------------------------")
print(daten_liste)
