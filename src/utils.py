"""FICHIER DE FONCTION UTILITAIRES"""
import spacy

# import stanza
from importateur import Texte

# stanza.download("fr")

def spacy_conv(texte : Texte) -> Doc :
    """
    Cette fonction a pour but de créer un objet Doc, qui est un objet utilisable
    avec les fonctions spacy. Cela permet de ne pas recréer le même objet dans
    chacun de nos fichiers d'analyse
    """
    nlp = spacy.load("fr_core_news_lg")
    # nlp = stanza.Pipeline("fr")
    return nlp(texte.contenu)
