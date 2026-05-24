import pytest


@pytest.mark.parametrize (("nom_perso", "genre"), [
    (["Ned Land", "Mr Aronnax"],
    ["Masc", "Fem", ""]),
])

def test_fonctions_perso_fonctionne(liste_perso, nom_perso, genre) :
    for p in liste_perso:
        assert p.nom in nom_perso
        assert p.genre in genre
