# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asyncakinator']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0']

setup_kwargs = {
    'name': 'asyncakinator',
    'version': '1.5.2',
    'description': 'An async API wrapper for Akinator, written in Python.',
    'long_description': 'asyncakinator\n=============\n\n\n.. image:: https://discord.com/api/guilds/751490725555994716/embed.png\n   :target: https://discord.gg/muTVFgDvKf\n   :alt: Support Server Invite\n\nAn async API wrapper for the online game, Akinator, written in Python.\n\n`Akinator <https://en.akinator.com/>`_ is a web-based game which tries to determine what character you are thinking of by asking a series of questions.\n\n\nInstalling\n----------\n\nTo install, just run the following command:\n\n.. code-block:: shell\n\n    # MacOS/Linux\n    python3 -m pip install -U asyncakinator\n\n    # Windows\n    py -3 -m pip install -U asyncakinator\n\n\nRequirements\n~~~~~~~~~~~~\n- Python ≥3.9\n\n- ``aiohttp``\n\n\nDocumentation\n-------------\nDocumention can be found `here. <https://asyncakinator.readthedocs.io/en/latest/>`_\n\n\nQuick Examples\n--------------\n\nHere\'s a quick little example of the library being used to make a simple, text-based Akinator game:\n\n.. code-block:: python\n\n    import asyncio\n\n    from asyncakinator import (\n        Akinator,\n        Answer,\n        CanNotGoBack,\n        InvalidAnswer,\n        Language,\n        NoMoreQuestions,\n        Theme\n    )\n\n\n    game = Akinator(\n        language=Language.ENGLISH,\n        theme=Theme.ANIMALS,\n    )\n\n\n    async def main():\n        question = await game.start()\n\n        while game.progression <= 80:\n            print(question)\n            user_input = input("Answer:  ")\n            try:\n                answer = Answer.from_str(user_input)\n            except InvalidAnswer:\n                print("Invalid answer")\n                continue\n            try:\n                question = await game.answer(answer)\n            except CanNotGoBack:\n                print("This is the first question, you can\'t go back.")\n                continue\n            except NoMoreQuestions:\n                break\n\n        await game.win()\n\n        correct = input(\n            f"You are thinking of {game.first_guess.name} ({game.first_guess.description}). "\n            f"Am I correct?\\n{game.first_guess.absolute_picture_path}\\n---\\nAnswer:  "\n        )\n        if Answer.from_str(correct) == Answer.YES:\n            print("Nice.")\n        else:\n            print("Maybe next time.")\n        await game.close()\n\n\n    asyncio.run(main())',
    'author': 'avizum',
    'author_email': 'juliusrt@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/avizum/asyncakinator',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
