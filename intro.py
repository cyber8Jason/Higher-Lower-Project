import wikipedia
import random
import json

def start_screen():
      print("*** Hallo User! ***\nWillkommen zu Higher/Lower, dem besten Wikipedia Spiel!")


def username_input():
      user_name = input("Gib deinen Namen ein: ")
      return user_name


def main_menu_start(user_name):
      print(f"\nHallo {user_name}.\nWas willst du tun?\n"
            f"\n1. Spiel starten"
            f"\n2. Highscore"
            f"\n3. Hilfe"
            f"\n4. Verlassen")

      user_choice1 = input("\nBitte treffe eine Wahl:\n")
      match user_choice1:
            case "1":
                  print("\nDas Spiel wird geladen...")
            case "2":
                  print("\nDein Highscore ist: ...")
            case "3":
                  print("\nHilfe wird angezeigt...")
            case "4":
                  print("\nProgramm wird beendet...")
            case  _:
                  print("\nUngültige Auswahl. Bitte versuche es erneut.")


def gamemode_menu():
      print(f"Folgende Spielmodi sind verfügbar:\n"
            f"\n1. Standard"
            f"\n2. Geo-Modus"
            f"\n3. Zeit-Modus"
            f"\n4. Random"
            f"\n5. Multiplayer")

      user_choice2 = input("\nBitte treffe eine Wahl:\n")
      match user_choice2:
            case "1":
                  print(f"\nDu hast den Modus 'Standard' gewählt.\n"
                  f"Das Spiel beginnt!")
            case "2":
                  print(f"\nDu hast den Modus 'Geo-Modus' gewählt.\n"
                  f"Das Spiel beginnt!")
            case "3":
                  print(f"\nDu hast den Modus 'Zeit-Modus' gewählt.\n"
                  f"Das Spiel beginnt!")
            case "4":
                  print(f"\nDu hast den Modus 'Random' gewählt.\n"
                  f"Das Spiel beginnt!")
            case "5":
                  print(f"\nDu hast den Modus 'Multiplayer' gewählt.\n"
                  f"Das Spiel beginnt!")


def game_over():
      print("\nDanke für's Spielen! Bis zum nächsten Mal.")


def main():
      start_screen()
      user_name = username_input()
      main_menu_start(user_name)
      gamemode_menu()
      game_over()


if __name__ == "__main__":
      main()
