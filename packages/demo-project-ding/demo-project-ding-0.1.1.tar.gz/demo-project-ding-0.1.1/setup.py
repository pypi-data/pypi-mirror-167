# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_tutorial_project', 'poetry_tutorial_project.util']

package_data = \
{'': ['*'], 'poetry_tutorial_project': ['static/*']}

setup_kwargs = {
    'name': 'demo-project-ding',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Python Poetry Tutorial\n\n![Python](https://img.shields.io/badge/Python-v3.8-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)\n![Psutil](https://img.shields.io/badge/psutil-v5.6.7-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)\n![Loguru](https://img.shields.io/badge/Loguru-v0.4.1-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)\n![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c&logo=GitHub)\n[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/python-poetry-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/python-poetry-tutorial/issues)\n[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/python-poetry-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/python-poetry-tutorial/stargazers)\n[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/python-poetry-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/python-poetry-tutorial/network)\n\n![Poetry](poetry_tutorial_project/static/social.jpg)\n\n## Getting Started\n\nRun the following to install and launch the demo app using [Poetry](https://python-poetry.org/):\n\n```shell\n$ git clone https://github.com/hackersandslackers/python-poetry-tutorial.git\n$ cd python-poetry-tutorial\n$ poetry shell\n$ poetry install\n$ poetry run\n```\n\n-----\n\n**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.\n',
    'author': 'shengqin ding',
    'author_email': 'dshengq@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
