# Contributor's Guide

# Installation
Git clone and navitage to the repo from your command-line:

```sh
git clone REMOTE_ADDRESS
cd /path/to/repo
```


Create/activate a virtual environment:

```sh
pipenv --python 3.7
pipenv install # now they can install all the packages inside the Pipfile
pipenv shell
```

Run example script:

```sh
python -m my_lambdata.hello
```