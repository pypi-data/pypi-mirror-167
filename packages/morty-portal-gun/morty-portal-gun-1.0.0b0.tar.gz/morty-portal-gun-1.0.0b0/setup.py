# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['morty_portal_gun']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['morty-portal-gun = morty_portal_gun.main:app']}

setup_kwargs = {
    'name': 'morty-portal-gun',
    'version': '1.0.0b0',
    'description': '',
    'long_description': '# Morty Portal Gun\n\nTest Project',
    'author': 'Test',
    'author_email': 'Test@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
