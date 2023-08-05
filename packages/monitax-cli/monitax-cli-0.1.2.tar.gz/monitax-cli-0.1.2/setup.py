# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['monitax_cli']

package_data = \
{'': ['*']}

install_requires = \
['pathlib>=1.0.1,<2.0.0',
 'pendulum>=2.1.2,<3.0.0',
 'requests>=2.28.1,<3.0.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['mon-cli = monitax_cli.main:app']}

setup_kwargs = {
    'name': 'monitax-cli',
    'version': '0.1.2',
    'description': 'Monitax Client',
    'long_description': None,
    'author': 'ekalaya2015',
    'author_email': 'ekalaya2015@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
