# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['opsrampcli']

package_data = \
{'': ['*']}

install_requires = \
['DateTime>=4.4,<5.0',
 'PyYAML>=6.0,<7.0',
 'XlsxWriter>=3.0.3,<4.0.0',
 'json5>=0.9.8,<0.10.0',
 'pandas>=1.4.3,<2.0.0',
 'requests>=2.28.0,<3.0.0']

entry_points = \
{'console_scripts': ['opcli = opsrampcli.opsrampcli:main']}

setup_kwargs = {
    'name': 'opsrampcli',
    'version': '0.4.1',
    'description': '',
    'long_description': None,
    'author': 'Michael Friedhoff',
    'author_email': 'michael.friedhoff@opsramp.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
