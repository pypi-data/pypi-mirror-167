# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['river_extra',
 'river_extra.compat',
 'river_extra.metrics',
 'river_extra.metrics.cluster']

package_data = \
{'': ['*']}

install_requires = \
['river==0.12.1']

setup_kwargs = {
    'name': 'river-extra',
    'version': '0.13.0',
    'description': 'Additional estimators for the River package',
    'long_description': None,
    'author': 'MaxHalford',
    'author_email': 'maxhalford25@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0',
}


setup(**setup_kwargs)
