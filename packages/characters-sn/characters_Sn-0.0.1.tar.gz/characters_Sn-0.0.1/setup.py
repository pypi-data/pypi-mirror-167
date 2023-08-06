# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['characters_sn']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'characters-sn',
    'version': '0.0.1',
    'description': 'functions to calculate characters of S_n.',
    'long_description': '# Characters_Sn\nFunctions for calculation characters of the symmetric group Sn\n\n\nThis code was written by Lizzie Hernandez \nfor Math 68 Algebraic Combinatorics course in Fall 2021 \nat Darmouth College',
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
