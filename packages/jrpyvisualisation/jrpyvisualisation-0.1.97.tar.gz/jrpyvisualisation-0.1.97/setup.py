# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jrpyvisualisation', 'jrpyvisualisation.datasets']

package_data = \
{'': ['*'],
 'jrpyvisualisation': ['vignettes/*'],
 'jrpyvisualisation.datasets': ['data/*']}

install_requires = \
['kaleido==0.2.1',
 'numpy>=1.23.2,<2.0.0',
 'pandas>=1.4.3,<2.0.0',
 'plotly>=4.1']

setup_kwargs = {
    'name': 'jrpyvisualisation',
    'version': '0.1.97',
    'description': 'Jumping Rivers: Introduction to Visualisation in Python',
    'long_description': None,
    'author': 'Jamie',
    'author_email': 'jamie@jumpingrivers.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
