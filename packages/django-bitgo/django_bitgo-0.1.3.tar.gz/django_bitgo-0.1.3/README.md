# django_bitgo

Django library for BitGo

[![Downloads](https://static.pepy.tech/personalized-badge/django-bitgo?period=month&units=international_system&left_color=black&right_color=blue&left_text=Downloads)](https://pepy.tech/project/django-bitgo)

# Overview

Django BitGo is a powerful and flexible library for connecting your BitGo account and integrate it with your Django project.

---

# Requirements

- Python (3.7, 3.8, 3.9, 3.10)
- Django (3.2, 4.0, 4.1)

We **highly recommend** and only officially support the latest patch release of
each Python and Django series.

# Installation

Install using `pip` ...

    pip install django-bitgo

Install using `poetry` ...

```
poetry add django-bitgo
```

Add `'django_bitgo'` to your `INSTALLED_APPS` setting.

```python
INSTALLED_APPS = [
    ...
    'django_bitgo',
]
```

# API Reference

## The `wallets` module

The top-level module for wallets.

Refer to the [documentation](https://api.bitgo.com/docs/#tag/Address) for details on the use of this package.

### Address

Example of get an address object.

```
    address = Address()
    address.get_address(address_id=ADDRESS_ID, coin=COIN, wallet_id=WALLET_ID)
```
