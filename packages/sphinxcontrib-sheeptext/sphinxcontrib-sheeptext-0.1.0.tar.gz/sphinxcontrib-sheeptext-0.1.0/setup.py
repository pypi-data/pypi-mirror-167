# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sphinxcontrib_sheeptext']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0']

setup_kwargs = {
    'name': 'sphinxcontrib-sheeptext',
    'version': '0.1.0',
    'description': 'Render SheepText diagrams in Sphinx',
    'long_description': '',
    'author': 'Asim Ihsan',
    'author_email': 'asim@ihsan.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
