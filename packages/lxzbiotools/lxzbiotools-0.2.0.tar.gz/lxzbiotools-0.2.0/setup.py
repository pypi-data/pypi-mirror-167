# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lxzbiotools']

package_data = \
{'': ['*']}

install_requires = \
['biopython>=1.79,<2.0',
 'openpyxl>=3.0.10,<4.0.0',
 'pandas>=1.4.4,<2.0.0',
 'pathlib>=1.0.1,<2.0.0',
 'rich>=12.5.1,<13.0.0',
 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['lxzbiotools = lxzbiotools.lxzbiotools:app']}

setup_kwargs = {
    'name': 'lxzbiotools',
    'version': '0.2.0',
    'description': "Xingze Li's Bioinformatics Analysis Scripts",
    'long_description': '',
    'author': 'Xingze_Li',
    'author_email': 'lixingzee@gmail.com',
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
