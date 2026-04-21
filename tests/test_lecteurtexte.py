from src.projetpoo.lecteurtexte import DecoupeMots
from src.projetpoo.texte import Texte
import pytest
@pytest.fixture
def texte_test() -> Texte:
    t = Texte(
        "20'000 lieux sous les mers",
        "L'année 1866 fut marquée par un événement bizarre, un phénomène "
        "inexpliqué et inexplicable que personne n'a sans doute oublié.",
    )
    return t

def test_decoupemots_fonctionne(texte_test):
    lecteur = DecoupeMots()
    assert len(lecteur.lecture(texte_test)) == 21


#test_decoupemots_fonctionne()
