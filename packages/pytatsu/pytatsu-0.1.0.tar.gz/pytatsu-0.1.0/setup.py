# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytatsu']

package_data = \
{'': ['*']}

install_requires = \
['pybmtool>=0.1.1,<0.2.0']

entry_points = \
{'console_scripts': ['Tatsu = pytatsu.__main__:cli']}

setup_kwargs = {
    'name': 'pytatsu',
    'version': '0.1.0',
    'description': "A Python library/CLI tool for requesting and saving shsh blobs from apple's tatsu signing server api.",
    'long_description': "# pytatsu \n## A Python library/CLI tool for requesting and saving shsh blobs from apple's tatsu signing server api.",
    'author': 'Cryptiiiic',
    'author_email': 'liamwqs@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Cryptiiiic/Tatsu',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
