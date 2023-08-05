# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zapier',
 'zapier.triggers',
 'zapier.triggers.migrations',
 'zapier.triggers.models']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.2,<5.0',
 'djangorestframework',
 'python-dateutil',
 'pytz',
 'requests']

setup_kwargs = {
    'name': 'django-zapier-trigger',
    'version': '1.0a3',
    'description': 'Django (DRF) backed app for managing Zapier triggers.',
    'long_description': '# Django Zapier Triggers\n\n**DO NOT USE IN PRODUCTION - ALPHA RELEASE**\n\nDjango app for managing Zapier triggers.\n\n### Version support\n\nThis app supports Django 3.2+ (`HttpResponse.headers`), and Python 3.10+.\n\nThis app provides the minimal scaffolding required to support a Zapier\ntrigger in your application. Specifically it supports token-based\nauthentication and endpoints for RestHook and Polling triggers.\n\nAs well as three Django apps (`zapier.contrib.authtoken`,\n`zapier.triggers.hooks` and `zapier.triggers.polling`) this project also\nincludes a working Zapier app (publishable using the Zapier CLI), and a\nDemo django project that you can use to test the Zapier integration.\nWith the Demo app running locally (and available to the internet via\ne.g. ngrok) you can test pushing data to a Zapier "zap".\n\n### Prequisites\n\nIf you want to run the end-to-end demo you will need:\n\n1. A Zapier account\n2. The Zapier CLI\n3. ngrok, or some equivalent tunnelling software\n\n## How does it work?\n\n\n\n## Usage\n',
    'author': 'YunoJuno',
    'author_email': 'code@yunojuno.com',
    'maintainer': 'YunoJuno',
    'maintainer_email': 'code@yunojuno.com',
    'url': 'https://github.com/yunojuno/django-zapier-trigger',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
