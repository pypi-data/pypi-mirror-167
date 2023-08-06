# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nodewui']

package_data = \
{'': ['*'], 'nodewui': ['media/*']}

install_requires = \
['CherryPy>=18.8.0,<19.0.0', 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['nodewui = nodewui.app:run']}

setup_kwargs = {
    'name': 'nodewui',
    'version': '0.1.1',
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
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
