# Modul zum Interagieren mit PDF
from PyPDF2 import PdfReader

# Öffne PDf mit PDF Reader
reader = PdfReader("A.pdf")
# Definiere die Seite die geöffnet werden soll
page = reader.pages[6]
# Extrahiere den TExt
text = page.extract_text()
# Splitte den TExt immer da wo ein Leerzeichen ist
text = text.split(",")


# Schreibe den Text Zeilenweise in eine Datei als txt Format
datei = open("T.txt", "w")
for i in text:
    datei.writelines(i.replace('\'', "\n"))
datei.close()


# Zeilen als einzelne Listen in eine Liste speichern
LISTE = []
datei = open("T.txt", "r")
for i in datei:
    LISTE.append(i.split())
datei.close()



# Definiere neue Listen für die Zuordnung der Termine zu den jeweiligen Monaten
JANUAR = []
FEBRUAR = []
MARZ = []

# Liste Zeilenweise SSortiert zu den Monaten hinzufügen
for L in LISTE:
    JANUAR.append(L[0])
    FEBRUAR.append([1])
    FEBRUAR.append([2])


print("Januar")
for i in range(len(JANUAR)):
    if "Di03Papier" in JANUAR:
        print(f"Index: {i}=", JANUAR[i])