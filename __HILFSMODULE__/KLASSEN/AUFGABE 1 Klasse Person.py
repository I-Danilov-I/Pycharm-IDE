# ---------------------------------------------------------------------------------------------------------------------
# 1. Klasse Person: Es ist die Klasse Person zu erstellen.
# Als Attribute besitzt sie Vorname, Name, Geburtsdatum und Wohnort, sowie eine Methode
# für die Namensänderung (name_aendern) und die Wohnort änderung (umziehen).
# Die Attribute sind als „private“ zu definieren, sodass der Zugriff von außerhalb der Klasse
# nicht erfolgen kann (z.B. p.name = "Lehmann" ist dann nicht gültig)
# ---------------------------------------------------------------------------------------------------------------------
# Modul zum durchsuchen nach
import re

# Modul zum Interagieren mit OS
import sys


# Klasse erstellen: Klassen sind Baupläne, wie soll etwas aussehen.
class Person:
    # Definieren Eigenschaften (Attribute, wie etwas aussehen soll).
    # Doppelter Unterstrich = Private Variable = Zugriff nur über die Klassen Methode
    def __init__(self, vorname, name, geburt, ort):
        """
        Beim Erzeugen eines Objekts wird für dieses ein eigener Satz von Instanz attributen angelegt. Diese Erzeugung
        und Initialisierung wird in einer speziellen Methode durchgeführt, dem Konstruktor.
        Der Konstruktor wird in Python durch die Kopfzeile: def __init__(self) definiert.
        """
        self.__vorname = vorname
        self.__name = name
        self.geburt = geburt
        self.__ort = ort


    # Methode zu Namensänderung über die Methode Direkt
    def namen_bearbeiten(self):
        while True:
            print("Zum beenden taste [Q] eingeben.")
            self.__vorname = input("Bitte geben sie Ihren Namen ein: ")
            print("-"*100)

            if self.__vorname.upper() == "Q":
                sys.exit("Programm Ende.")

            if not re.match("^[A-Za-z]*$", self.__vorname):
                print("Der Name darf nur Buchstaben erhalten! \n")

            else:
                print("Vorname erfolgreich eingetragen! \n")
                return self.__vorname


    # Methode zu Namensänderung über Console input
    def ort_bearbeiten(self):
        while True:
            print("Zum beenden taste [Q] eingeben.")
            self.__ort = input("Bitte geben sie Ihren Wohnort ein: ")
            print("-"*100)

            if self.__ort.upper() == "Q":
                sys.exit("Programm Ende.")

            if not re.match("^[A-Za-z]*$", self.__ort):
                print("Der ORT darf nur Buchstaben erhalten! \n")

            else:
                print("Wohnort erfolgreich eingetragen! \n")
                return self.__ort


# ------------------------------------------------[ HAUPTPROGRAMM ]---------------------------------------------------
# Objekt nach der Klasse (Bauplan) erzeugen
person1 = Person("Alex", "Wall", 1993, "Hille")
person2 = Person("Felix", "Sturm", 1990, "Berlin")


# Eigenschaften von Objekt als Dictionary ausgeben
print("Before:", person1.__dict__)
print("Before:", person2.__dict__)
print("_"*125)


# Methode zu Namensänderung ausführen
person1.namen_bearbeiten()


# Methode zu Ortsänderung ausführen über Console input
person2.ort_bearbeiten()


# Eigenschaften als Dictionary ausgeben
print("After:", person1.__dict__)
print("After:", person2.__dict__)
