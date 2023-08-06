# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['norsvinpy']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.3,<2.0.0', 'requests>=2.28.1,<3.0.0', 'scipy>=1.9.1,<2.0.0']

setup_kwargs = {
    'name': 'norsvinpy',
    'version': '0.1.3',
    'description': 'Python development in Norsvin',
    'long_description': '# Norsvinpy\n\nRepository of useful functions in use in Norsvin',
    'author': 'Christopher',
    'author_email': 'christopher.coello@norsvin.no',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.12',
}


setup(**setup_kwargs)
