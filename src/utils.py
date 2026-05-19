"""FICHIER DE FONCTION UTILITAIRES"""
import spacy
import time
from spacy.tokens import Doc

from importateur import Texte


def spacy_conv(texte : Texte) -> Doc :
    """
    Cette fonction a pour but de créer un objet Doc, qui est un objet utilisable
    avec les fonctions spacy. Cela permet de ne pas recréer le même objet dans
    chacun de nos fichiers d'analyse
    """
    nlp = spacy.load("fr_core_news_lg")
    nlp.add_pipe("sentencizer", before="parser")
    return nlp(nettoyer(texte.contenu))

def nettoyer(txt: str) -> str :
    """supprime les artefacts comme sauts de ligne, underscores,..."""
    return (
        txt.replace("\n", " ").replace("_", "").replace("--", "")
    )

def patienter() -> None:
    """Affiche une animation de chargement dans la console."""
    print("Patientez", end="", flush=True)

    for _ in range(3):
        time.sleep(0.2)
        print(".", end="", flush=True)

    print()
