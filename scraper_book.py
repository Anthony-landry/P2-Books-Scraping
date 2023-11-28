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


# Création et retour du dictionnaire , qui représente le livre.
def get_dict_book(url):
    soup = get_soup(url)
    bookInfos = {}
    bookInfos.update(book_url(url))

    return bookInfos
