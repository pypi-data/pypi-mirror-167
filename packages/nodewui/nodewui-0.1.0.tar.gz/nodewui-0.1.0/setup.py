# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nodewui']

package_data = \
{'': ['*'], 'nodewui': ['media/*']}

install_requires = \
['CherryPy>=18.8.0,<19.0.0']

setup_kwargs = {
    'name': 'nodewui',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'uak',
    'author_email': '4626956-uak@users.noreply.gitlab.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
