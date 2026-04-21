from decoupeur import DecoupeMots, DecoupePhrases


def test_decoupemots_fonctionne(texte_test):
    lecteur = DecoupeMots()
    nb_mots = 48
    assert len(lecteur.lecture(texte_test)) == nb_mots

def test_decoupe_phrases_fonctionne(texte_test):
    lecteur = DecoupePhrases()
    assert len(lecteur.lecture(texte_test)) == 2
