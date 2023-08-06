# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fieldedge_pcap']

package_data = \
{'': ['*']}

install_requires = \
['pyshark>=0.5.3,<0.6.0']

setup_kwargs = {
    'name': 'fieldedge-pcap',
    'version': '0.3.0',
    'description': 'Library and models for working with packet capture and analysis.',
    'long_description': None,
    'author': 'geoffbrucepayne',
    'author_email': 'geoff.bruce-payne@inmarsat.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
