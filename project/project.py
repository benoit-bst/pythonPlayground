/*----------------------------------

  Agencement des sources

  projet
    |
    |-------- debian
    |
    |-------- src
    |          |------kermel
    |          |------libs
    |          |------modules
    |          |-main
    |
    |-------- tests
    |          |------install-tests.sh
    |          |-----depends
    |          |       |-----requirements-tests.txt
    |          |       |-----lib1
    |          |       |-----lib2
    |          |       |-----lib3
    |          |       |-----lib4
    |          |       |-----lib5
    |          |------run-all-tests.sh
    |          |------test1
    |          |------test2
    |
    |-------- doc
    |
    |-------- config
    |          |------apache
    |          |------deamon
    |
    |-------- install
    |          |-----install.sh
    |          |-----core-depends
    |          |       |-----pypy
    |          |       |-----setuptools
    |          |       |-----pip
    |          |       |-----virtualenv
    |          |       |-----wheel
    |          |-----depends
    |          |       |-----requirements.txt
    |          |       |-----lib1
    |          |       |-----lib2
    |          |       |-----lib3
    |          |       |-----lib4
    |          |       |-----lib5


----------------------------------*/

/*----------------------------------

1 * install via depends du .deb
     - apache
     - python

2 * install via postinst qui appel install.sh
     - install pypy - interpréteur python fast (comment lnker avec ?)
     - install setuptools - facilite les actions de packaging python
     - install pip
     - wheel
     - install virtualenv
     - depends/requirements.txt
     - lancement du virtual env
          créer un dossier :
          virtualenv --quiet nomdossierVirtualEnv
          lancer l environnment :
          source /tmp/data/app/bin/activate

----------------------------------*/