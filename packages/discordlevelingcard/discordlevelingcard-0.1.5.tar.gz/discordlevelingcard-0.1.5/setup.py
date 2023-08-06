# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['DiscordLevelingCard']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'disnake>=2.5.2,<3.0.0',
 'nextcord>=2.2.0,<3.0.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'discordlevelingcard',
    'version': '0.1.5',
    'description': 'A library with leveling cards for your discord bot.',
    'long_description': None,
    'author': 'Reset',
    'author_email': 'resetwastakenwastaken@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
