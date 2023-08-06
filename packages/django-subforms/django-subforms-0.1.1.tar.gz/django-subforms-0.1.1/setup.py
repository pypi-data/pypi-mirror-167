# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['subforms', 'subforms.migrations', 'subforms.templatetags']

package_data = \
{'': ['*'],
 'subforms': ['locale/fi/LC_MESSAGES/*',
              'static/css/*',
              'static/js/*',
              'templates/subforms/*']}

install_requires = \
['Django>=3.1']

setup_kwargs = {
    'name': 'django-subforms',
    'version': '0.1.1',
    'description': 'Wrap django forms as fields and fields as dynamic arrays.',
    'long_description': '# Django Subforms\n\n[![Coverage Status][coverage-badge]][coverage]\n[![GitHub Workflow Status][status-badge]][status]\n[![PyPI][pypi-badge]][pypi]\n[![GitHub][licence-badge]][licence]\n[![GitHub Last Commit][repo-badge]][repo]\n[![GitHub Issues][issues-badge]][issues]\n[![Downloads][downloads-badge]][pypi]\n[![Python Version][version-badge]][pypi]\n\n```shell\npip install django-subforms\n```\n\n---\n\n**Documentation**: [https://mrthearman.github.io/django-subforms/](https://mrthearman.github.io/django-subforms/)\n\n**Source Code**: [https://github.com/MrThearMan/django-subforms/](https://github.com/MrThearMan/django-subforms/)\n\n---\n\nThis library adds two new fields: `NestedFormField`, which can wrap forms as fields on another form\nand thus provide validation for, e.g., a JSON field, and `DynamicArrayField`, which can wrap\nfields, including `NestedFormField`, as dynamically expandable lists of fields.\n\n![Example image](https://github.com/MrThearMan/django-subforms/raw/main/docs/img/example.png)\n\n[coverage-badge]: https://coveralls.io/repos/github/MrThearMan/django-subforms/badge.svg?branch=main\n[status-badge]: https://img.shields.io/github/workflow/status/MrThearMan/django-subforms/Test\n[pypi-badge]: https://img.shields.io/pypi/v/django-subforms\n[licence-badge]: https://img.shields.io/github/license/MrThearMan/django-subforms\n[repo-badge]: https://img.shields.io/github/last-commit/MrThearMan/django-subforms\n[issues-badge]: https://img.shields.io/github/issues-raw/MrThearMan/django-subforms\n[version-badge]: https://img.shields.io/pypi/pyversions/django-subforms\n[downloads-badge]: https://img.shields.io/pypi/dm/django-subforms\n\n[coverage]: https://coveralls.io/github/MrThearMan/django-subforms?branch=main\n[status]: https://github.com/MrThearMan/django-subforms/actions/workflows/test.yml\n[pypi]: https://pypi.org/project/django-subforms\n[licence]: https://github.com/MrThearMan/django-subforms/blob/main/LICENSE\n[repo]: https://github.com/MrThearMan/django-subforms/commits/main\n[issues]: https://github.com/MrThearMan/django-subforms/issues\n',
    'author': 'Matti Lamppu',
    'author_email': 'lamppu.matti.akseli@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://mrthearman.github.io/django-subforms/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
