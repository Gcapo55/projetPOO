from collections import Counter

from spacy.tokens import Doc, Token

from utils import nettoyer


def check_attribut(N: str, tok: Token, doc: Doc) -> str | None:
    """fonction qui utilise les tags de spacy pour vérifier
    qu'il s'agit d'un adjectif"""
    nom = N.split(" ")
    if tok.text not in nom and tok.head.text not in nom:
        return None
    if tok.text in nom:
        if (
            tok.dep_ == "appos"
            and tok.head.pos_ == "ADJ"
            or tok.dep_ == "nsubj"
            and tok.head.pos_ == "ADJ"
        ):
            return tok.head.lemma_

        elif tok.dep_ == "appos" and doc[tok.i - 1].pos_ == "ADJ":
            return doc[tok.i - 1].lemma_

        else:
            return None

    elif tok.head.text in nom and tok.dep_ == "amod":
        return tok.lemma_

    else:
        return None


def trouver_attributs(nom: str, doc: Doc) -> list[str]:
    """Détermine les 3 adjectifs les plus associés à chaque personnage"""
    liste_compl = [
        nettoyer(result)
        for token in doc
        if (result := check_attribut(nom, token, doc)) is not None
    ]

    return [att for att, _ in Counter(liste_compl).most_common(3)]


def trouver_genre(nom: str, doc: Doc) -> str | None:
    """Détermine le genre d'un personnage"""
    liste_compl = [
        "".join(token.morph.get("Gender", [])) for token in doc if token.text in nom
    ]
    if liste_compl:
        return Counter(liste_compl).most_common(1)[0][0]

    return None
