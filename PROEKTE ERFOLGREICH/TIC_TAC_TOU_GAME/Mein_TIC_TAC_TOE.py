### [ --- Tic Tac Toe ---]

### [--- Import ---]
import time
from colorama import Back, Fore
from pynput import keyboard


### [--- Variablen ----]
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]       # Eine Liste (Wert veränderbar)
derzeitiger_spieler = "Spieler_X"
boardeingabe = " "
player_1_name = " "
player_2_name = " "


### Einleitung
def einleitung():
    global player_1_name
    global player_2_name
    print("---[TIC TAC TOU]---                               ---[EINLEITUNG]---")
    print("   -------------                       Die Eingabe erfolg über die zugewiesen Zahlen")
    print("   | 1 | 2 | 3 |                       wie links in der Tabelle zu sehen ist!")
    print("   |-----------|                       Beispiel: drücken sie die Zahl [5] und bestätigen mit [ENTER]")
    print("   | 4 | 5 | 6 |                       Ein [X] oder ein [O] wird das Feld 5 platziert. Der Spieler der")
    print("   |-----------|                       als erstes 3 Zeichen Waagerecht, Diagonal oder Horizontal")
    print("   | 7 | 8 | 9 |                       positioniert, hat gewonnen.")
    print("   _____________\n")


    player_1_name = input("Spieler 1 Bitte geben sie einen Nickname ein: ")
    player_2_name = input("Spieler 2 Bitte geben sie einen Nickname ein: ")


### Steuerung durch benutzer durch direkte Tasteneingabe ohne Bestätigung mit Enter
def spiel_start_benutzer_eingabe():
    zeahler = 1
    while True:
        print(f"Drücke [Q] um das Spiel zu starten oder [E] um zu beenden!: ")
        time.sleep(1.5)
        with keyboard.Events() as events:
            event = events.get()
            if event.key == keyboard.KeyCode.from_char("Q") or event.key == keyboard.KeyCode.from_char("q"):
                print("")
                break
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


### Zeichnet das Spielfeld
def feld_zeichen():
    print("")
    print('┌───┬───┬───┐')
    print(f'│ {board[0]} │ {board[1]} │ {board[2]} │')
    print('├───┼───┼───┤')
    print(f'│ {board[3]} │ {board[4]} │ {board[5]} │')
    print('├───┼───┼───┤')
    print(f'│ {board[6]} │ {board[7]} │ {board[8]} │')
    print('└───┴───┴───┘')


### Prüft auf korrekte Eingabe, wechselt automatisch den Spieler, fügt den eingegebenen Namen ein
def eingabe_anfordern_prufen_wechseln():
    global derzeitiger_spieler
    while True:
        try:
            if derzeitiger_spieler == "Spieler_X":
                eingabe = int(input(f"{player_1_name} wohin möchtest du setzen?: "))
                eingabe = eingabe - 1
            else:
                eingabe = int(input(f"{player_2_name} wohin möchtest du setzen?: "))
                eingabe = eingabe - 1

            if eingabe <= 0 or eingabe >= 9:
                pass
            if board[eingabe] == "X":
                print(f"Dieses Feld hat {player_1_name} besetzt!")
            elif board[eingabe] == "O":
                print(f"Dieses Feld hat {player_2_name} besetzt!")
            else:
                pass
                if derzeitiger_spieler == "Spieler_X":
                    board[eingabe] = "X"
                    derzeitiger_spieler = "Spieler_O"
                    break
                elif derzeitiger_spieler == "Spieler_O":
                    board[eingabe] = "O"
                    derzeitiger_spieler = "Spieler_X"
                    break
        except IndexError:
            print("Nur Zahlen von 1 - 9 Zulässig!")
        except ValueError:
            print("Es sind nur Zahlen als Eingabe erlaubt!")


### Überprüft, ob sich 3 gleiche Zeichen waagerecht, diagonal un senkrecht befinden
def uberprufe_gewinnier():
    ## Gewinner Ausgabe Spieler 1 [X]
    if "X" == board[0] == board[1] == board[2]:
        feld_zeichen()
        print(f"HERZLICHEN GLÜCKWUNSCH {player_1_name}!!!\n"
              f"Du hast Gewonnen!!!")
        exit()
    elif "X" == board[3] == board[4] == board[5]:
        feld_zeichen()
        print(f"{Back.BLACK}HERZLICHEN GLÜCKWUNSCH {player_1_name}!!!\n"
              f"Du hast Gewonnen!!!")
    elif "X" == board[6] == board[7] == board[8]:
        feld_zeichen()
        print(f"HERZLICHEN GLÜCKWUNSCH {player_1_name}!!!\n"
              f"Du hast Gewonnen!!!")
        exit()

    elif "X" == board[0] == board[3] == board[4]:
        feld_zeichen()
        print(f"HERZLICHEN GLÜCKWUNSCH {player_1_name}!!!\n"
              f"Du hast Gewonnen!!!")
        exit()
    elif "X" == board[1] == board[4] == board[7]:
        feld_zeichen()
        print(f"HERZLICHEN GLÜCKWUNSCH {player_1_name}!!!\n"
              f"Du hast Gewonnen!!!")
        exit()
    elif "X" == board[2] == board[5] == board[8]:
        feld_zeichen()
        print(f"HERZLICHEN GLÜCKWUNSCH {player_1_name}!!!\n"
              f"Du hast Gewonnen!!!")
        exit()
    elif "X" == board[0] == board[4] == board[8]:
        feld_zeichen()
        print(f"HERZLICHEN GLÜCKWUNSCH {player_1_name}!!!\n"
              f"Du hast Gewonnen!!!")
        exit()
    elif "X" == board[2] == board[4] == board[6]:
        feld_zeichen()
        print(f"HERZLICHEN GLÜCKWUNSCH {player_1_name}!!!\n"
              f"Du hast Gewonnen!!!")
        exit()



    ## Gewinner Ausgabe Spieler 1 [X]
    if "O" == board[0] == board[1] == board[2]:
        feld_zeichen()
        print(f"HERZLICHEN GLÜCKWUNSCH {player_2_name}!!!\n"
              f"Du hast Gewonnen!!!")
        exit()
    elif "O" == board[3] == board[4] == board[5]:
        feld_zeichen()
        print(f"HERZLICHEN GLÜCKWUNSCH {player_2_name}!!!\n"
              f"Du hast Gewonnen!!!")
        exit()
    elif "O" == board[6] == board[7] == board[8]:
        feld_zeichen()
        print(f"HERZLICHEN GLÜCKWUNSCH {player_2_name}!!!\n"
              f"Du hast Gewonnen!!!")
        exit()

    elif "O" == board[0] == board[3] == board[4]:
        feld_zeichen()
        print(f"HERZLICHEN GLÜCKWUNSCH {player_2_name}!!!\n"
              f"Du hast Gewonnen!!!")
        exit()
    elif "O" == board[1] == board[4] == board[7]:
        feld_zeichen()
        print(f"HERZLICHEN GLÜCKWUNSCH {player_2_name}!!!\n"
              f"Du hast Gewonnen!!!")
        exit()
    elif "O" == board[2] == board[5] == board[8]:
        feld_zeichen()
        print(f"HERZLICHEN GLÜCKWUNSCH {player_2_name}!!!\n"
              f"Du hast Gewonnen!!!")
        exit()
    elif "O" == board[0] == board[4] == board[8]:
        feld_zeichen()
        print(f"HERZLICHEN GLÜCKWUNSCH {player_2_name}!!!\n"
              f"Du hast Gewonnen!!!")
        exit()
    elif "O" == board[2] == board[4] == board[6]:
        feld_zeichen()
        print(f"HERZLICHEN GLÜCKWUNSCH {player_2_name}!!!\n"
              f"Du hast Gewonnen!!!")
        exit()

    ## Unentschieden
    else:
        feld_voll_check()


### Prüft, ob das Feld Voll ist, indem das bord auf leerstring geprüft wird
def feld_voll_check():
    if " " not in board:
        feld_zeichen()
        print(f"{Back.BLACK}{Fore.RED}Herzlichen Glückwunsch!\n"
              "Wir haben zwei Gewinner!\n"
              "Gratulation an", player_1_name, "und", player_2_name, "\n"
              "oder es ist Unentschieden,\n"
              f"aber das klärt mal unter euch.)")
        exit()


### [--- Hauptprogramm ---]
try:
    einleitung()
    spiel_start_benutzer_eingabe()
    while True:
        feld_zeichen()
        eingabe_anfordern_prufen_wechseln()
        uberprufe_gewinnier()
        feld_voll_check()
except (TypeError, KeyboardInterrupt):
    print("\n")
    print("[Programm wurde über python beendet]")
