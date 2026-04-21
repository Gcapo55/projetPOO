from lecteurtexte import DecoupeMots, DecoupePhrases
from importateur import Texte
import pytest
@pytest.fixture
def texte_test() -> Texte:
    t = Texte(
        "20'000 lieux sous les mers", "Jules Verne",
        "L'année 1866 fut marquée par un événement bizarre, un phénomène"
        " inexpliqué et inexplicable que personne n'a sans doute oublié. Sans parler"
        " des rumeurs qui agitaient les populations des ports et surexcitaient l'esprit"
        " public à l'intérieur des continents les gens de mer furent particulièrement émus.", 1869
    )
    return t

def test_decoupemots_fonctionne(texte_test):
    lecteur = DecoupeMots()
    assert len(lecteur.lecture(texte_test)) == 48

def test_decoupe_phrases_fonctionne(texte_test):
    lecteur = DecoupePhrases()
    assert len(lecteur.lecture(texte_test)) == 2


#test_decoupemots_fonctionne()
