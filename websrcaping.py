import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import csv
from urllib.parse import urlparse

# 🔗 URL du site à analyser
url = input("Collez l'url du site web ici: ")

# 🌍 Extraire le nom de domaine
nom_site = urlparse(url).netloc

# 📩 Télécharger la page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 🧼 Nettoyage du texte
text = soup.get_text(separator=' ')
text = re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', text).lower()
words = text.split()

# ❌ Mots à ignorer
stopwords = ["et", "le", "la", "les", "de", "des", "du", "un", "une", "en", "à", "au", "aux", "pour", "avec", "que", "qui", "dans", "sur", "par", "ce", "ces", "se", "sa", "son", "ou", "mais", "il", "elle", "nous", "vous", "ils", "elles"]
keywords = [word for word in words if word not in stopwords and len(word) > 2]

# 🔢 Compter les mots
frequence = Counter(keywords)

# 📝 Écriture dans un fichier CSV
with open("resultats.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Site", "Mot clé", "Fréquence"])  # entête

    for mot, count in frequence.most_common(20):  # top 20 mots
        writer.writerow([nom_site, mot, count])

print("✅ Résultats enregistrés dans resultats.csv")

