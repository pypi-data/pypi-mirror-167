# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['downloader_app']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'downloader-app',
    'version': '1.0.0',
    'description': 'The routines available in this package are designed to capture and process satellite images',
    'long_description': '# downloader_app',
    'author': 'Flavio Codeco Coelho',
    'author_email': 'fccoelho@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/esloch/downloader_app',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
