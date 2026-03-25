 # DataCo Smart Supply Chain Analytics

##  Objectif du projet

Ce projet a pour but d'explorer et d'exploiter le dataset **DataCo Smart
Supply Chain** afin de construire une pipeline data complète.

L'idée est de couvrir tout le cycle : - exploration des données (EDA) -
transformation avec PySpark - stockage structuré dans PostgreSQL -
visualisation avec Power BI


------------------------------------------------------------------------

##  Sprint 1 --- Mise en place de l'environnement 


###  Environnement

  Outil        Version       Notes
  ------------ ------------- ----------------------
  Python       3.11.9        Ajouté au PATH
  Java (JDK)   17.0.14 LTS   Requis pour PySpark
  PySpark      3.5.2         Installation via pip
  PostgreSQL   16.13         Port 5432
  VS Code      1.109.0       IDE principal

------------------------------------------------------------------------

##  Installation & vérifications

### Python

``` bash
python --version
```

✔️ Python 3.11.9

------------------------------------------------------------------------

### Java (JDK 17)

``` bash
java --version
```

✔️ Java correctement installé\
✔️ Variable `JAVA_HOME` configurée\
✔️ Ajout de `%JAVA_HOME%\bin` dans le PATH

------------------------------------------------------------------------

### PySpark

``` bash
python -m pip install pyspark==3.5.2
```

Test :

``` bash
python -c "import pyspark; print(pyspark.__version__)"
```

✔️ Version 3.5.2 détectée

------------------------------------------------------------------------

### PostgreSQL

-   Installation locale
-   Port : 5432
-   Accès via pgAdmin

✔️ Connexion validée sur `localhost`

------------------------------------------------------------------------

### VS Code

Extensions utilisées : - Python (Microsoft) - PostgreSQL



------------------------------------------------------------------------

## 📁 Structure du projet


.
├── data/               # données brutes (non versionnées)
├── notebooks/          # EDA + tests PySpark
├── src/                # scripts ETL
├── sql/                # schémas + requêtes
├── docs/               # documentation projet
├── README.md
└── .gitignore


------------------------------------------------------------------------

