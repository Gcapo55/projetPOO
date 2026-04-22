import pytest
from importateur import Texte

"""Ce fichier permet de configurer des fixtures
qui seront réutilisées dans tous les fichiers de test"""

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
