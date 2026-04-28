"""FICHIER DE FONCTION UTILITAIRES"""
import spacy
from spacy.tokens import Doc

from importateur import Texte


def spacy_conv(texte : Texte) -> Doc :
    """
    Cette fonction a pour but de créer un objet Doc, qui est un objet utilisable
    avec les fonctions spacy. Cela permet de ne pas recréer le même objet dans
    chacun de nos fichiers d'analyse
    """
    nlp = spacy.load("fr_core_news_lg")
    return nlp(texte.contenu)
