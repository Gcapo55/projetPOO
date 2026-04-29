from collections import Counter, defaultdict

from spacy.tokens import Doc

from utils import nettoyer

def trouver_attributs(nom: str, doc : Document, lst_words: list[words]) -> list:
    liste_compl = [
             nettoyer(word.lemma) for word in lst_words
             if lst_words[word.head].text == nom and word.deprel == "amod"
         ]
    return [att for att, _ in Counter(liste_compl).most_common(3)]

# def trouver_genre():
