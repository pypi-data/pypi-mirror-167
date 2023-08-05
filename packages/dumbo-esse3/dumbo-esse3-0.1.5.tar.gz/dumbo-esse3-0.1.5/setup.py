# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dumbo_esse3', 'dumbo_esse3.utils']

package_data = \
{'': ['*']}

install_requires = \
['dataclass-type-validator>=0.1.2,<0.2.0',
 'dateutils>=0.6.12,<0.7.0',
 'rich>=12.5.1,<13.0.0',
 'selenium>=4.4.3,<5.0.0',
 'typeguard>=2.13.3,<3.0.0',
 'typer>=0.6.1,<0.7.0',
 'valid8>=5.1.2,<6.0.0']

setup_kwargs = {
    'name': 'dumbo-esse3',
    'version': '0.1.5',
    'description': 'Esse3 command line utility, to save my future time!',
    'long_description': None,
    'author': 'Mario Alviano',
    'author_email': 'mario.alviano@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
