# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mait_manager']

package_data = \
{'': ['*']}

install_requires = \
['typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['mait = mait_manager.main:app']}

setup_kwargs = {
    'name': 'mait-manager',
    'version': '0.1.6.1',
    'description': '',
    'long_description': '# mait: package manager for text adventure games.\n![154_mait](https://user-images.githubusercontent.com/66521670/189254832-397db858-b949-4ffa-9593-c041cebf3a7b.gif)\n\n### Installing is by the PIP manager [Linux]\n```commandline\npip3 install mait-manager\n```\n### Similar for [Windows]\n```commandline\npy -m pip install mait-manager\n```\n***You invoke mait via CLI by using the following:***\n```commandline\nmait --help\n```\n\n# uploading.\n[![upload-mait.gif](https://i.postimg.cc/BvKq5Gjq/upload-mait.gif)](https://postimg.cc/B8J9sk5y)\nThe above demonstrates how to upload a single file **(You can now upload folders in 0.1.5.4v!!!)**\n### Uploading.\n```commandline\nmait upload\n```\nCode must be source code! Compiled sources are not allowed!\n### Providing a JSON.\n```json\n{\n  "name": "Donuts!!!",\n  "short": "I do donuts",\n  "long": "Now this is a long description.",\n  "creator": "@Porplax",\n  "exec": "python3 donut.py"\n}\n```\nA JSON provides the command to compile/or interpret the code & **is required**.\n\nYou must put it in the parent directory of your project.',
    'author': 'Zayne Marsh',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
