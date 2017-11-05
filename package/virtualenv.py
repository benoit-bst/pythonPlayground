"""

Création d'un environnement virtualenv

install virtualenv
virtualenv ap

créer un dossier de configuration ou on veut :
vitualenv data/app

lancer l'environnment :
source /tmp/data/app/bin/activate

sortir du virtualenv:
deactivate

"""

"""

pour créer un package python propre il faut :
  1 - mettre dans le control debian l'install de python
  2 - appeler dans le postinst l'installation de :
    * setuptools
    * pip
    * virtualenv
    * wheel
  3 - installer les librairis python dans le virtualenv via le requirements.txt
    * source /tmp/data/app/bin/activate
    * pip install -U -r requirements.txt -q source /tmp/data/app/bin/activate
    * source /tmp/data/app/bin/activate

"""