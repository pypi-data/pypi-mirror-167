# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['extndjson']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'extndjson',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Iain Allan',
    'author_email': 'iain_allan@mac.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
