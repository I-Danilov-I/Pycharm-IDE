import webbrowser

# Link zu Webseite in Variablen gespeichert
url_klassenraum = "https://inspire.vitero.de/login"
url_online_bucher = "https://bibox2.westermann.de/shelf"
url_musik = "https://www.youtube.com/watch?v=tDqfI1Yz4VI&list=RDp1Aj8cri2VA&index=9"

# Funktion zu Browser Auswahl aufrufen("Speicherort der EXE Datei") und zu aufrufen in Variable ablegen. %s = Pfad Ende
firefox = webbrowser.get("C:/Program Files/Mozilla Firefox/firefox.exe %s")
opera_gx = webbrowser.get("C:/Users/A.Danilov/AppData/Local/Programs/Opera GX/opera.exe %s")
google_chrome = webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s")

# Eine STANDART_URL mit dem in der Variable festgelegtem Browser öffnen
firefox.open(url_online_bucher)
opera_gx.open(url_musik)
google_chrome.open(url_klassenraum)
