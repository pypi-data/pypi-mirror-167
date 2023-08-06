# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prefapi']

package_data = \
{'': ['*']}

install_requires = \
['UrsinaNetworking>=2.1.4,<3.0.0']

setup_kwargs = {
    'name': 'prefapi',
    'version': '0.2a1',
    'description': 'API for Pref game servers',
    'long_description': 'No description yet. I will add it later :D',
    'author': 'Cubic',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
