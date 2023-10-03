import cv2
import numpy as np
import mss

def erkennung():
    # Bildschirmaufnahme erstellen
    with mss.mss() as sct:
        sct.shot(output='screenshot.png')

    # Laden Sie das aufgenommene Bild
    image = cv2.imread('screenshot.png')

    # Konvertieren Sie das Bild in den HSV-Farbraum
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

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

            # Zeichnen Sie ein Kreuz an der Position des orangefarbenen Punkts auf dem aufgenommenen Bild
            cv2.drawMarker(image, (target_x, target_y), (0, 255, 0), markerType=cv2.MARKER_CROSS, markerSize=20,
                           thickness=2)

            # Erstellen Sie ein OpenCV-Fenster mit der Bildschirmauflösung
            cv2.namedWindow('Vollbild', cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('Vollbild', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

            # Zeigen Sie das Bild im Vollbildmodus an
            cv2.imshow('Vollbild', image)

            # Zur Übersicht, wo sich der gefundene orangefarbene Punkt befindet
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Koordinaten des orangefarbenen Punkts
            return [target_x, target_y]

    else:
        print("Orangefarbener Punkt nicht gefunden.")
        return False
