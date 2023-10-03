# Klasse RemoteControl definieren
class RemoteControl:
    # Konstruktor-Methode
    def __init__(self, num):
        self.__programs = []

        for i in range(0,num):
            self.__programs.append("Prog"+str(i))

        # aktuelle Programmnummer (Index) als privates Attribut
        self.__curr_program_number = 0

    # Methode zum Ausgeben des Objektes
    def __str__(self):
        return str(self.__programs)

    # Methode zum Setzen des Programmnamen
    def set_program_name(self, number, name):
        program_pool = ["CNN", "NDR", "WDR", "BBC"]
        # Index
        if number <= len(self.__programs):
            # Name
            if name in program_pool:
               self.__programs[number] = name
            else:
              print(name, "Ungültiger Name.")
        else:
            print(number, "Ungültiger Index.")

    # Methode zum Lesen des Programmnamens
    def get_program_name(self):
        return self.__programs[self.__curr_program_number]

    # Methode für den Programmwechsel nach oben
    def next_program(self):
        self.__curr_program_number += 1

    # Methode für den Programmwechsel nach unten
    def last_program(self):
        self.__curr_program_number -= 1

    def volumen(self):
        pass

r = RemoteControl
