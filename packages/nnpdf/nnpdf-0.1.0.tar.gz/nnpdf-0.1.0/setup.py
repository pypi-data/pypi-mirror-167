# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nnpdf']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'nnpdf',
    'version': '0.1.0',
    'description': 'NNPDF ecosystem meta-package',
    'long_description': '',
    'author': 'Alessandro Candido',
    'author_email': 'candido.ale@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
