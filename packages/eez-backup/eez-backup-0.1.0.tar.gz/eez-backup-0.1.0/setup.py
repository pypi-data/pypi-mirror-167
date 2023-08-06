# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eez_backup']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'frozendict>=2.3.4,<3.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'pytest>=7.1.3,<8.0.0',
 'tqdm>=4.64.1,<5.0.0']

entry_points = \
{'console_scripts': ['backup = eez_backup.__main__:cli']}

setup_kwargs = {
    'name': 'eez-backup',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': '0b11001111',
    'author_email': '19192307+0b11001111@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
