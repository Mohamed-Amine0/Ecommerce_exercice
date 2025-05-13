# GearEdge E-commerce

GearEdge est une application e-commerce Django qui présente une boutique en ligne pour des équipements outdoor, multitools, accessoires EDC (Everyday Carry), éclairage et matériel de camping.

## Fonctionnalités

### Implémentées
- ✅ Catalogue de produits avec affichage en grille
- ✅ Système de catégories pour organiser les produits
- ✅ Page détaillée par produit
- ✅ Mise en avant des produits populaires sur la page d'accueil
- ✅ Panier d'achat complet (ajout, suppression, mise à jour des quantités)
- ✅ Interface responsive avec design moderne
- ✅ Notifications utilisateur pour les actions du panier

### À venir
- ⏳ Système de recherche de produits
- ⏳ Système de comptes utilisateurs
- ⏳ Processus de commande et checkout
- ⏳ Système de paiement
- ⏳ Avis et notes sur les produits
- ⏳ Filtrage et tri avancés des produits

## Technologies utilisées

- Django 5.2
- Bootstrap 5
- FontAwesome
- JavaScript
- HTML5 / CSS3
- SQLite (développement)

## Structure du projet

```
ecommerce/              # Projet principal Django
│
├── products/           # Application pour les produits et catégories
│   ├── models.py       # Modèles de données (Product, Category)
│   ├── views.py        # Vues pour afficher les produits
│   ├── templates/      # Templates des pages produits
│   └── fixtures/       # Données de démo
│
├── cart/               # Application pour le panier d'achat
│   ├── cart.py         # Classe principale du panier
│   ├── views.py        # Vues pour gérer le panier
│   └── templates/      # Templates du panier
│
├── static/             # Fichiers statiques
│   ├── css/            # Styles CSS
│   └── js/             # Scripts JavaScript
│
└── templates/          # Templates de base partagés
```

## Installation

1. Cloner le dépôt
2. Créer un environnement virtuel: `python -m venv env`
3. Activer l'environnement: `env\Scripts\activate` (Windows) ou `source env/bin/activate` (Linux/Mac)
4. Installer les dépendances: `pip install -r requirements.txt`
5. Effectuer les migrations: `python manage.py migrate`
6. Charger les données de démo: `python manage.py loaddata categories sample_products`
7. Lancer le serveur: `python manage.py runserver`

## Screenshots

*Screenshots à venir*

## Auteurs

- Team GearEdge

## Licence

Ce projet est sous licence MIT.
