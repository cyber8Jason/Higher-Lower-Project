import json
import wikipedia_database

# Pfad zur JSON-Datei für die Highscores
HIGHSCORES_FILE = "highscores.json"
USER_NAME = "TEST"


# Funktion zum Laden der Highscores
def load_highscores():
    try:
        with open(HIGHSCORES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Falls die Datei nicht existiert, starte mit einer leeren Liste


# Funktion zum Speichern der Highscores
def save_highscores(highscores):
    with open(HIGHSCORES_FILE, "w") as file:
        json.dump(highscores, file, indent=4)


def update_highscore(USER_NAME, score):
    # Lade die aktuellen Highscores
    highscores = load_highscores()

    # Füge den neuen Score der Liste hinzu
    highscores.append({USER_NAME: score})

    # Sortiere die Highscores absteigend (bester Score zuerst)
    highscores_sorted = sorted(highscores, key=lambda x: list(x.values())[0], reverse=True)

    # Begrenze die Liste auf die Top 5 Highscores
    highscores_sorted = highscores_sorted[:5]

    # Speichere die neuen Highscores
    save_highscores(highscores_sorted)

    print(f"\033[1;32mHighscore aktualisiert! Dein Name und Score wurden hinzugefügt.\033[0m")


# Liste der Top-Artikel aus der Wikipedia-Datenbank abrufen
TOP_ARTICLES = wikipedia_database.get_top_titles()
# Globale Variable für den HIGHSCORE
HIGHSCORE = 0


def start_screen():
    """
    Zeigt den Begrüßungsbildschirm für das Spiel an.
    Dieser Bildschirm begrüßt den Benutzer und gibt eine kurze Beschreibung des Spiels.
    """
    print("=" * 66)
    print("\033[1;36m*** Hallo User! ***\033[0m")  # Cyan für Titel
    print("\n\033[1;32mWillkommen zu Higher/Lower, dem besten Wikipedia-Spiel!\033[0m")
    print("\n" + "=" * 66)
    print("\nBereite dich auf ein spannendes Spiel vor!")
    print("=" * 66)


def username_input():
    """
    Fordert den Benutzer auf, seinen Namen einzugeben. Wenn der Name leer ist, wird der Benutzer
    erneut zur Eingabe aufgefordert. Sobald ein gültiger Name eingegeben wurde, wird der Benutzer begrüßt.

    Rückgabewert:
        str: Der eingegebene Benutzername.
    """
    print("=" * 66)
    print("\033[1;36mBitte gib deinen Namen ein:\033[0m")
    USER_NAME = input("\033[1;33mName: \033[0m")  # Gelb für die Eingabeaufforderung
    print("=" * 66)
    if USER_NAME.strip() == "":  # Überprüfe, ob der Name leer ist
        print("\033[1;31mDu musst einen Namen eingeben!\033[0m")  # Rot für Fehler
        return username_input()  # Fordert erneut die Eingabe an
    else:
        print(f"\n\033[1;32mWillkommen, {USER_NAME}!\033[0m")  # Begrüßung des Benutzers
    return USER_NAME


def main_menu(USER_NAME):
    """
    Zeigt das Hauptmenü des Spiels an und ermöglicht es dem Benutzer, eine Auswahl zu treffen.
    Der Benutzer kann zwischen folgenden Optionen wählen:
    1. Das Spiel starten
    2. Den Highscore anzeigen
    3. Hilfe anzeigen
    4. Das Programm beenden

    Parameter:
    USER_NAME (str): Der Name des Benutzers, der das Menü aufruft.

    Rückgabewert:
    str: Gibt den nächsten Schritt zurück, basierend auf der Benutzerauswahl:
         - "start_game" zum Starten des Spiels
         - "HIGHSCORE" zum Anzeigen des Highscores
         - "help" für die Hilfe
         - "exit" zum Beenden des Programms
    """
    global HIGHSCORE

    # Druckt die Menüselektion und Eingabeaufforderung
    print("=" * 66)
    print("\n\033[1;36mWas möchtest du tun?\033[0m\n")  # Menüüberschrift
    print("\033[1;33m1.\033[0m Spiel starten")  # Option 1: Spiel starten
    print("\033[1;33m2.\033[0m HIGHSCORE anzeigen")  # Option 2: Highscore anzeigen
    print("\033[1;33m3.\033[0m Hilfe anzeigen")  # Option 3: Hilfe anzeigen
    print("\033[1;33m4.\033[0m Verlassen\033[0m")  # Option 4: Programm beenden
    print("=" * 66)

    # Benutzeraufforderung, eine Auswahl zu treffen (1-4)
    while True:
        user_choice1 = input("\n\033[1;33mBitte triff eine Wahl (1-4): \033[0m")  # Grün für Eingabeaufforderung
        if user_choice1 in ["1", "2", "3", "4"]:
            break
        else:
            # Wenn die Eingabe ungültig ist, wird eine Fehlermeldung angezeigt
            print("\033[1;31mUngültige Auswahl! Bitte gib eine Zahl zwischen 1 und 4 ein: \033[0m")

    print("=" * 66)

    # Wählt den nächsten Schritt basierend auf der Benutzerauswahl
    match user_choice1:
        case "1":
            # Startet das Spiel
            print("\n\033[1;32mDas Spiel wird jetzt gestartet...\033[0m")
            return "start_game"  # Das Spiel wird gestartet
        case "2":
            # Zeigt den Highscore an
            print(f"\n\033[1;32mAktuelle Highscores:\033[0m")
            highscores = load_highscores()
            for entry in highscores:
                for name, score in entry.items():
                    print(f"{name}: {score}")
            return "HIGHSCORE"  # Zurück ins Menü
        case "3":
            # Zeigt Hilfe an
            print("\n\033[1;32mHier ist die Hilfe...\033[0m")
            return "help"  # Zurück ins Menü
        case "4":
            # Beendet das Programm
            print("\n\033[1;31mProgramm wird beendet...\033[0m")  # Rot für "Verlassen"
            return "exit"  # Beenden


def gamemode_menu():
    """
    Zeigt das Menü zur Auswahl des Spielmodus an und ermöglicht dem Benutzer, einen Modus auszuwählen.

    Die Auswahlmöglichkeiten umfassen:
    - Standard-Modus
    - Random-Modus
    - Zeit-Modus
    - Geo-Modus
    - Multiplayer-Modus

    Abhängig von der Auswahl wird der entsprechende Spielmodus gestartet.
    """
    # Anzeige des Menüs zur Auswahl des Spielmodus
    print("=" * 66)
    print("\033[1;36mWähle deinen Spielmodus:\033[0m")  # Cyan für den Titel
    print("\n\033[1;33m1.\033[0m Standard")  # Option 1: Standard-Modus
    print("\033[1;33m2.\033[0m Random")  # Option 2: Random-Modus
    print("\033[1;33m3.\033[0m Zeit-Modus")  # Option 3: Zeit-Modus
    print("\033[1;33m4.\033[0m Geo-Modus")  # Option 4: Geo-Modus
    print("\033[1;33m5.\033[0m Multiplayer")  # Option 5: Multiplayer-Modus
    print("=" * 66)

    # Schleife, um sicherzustellen, dass der Benutzer eine gültige Wahl trifft
    while True:
        # Eingabeaufforderung für den Benutzer zur Auswahl eines Modus
        user_choice2 = input("\n\033[1;33mBitte triff eine Wahl (1-5): \033[0m")

        # Überprüfung, ob die Eingabe eine gültige Zahl (zwischen 1 und 5) ist
        if user_choice2 in ["1", "2", "3", "4", "5"]:
            break  # Schleife verlassen, wenn eine gültige Eingabe gemacht wurde
        else:
            # Hinweis, wenn die Eingabe ungültig ist
            print("\033[1;31mUngültige Auswahl! Bitte gib eine Zahl zwischen 1 und 5 ein: \033[0m")
    print("=" * 66)

    # Auswahl des Spielmodus basierend auf der Benutzereingabe
    match user_choice2:
        case "1":
            print("\n\033[1;32mDu hast den Modus 'Standard' gewählt.\033[0m")
            spielanfang_generieren()  # Initialisiert das Spiel
            standard_spiel_loop()  # Startet den Standard-Spielmodus
        case "2":
            print("\n\033[1;32mDu hast den Modus 'Random' gewählt.\033[0m")
            spielanfang_generieren()  # Initialisiert das Spiel
            random_spiel_loop()  # Startet den Random-Spielmodus
        case "3":
            print("\n\033[1;32mDu hast den Modus 'Zeit-Modus' gewählt.\033[0m")
            spielanfang_generieren()  # Initialisiert das Spiel
            zeit_spiel_loop()  # Startet den Zeit-Modus
        case "4":
            print("\n\033[1;32mDu hast den Modus 'Geo-Modus' gewählt.\033[0m")
            spielanfang_generieren()  # Initialisiert das Spiel
            geo_spiel_loop()  # Startet den Geo-Modus
        case "5":
            print("\n\033[1;32mDu hast den Modus 'Multiplayer' gewählt.\033[0m")
            spielanfang_generieren()  # Initialisiert das Spiel
            multiplayer_spiel_loop()  # Startet den Multiplayer-Modus


def spielanfang_generieren():
    """
    Diese Funktion zeigt die Startnachricht an, wenn das Spiel beginnt.

    Sie gibt eine Reihe von Formatierungen und Nachrichten aus, um den Benutzer auf den Beginn des Spiels vorzubereiten.
    """
    # Anzeige einer Trennlinie zu Beginn des Spiels
    print("=" * 66)

    # Anzeigen der Startnachricht mit mittiger Formatierungen (Cyan für den Titel)
    print("\033[1;36m*" + " " * ((65 - len("DAS SPIEL BEGINNT!")) // 2) + "DAS SPIEL BEGINNT!" + " " * (
            (65 - len("DAS SPIEL BEGINNT!")) // 2) + "*\033[0m")

    # Weitere Trennlinie für visuelle Trennung
    print("=" * 66)

    # Anzeige einer Nachricht: Viel Spaß
    print("\n\033[1;32mViel Spaß beim Spiel! \nDenk daran: Höher oder niedriger!\n \033[0m")

    # Abschließende Trennlinie
    print("=" * 66)


def rundenende_generieren(rundenanzahl, score):
    """
    Diese Funktion zeigt das Ende einer Runde an, einschließlich des aktuellen Scores und der nächsten Runde.

    Args:
    rundenanzahl (int): Die aktuelle Rundenanzahl, die angibt, welche Runde als Nächstes kommt.
    score (int): Der aktuelle Score des Benutzers, der die Anzahl der richtig beantworteten Fragen widerspiegelt.
    """
    # Anzeige einer Trennlinie am Ende der Runde
    print("=" * 66)

    # Erfolgsmeldung in grün, um dem Benutzer zu zeigen, dass er die Runde erfolgreich gemeistert hat
    print("\033[1;32mKorrekt! Du hast die Runde erfolgreich gemeistert!\033[0m")  # Grün für Erfolg

    # Anzeige des aktuellen Scores in Gelb
    print(f"\n\033[1;33mDein neuer Score ist: {score}\033[0m")  # Gelb für Score

    # Weitere Trennlinie zur visuellen Struktur
    print("=" * 66)

    # Anzeige der nächsten Runde in Blau
    print(f"\n\033[1;34mRunde {rundenanzahl} beginnt!\033[0m")  # Blau für die Runde

    # Abschließende Trennlinie für visuelle Struktur
    print("=" * 66)


def standard_spiel_loop():
    """
    Diese Funktion stellt den Ablauf des Spielmodus "Standart" dar, bei dem der Benutzer entscheiden muss,
    welche von zwei Wikipedia-Seiten häufiger aufgerufen wurde.
    Dabei werden die Artikel in einer Kette ausgegeben. Man bekommt Nach jeder Runde einen neuen Artikel.
    Der neue Artikel wird dem zweiten Artikel der Vorrunde gegenübergestellt.

    Der Benutzer wird wiederholt gefragt, welche der beiden Seiten häufiger aufgerufen wurde. Je nach der Auswahl
    des Benutzers wird das Spiel entweder fortgesetzt oder beendet, wenn eine falsche Antwort gegeben wird.
    Der Score und die Rundenanzahl werden nach jeder richtigen Antwort erhöht.

    Es wird auch der Highscore aktualisiert, falls der Benutzer eine höhere Punktzahl erreicht.
    """
    # Initialisiere die Rundenanzahl und den Score des Benutzers
    rundenanzahl = 1
    score = 0

    # Verwende die globale Variable für den Highscore
    global HIGHSCORE
    wiki_name1, wiki_num1 = wikipedia_database.get_random_article(TOP_ARTICLES)

    while True:
        # Generiere zwei zufällige Wikipedia-Artikel und deren Aufrufzahlen
        wiki_name2, wiki_num2 = wikipedia_database.get_random_article(TOP_ARTICLES)

        # Zeige die beiden Artikel an, wobei der zweite Artikel noch unbekannt ist
        print("=" * 66)
        print(f"\n\033[1;35m1. {wiki_name1}: {wiki_num1:,}\n\033[0m")  # Magenta für Artikel
        print(f"\033[1;35m2. {wiki_name2}: ???\n\033[0m")  # Magenta für Artikel
        print("=" * 66)

        # Frage den Benutzer, welche Seite häufiger aufgerufen wurde
        while True:
            user_choice = input(
                "\033[1;33mWelche Seite wurde häufiger aufgerufen?: \033[0m")  # Eingabeaufforderung in Grün
            if user_choice == "1" or user_choice == "2":
                break  # Verlasse die Schleife, wenn eine gültige Eingabe (1 oder 2) gemacht wurde
            else:
                print("\033[1;31mFalsche Eingabe! Tippe (1) oder (2): \033[0m")  # Fehlerhinweis in Rot

        # Zeige die tatsächlichen Aufrufzahlen für beide Artikel
        print(f"\n\033[1;35m1. {wiki_name1}: {wiki_num1:,}\n\033[0m")
        print(f"\033[1;35m2. {wiki_name2}: {wiki_num2:,}\n\033[0m")

        # Überprüfe die Wahl des Benutzers
        if user_choice == "1":  # Der Benutzer hat "1" gewählt (d.h. die erste Seite war häufiger)
            if wiki_num1 > wiki_num2:
                # Erhöhe die Rundenanzahl und den Score, wenn die Wahl richtig war
                rundenanzahl += 1
                score += 1
                wiki_name1, wiki_num1 = wiki_name2, wiki_num2
                rundenende_generieren(rundenanzahl, score)  # Zeige das Ergebnis der Runde an
            else:
                # Fehlerbehandlung bei falscher Antwort
                print("\033[1;31mFalsch! Die Zahl ist nicht höher.\033[0m")  # Fehlerhinweis in Rot
                print(f"\033[1;31mDein Finalscore ist: {score}\033[0m")
                print(f"\033[1;31mHIGHSCORE: {HIGHSCORE}\033[0m")
                HIGHSCORE = max(HIGHSCORE, score)  # Setze den Highscore, wenn der neue Score höher ist
                update_highscore(USER_NAME, score)  # Aktualisiere den Highscore
                break  # Beende das Spiel bei falscher Antwort
        elif user_choice == "2":  # Der Benutzer hat "2" gewählt (d.h. die zweite Seite war häufiger)
            if wiki_num1 < wiki_num2:
                # Erhöhe die Rundenanzahl und den Score, wenn die Wahl richtig war
                rundenanzahl += 1
                score += 1
                wiki_name1, wiki_num1 = wiki_name2, wiki_num2
                rundenende_generieren(rundenanzahl, score)  # Zeige das Ergebnis der Runde an
            else:
                # Fehlerbehandlung bei falscher Antwort
                print("\033[1;31mFalsch! Die Zahl ist nicht niedriger.\033[0m")  # Fehlerhinweis in Rot
                print(f"\033[1;31mDein Finalscore ist: {score}\033[0m")
                print(f"\033[1;31mHIGHSCORE: {HIGHSCORE}\033[0m")
                HIGHSCORE = max(HIGHSCORE, score)  # Setze den Highscore, wenn der neue Score höher ist
                update_highscore(USER_NAME, score)  # Aktualisiere den Highscore
                break  # Beende das Spiel bei falscher Antwort


def random_spiel_loop():
    """
    Diese Funktion stellt den Ablauf des Spielmodus "Random" dar, bei dem der Benutzer entscheiden muss,
    welche von zwei Wikipedia-Seiten häufiger aufgerufen wurde.

    Der Benutzer wird wiederholt gefragt, welche der beiden Seiten häufiger aufgerufen wurde. Je nach der Auswahl
    des Benutzers wird das Spiel entweder fortgesetzt oder beendet, wenn eine falsche Antwort gegeben wird.
    Der Score und die Rundenanzahl werden nach jeder richtigen Antwort erhöht.

    Es wird auch der Highscore aktualisiert, falls der Benutzer eine höhere Punktzahl erreicht.
    """
    # Initialisiere die Rundenanzahl und den Score des Benutzers
    rundenanzahl = 1
    score = 0

    # Verwende die globale Variable für den Highscore
    global HIGHSCORE

    while True:
        # Generiere zwei zufällige Wikipedia-Artikel und deren Aufrufzahlen
        wiki_name1, wiki_num1 = wikipedia_database.get_random_article(TOP_ARTICLES)
        wiki_name2, wiki_num2 = wikipedia_database.get_random_article(TOP_ARTICLES)

        # Zeige die beiden Artikel an, wobei der zweite Artikel noch unbekannt ist
        print("=" * 66)
        print(f"\n\033[1;35m1. {wiki_name1}: {wiki_num1:,}\n\033[0m")  # Magenta für Artikel
        print(f"\033[1;35m2. {wiki_name2}: ???\n\033[0m")  # Magenta für Artikel
        print("=" * 66)

        # Frage den Benutzer, welche Seite häufiger aufgerufen wurde
        while True:
            user_choice = input(
                "\033[1;33mWelche Seite wurde häufiger aufgerufen?: \033[0m")  # Eingabeaufforderung in Grün
            if user_choice == "1" or user_choice == "2":
                break  # Verlasse die Schleife, wenn eine gültige Eingabe (1 oder 2) gemacht wurde
            else:
                print("\033[1;31mFalsche Eingabe! Tippe (1) oder (2): \033[0m")  # Fehlerhinweis in Rot

        # Zeige die tatsächlichen Aufrufzahlen für beide Artikel
        print(f"\n\033[1;35m1. {wiki_name1}: {wiki_num1:,}\n\033[0m")
        print(f"\033[1;35m2. {wiki_name2}: {wiki_num2:,}\n\033[0m")

        # Überprüfe die Wahl des Benutzers
        if user_choice == "1":  # Der Benutzer hat "1" gewählt (d.h. die erste Seite war häufiger)
            if wiki_num1 > wiki_num2:
                # Erhöhe die Rundenanzahl und den Score, wenn die Wahl richtig war
                rundenanzahl += 1
                score += 1
                rundenende_generieren(rundenanzahl, score)  # Zeige das Ergebnis der Runde an
            else:
                # Fehlerbehandlung bei falscher Antwort
                print("\033[1;31mFalsch! Die Zahl ist nicht höher.\033[0m")  # Fehlerhinweis in Rot
                print(f"\033[1;31mDein Finalscore ist: {score}\033[0m")
                print(f"\033[1;31mHIGHSCORE: {HIGHSCORE}\033[0m")
                HIGHSCORE = max(HIGHSCORE, score)  # Setze den Highscore, wenn der neue Score höher ist
                update_highscore(USER_NAME, score)  # Aktualisiere den Highscore
                break  # Beende das Spiel bei falscher Antwort
        elif user_choice == "2":  # Der Benutzer hat "2" gewählt (d.h. die zweite Seite war häufiger)
            if wiki_num1 < wiki_num2:
                # Erhöhe die Rundenanzahl und den Score, wenn die Wahl richtig war
                rundenanzahl += 1
                score += 1
                rundenende_generieren(rundenanzahl, score)  # Zeige das Ergebnis der Runde an
            else:
                # Fehlerbehandlung bei falscher Antwort
                print("\033[1;31mFalsch! Die Zahl ist nicht niedriger.\033[0m")  # Fehlerhinweis in Rot
                print(f"\033[1;31mDein Finalscore ist: {score}\033[0m")
                print(f"\033[1;31mHIGHSCORE: {HIGHSCORE}\033[0m")
                HIGHSCORE = max(HIGHSCORE, score)  # Setze den Highscore, wenn der neue Score höher ist
                update_highscore(USER_NAME, score)  # Aktualisiere den Highscore
                break  # Beende das Spiel bei falscher Antwort


def zeit_spiel_loop():
    print("TO DO")


def geo_spiel_loop():
    print("TO DO")


def multiplayer_spiel_loop():
    print("TO DO")


def game_over():
    """
    Zeigt den "Game Over"-Bildschirm mit ASCII-Art an und wartet auf eine Eingabe des Benutzers,
    um das Spiel zu beenden oder fortzufahren.

    Dieser Bildschirm enthält:
    - Eine ASCII-Art-Darstellung des Texts "GAME OVER".
    - Eine Nachricht, die dem Spieler für das Spielen dankt.
    - Eine Eingabeaufforderung, um mit der Tasteneingabe fortzufahren.
    """
    # ASCII-Art für den Game Over-Bildschirm
    game_over_art = """
    GGGGG   AAAAA   M   M   EEEEE    OOO   V   V  EEEEE  RRRRR
    G       A   A   MM MM   E       O   O  V   V  E      R   R
    G  GG   AAAAA   M M M   EEEE    O   O  V   V  EEEE   RRRRR
    G   G   A   A   M   M   E       O   O   V V   E      R  R
    GGGGG   A   A   M   M   EEEEE    OOO     V    EEEEE  R   R
    """

    # Ausgabe des Game Over-Bildschirms
    print("=" * 66)
    print("\033[1;31m" + game_over_art + "\033[0m")  # Rote Farbe für GAME OVER ASCII Art
    print("=" * 66)

    # Dankesnachricht an den Spieler
    print("\n\033[1;32mDanke fürs Spielen! Deine Reise endet hier.\033[0m")  # Grüner Text für Dankeschön
    print("\033[1;33mDrücke Enter, um fortzufahren...\033[0m")  # Gelber Text für Eingabeaufforderung

    # Wartet auf die Eingabe des Spielers, um fortzufahren oder zu beenden
    input()  # Erwartet eine Eingabe des Spielers (Enter-Taste)

    print("=" * 66)  # Trennlinie zur Visualisierung


def main():
    """
    Die Hauptfunktion des Spiels, die den Ablauf des Spiels steuert. Sie zeigt den Startbildschirm an,
    fordert den Benutzer zur Eingabe eines Benutzernamens auf und zeigt dann das Hauptmenü an.
    Je nach Auswahl des Benutzers führt sie zu den verschiedenen Spielmodi, zeigt den Highscore an,
    gibt Hilfestellungen oder beendet das Spiel.

    Die Funktion läuft in einer Endlosschleife, die nur durch die Auswahl 'exit' vom Benutzer beendet wird.
    """

    global USER_NAME

    # Zeigt den Startbildschirm des Spiels an
    start_screen()

    # Fordert den Benutzer auf, einen Benutzernamen einzugeben
    USER_NAME = username_input()

    # Hauptspiel-Loop, der das Menü und die Spieloptionen steuert
    while True:
        # Zeigt das Hauptmenü an und speichert die Auswahl des Benutzers
        choice = main_menu(USER_NAME)

        # Wenn der Benutzer das Spiel beenden möchte, bricht die Schleife ab
        if choice == "exit":
            break  # Das Spiel wird beendet

        # Wenn der Benutzer das Spiel starten möchte, öffnet das Auswahlmenü für den Spielmodus
        elif choice == "start_game":
            gamemode_menu()  # Zeigt das Menü zur Auswahl des Spielmodus
            game_over()  # Zeigt das Ende des Spiels (kann an das Ende des Spiels angepasst werden)

        # Wenn der Benutzer den Highscore sehen möchte, bleibt er im Menü
        elif choice == "HIGHSCORE":
            # Hier könnte der Highscore angezeigt werden, aber danach geht es zurück zum Menü
            continue  # Wieder zurück ins Menü

        # Wenn der Benutzer Hilfe anfordert, wird das Hilfemenü angezeigt
        elif choice == "help":
            # Hier kann Hilfe angezeigt werden, aber danach geht es zurück ins Menü
            continue  # Wieder zurück ins Menü


if __name__ == "__main__":
    main()
