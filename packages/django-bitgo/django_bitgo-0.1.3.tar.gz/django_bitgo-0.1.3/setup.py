# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_bitgo', 'django_bitgo.migrations', 'django_bitgo.wallets']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.2.14,<4.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'django-bitgo',
    'version': '0.1.3',
    'description': 'Django app for bitGo',
    'long_description': "# django_bitgo\n\nDjango library for BitGo\n\n[![Downloads](https://static.pepy.tech/personalized-badge/django-bitgo?period=month&units=international_system&left_color=black&right_color=blue&left_text=Downloads)](https://pepy.tech/project/django-bitgo)\n\n# Overview\n\nDjango BitGo is a powerful and flexible library for connecting your BitGo account and integrate it with your Django project.\n\n---\n\n# Requirements\n\n- Python (3.7, 3.8, 3.9, 3.10)\n- Django (3.2, 4.0, 4.1)\n\nWe **highly recommend** and only officially support the latest patch release of\neach Python and Django series.\n\n# Installation\n\nInstall using `pip` ...\n\n    pip install django-bitgo\n\nInstall using `poetry` ...\n\n```\npoetry add django-bitgo\n```\n\nAdd `'django_bitgo'` to your `INSTALLED_APPS` setting.\n\n```python\nINSTALLED_APPS = [\n    ...\n    'django_bitgo',\n]\n```\n\n# API Reference\n\n## The `wallets` module\n\nThe top-level module for wallets.\n\nRefer to the [documentation](https://api.bitgo.com/docs/#tag/Address) for details on the use of this package.\n\n### Address\n\nExample of get an address object.\n\n```\n    address = Address()\n    address.get_address(address_id=ADDRESS_ID, coin=COIN, wallet_id=WALLET_ID)\n```\n",
    'author': 'panosangelopoulos',
    'author_email': 'panos.angelopoulos@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/panosangelopoulos/django_bitgo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
