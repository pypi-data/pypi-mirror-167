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
    'version': '1.0b2',
    'description': 'Django (DRF) backed app for managing Zapier triggers.',
    'long_description': '# Django Zapier Triggers\n\nDjango (DRF) app for managing Zapier triggers.\n\n### Version support\n\nThis app supports Django 3.2+ and Python 3.10+.\n\n## Background\n\nThis app provides the minimal scaffolding required to support Zapier triggers in your Django application. It is based on DRF.\n\nIn addition to the `zapier.triggers` Django app, this project includes two additional applications: a complete Zapier CLI application that you can publish to Zapier, and a Demo project that provides the Django support for it. With these two projects you have a complete end-to-end Zapier integration.\n\n## Zapier Triggers\n\nA Zapier trigger is an event source for Zapier workflows ("Zaps"), that can operate in one of two modes - "Instant", or "Polling". Either way the net result is that JSON data objects are received by Zapier and can be used as the first step in a Zap.\n\nThere is a _lot_ of documentation online from Zapier about how to create a trigger, and I would strongly recommend reading it before attempting to build your own. Here are a couple of good articles to start with:\n\n- https://platform.zapier.com/docs/start\n- https://platform.zapier.com/cli_tutorials/getting-started\n\n### Prequisites\n\nIf you want to run the end-to-end demo you will need:\n\n1. A Zapier account\n2. The Zapier CLI\n3. ngrok, or some equivalent tunnelling software\n\n## What\'s in the box?\n\nThe core implementation detail of this package is the `TriggerView`. This is a DRF `APIView` class that handles `GET`, `POST`, and `DELETE` methods, mapping them to the Zapier trigger methods for polling ("list"), susbscribe and unsubscribe functions.\n\n### `GET /triggers/{{trigger}}/`\n\nWhen Zapier makes a `GET` request to your application endpoint one of two things is happening. For a REST Hook ("Instant") trigger this is request sample data that Zapier can use to create its Zap builder UI. If your trigger is a push ("Instant") then you can just return static data - as long as it conforms to the same schema as real data. The `demo.views.new_book` view demonstrates this.\n\nIf your trigger is a polling trigger then this endpoint should return real data - the `demo.views.new_film` view is an example of this.\n\nThe view returns a `200` status code.\n\n### `POST /triggers/{{trigger}}/subscriptions/`\n\nWhen Zapier makes a `POST` request it is expecting to create a new webhook (rebranded "REST Hook" by Zapier) susbscription. This is handled automatically by the view, which creates a new `TriggerSubscription` object for the user + trigger combination, and returns the `uuid` property to Zapier, which stores it in its `bundle.subscriptionData.id` property.\n\nThe view returns a `201` status code.\n\n### `DELETE /triggers/{{trigger}}/subscriptions/{{subscription_id}}`\n\nWhen Zapier makes a `DELETE` request it is expecting to delete the subscription identified by the `subscription_id` value, which maps to the `uuid` property. We do not delete the subscription but instead mark it as "inactive". This is because we record all of the event data that is sent by a trigger subscription, and we we want to keep this for a period for auditing purposes. If a new `POST` request is made for the same user + trigger combination the subscription is reactivated.\n\nThe view returns a `204` status code.\n\n## Settings\n\nThe settings are all read in from the Django setting `ZAPIER_TRIGGER`, which is a dict containing the following keys:\n\n* `STRICT_MODE`\n\nThe JSON key used to extract the Zapier subscription URL endpoint in the body of the `POST` request - defaults to `hookUrl`.\n\n* `TRIGGERS`\n\nThis is a dict containing the name of the trigger and a string path to a view-like function that must accept a single `Request` arg and return a list of JSON-serializable dict objects. Every trigger that your Zapier app supports must be in this setting - otherwise any request made to `/triggers/{{trigger}}` will return a `404`.\n\n## Demo + zapier-app\n\nThe easiest way to work out how this all fits together is to run the demo app and push the zapier-app to Zapier under your own account.\n',
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
