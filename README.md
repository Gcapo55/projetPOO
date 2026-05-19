# Extracteur d'Ontologie de Narration (version 0.1)


## UTILISATION

- indiquer si installation de spacy souhaitée
- télécharger fichier depuis Projet Gutenberg en Plain Text
- indiquer chemin et nom du fichier texte à importer


## Fonctionnalités du programme

- lire un texte importé
- reconnaître les éléments ontologiques présents dans le texte selon leur catégorie (Personnage, Lieu, Événement)
- reconnaître les attributs éventuels pour chaque élément
- exporter proprement ces éléments et leurs attributs respectifs dans un fichier .csv


## Création du programme

- Ce programme a été réalisé dans le cadre du cours Programmation orientée objet : Python (SP26)
- Il est le fruit d'une collaboration de cinq étudiants, Clémence Detroyat, Gianni Caporizzo, Nathan Kunz, Guilherme Meireles Pereira et Timoté Sarrasin

## Diagrammes UML de classe

```mermaid
classDiagram
    class Corpus {
        +str nom
        +int occurrences
        +compter() void
    }

    class Personnage {
        +list[str] attributs
        +str genre
    }

    class Lieu {
        +str categorie
    }

    class Evenement {
        +str date
        +str heure
        +Lieu lieu
        +list[Personnage] participants
        +__str__() str
    }

    Corpus <|-- Personnage
    Corpus <|-- Lieu
    Corpus <|-- Evenement
    Evenement --> Lieu : lieu
    Evenement --> Personnage : participants

    class Texte {
        -_titre: str
        -_auteur: str
        -_annee: str
        +contenu: str
        +__str__() str
        +titre() str
        +auteur() str
        +annee() str
    }

    class ChargeurTexte {
        +charger(source: str) Texte
    }

    ChargeurTexte --> Texte : creates

    class AnalyseTexte {
        -personnages: list[Personnage]
        -lieux: list[Lieu]
        -evenements: list[Evenement]
        -_liste_noms_perso: list[str]
        -_liste_noms_lieux: list[str]
        +analyser(doc: Doc, min_occ: int) void
        -_ajouter_personnage(nom: str, doc: Doc) void
        -_ajouter_lieu(nom: str) void
        -_ajouter_events(doc: Doc) void
    }

    AnalyseTexte --> Personnage : creates
    AnalyseTexte --> Lieu : creates
    AnalyseTexte --> Evenement : creates

    class Exportateur {
        +ExporterPersonnages() void
        +ExporterLieux() void
        +ExporterEvenements() void
    }

    class Pipeline {
        -source: str
        -_chargeur: ChargeurTexte
        -_finder: AnalyseTexte
        -_exportateur: Exportateur
        +executer() void
    }

    Pipeline --> ChargeurTexte
    Pipeline --> AnalyseTexte
    Pipeline --> Exportateur

    class Utils {
        +spacy_conv(texte: Texte) Doc
        +nettoyer(txt: str) str
        +patienter() void
    }

    class InstallateurSpacy {
        +install_spacy() void
    }

    class fonction_perso {
        +trouver_attributs(nom: str, doc: Doc) list
        +trouver_genre(nom: str, doc: Doc) str
    }

    class fonctions_evenement {
        +trouver_date(texte: str) str
        +trouver_heure(texte: str) str
        +trouver_lieu(texte: str, liste_lieux: list[Lieu]) Lieu
        +trouver_participants(texte: str, liste_perso: list[Personnage]) list[Personnage]
    }
```

## Diagramme de séquence

```mermaid
sequenceDiagram
    participant User
    participant Pipeline
    participant Installateur as InstallateurSpacy
    participant Chargeur as ChargeurTexte
    participant FS as Filesystem
    participant TexteObj as Texte
    participant Utils
    participant spaCy
    participant Analyse as AnalyseTexte
    participant FP as fonction_perso
    participant FE as fonctions_evenement
    participant Corpus
    participant Exporteur

    User->>Pipeline: run python pipeline.py
    activate Pipeline

    Pipeline->>Installateur: import installation_spacy
    alt spaCy not installed
        Installateur->>User: prompt to install spaCy and fr_core_news_lg
        User-->>Installateur: Y/N
        Installateur-->>Pipeline: returns after install attempt
    end

    Pipeline->>Chargeur: charger(source)
    Chargeur->>FS: open docs/<source>.txt
    FS-->>Chargeur: file content
    Chargeur-->>Pipeline: Texte(titre,auteur,contenu,annee)

    Pipeline->>Utils: spacy_conv(texte)
    Utils->>spaCy: load fr_core_news_lg, add sentencizer
    spaCy-->>Utils: Doc
    Utils-->>Pipeline: Doc

    Pipeline->>Analyse: analyser(Doc, min_occ=10)
    activate Analyse
    Analyse->>Analyse: iterate doc.ents
    alt person entity
        Analyse->>FP: trouver_attributs / trouver_genre
        FP-->>Analyse: attributs / genre
    end
    alt location entity
        Analyse->>Analyse: _ajouter_lieu
    end
    Analyse->>Analyse: filter personnages / lieux by occurrences
    Analyse->>Analyse: _ajouter_events(doc)
    Analyse->>FE: trouver_lieu / trouver_participants / trouver_date / trouver_heure
    FE-->>Analyse: lieu / participants / date / heure
    Analyse->>Corpus: create Personnage / Lieu / Evenement
    Corpus-->>Analyse: instances appended
    Analyse-->>Pipeline: personnages, lieux, evenements
    deactivate Analyse

    Pipeline->>Exporteur: ExporterPersonnages / ExporterLieux / ExporterEvenements
    Exporteur->>FS: write CSV files
    Exporteur-->>Pipeline: export complete

    Pipeline->>User: complete
    deactivate Pipeline
```
