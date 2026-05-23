import csv
import json
from dataclasses import asdict
from pathlib import Path


class Exportateur:
    """Classe qui exporte les données extraites par le lecteur dans des fichiers CSV"""
    def __init__(self,liste_persos,liste_lieux,liste_evenements) -> None:
        self.personnages=liste_persos
        self.lieux=liste_lieux
        self.evenements=liste_evenements


    def exporter_personnages(self):

        filename=Path("./docs/personnages.csv")

        with Path.open(filename, "w") as csvfile:
            csvwriter=csv.writer(csvfile)
            fields=self.personnages[0].__dict__.keys()
            csvwriter.writerow(fields)
            for perso in self.personnages:
                values_lists=[]
                for value in perso.__dict__.values():
                    if type(value) is list:
                        values_lists.append(", ".join(map(str, value)))
                    else:
                        values_lists.append([value])
                csvwriter.writerow(values_lists)

    def exporter_lieux(self):

        filename=Path("./docs/lieux.csv")

        with Path.open(filename, "w") as csvfile:
            csvwriter=csv.writer(csvfile)
            fields=self.lieux[0].__dict__.keys()
            csvwriter.writerow(fields)
            for lieu in self.lieux:
                values_lists=[]
                for value in lieu.__dict__.values():
                    if type(value) is list:
                        values_lists.append(", ".join(map(str, value)))
                    else:
                        values_lists.append([value])
                csvwriter.writerow(values_lists)

    def exporter_evenements(self):

        filename=Path("./docs/evenements.csv")

        with Path.open(filename, "w") as csvfile:
            csvwriter=csv.writer(csvfile)
            fields=self.evenements[0].__dict__.keys()
            csvwriter.writerow(fields)
            for event in self.evenements:
                values_lists=[]
                for value in event.__dict__.values():
                    if type(value) is list:
                        values_lists.append(", ".join(map(str, value)))
                    else:
                        values_lists.append([value])
                csvwriter.writerow(values_lists)

    def exporter_json(self):

        data = {
            "personnages": [asdict(perso) for perso in self.personnages],
            "lieux": [asdict(lieu) for lieu in self.lieux],
            "evenements": [asdict(event) for event in self.evenements]
        }

        filename = Path("./docs/donnees.json")
        with Path.open(filename, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)
