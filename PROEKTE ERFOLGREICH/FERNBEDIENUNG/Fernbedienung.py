# Klasse RemoteControl definieren.
class RemoteControl:
    # Konstruktor
    def __init__(self):
        # Dictionary: zum Speichern der Programmsender.
        self.__programs = {}
        # TV-Programmnummer
        self.__num = 0
        # Volumen
        self.__volumen = 10


    # Methode: Sender in Dictionary hinzufügen. Par1=TV-ProgNr, Par2=Programmname.
    def set(self, num, name):
        if num in self.__programs:
            num =+ 1
        self.__programs[num] = name
        return "Nr.", self.__num, ":", self.__programs.get(self.__num)


    # Methode: Sender umschalten. Par=TV-ProgNr Return=Ausgewählter sender aus dem Dictionary.
    def schalten(self, num):
        try:
            num = int(num)
            self.__num = num
            if self.__num < 1:
                self.__num = 1

            if num > 100:
                self.__num = 100
                return "Nr.", self.__num, ":", "Max 100 Sender"
            elif num > len(self.__programs):
                return "Nr.", self.__num, ":", "Platz Leer"
            elif num <= len(self.__programs):
                return "Nr.", self.__num, ":", self.__programs.get(self.__num)

        except ValueError:
            return "Eingabe nicht erkannt!"


    # Methode: Sender in 1 Schritten vorwärts umschalten.
    def pfeil_oben(self):
        # Aktuelle ProgNr. + 1 rechnen
        self.__num += 1

        # Wenn größer als 100 ist, stelle sender Nr. 1 (Senderwechsel Vorwärts )
        if self.__num > 100:
            self.__num = 1

        # Wenn nummer größer ist als die Länge der Programme, gebe den leeren Programmplatz zurück.
        if self.__num > len(self.__programs):
            return "Nr.", self.__num, ":", "Platz Leer"

        # Wenn nichts zutrifft, gebe den Sender aus.
        else:
            return "Nr.", self.__num, ":", self.__programs.get(self.__num)


    # Methode: Sender in 1 Schritten rückwärts umschalten.
    def pfeil_unten(self):
        # Aktuelle ProgNr. - 1 rechnen
        self.__num -= 1

        # Wenn kleiner als 1 ist, stelle sender Nr. 100 (Senderwechsel Rückwärts )
        if self.__num < 1:
            self.__num = 100

        # Wenn nummer größer ist als die Länge der Programme, gebe den leeren Programmplatz zurück.
        if self.__num > len(self.__programs):
            return "Nr.", self.__num, ":", "Platz Leer"

        # Wenn nichts zutrifft, gebe den Sender aus.
        else:
            return "Nr.", self.__num, ":", self.__programs.get(self.__num)


    # Methode: Laustärke erhöhen
    def vol_plus(self):
        if self.__volumen > 50:
            self.__volumen = 50
            return self.__volumen
        else:
            self.__volumen += 1
            return self.__volumen


    # Methode: Laustärke verringer
    def vol_minus(self):
        if self.__volumen < 1:
            self.__volumen = 0
            return self.__volumen
        else:
            self.__volumen -= 1
            return self.__volumen


    # Programm Bibliothek ausgeben
    def zeige_tv_prog(self):
        return self.__programs




# Klasse RemoteControl instanziieren.
RC = RemoteControl()

# _______________________________________________[ HAUPTPROGRAMM ]_____________________________________________________
# Methodenaufruf: Sender hinzufügen.
RC.set(1, "Das Erste")
RC.set(2, "ZDF")
RC.set(3, "CHANNEL Tree")
RC.set(4, "DOKU")
RC.set(5, "KIKA")
RC.set(6, "NICK-TV")
RC.set(7, "RTL")
RC.set(8, "ARD")
RC.set(9, "DMAX")
RC.set(10, "MUSIK")


# __________________________________________________[ AUSGABE ]________________________________________________________
# # Sender automatisch hinzufügen, wenn dieser nicht existiert.
# prog_num = 0
# for i in range(1, 10):
#     prog_num += 1
#     if prog_num in RC.zeige_tv_prog():
#         print("Platz:", prog_num, "ist vergeben.")
#     else:
#         RC.set(prog_num, "Name")


# # Programmbibliothek ausgeben
# print(RC.zeige_tv_prog())

# Ausgabe Konstruktor
# print(RC.__dict__)
