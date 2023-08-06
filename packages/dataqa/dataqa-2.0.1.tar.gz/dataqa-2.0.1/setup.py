# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dataqa', 'dataqa.tests']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.4,<2.0.0', 'pytest>=7.1.3,<8.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'dataqa',
    'version': '2.0.1',
    'description': 'Python Client library for DataQA',
    'long_description': None,
    'author': 'Maria Mestre',
    'author_email': 'maria@dataqa.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
