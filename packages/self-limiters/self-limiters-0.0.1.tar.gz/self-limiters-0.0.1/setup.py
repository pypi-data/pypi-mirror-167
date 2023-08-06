# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['self_limiters']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'self-limiters',
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'Sondre Lillebø Gundersen',
    'author_email': 'sondrelg@live.no',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
