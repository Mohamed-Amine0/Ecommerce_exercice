# Comment contribuer à GearEdge

Nous sommes très heureux que vous envisagiez de contribuer au projet GearEdge! Si vous avez des questions, n'hésitez pas à ouvrir une issue sur GitHub.

## Instructions de contribution

1. Forkez le dépôt
2. Clonez votre fork: `git clone https://github.com/votre-nom-utilisateur/GearEdge.git`
3. Créez une branche pour votre fonctionnalité: `git checkout -b nouvelle-fonctionnalité`
4. Apportez vos modifications
5. Committez vos changements: `git commit -m 'Ajout de nouvelle-fonctionnalité'`
6. Poussez vers la branche: `git push origin nouvelle-fonctionnalité`
7. Créez une Pull Request

## Installation de l'environnement de développement

```bash
# Créer un environnement virtuel
python -m venv env

# Activer l'environnement
# Windows
env\Scripts\activate
# Unix ou MacOS
source env/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Effectuer les migrations
python manage.py migrate

# Charger les données de test
python manage.py loaddata categories
python manage.py loaddata sample_products

# Lancer le serveur
python manage.py runserver
```

## Style de code

- Suivez PEP 8 pour le code Python
- Utilisez des noms de variables et de fonctions explicites
- Écrivez des docstrings pour toutes les fonctions, classes et modules
- Ajoutez des tests pour toutes les nouvelles fonctionnalités

## Processus de revue

1. Un mainteneur examinera votre Pull Request
2. Des modifications peuvent être demandées
3. Une fois approuvée, votre Pull Request sera fusionnée

Merci de contribuer à GearEdge!
