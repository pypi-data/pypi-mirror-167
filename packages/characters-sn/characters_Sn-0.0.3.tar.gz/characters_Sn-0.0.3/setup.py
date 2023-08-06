# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['characters_sn']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'characters-sn',
    'version': '0.0.3',
    'description': 'functions to calculate group characters of S_n.',
    'long_description': '# Characters_Sn\nFunctions for calculation group characters of the symmetric group Sn\n\n\nThis code was written by Lizzie Hernandez \nfor Math 68 Algebraic Combinatorics course in Fall 2021 \nat Darmouth College \n\n[GitHub Link] (https://github.com/lizziehv/math68-final)\n[Google Colab Link] (https://colab.research.google.com/drive/1GMeXdseX97ZfMtfsO6Tvf5pijP4Zslc6?usp=sharing)',
    'author': 'Vladislav Kargin',
    'author_email': 'slavakargin@yahoo.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': '',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
