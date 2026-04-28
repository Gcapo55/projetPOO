"""Module to install spaCy"""

import subprocess

def install_spacy():

    """Demande à l'utilisateur s'il veut installer spaCy, et si oui l'installe"""

    rep = input("Souhaitez-vous installer SpaCy et son extension française (nécessaire au fonctionnement du programme) Y/N ? ").strip().lower()

    if rep == "n":
        return

    if rep == "y":
        try:
            print("Installation de spaCy...\n")

            subprocess.check_call(["python", "-m", "pip", "install", "spacy"])

            print("\nInstallation du modèle français...\n")

            subprocess.check_call(["python", "-m", "spacy", "download", "fr_core_news_sm"])

            print("\nInstallation terminée :)")

        except subprocess.CalledProcessError:
            print("\nÉchec de l'installation :(")

        input("\nAppuyer sur 'Enter' pour continuer")

install_spacy()
