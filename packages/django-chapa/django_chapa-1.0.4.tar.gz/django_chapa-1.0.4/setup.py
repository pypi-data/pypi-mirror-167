# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_chapa', 'django_chapa.migrations']

package_data = \
{'': ['*']}

install_requires = \
['Django>=4.1,<5.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'django-chapa',
    'version': '1.0.4',
    'description': 'Unofficial Django Implementation For Chapa Payment Gateway',
    'long_description': '# Django-Chapa \n\nDjango wrapper for the chapa payment gateway\n\n\n# Instruction\nthis package also includes abstract transaction for chapa\n\n## Installation\n\nrequired python >= 3.6 and django >=3.2 installed\n\n```\npip install django-chapa\n```\n\n## Django Config\nset your config values in `settings.py`\n\n```\nINSTALLED_APPS = [\n    ...\n    \'django_chapa\',\n    ...\n]\n\nCHAPA_SECRET = "Secret"\n\nCHAPA_API_URL = \'\'\n\nCHAPA_API_VERSION = \'v1\'\n\n```\n\nadd webhook url in `urls.py` \n\n```\nurlpatterns = [\n    path(\'chapa-webhook\', include(\'django_chapa.urls\'))\n]\n```\n\n- if you are using default chapa transaction model run `./manage.py migrate`\n\n\nregister your chapa transaction model in    ``settings.py``\n\n```CHAPA_TRANSACTION_MODEL = \'yourapp.chapa_model```\n\n- Note: your chapa transaction model should implement ``django_chapa.models.ChapaTransactionMixin``\n    \n    - or must contain required fields for the webhook to work properly',
    'author': 'abelayalew',
    'author_email': 'abelayalew81@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/abelayalew/django-chapa',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
