# Erlaubt es Dateien inter Windowsverzeichnis zu verschieben
import shutil


# Von diesem Verzeichnis verschieben (Source path)
source = "C:/Users/A.Danilov/Desktop/Informatik/01_AnwP-Phyton_Teichert_Wilfried/My_Python/Phython_Umgebung" \
		"/My_Scripts/Dateien in einen Ordner unter Windows " \
		"verschieben/Daueraufträge.pdf"

# Zu diesem Verzeichnis verschieben (Destination path)
destination = "C:/Users/A.Danilov/Desktop/Neuer Ordner2"

# Funktion mit entsprechenden parameter aufrufen
dest = shutil.move(source, destination, copy_function=shutil.copytree)
