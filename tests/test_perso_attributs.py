from perso_attributs import AnalyseurPersonnages

def test_perso_attributs_fonctionne(doc_test, dico_perso):
    analyseur = AnalyseurPersonnages(dico_perso, doc_test)
    dico_attributs = analyseur.trouver_attributs()
    assert len(dico_attributs) == len (dico_perso)
