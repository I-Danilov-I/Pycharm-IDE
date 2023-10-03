import cv2
import numpy as np
import pyautogui
import mss


def erkennung():
    # Bildschirmaufnahme erstellen
    with mss.mss() as sct:
        screenshot = sct.shot(output='screenshot.png')

    # Laden Sie das aufgenommene Bild
    image = cv2.imread('screenshot.png')

    # Ziel-Farbwert, den Sie suchen möchten (im BGR-Format)
    target_color = (0, 0, 255)  # Zum Beispiel Rot

    # Konvertieren Sie das Bild in den HSV-Farbraum (Hue, Saturation, Value)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Definieren Sie den Farbbereich für den Ziel-Farbwert im HSV-Farbraum
    lower_color = np.array([0, 50, 50])  # Untere Grenze
    upper_color = np.array([10, 255, 255])  # Obere Grenze

    # Erstellen Sie eine Maske, um nur die Farbpixel im Farbbereich zu behalten
    mask = cv2.inRange(hsv_image, lower_color, upper_color)

    # Suchen Sie nach Konturen in der Maske
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        # Berechnen Sie den Schwerpunkt des größten gefundenen Bereichs (Kontur)
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            target_x = int(M["m10"] / M["m00"])
            target_y = int(M["m01"] / M["m00"])
            print(f"Position des Farbpunkts: ({target_x}, {target_y})")

            # Zeichnen Sie ein Kreuz an der Position des Farbpunkts auf dem aufgenommenen Bild
            cv2.drawMarker(image, (target_x, target_y), (0, 255, 0), markerType=cv2.MARKER_CROSS, markerSize=20,
                           thickness=2)

            # Bild mit markiertem Farbpunkt anzeigen
            cv2.imshow("Image with Cross", image)

            # Zur übersicht wo sich der gefundene Farbpunkt befindet
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Koordinaten des Farbpunktes
            return [target_x, target_y]

    else:
        print("Farbpunkt nicht gefunden.")

