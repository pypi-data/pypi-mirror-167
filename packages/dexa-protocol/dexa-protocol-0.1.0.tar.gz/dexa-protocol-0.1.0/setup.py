# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dexa_protocol',
 'dexa_protocol.v1_0',
 'dexa_protocol.v1_0.handlers',
 'dexa_protocol.v1_0.messages',
 'dexa_protocol.v1_0.messages.marketplace',
 'dexa_protocol.v1_0.messages.negotiation',
 'dexa_protocol.v1_0.models',
 'dexa_protocol.v1_0.routes',
 'dexa_protocol.v1_0.routes.maps',
 'dexa_protocol.v1_0.routes.openapi']

package_data = \
{'': ['*']}

install_requires = \
['acapy-patched==0.5.6-dev1', 'dexa-sdk==0.1.1']

setup_kwargs = {
    'name': 'dexa-protocol',
    'version': '0.1.0',
    'description': 'Hosts Data Disclosure Agreement protocols',
    'long_description': None,
    'author': 'George J Padayatti',
    'author_email': 'george.padayatti@igrant.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
