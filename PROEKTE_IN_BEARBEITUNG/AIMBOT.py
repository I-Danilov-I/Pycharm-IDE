import cv2
import numpy as np
import mss
from pynput import mouse
import pyautogui

# Variable zur Verfolgung des Mauszustands
right_mouse_pressed = False

def on_click(x, y, button, pressed):
    """
    Callback-Funktion, die aufgerufen wird, wenn eine Maustaste gedrückt oder losgelassen wird.

    :param x: Die X-Koordinate des Mausklicks.
    :param y: Die Y-Koordinate des Mausklicks.
    :param button: Die gedrückte Maustaste (left, right, middle).
    :param pressed: Ein Boolean-Wert, der angibt, ob die Maustaste gedrückt wurde (True) oder losgelassen wurde (False).
    """
    global right_mouse_pressed
    if button == mouse.Button.right:
        right_mouse_pressed = pressed

def anvisieren(x, y):
    """
    Bewegt die Maus zur angegebenen Position.

    :param x: Die X-Koordinate, zu der die Maus bewegt werden soll.
    :param y: Die Y-Koordinate, zu der die Maus bewegt werden soll.
    """
    pyautogui.moveTo(x, y, duration=0.5)  # duration: Dauer der Bewegung anpassen

def erkennung():
    """
    Hauptfunktion zur Erkennung und Steuerung der Mausposition.
    Diese Funktion überwacht die rechte Maustaste und bewegt die Maus zur Position eines orangefarbenen Punkts.
    """
    with mss.mss() as sct:
        monitor = sct.monitors[0]
        while True:
            # Überprüfen Sie, ob die rechte Maustaste gedrückt wurde
            if right_mouse_pressed:
                # Bildschirmbild aufnehmen
                screenshot = np.array(sct.grab(monitor))

                # Konvertieren Sie das aufgenommene Bild in den HSV-Farbraum
                hsv_image = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)

                # Definieren Sie den Farbbereich für Orange im HSV-Farbraum
                lower_orange = np.array([5, 50, 50])  # Untere Grenze für Orange in HSV
                upper_orange = np.array([15, 255, 255])  # Obere Grenze für Orange in HSV

                # Erstellen Sie eine Maske, um nur die orangefarbenen Pixel zu behalten
                mask = cv2.inRange(hsv_image, lower_orange, upper_orange)

                # Suchen Sie nach Konturen in der Maske
                contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                if len(contours) > 0:
                    # Berechnen Sie den Schwerpunkt des größten gefundenen Bereichs (Kontur)
                    largest_contour = max(contours, key=cv2.contourArea)
                    M = cv2.moments(largest_contour)
                    if M["m00"] != 0:
                        target_x = int(M["m10"] / M["m00"])
                        target_y = int(M["m01"] / M["m00"])
                        print(f"Position des orangefarbenen Punkts: ({target_x}, {target_y})")
                        anvisieren(target_x, target_y)

# Mausklick-Listener initialisieren
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# Starten Sie die Haupterkennungsfunktion
erkennung()
