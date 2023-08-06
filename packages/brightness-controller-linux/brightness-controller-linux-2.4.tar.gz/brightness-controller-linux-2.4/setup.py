# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['brightness_controller_linux',
 'brightness_controller_linux.icons',
 'brightness_controller_linux.ui',
 'brightness_controller_linux.util']

package_data = \
{'': ['*']}

install_requires = \
['PyQt5>=5.15,<6.0', 'QtPy>=2.2.0,<3.0.0']

entry_points = \
{'console_scripts': ['brightness-controller = '
                     'brightness_controller_linux.init:main']}

setup_kwargs = {
    'name': 'brightness-controller-linux',
    'version': '2.4',
    'description': 'Using Brightness Controller, you can control brightness of both primary and external displays in Linux. Check it out!',
    'long_description': '# Brightness Controller for Linux\n\n## Dev Docs\n\n### Installing Dependencies\nYou will need [poetry](https://python-poetry.org/docs/#installation). After navigating to this directory, run the following:\n\n```\npoetry install\n```\n\nIt will install dependencies as defined in `pyproject.toml`.\n\n\n### Building\n\n```\npoetry build\n```\n\n### Running Brightness Controller\n\n```\npoetry run python src/brightness_controller_linux/init.py\n```\n\n### Testing\n\n```\npoetry run pytest\n```',
    'author': 'Amit',
    'author_email': 'lordamit@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/LordAmit/Brightness',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
