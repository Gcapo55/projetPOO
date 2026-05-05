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
        "L'année 1866 fut marquée par un événement bizarre, un phénomène"
        " inexpliqué et inexplicable que personne n'a sans doute oublié. Sans parler"
        " des rumeurs qui agitaient les populations des ports et surexcitaient l'esprit"
        " public à l'intérieur des continents les gens de mer furent"
        " particulièrement émus.", 1869
    )


@pytest.fixture
def doc_test(texte_test) -> Doc:
    """Retourne un Doc analysé par spacy"""
    return spacy_conv(texte_test)

@pytest.fixture
def liste_perso(doc_test) :
    """Retourne une liste des personnages d'un Doc"""
    resultat = AnalyseTexte()
    resultat.analyser(doc_test)
    return resultat.personnages


@pytest.fixture
def liste_lieux(doc_test) :
    """Retourne une liste des lieux d'un Doc"""
    resultat = AnalyseTexte()
    resultat.analyser(doc_test)
    return resultat.lieux

