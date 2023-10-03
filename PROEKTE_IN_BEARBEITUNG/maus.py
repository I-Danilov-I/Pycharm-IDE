import pyautogui


def anvisieren(x, y):
    pyautogui.moveTo(x, y)  # Ziehen Sie die Maus zur neuen Position (400, 400)

    # Linksklick an der aktuellen Mausposition
    pyautogui.leftClick()
