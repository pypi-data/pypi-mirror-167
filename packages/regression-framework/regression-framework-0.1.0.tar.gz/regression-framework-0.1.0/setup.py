# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['regression_framework',
 'regression_framework.bp',
 'regression_framework.dmo',
 'regression_framework.svc']

package_data = \
{'': ['*']}

install_requires = \
['baseblock']

setup_kwargs = {
    'name': 'regression-framework',
    'version': '0.1.0',
    'description': 'Provide a Framework for Regression Testing',
    'long_description': None,
    'author': 'Craig Trim',
    'author_email': 'craigtrim@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.8.5',
}


setup(**setup_kwargs)
