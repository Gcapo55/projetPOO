"""Module pour installer spaCy"""

import subprocess
import sys


def install_spacy():
    """Installe spaCy seulement s'il n'est pas déjà installé"""

    # 1. Vérifier si spaCy est déjà installé
    try:
        import spacy
        return
    except ImportError:
        pass

    # 2. Demande utilisateur
    rep = input(
        "Souhaitez-vous installer SpaCy et son modèle français "
        "(nécessaire au fonctionnement du programme) Y/N ? "
    ).strip().lower()

    if rep != "y":
        return

    # 3. Installation
    try:
        print("Installation de spaCy...\n")

        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "spacy"
        ])

        print("\nInstallation du modèle français...\n")

        subprocess.check_call([
            sys.executable, "-m", "spacy", "download", "fr_core_news_sm"
        ])

        print("\nInstallation terminée :)")

    except subprocess.CalledProcessError:
        print("\nÉchec de l'installation :(")

    input("\nAppuyer sur 'Entrée' pour continuer")

install_spacy()
