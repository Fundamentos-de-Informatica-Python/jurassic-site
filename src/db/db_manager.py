import csv
from db.models.Dino import Dinos

def load_dinos():
    dinos = []
    with open('db/dino_files.csv', 'r') as dino_file:
        rows = csv.DictReader(dino_file)

        for row in rows:
            dinos.append(
                Dinos(
                    row['type'],
                    row['name'],
                    row['weight'],
                    row['long'],
                    row['height'],
                    row['img']
                )
            )

        return dinos




def save_dinos(Dinos):
    with open('db/dino_files.csv', 'a') as dino_file:
        header = ['type','name','weight','long','height','img']

        writer = csv.DictWriter(dino_file, fieldnames=header)

        if dino_file.tell() == 0:
            writer.writeheader()

        writer.writerow(Dinos)
