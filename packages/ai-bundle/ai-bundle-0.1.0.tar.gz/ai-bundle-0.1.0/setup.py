# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ai_bundle']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.84.0,<0.85.0', 'uvicorn>=0.18.3,<0.19.0']

setup_kwargs = {
    'name': 'ai-bundle',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Toufik Al Khawli',
    'author_email': 'toufik.al.khawli@pwc.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
