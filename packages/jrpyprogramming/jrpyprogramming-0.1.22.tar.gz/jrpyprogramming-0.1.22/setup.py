# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jrpyprogramming']

package_data = \
{'': ['*'], 'jrpyprogramming': ['data/*', 'vignettes/*']}

install_requires = \
['jrpyintroduction>=0.2.2',
 'matplotlib>=3.5,<4.0',
 'numpy>=1.23,<2.0',
 'pandas>=1.4,<2.0']

setup_kwargs = {
    'name': 'jrpyprogramming',
    'version': '0.1.22',
    'description': 'Jumping Rivers: Programming with Python',
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
