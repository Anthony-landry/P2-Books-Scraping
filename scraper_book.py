# -*- coding: utf-8 -*-

# Importe bibliothèque requete HTTP.
import requests
# Manipuler la structure arborescente d’un document HTML.
from bs4 import BeautifulSoup

# Importe bibliothèque les fonctionnalités dépendantes du système d'exploitation.

import os


# Récupere le contenu de la page
def get_soup(url):
    # Recuperation du contenu de la page passée en "url"
    htmlResponse = requests.get(url)
    html = htmlResponse.content
    html_encode_fixed = html.decode('utf8').encode('utf8', 'ignore')
    # Parsage de la page du livre.
    soup = BeautifulSoup(html_encode_fixed, 'lxml')
    return soup


# Retourne un dictionnaire qui contient url de la page prodcut.
def book_url(url):
    return {'product_page_url': url}


# Retourne un dictionnaire qui contient le titre H1 de la page.
def book_title(soup):
    return {'title': soup.h1.text}


# Retourne un dictionnaire qui contient les avis .
def book_reviews(soup):
    review = ""

    product = soup.find('div', {'class': 'product_main'})
    if product:
        # Boucle qui parcours les paragraphes la page en cours.
        for p in product.find_all('p'):
            try:
                rating = p['class']
                if 'star-rating' in rating:
                    review = rating[1]
            except KeyError:
                pass
    return {
        'review_rating': review,
    }


# Retourne un dictionnaire qui contient la description.
def book_desc(soup):
    desc = ""

    product = soup.find('article', {'class': 'product_page'})
    if product:
        # Boucle qui parcours les paragraphes la page en cours.
        for p in product.find_all('p', recursive=False):
            desc = p.text
    return {
        'product_description': desc
    }


# Retourne un dictionnaire qui contient la categorie du livre.
def book_category(soup):
    for a in soup.ul.find_all('a'):
        if 'Home' not in a.text and 'Books' not in a.text:
            return {'category': a.text}


# Retourne un dictionnaire qui contient un code UPC, prix sans TVA et avec TVA ,quantitée disponible.
def book_upc_prices_stocks(soup):
    upc = ""
    priceExclTax = ""
    priceInclTax = ""
    stock = ""

    for tr in soup.find_all('tr'):
        if 'UPC' in tr.text:
            upc = tr.td.text
        elif 'excl' in tr.text:
            priceExclTax = tr.td.text.replace('Â', '')
        elif 'incl' in tr.text:
            priceInclTax = tr.td.text.replace('Â', '')
        elif 'Availability' in tr.text:
            stock = tr.td.text.split(' ')[2].replace('(', '')
    return {
        'upc': upc,
        'price_excluding_tax': priceExclTax,
        'price_including_tax': priceInclTax,
        'number_available': stock
    }


# Télécharge et enregistré l'image dans le dossier "data".
# puis dans un sous dossier le nom de la catégorie.
# puis dans un dossier imgs.
# retourne un dictionnaire qui contient
def book_img(soup):
    imageUrl = soup.img['src'].replace('../..', 'http://books.toscrape.com')
    imageBinary = requests.get(imageUrl)
    category = book_category(soup)
    title = book_title(soup)
    path = 'data/' + category['category'] + '/imgs'
    imgTitle = ''.join([x for x in title['title'] if x.isalnum()]) + '.jpg'

    if not os.path.exists(path):
        os.makedirs(path)
    # write image
    open(path + '/' + imgTitle, 'wb').write(imageBinary.content)

    return {
        'image_url': imageUrl,
        'image_path': path + '/' + imgTitle
    }


# Création et retour du dictionnaire , qui représente le livre.
def get_dict_book(url):
    soup = get_soup(url)
    bookInfos = {}
    bookInfos.update(book_url(url))
    bookInfos.update(book_title(soup))
    bookInfos.update(book_reviews(soup))
    bookInfos.update(book_desc(soup))
    bookInfos.update(book_category(soup))
    bookInfos.update(book_upc_prices_stocks(soup))
    bookInfos.update(book_img(soup))

    return bookInfos
