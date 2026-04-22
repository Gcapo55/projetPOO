from decoupeur import DecoupeMots, DecoupePhrases


def test_decoupemots_fonctionne(texte_test):
    lecteur = DecoupeMots()
    nb_mots = 51
    assert len(lecteur.lecture(texte_test)) == nb_mots

def test_decoupe_phrases_fonctionne(texte_test):
    lecteur = DecoupePhrases()
    nb_phrases = 2
    assert len(lecteur.lecture(texte_test)) == nb_phrases
