
import csv


class Inventory:
    inventory = []

    def __init__(self, id, title, rating, release_year, copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = copies_available

    @classmethod
    def inventory_info_csv(cls):
        cls.inventory = []
        with open('data/inventory.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                cls.inventory.append(Inventory(**row))
        return cls.inventory 

    @classmethod
    def write_inventory_to_csv(cls):
        with open('data/inventory.csv', mode='w', newline='') as csv_file:
            fieldnames = ['id', 'title', 'rating','release_year', 'copies_available']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for video in cls.inventory:
                writer.writerow({
                    'id': video.id,
                    'title': video.title,
                    'rating': video.rating,
                    'release_year': video.release_year,
                    'copies_available': video.copies_available
                })
