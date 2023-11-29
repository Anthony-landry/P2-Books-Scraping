# -*- coding: utf-8 -*-

# Import de la bibliothèque des fichiers csv.
import csv


# Creation du fichier .csv avec les données du dictionnaire.
def write_csv(list_books_dicts):

    csvColumns = ['product_page_url', 'upc', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url', 'image_path']
    categorie = list_books_dicts[0]['category']
    csvFile = categorie + '.csv'

    with open('data/' + categorie + '/' + csvFile, 'w', encoding='utf-8', newline='', errors='replace') as csvFile:
        writer = csv.DictWriter(csvFile, delimiter=";", fieldnames=csvColumns)
        writer.writeheader()
        for data in list_books_dicts:
            writer.writerow(data)
