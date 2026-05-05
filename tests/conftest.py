import pytest
from spacy.tokens import Doc
"""Ce fichier permet de configurer des fixtures
qui seront réutilisées dans tous les fichiers de test"""

from importateur import Texte
import Lecteur
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
        " particulièrement émus."
        " C'est aussi le cas de Pablo.", 1869
    )

@pytest.fixture
def analyseur(doc_test):
    instance = AnalyseTexte()
    instance.analyser(doc_test, 1)
    return instance

@pytest.fixture
def doc_test(texte_test) -> Doc:
    """Retourne un Doc analysé par spacy"""
    return spacy_conv(texte_test)

@pytest.fixture
def dico_perso(analyseur) :
    return analyseur.personnages

@pytest.fixture
def dico_lieux(analyseur) :
    return analyseur.lieux

