# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wordle_helper']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.0,<2.0.0', 'requests>=2.28.1,<3.0.0', 'wordfreq>=3.0.1,<4.0.0']

entry_points = \
{'console_scripts': ['wordle-helper = wordle_helper.cli:main']}

setup_kwargs = {
    'name': 'python-wordle-helper',
    'version': '1.0.0',
    'description': 'Cheat at Wordle!',
    'long_description': '# Cheat at wordle!\n\n`wordle-helper` takes a list of arguments that constrain the possibile letter placements. The\narguments take the form of \\<word\\>,\\<constraints\\>, where \\<word\\> is the word guessed and\n\\<constraints\\> are the color of each letter returned by Wordle. The allowed colors are **y**ellow,\n**b**lack, and **g**reen:\n\n"y": represents yellow letters\n\n"b": represents unused letters\n\n"g": represents green letters\n\nEach five letter \\<word\\> will have a five letter \\<constraints\\> string. For example:\n\n```\n~$ poetry run wordle-helper least,ybbyb\nINFO:wordle-helper:Found 320 possibilites, the most common one is \'girls\'\nINFO:wordle-helper:Check \'words_3b035b135cec4e10aad9abd5940fff75\' for all possibilites, sorted by frequency\n~$ poetry run wordle-helper least,ybbyb girls,bbygg\nINFO:wordle-helper:Found 2 possibilites, the most common one is \'rolls\'\nINFO:wordle-helper:All valid guesses, sorted by frequency:\nrolls\nrouls\n```\n\n# Installation\n\n`wordle-helper` is available on [PyPI](https://pypi.org/project/python-wordle-helper/):\n\n```\n~$ pip install python-wordle-helper\n...\n~$ wordle-helper -h\n```\n\n## Installation from source\n\nThis assumes you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [Python 3.9+](https://www.python.org/downloads/), and [poetry](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) installed already.\n\n```\n~$ git clone git@gitlab.com:henxing/wordle_helper.git\n~$ cd wordle_helper\nwordle_helper$ poetry install\n...\nwordle_helper$ poetry run wordle-helper -h\n```\n',
    'author': 'Hugh Enxing',
    'author_email': 'henxing@gmail.com',
    'maintainer': 'Hugh Enxing',
    'maintainer_email': 'henxing@gmail.com',
    'url': 'https://gitlab.com/henxing/wordle_helper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
