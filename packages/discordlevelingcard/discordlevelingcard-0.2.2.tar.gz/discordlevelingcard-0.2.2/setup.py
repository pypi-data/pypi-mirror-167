# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['DiscordLevelingCard']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0', 'aiohttp>=3.8.1,<4.0.0']

setup_kwargs = {
    'name': 'discordlevelingcard',
    'version': '0.2.2',
    'description': 'A library with leveling cards for your discord bot.',
    'long_description': '# DiscordLevelingCard\nA library with Rank cards for your discord bot.\n\n\n\n## card preview\n\n`card1`\n\n![card1](https://cdn.discordapp.com/attachments/907213435358547968/994620579816681572/unknown.png)\n\n\n<br>\n\n## installation\n\n`for pypi version`\n```sh\npip install discordlevelingcard\n```\n\n`for github developement version`\n```sh\npip install git+https://github.com/ResetXD/DiscordLevelingCard\n```\n\n## How To Use\n\nIf you don\'t provide `path` then the method will return `bytes` which can directly be used in discord.py/disnake/pycord/nextcord \'s `File class`.\n\n\n<br>\n\n\n## Example\n\n`since no path was given, it returns bytes which can directly be used in discord.py and its fork \'s File class.`\n\n```py\n\nfrom disnake.ext import commands\nfrom DiscordLevelingCard import RankCard\nimport disnake\n\nclient = commands.Bot()\n\n@client.slash_command(name="rank")\nasync def user_rank_card(ctx, user:disnake.Member):\n    await ctx.response.defer()\n    a = RankCard(\n        background=user.banner.url,\n        avatar=user.display_avatar.url,\n        level=1,\n        current_exp=1,\n        max_exp=1,\n        username="cool username"\n    )\n    image = await a.card1()\n    await ctx.edit_original_message(file=disnake.File(image, filename="rank.png")) # providing filename is very important\n\n```\n\n<br>\n\n`if you want to use path`\n```py\n@client.slash_command(name="rank")\nasync def user_rank_card(ctx, user:disnake.Member):\n    await ctx.response.defer()\n    a = RankCard(\n        background="https://cool-banner-url.com",\n        avatar=user.display_avatar.url,\n        level=1,\n        current_exp=1,\n        max_exp=1,\n        username="cool username",\n        bar_color="red",\n        text_color="white",\n        path="./user_cards/rank_card.png"\n    )\n    # image return the path provided i.e. "./user_cards/rank_card.png"\n    image = await a.card1()\n    await ctx.edit_original_message(file=disnake.File(image, filename="rank.png")) # providing filename is very important\n```\n\n\n## Documentation\n\n`RankCard` class\n\n`__init__` method\n\n```py\nRankCard(\n    background:Union[PathLike, BufferedIOBase],\n    avatar:Union[PathLike, BufferedIOBase],\n    level:int,\n    current_exp:int,\n    max_exp:int,\n    username:str,\n    bar_color:str="white",\n    text_color:str="white",\n    path:str=None\n)\n```\n\n`background` - background image url or file-object in `rb` mode\n\n`avatar` - avatar image url or file-object in `rb` mode\n\n`level` - level of the user\n\n`current_exp` - current exp of the user\n\n`max_exp` - max exp of the user\n\n`username` - username of the user\n\n`bar_color` - color of the bar [example: "white" or "#000000"]\n\n`text_color` - color of the text [example: "white" or "#000000"]\n\n`path` - path to save the card [if not provided will return `bytes` instead]\n\n<br>\n\n`card1` method\n\n```py\nRankCard.card1()\n```\n\n`returns` - `path` if `path` was provided in `__init__` or `bytes` if `path` was not provided in `__init__`\n\n<br>\n\n## todo\n\n- [ ] add more cards\n- [ ] better documentation\n',
    'author': 'Reset',
    'author_email': 'resetwastakenwastaken@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ResetXD/DiscordLevelingCard',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
