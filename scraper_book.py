# -*- coding: utf-8 -*-

# Importe bibliothèque requete HTTP.
import requests
# Manipuler la structure arborescente d’un document HTML.
from bs4 import BeautifulSoup

# Importe bibliothèque les fonctionnalités dépendantes du système d'exploitation.

import os


# Retourne un dictionnaire qui contient url de la page prodcut.
def book_url(url):
    return {'product_page_url': url}


# Retourne un dictionnaire qui contient le titre H1 de la page.
def book_title(soup):
    return {'title': soup.h1.text}


# Retourne un dictionnaire qui contient les avis et la description.
def book_desc_reviews(soup):
    desc = ""
    review = ""
    # Boucle qui parcours les paragraphes la page en cours.
    for p in soup.find_all('p'):
        try:
            rating = p['class']
            if 'star-rating' in rating:
                review = rating[1]
        except KeyError:
            desc = p.text
    return {
        'review_rating': review,
        'product_description': desc
    }

# Création et retour du dictionnaire , qui représente le livre.
def get_dict_book(url):
    soup = get_soup(url)
    bookInfos = {}
    bookInfos.update(book_url(url))
    bookInfos.update(book_title(soup))
    bookInfos.update(book_desc_reviews(soup))

    return bookInfos
