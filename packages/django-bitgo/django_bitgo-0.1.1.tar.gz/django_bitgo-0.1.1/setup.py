# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_bitgo', 'django_bitgo.migrations']

package_data = \
{'': ['*']}

install_requires = \
['Django>=4.1.1,<5.0.0', 'black>=22.8.0,<23.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'django-bitgo',
    'version': '0.1.1',
    'description': 'Django app for bitGo',
    'long_description': '# django_bitgo\nDjango library for BitGo\n',
    'author': 'panosangelopoulos',
    'author_email': 'panos.angelopoulos@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/panosangelopoulos/django_bitgo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
