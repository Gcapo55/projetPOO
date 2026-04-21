import spacy
import fr_core_news_sm
from corpus import *

nlp = fr_core_news_sm.load()

texte = """
Henry allait au marché à Nice et se baladait au bord du port avec Sophie. Pour que Matthias puisse les rejoindre, il envoya son adresse à sa maman qui habite à Lausanne. C'était Carnaval.
Ils ont fini par rejoindre Jean.
"""

doc = nlp(texte)

personnes = {}
lieux = set()
evenements = set()

for ent in doc.ents:
    if ent.label_ == "PER":
        personnes[ent.text] = Personnage(nom)

    elif ent.label_ in "LOC":
        lieux.add(ent.text)

    elif ent.label_ in "MISC":
        evenements.add(ent.text)

for personne in personnes:
    Personnage(nom)
