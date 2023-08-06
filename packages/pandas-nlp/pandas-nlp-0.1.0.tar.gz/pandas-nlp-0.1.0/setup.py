# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pandas_nlp']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.4,<2.0.0', 'spacy>=3.4.1,<4.0.0']

setup_kwargs = {
    'name': 'pandas-nlp',
    'version': '0.1.0',
    'description': 'Pandas extension with NLP functionalities',
    'long_description': None,
    'author': 'Jaume Ferrarons',
    'author_email': 'jaume.ferrarons@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
