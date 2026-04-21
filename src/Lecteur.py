import spacy
import fr_core_news_sm
from corpus import *

nlp = fr_core_news_sm.load()

texte = """
Henry allait au marché à Nice et se baladait au bord du port avec Sophie. Pour que Matthias puisse les rejoindre, il envoya son adresse à sa maman qui habite à Lausanne. C'était Carnaval.
Ils ont fini par rejoindre Jean.
"""

doc = nlp(texte)

personnages = {}
lieux = {}
    
for ent in doc.ents:
    if ent.label_ == "PER":
        nom = ent.text
        if nom not in personnages:
            personnages[nom] = Personnage(nom)
        personnages[nom].compter()
        
    elif ent.label_ in ["LOC", "GPE"]:
        nom = ent.text
        if nom not in lieux:
            lieux[nom] = Lieu(nom)
        lieux[nom].compter()

for p in personnages:
    print(p)
