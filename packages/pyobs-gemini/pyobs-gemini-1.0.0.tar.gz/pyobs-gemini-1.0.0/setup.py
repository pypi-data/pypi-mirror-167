# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyobs_gemini']

package_data = \
{'': ['*']}

install_requires = \
['aioserial>=1.3,<2.0', 'astropy>=5.1,<6.0', 'pyobs-core>=1.0,<2.0']

setup_kwargs = {
    'name': 'pyobs-gemini',
    'version': '1.0.0',
    'description': 'pyobs module for Optec Gemini focusser/rotator',
    'long_description': 'None',
    'author': 'Tim-Oliver Husser',
    'author_email': 'thusser@uni-goettingen.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
