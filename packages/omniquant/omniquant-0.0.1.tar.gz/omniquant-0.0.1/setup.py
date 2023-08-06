# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['omniquant']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'omniquant',
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'LoloPopoPy',
    'author_email': 'legregam@insa-toulouse.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
