# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pybmtool']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'remotezip>=0.9.4,<0.10.0']

entry_points = \
{'console_scripts': ['BMTool = pybmtool.__main__:cli']}

setup_kwargs = {
    'name': 'pybmtool',
    'version': '0.1.1',
    'description': "A Python library/CLI tool for parsing Apple's BuildManifest plist files inside a firmware ipsw/ota.",
    'long_description': "# pybmtool \n## A Python library/CLI tool for parsing Apple's BuildManifest plist files inside a firmware ipsw/ota.",
    'author': 'Cryptiiiic',
    'author_email': 'liamwqs@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Cryptiiiic/BMTool',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
