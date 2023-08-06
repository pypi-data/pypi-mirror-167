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
    'version': '0.1.6',
    'description': 'A library with leveling cards for your discord bot.',
    'long_description': '# DiscordLevelingCard\nA library with Rank cards for your discord bot.\n\n\n\n## card preview\n\n`card1`\n\n![card1](https://cdn.discordapp.com/attachments/907213435358547968/994620579816681572/unknown.png)\n\n\n<br>\n\n\n## How To Use\n\nIf you don\'t provide `path` then the method will return `bytes` which can directly be used in discord.py/disnake/pycord/nextcord \'s `File class`.\n\n\n<br>\n\n\n## Example\n\n```py\n\nfrom disnake.ext import commands\nfrom DiscordLevelingCard import RankCard\nimport disnake\n\nclient = commands.Bot()\n\n@client.slash_command(name="rank")\nasync def user_rank_card(ctx, user:disnake.Member):\n    await ctx.response.defer()\n    a = RankCard(\n        background="./my_cool_background.png",\n        avatar=user.display_avatar.url,\n        level=1,\n        current_exp=1,\n        max_exp=1,\n        username="cool username",\n        type="disnake"\n    )\n    image = await a.card1()\n    await ctx.edit_original_message(file=image)\n\n```\n\n`or you can use no type`\n\n```py\n@client.slash_command(name="rank")\nasync def user_rank_card(ctx, user:disnake.Member):\n    await ctx.response.defer()\n    a = RankCard(\n        background=user.banner.url,\n        avatar=user.display_avatar.url,\n        level=1,\n        current_exp=1,\n        max_exp=1,\n        username="cool username"\n    )\n    image = await a.card1()\n    await ctx.edit_original_message(file=disnake.File(image))\n```\n\n`if you want to use path`\n```py\n@client.slash_command(name="rank")\nasync def user_rank_card(ctx, user:disnake.Member):\n    await ctx.response.defer()\n    a = RankCard(\n        background=user.banner.url,\n        avatar=user.display_avatar.url,\n        level=1,\n        current_exp=1,\n        max_exp=1,\n        username="cool username",\n        bar_color="red",\n        text_color="white",\n        path="./user_cards/rank_card.png"\n    )\n    # image return the path provided i.e. "./user_cards/rank_card.png"\n    image = await a.card1()\n    await ctx.edit_original_message(file=disnake.File(image))\n```',
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
