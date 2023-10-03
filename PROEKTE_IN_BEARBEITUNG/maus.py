import pyautogui


def anvisieren(x, y):
    # Ziehen Sie die Maus zur neuen Position (400, 400)
    pyautogui.moveTo(x, y, duration=2.0)  # duration: Dauer der Bewegung anpassen
    
