# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['maser', 'maser.plot', 'maser.plot.rpw']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.2,<4.0.0']

setup_kwargs = {
    'name': 'maser.plot',
    'version': '0.2.1',
    'description': '',
    'long_description': None,
    'author': 'MASER Team',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
