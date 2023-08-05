# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['markymark', 'markymark.extensions', 'markymark.templatetags']

package_data = \
{'': ['*'],
 'markymark': ['static/markymark/css/*',
               'static/markymark/extensions/*',
               'static/markymark/fontawesome/*',
               'static/markymark/js/*',
               'templates/markymark/*']}

install_requires = \
['Django>=3.2,<4', 'Markdown>=3.4']

extras_require = \
{'docs': ['Sphinx>=5.1', 'django-anylink>=2.0.1', 'django-filer>=2.2.3']}

setup_kwargs = {
    'name': 'django-markymark',
    'version': '3.0.0',
    'description': 'django-markymark provides helpers and tools to integrate markdown.',
    'long_description': "django-markymark\n================\n\n.. image:: https://img.shields.io/pypi/v/django-markymark.svg\n   :target: https://pypi.org/project/django-markymark/\n   :alt: Latest Version\n\n.. image:: https://github.com/stephrdev/django-markymark/workflows/Test/badge.svg?branch=master\n   :target: https://github.com/stephrdev/django-markymark/actions?workflow=Test\n   :alt: CI Status\n\n.. image:: https://codecov.io/gh/stephrdev/django-markymark/branch/master/graph/badge.svg\n   :target: https://codecov.io/gh/stephrdev/django-markymark\n   :alt: Coverage Status\n\n.. image:: https://readthedocs.org/projects/django-markymark/badge/?version=latest\n   :target: https://django-markymark.readthedocs.io/en/stable/?badge=latest\n   :alt: Documentation Status\n\n\n*django-markymark* provides helpers and tools to integrate markdown into Django.\n\n\nFeatures\n--------\n\n* Django form fields to integrate the bootstrap markdown editor (without the dependency on bootstrap)\n* `django-filer <https://github.com/divio/django-filer>`_ integration\n* `django-anylink <https://github.com/moccu/django-anylink>`_ integration\n\n\nRequirements\n------------\n\ndjango-markymark supports Python 3 only and requires at least Django 3.2\n\n\nPrepare for development\n-----------------------\n\nA Python 3 interpreter is required in addition to Poetry.\n\n.. code-block:: shell\n\n    $ poetry install\n\n\nNow you're ready to start the example project to experiment with markymark.\n\n.. code-block:: shell\n\n    $ poetry run python examples/manage.py runserver\n\n\nResources\n---------\n\n* `Documentation <https://django-markymark.readthedocs.org/>`_\n* `Bug Tracker <https://github.com/stephrdev/django-markymark/issues>`_\n* `Code <https://github.com/stephrdev/django-markymark/>`_\n",
    'author': 'Stephan Jaekel',
    'author_email': 'steph@rdev.info',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/stephrdev/django-markymark',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
