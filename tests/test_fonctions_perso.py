from fonction_perso import trouver_attributs


def test_trouver_attributs_fonctionne(doc_test, liste_perso):
    """Teste que la fonction trouver_attributs retourne une liste d'adjectifs"""
    dico_attributs = {perso.nom : trouver_attributs(perso.nom, doc_test) for perso in liste_perso}
    assert len(dico_attributs) == len (liste_perso)
