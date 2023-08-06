# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blueye',
 'blueye.protocol',
 'blueye.protocol.services',
 'blueye.protocol.types']

package_data = \
{'': ['*']}

install_requires = \
['proto-plus>=1.22.0,<2.0.0']

setup_kwargs = {
    'name': 'blueye.protocol',
    'version': '3.0.0',
    'description': 'Protobuf-based protocol definitions for the Blueye drones',
    'long_description': '# blueye.protocol\n\n`blueye.protocol` is a python package generated from the Protobuf API defined in [ProtocolDefintions](https://github.com/BluEye-Robotics/ProtocolDefinitions).\n\nIt is generated with the [proto-plus library](https://proto-plus-python.readthedocs.io/en/latest/) create a more Pythonic way to interact with protocol buffers.\n\n## Usage\nThe primary user of this package is the [blueye.sdk](https://github.com/blueye-robotics/blueye.sdk). The SDK configures the necessary ZeroMQ sockets and wraps everything up in an easy to use Python-object, allowing you to control the Blueye drones remotely.\n',
    'author': 'Sindre Hansen',
    'author_email': 'sindre.hansen@blueye.no',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://www.blueyerobotics.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
