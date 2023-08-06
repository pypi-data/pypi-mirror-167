# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['owl_parser',
 'owl_parser.multiquery',
 'owl_parser.multiquery.bp',
 'owl_parser.multiquery.dmo',
 'owl_parser.multiquery.dmo.span',
 'owl_parser.multiquery.svc',
 'owl_parser.multiquery.tests',
 'owl_parser.mutato',
 'owl_parser.mutato.bp',
 'owl_parser.mutato.dmo',
 'owl_parser.mutato.dmo.core',
 'owl_parser.mutato.dmo.exact',
 'owl_parser.mutato.dmo.hierarchy',
 'owl_parser.mutato.dmo.spans',
 'owl_parser.mutato.dto',
 'owl_parser.mutato.svc',
 'owl_parser.singlequery',
 'owl_parser.singlequery.bp',
 'owl_parser.singlequery.dmo',
 'owl_parser.singlequery.dto',
 'owl_parser.singlequery.svc',
 'owl_parser.singlequery.tests']

package_data = \
{'': ['*']}

install_requires = \
['baseblock', 'owl-builder', 'regression-framework']

setup_kwargs = {
    'name': 'owl-parser',
    'version': '0.1.1',
    'description': 'Parse Input Text using One-or-More Ontology (OWL) files',
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
