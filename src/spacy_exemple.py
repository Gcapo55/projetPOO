import spacy
import fr_core_news_sm

nlp = fr_core_news_sm.load()

texte = """
Henry allait au marché à Nice et se baladait au bord du port avec Sophie. Pour que Matthias puisse les rejoindre, il envoya son adresse à sa maman qui habite à Lausanne. C'était Carnaval.
Ils ont fini par rejoindre Jean.
"""

doc = nlp(texte)

personnes = set()
lieux = set()
evenements = set()

for ent in doc.ents:
    if ent.label_ == "PER":
        personnes.add(ent.text)

    elif ent.label_ in "LOC":
        lieux.add(ent.text)

    elif ent.label_ in "MISC":
        evenements.add(ent.text)

print("Personnes :", personnes)
print("Lieux :", lieux)
print("Événements :", evenements)