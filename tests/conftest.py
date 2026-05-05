import pytest
from spacy.tokens import Doc
"""Ce fichier permet de configurer des fixtures
qui seront réutilisées dans tous les fichiers de test"""

from importateur import Texte
from Lecteur import AnalyseTexte
from utils import spacy_conv

@pytest.fixture
def texte_test() -> Texte:
    return Texte(
        "20'000 lieux sous les mers", "Jules Verne",
        "Le brave Ned Land alla à Paris. Il y rencontra le soir venu,"
        "Mr Aronnax. Malgré le froid terrible qui faisait grelotter le pauvre"
        "Ned Land - L'hiver de 1864 était particulièrement rigoureux - il se"
        "sentait réchauffé par la présence de son ami, le sympathique Mr Aronnax",
        "1869"
    )


@pytest.fixture
def doc_test(texte_test) -> Doc:
    """Retourne un Doc analysé par spacy"""
    return spacy_conv(texte_test)

@pytest.fixture
def liste_perso(doc_test) :
    """Retourne une liste des personnages d'un Doc"""
    resultat = AnalyseTexte()
    resultat.analyser(doc_test, 1)
    return resultat.personnages


@pytest.fixture
def liste_lieux(doc_test) :
    """Retourne une liste des lieux d'un Doc"""
    resultat = AnalyseTexte()
    resultat.analyser(doc_test, 1)
    return resultat.lieux

