# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['click_skeleton']

package_data = \
{'': ['*']}

install_requires = \
['click-aliases>=1.0.1,<2.0.0',
 'click-completion>=0.5.0,<0.6.0',
 'click-didyoumean>=0.3.0,<0.4.0',
 'click-help-colors>=0.9,<0.10',
 'click-option-group>=0.5.1,<0.6.0',
 'click>=8.0.1,<9.0.0',
 'dotmap>=1.3.30,<2.0.0',
 'requests>=2.24.0,<3.0.0',
 'semver>=2.10.2,<3.0.0',
 'types-requests>=2.25.0,<3.0.0']

setup_kwargs = {
    'name': 'click-skeleton',
    'version': '0.26',
    'description': 'Click app skeleton',
    'long_description': 'None',
    'author': 'Adrien Pensart',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
