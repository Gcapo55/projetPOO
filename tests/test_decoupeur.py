from decoupeur import DecoupeMots, DecoupePhrases

"""Tests des Découpeurs, utilisation de la fixture doc_test de conftest.py"""


def test_decoupemots_fonctionne(doc_test):
    lecteur = DecoupeMots()
    nb_mots = 53
    assert len(lecteur.lecture(doc_test)) == nb_mots


def test_decoupe_phrases_fonctionne(doc_test):
    lecteur = DecoupePhrases()
    nb_phrases = 2
    assert len(lecteur.lecture(doc_test)) == nb_phrases
