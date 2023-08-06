# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['DiscordLevelingCard']

package_data = \
{'': ['*'], 'DiscordLevelingCard': ['assets/*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0', 'aiohttp>=3.8.1,<4.0.0']

setup_kwargs = {
    'name': 'discordlevelingcard',
    'version': '0.3.1',
    'description': 'A library with leveling cards for your discord bot.',
    'long_description': '# DiscordLevelingCard\nA library with Rank cards for your discord bot.\n\n\n\n## card preview\n\n`card1`\n\n![card1](https://cdn.discordapp.com/attachments/907213435358547968/994620579816681572/unknown.png)\n\n\n<br>\n\n## installation\n\n`for pypi version`\n```sh\npip install discordlevelingcard\n```\n\n`for github developement version`\n```sh\npip install git+https://github.com/ResetXD/DiscordLevelingCard\n```\n\n## How To Use\n\nIf you don\'t provide `path` then the method will return `bytes` which can directly be used in discord.py/disnake/pycord/nextcord \'s `File class`.\n\n\n<br>\n\n\n## Example\n\n`since no path was given, it returns bytes which can directly be used in discord.py and its fork \'s File class.`\n\n```py\n\nfrom disnake.ext import commands\nfrom DiscordLevelingCard import RankCard, Settings\nimport disnake\n\nclient = commands.Bot()\n# define background, bar_color, text_color at one place\ncard_settings = Settings(\n    background="url or path to background image",\n    text_color="white",\n    bar_color="#000000"\n)\n\n@client.slash_command(name="rank")\nasync def user_rank_card(ctx, user:disnake.Member):\n    await ctx.response.defer()\n    a = RankCard(\n        settings=card_settings\n        background=user.banner.url,\n        avatar=user.display_avatar.url,\n        level=1,\n        current_exp=1,\n        max_exp=1,\n        username="cool username"\n    )\n    image = await a.card1()\n    await ctx.edit_original_message(file=disnake.File(image, filename="rank.png")) # providing filename is very important\n\n```\n\n<br>\n\n## Documentation\n\n\n<details>\n\n<summary> <span style="color:yellow">RankCard</span> class</summary>\n\n<br>\n\n`__init__` method\n\n```py\nRankCard(\n    settings: Settings,\n    avatar:str,\n    level:int,\n    current_exp:int,\n    max_exp:int,\n    username:str,\n)\n```\n\n- `settings` - Settings class from DiscordLevelingCard.\n\n- `avatar` - avatar image url.\n\n- `level` - level of the user.\n\n- `current_exp` - current exp of the user.\n\n- `max_exp` - max exp of the user.\n\n- `username` - username of the user.\n- \n</details>\n\n<details>\n\n<summary> <span style="color:yellow">Settings</span> class</summary>\n\n<br>\n\n`__init__` method\n\n```py\nRankCard(\n    backgroud: Union[PathLike, BufferedIOBase, str],\n    bar_color: Optional[str] = \'white\',\n    text_color: Optional[str] = \'white\'\n\n)\n```\n\n- `background` - background image url or file-object in `rb` mode.\n\n- `bar_color` - color of the bar [example: "white" or "#000000"]\n\n- `text_color` - color of the text [example: "white" or "#000000"]\n\n</details>\n\n\n<details>\n\n<summary> <span style="color:yellow">card1</span> method</summary>\n\n\n```py\nRankCard.card1()\n```\n\n`returns` - `bytes` which can directly be used within `discord.File` class.\n\n\n\n![card1](https://cdn.discordapp.com/attachments/907213435358547968/994620579816681572/unknown.png)\n\n<br>\n\n</details>',
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
