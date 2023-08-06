# Cheat at wordle!

`wordle-helper` takes a list of arguments that constrain the possibile letter placements. The
arguments take the form of \<word\>,\<constraints\>, where \<word\> is the word guessed and
\<constraints\> are the color of each letter returned by Wordle. The allowed colors are **y**ellow,
**b**lack, and **g**reen:

"y": represents yellow letters

"b": represents unused letters

"g": represents green letters

Each five letter \<word\> will have a five letter \<constraints\> string. For example:

```
~$ poetry run wordle-helper least,ybbyb
INFO:wordle-helper:Found 320 possibilites, the most common one is 'girls'
INFO:wordle-helper:Check 'words_3b035b135cec4e10aad9abd5940fff75' for all possibilites, sorted by frequency
~$ poetry run wordle-helper least,ybbyb girls,bbygg
INFO:wordle-helper:Found 2 possibilites, the most common one is 'rolls'
INFO:wordle-helper:All valid guesses, sorted by frequency:
rolls
rouls
```

# Installation

`wordle-helper` is available on [PyPI](https://pypi.org/project/python-wordle-helper/):

```
~$ pip install python-wordle-helper
...
~$ wordle-helper -h
```

## Installation from source

This assumes you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [Python 3.9+](https://www.python.org/downloads/), and [poetry](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) installed already.

```
~$ git clone git@gitlab.com:henxing/wordle_helper.git
~$ cd wordle_helper
wordle_helper$ poetry install
...
wordle_helper$ poetry run wordle-helper -h
```
