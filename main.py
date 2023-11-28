# manipuler la structure arborescente d’un document HTML.
from bs4 import BeautifulSoup

# importe bibliothèque requete HTTP.
import requests


# Importation de la fonction "Book"
from scraper_book import get_dict_book
# Recuperation du contenu de la page d'acceuil.
htmlResponse = requests.get('http://books.toscrape.com/index.html')

# lxml, analyseur HTML (parseur)
# Parsage de la page d'accueil.
soup = BeautifulSoup(htmlResponse.text, 'lxml')

categories = {}
print("Scrapping in progress...")
# Recuperation de toutes les categories.
for a in soup.find('div', {'class': 'side_categories'}).ul.find_all('a'):
    # lien ignoré du lien Titre vers l'accueil.
    if 'books_1' not in a.get('href'):
        categories[a.text.replace('\n', '').replace('  ', '')] = 'http://books.toscrape.com/' + a.get('href')

# Scrap des livres de chaque catégorie.
for categorie, catUrl in categories.items():
    # categorie = key , catUrl = value.

    # Recupère un objet qui represente la réponse à la requete pour la categorie parcouru.
    htmlResponse = requests.get(catUrl)
    # Parsage du HTML.
    soup = BeautifulSoup(htmlResponse.text, 'lxml')

    # Determination du nombre de pages de la catégorie.
    if soup.find('ul', {'class': 'pager'}):
        nbPages = int(soup.find('li', {'class': 'current'}).text.split(' ')[31].replace('\n', ''))
    else:
        # pagination
        nbPages = 1

    # Récupération des urls de chaque livre présent dans la catégorie.
    i = 0
    booksUrl = []
    # Parcours de toutes les pages.
    while i < nbPages:
        # Recuperation des url present sur la pages.
        for book in soup.find_all('article'):
            bookUrl = book.h3.a.get('href').replace('../../../', 'http://books.toscrape.com/catalogue/')
            booksUrl.append(bookUrl)
        i += 1
        # Si la pagination est supérieur a une page , passage à la suivante.
        if nbPages > 1:
            nextPage = requests.get(catUrl.replace('index.html', 'page-' + str(i+1) + '.html'))
            soup = BeautifulSoup(nextPage.text, 'lxml')

    # Scrap des informations de chaque livre.
    allBooksFromCurrentCategory = []
    for url in booksUrl:
        # Generation d'un dict à partir d'un URL.
        currentBook = get_dict_book(url)
        print(url)
        currentBook = {}
        allBooksFromCurrentCategory.append(currentBook)
