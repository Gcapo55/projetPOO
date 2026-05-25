"""
Classe InstallateurSpacy qui vérifie la présence de spaCy au démarrage et propose à
l'utilisateur de l'installer ainsi que le modèle français fr_core_news_lg si nécessaire.
"""

import importlib.util
import subprocess
import sys


class InstallateurSpacy:
    """Classe permettant d'installer spaCy et son modèle français"""
    @staticmethod
    def install_spacy() -> None:
        """Installe spaCy seulement s'il n'est pas déjà installé"""

        # 1. Vérifie si spaCy est déjà installé
        if importlib.util.find_spec("spacy") is not None:
            return

        # 2. Demande à l'utilisateur s'il veut l'installer
        rep = input(
            "Souhaitez-vous installer SpaCy et son modèle français "
            "(nécessaire au fonctionnement du programme) Y/N ? "
        ).strip().lower()

        if rep != "y":
            return

        # 3. Installe spaCy
        try:
            print("Installation de spaCy...\n")

            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "spacy"
            ])

            print("\nInstallation du modèle français...\n")

            subprocess.check_call([
                sys.executable, "-m", "spacy", "download", "fr_core_news_lg"
            ])

            print("\nInstallation terminée :)")

        except subprocess.CalledProcessError:
            print("\nÉchec de l'installation :(")

        input("\nAppuyer sur 'Entrée' pour continuer")

InstallateurSpacy.install_spacy()
