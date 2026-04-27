import spacy
from lecteur import AnalyseTexte

nlp = spacy.load("fr_core_news_lg")
nlp.add_pipe("sentencizer", before="parser")

texte = """
"Le 3 mai 1815 à 14h30, Napoléon quitta Paris."
"Le 14 juillet à midi, la fête commença à Lyon."
"Le 21 janvier 1793 à 10:00, Louis XVI fut exécuté à Paris."
"""

doc = nlp(texte)

analyse = AnalyseTexte(doc)
analyse.analyser()

print("=== Personnages ===")
for p in analyse.personnages.values():
    p.afficher()

print("=== Lieux ===")
for l in analyse.lieux.values():
    l.afficher()

print("=== Événements ===")
for e in analyse.evenements.values():
    e.afficher()