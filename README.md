# OpenClassrooms: Projet 2: Books To Scrape

![books_to_scrape ](.readme/landry_anthony_developpeur_application-python_openclassrooms_books_to_scrape.png)

Ce script permet de récupérer les informations de tout les produits sur le site http://books.toscrape.com/.
Ces informations sont les suivantes:
 - URL du livre
 - Universal Product Code (upc)
 - Titre du livre
 - Prix, taxe incluse
 - Prix, taxe exclue
 - Quantité disponible
 - Description du produit
 - Catégorie
 - Rating
 - URL de l'image
 - Chemin local de l'image téléchargée


En plus de cela, les images des livres sont téléchargées.
Ces données sont ensuite classées par catégories et inscrites dans un fichier CSV correspondant.
Les données sont générées à la racine du projet suivant cette arborescence:
```
|-- data/
    |-- categorie1/
        |-- categorie1.csv
        |-- imgs/
            |-- img1.jpg
            |-- img2.jpg
            ...etc
    |-- categorie2/
    ...etc
```
# Installation:
Commencez tout d'abord par installer Python.
Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:
```
git clone https://github.com/Anthony-landry/P2-Books-Scraping
```
Placez vous dans le dossier OC_P2_BooksToScrape, puis créez un nouvel environnement virtuel:
```
python -m venv env
```
Ensuite, activez-le.
Windows:
```
env\scripts\activate.bat
```
Linux:
```
source env/bin/activate
```
Il ne reste plus qu'à installer les packages requis:
```
pip install -r requirements.txt
```
Vous pouvez enfin lancer le script:
```
python main.py
```