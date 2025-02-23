import os
import sys
import time

def show_doge():
    doge_art = """
    ░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░
    ░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░
    ░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░
    ░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░
    ░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░
    ░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░ 
    ░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░
    ░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░
    ░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░
    ░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░
    ▐▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░
    ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
    ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░
    ░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░
    ░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░░
    ░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░░
    ░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░░
    ░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░░
    ░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░
    """
    for i in range(200):
        print(f"Durchlauf {i + 1}:")
        print(doge_art)
    input("Drücke Enter zum Beenden...")

# Prüfe, ob das Skript direkt oder als Unterprozess gestartet wurde
if len(sys.argv) == 1:  # Erster Start
    # Öffne 10 Fenster
    for _ in range(35):
        # Starte die .exe selbst in einem neuen Fenster
        os.system(f'start "" "{sys.executable}" "{__file__}" child')
        time.sleep(0.1)  # Kurze Pause zwischen den Fenstern
else:  # Als "child" gestartet
    show_doge()  # Zeige die 200 Wiederholungen