import json

# Pfad zur JSON-Datei für die Highscores
HIGHSCORES_FILE = "highscores.json"

highscores = [
    {"Marc": 3},
    {"Manuel": 8},
    {"Nico": 9},
    {"Ozan": 5},
    {"Raffael": 4}
]

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

def update_highscore(user_name, score):
    # Lade die aktuellen Highscores
    highscores = load_highscores()

    # Füge den neuen Score der Liste hinzu
    highscores.append({user_name: score})

    # Sortiere die Highscores absteigend (bester Score zuerst)
    highscores_sorted = sorted(highscores, key=lambda x: list(x.values())[0], reverse=True)

    # Begrenze die Liste auf die Top 5 Highscores
    highscores_sorted = highscores_sorted[:5]

    # Speichere die neuen Highscores
    save_highscores(highscores_sorted)

    print(f"\033[1;32mHighscore aktualisiert! Dein Name und Score wurden hinzugefügt.\033[0m")

# Funktion für Highscore-Update und Verabschiedung
def game_over():
    global Highscore

    # Spiel-Szenario nach der Runde: Der Spieler hat einen Score
    print(f"\033[1;31mDein Final score ist: {Highscore}\033[0m")

    # Update den Highscore
    update_highscore(user_name, Highscore)

    print("\n\033[1;32mAktualisierte Highscores:\033[0m")
    highscores = load_highscores()
    for entry in highscores:
        for name, score in entry.items():
            print(f"{name}: {score}")

    print("\nDanke für's Spielen! Bis zum nächsten Mal.")

