from colorama import Fore, Back, Style

print(f"{Fore.BLACK}{Back.LIGHTYELLOW_EX}[---Generator einer Bewerbung für eine Wohnung---]{Style.RESET_ALL}\n")
import re

jaeingabe = ("Ja", "J", "j", "ja", "Y", "y", "Yes", "yes", "ye", "yeh")
neineingabe = ("Nein", "nein", "N", "n", "nö", "No", "N", "n", "Nop", "ne", "Ne")

# Namen Eingabe
while True:
    name = input("Bitte geben Sie ihren Familiennamen ein: ")
    vorname = input("Jetzt ihren Vornamen: ")
    if not re.match("^[A-Za-züÖöÜäÄ ]*$", name or vorname):
        print(f"{Fore.BLACK}{Back.RED}[Der Name darf keine Zahlen oder Sonderzeichen haben!]"
              f"{Style.RESET_ALL}")
    else:
        break

# Geschlecht Abfrage
while True:
    mann = ("m", "M", "Herr", "Mann", "Männlich", "männlich", "menlich", "Menlich")
    frau = ("w", "W", "Frau", "frau", "weiblich", "Weiblich", "weib")
    geschlecht = input("Bitte geben Sie ihr geschlecht mit [M] oder [W] ein:"
                       f" ")
    if geschlecht in mann:
        anrede = "Herr"
        break
    elif geschlecht in frau:
        anrede = "Frau"
        break
    else:
        print(f"{Fore.BLACK}{Back.RED}Falsche Eingabe{Style.RESET_ALL}")

# Uhrzeit abfrage (Muss verbessert werden!)
while True:
    try:
        uhrzeit = int(input("Bitte geben sie die Tagesstunde ein (zb. 17): "))
        if 0 <= uhrzeit < 9:
            grus = "Guten Morgen"
            break
        elif 9 <= uhrzeit < 17:
            grus = "Guten Tag"
            break
        elif 17 <= uhrzeit < 24:
            grus = "Guten Abend"
            break
        else:
            print(f"{Fore.BLACK}{Back.RED}Falsche Eingabe{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.BLACK}{Back.RED}Nur Zahlen erlaubt{Style.RESET_ALL}")
print("\n")
print(grus, anrede, name + "!\n")
print(f"{Fore.LIGHTYELLOW_EX}{Back.BLACK}Für eine gute Bewerbung brauchen wir ein paar Eingaben von ihnen.\n"
      f"In weniger als 3 Minuten ist deine Bewerbung Fertig! {Style.RESET_ALL}\n")

# Alter Abfrage
while True:
    try:
        age = int(input("Bitte geben sie ihr alter an: "))
        if 90 > age > 18:
            print(f"{Fore.LIGHTYELLOW_EX}{Back.BLACK}Weiter Gehts!{Style.RESET_ALL}")
            break
        elif age > 90:
            abfrage = input("Möchten sie wirklich in diesem Alter noch umziehen?: ")
            if abfrage in jaeingabe:
                print(f"Okay dann weiter gehts {Fore.BLACK}{Back.GREEN} HARD MANN 4.0! {Style.RESET_ALL}")
                break
            elif abfrage in neineingabe:
                print("Ok dann einen schönen Abend noch!")
                print("Programmende")
                break
        elif age < 18:
            abfragejung = input("Du bist ziemlich jung sicher, dass du Umziehen willst? ")
            if abfragejung in jaeingabe:
                print(f"Na gut {Fore.BLACK}{Back.GREEN} SEHR MUTIG! {Style.RESET_ALL} Versuchen wir es!)")
                break
            elif abfragejung in neineingabe:
                print("Ok bis bald junger Mann!")
                print("Programmende")
                break
            else:
                print(f"{Fore.BLACK}{Back.RED}Antworte mit [Ja] oder [Nein]{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.BLACK}{Back.GREEN}Opps da ist was schief gelaufen!{Style.RESET_ALL}")

# Datenbank


# Berufsstatus Abfrage
while True:
    try:
        statusfrage = input("Sin sie Berufstätig?: ")
        if statusfrage in jaeingabe:
            print("Weiter gehts!")
            job = input("Sie Arbeit als....>: ")
            betrieb = input("Bitte geben sie den Namen ihrer Firma ein: ")
            einkommen = int(input("Bitte geben sie ihr gesamt Einkommen ein: "))
            break
        elif statusfrage in neineingabe:
            print(f"{Back.BLACK}{Fore.YELLOW}Kein Thema! Ich formuliere es geschickt "
                  f"und es wird dir nicht im Weg stehen;){Style.RESET_ALL}")
            break
        else:
            print("Falsche eingabe! Antwort bitte mit [j] oder [n]")
    except ValueError:
        print("Falsche Eingabe")

# Personen Anzahl
while True:
    try:
        personen = int(input("Personenanzahl: "))
        break
    except ValueError:
        print("Falsche Eingabe, kein Text oder Zeichen erlaubt!")

# Einzugsdatum
while True:
    einzugsdatum = input("Bitte geben sie ihr frühstes Einzugsdatum in diesem Format ein [  xx.xx.xxxx  ]: ")
    if not re.match("^[0-9.:]*$", einzugsdatum):
        print("Falsche Eingabe!")
    else:
        pass
        break


def statusfragefunktion():
    while True:
        if statusfrage in jaeingabe:
            print("Zurzeit arbeite ich als", job, "bei der Firma", betrieb + ".")
            print("Derzeit beträgt das Gesamteinkommen", einkommen, "€.")
            break
        elif statusfrage in neineingabe:
            print("Zurzeit beziehe ich Leistungen von Arge was für Vermieter immer zum Vorteil ist! \n"
                  "Das bietet ihnen mehr Sicherheit, weil das Geld ohne umweg und von einer stattlichen \n"
                  "Einrichtung und nicht von einer Privat person auf ihr Konto ohne umwege überwiesen wird.")
            break
        else:
            print("Falsche Eingabe, antworte mit [j] oder [n]")


def personen_abfrage():
    while True:
        try:
            if personen > 1:
                print("Insgesamt sind wir", personen, "Personen und ab dem", einzugsdatum, "einzugsbereit.")
                print("Auf einen Besichtigungstermin würde wir uns riesig freuen!")
                print("Mit freundlichen Grüßen,")
                print(vorname, name)
                break
            elif personen <= 1:
                print("Ich bin alleinstehend und ab dem", einzugsdatum, "einzugsbereit.")
                print("Auf einen Besichtigungstermin würde ich mich sehr freuen!")
                print("Mit freundlichen Grüßen,")
                print(vorname, name)
                break
            else:
                print("Oops da ist was schiefgelaufen")
        except ValueError:
            print("Nur Zahlen erlaubt!")


print("\n")
print(f"{Fore.LIGHTYELLOW_EX}{Back.BLACK}---[Deine Bewerbung fertig!]---{Style.RESET_ALL}")
print("\n")
print("Sehr geehrte Damen und Herren,"
      "\nmein name ist " + name, vorname, "und ich bin", age, "Jahre alt.")
statusfragefunktion()
personen_abfrage()
