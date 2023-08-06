# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['demo_project']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'demo-project-ding',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
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
