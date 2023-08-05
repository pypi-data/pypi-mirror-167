# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['monoid']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'monoid',
    'version': '0.1.0a0',
    'description': 'Monorepo Workspace Manager for Python-based Microservices',
    'long_description': '# Monoid: A Monorepo Workspace Manager\n',
    'author': 'Sebastiaan Zeeff',
    'author_email': 'sebastiaan.zeeff@gmail.com',
    'maintainer': 'Sebastiaan Zeeff',
    'maintainer_email': 'sebastiaan.zeeff@gmail.com',
    'url': 'https://github.com/SebastiaanZ/wx',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
