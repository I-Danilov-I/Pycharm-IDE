
### Steuerung durch benutzer durch direkte Tasteneingabe ohne Bestätigung mit Enter
import time
from pynput import keyboard


def spiel_start_benutzer_eingabe():
    zeahler = 1
    while True:
        print("Drücke [Q] um das Spiel zu starten oder [E] um zu beenden!: ")
        with keyboard.Events() as events:
            event = events.get()
            if event.key == keyboard.KeyCode.from_char("Q") or event.key == keyboard.KeyCode.from_char("q"):
                print("hft")

            elif event.key == keyboard.KeyCode.from_char("E") or event.key == keyboard.KeyCode.from_char("e"):
                print("")
                print("Spiel wird beendet...")
                time.sleep(3)
                exit("[Spiel wurde verlassen!]")

            else:
                print("Eingabe wird überprüft...\n")
                time.sleep(3)
                print("Falsche Eingabe!\n")
                zeahler = zeahler + 1
                if zeahler == 4:
                    print("Spiel wird beendet...\n   ")
                    time.sleep(3)
                    exit("[Spiel wurde verlassen]")
                    break

