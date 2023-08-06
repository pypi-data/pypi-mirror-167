# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['downloader_app']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'downloader-app',
    'version': '0.1.0',
    'description': 'The routines available in this package are designed to capture and process satellite images',
    'long_description': None,
    'author': 'Flavio Codeco Coelho',
    'author_email': 'fccoelho@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
