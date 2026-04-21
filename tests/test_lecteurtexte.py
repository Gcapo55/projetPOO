from importateur import Texte
from lecteurtexte import DecoupeMots

TexteTest = Texte("Le Bon, la Brute et le Truand", "Joseph Morrington",
                  """Le Bon a vu la Brute et le Truand s'entretuer""", 1957)

def test_decoupemots_fonctionne():
    lecteur = DecoupeMots()
    nb_mots = 11
    assert len(lecteur.lecture(TexteTest)) == nb_mots
