# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gitbook']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'gitbook',
    'version': '0.1.0',
    'description': "Python library for interacting with GitBook's API.",
    'long_description': "# gitbook\n Python library for interacting with GitBook's API.\n",
    'author': 'CircuitSacul',
    'author_email': 'circuitsacul@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
