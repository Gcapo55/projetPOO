import pytest
from fonction_perso import trouver_attributs


@pytest.mark.parametrize

def test_fonctions_perso_fonctionne(doc_test, liste_perso):
    analyseur = AnalyseurPersonnages(liste_perso, doc_test)
    dico_attributs = analyseur.trouver_attributs()
    assert len(dico_attributs) == len (dico_perso)
