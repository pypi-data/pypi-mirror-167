# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['owl_builder',
 'owl_builder.autorels',
 'owl_builder.autorels.bp',
 'owl_builder.autorels.svc',
 'owl_builder.autorels.tests',
 'owl_builder.autosyns',
 'owl_builder.autosyns.bp',
 'owl_builder.autosyns.dmo',
 'owl_builder.autosyns.dto',
 'owl_builder.autosyns.svc',
 'owl_builder.autosyns.tests',
 'owl_builder.autotaxo',
 'owl_builder.autotaxo.bp',
 'owl_builder.autotaxo.dmo',
 'owl_builder.autotaxo.dto',
 'owl_builder.autotaxo.svc',
 'owl_builder.autotaxo.tests',
 'owl_builder.buildr',
 'owl_builder.buildr.bp',
 'owl_builder.buildr.dmo',
 'owl_builder.buildr.svc',
 'owl_builder.buildr.tests']

package_data = \
{'': ['*']}

install_requires = \
['baseblock',
 'fuzzywuzzy>=0.18.0,<0.19.0',
 'nltk>=3.7,<4.0',
 'openai>=0.20.0,<0.21.0',
 'pandas>=1.4.0,<2.0.0',
 'python-Levenshtein',
 'rdflib>=6.1.1,<7.0.0',
 'regex==2022.7.9',
 'spacy==3.3',
 'tabulate',
 'textacy==0.12.0',
 'textblob>=0.17.1,<0.18.0']

setup_kwargs = {
    'name': 'owl-builder',
    'version': '0.1.5',
    'description': 'Tools for Automating the Construction of an Ontology (OWL)',
    'long_description': None,
    'author': 'Craig Trim',
    'author_email': 'craigtrim@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.8.5',
}


setup(**setup_kwargs)
