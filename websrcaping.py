import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

#url du site à analyser

url="https://www.advalorem-solutions.com/"

reponse = requests.get(url)
soup = BeautifulSoup(reponse.text, "html.parser")

#enleve tous les balise html

text = soup.get_text(separator=' ')

#enleve les caractere sauf lettre et espace

text = re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', text).lower()

#transforme les texte en liste de mot

words = text.split()

#mot à ignorer

mot_ignorer = ["et", "le", "la", "les", "de", "des", "du", "un", "une", "en", "à", "au", "aux", "pour", "avec", "que", "qui", "dans", "sur", "par", "ce", "ces", "se", "sa", "son", "ou", "mais", "il", "elle", "nous", "vous", "ils", "elles"]

#prend les mots interessent

mot_interessent = [word for word in words if word not in mot_ignorer and len(word) > 2]

#compte les mot les plus utiliser

frequence = Counter(mot_interessent)

#donne les mot les plus utiliser

print("Mots les plus utiliser :")
for mot, count in frequence.most_common(10):
    print(f"{mot} : {count} fois")



