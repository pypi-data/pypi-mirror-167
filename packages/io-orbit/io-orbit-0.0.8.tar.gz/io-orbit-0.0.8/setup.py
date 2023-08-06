# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['io_orbit',
 'io_orbit.cloud_configurations',
 'io_orbit.events',
 'io_orbit.logger',
 'io_orbit.workflow']

package_data = \
{'': ['*']}

install_requires = \
['firebase-admin>=5.2.0,<6.0.0',
 'google-cloud-storage>=2.4.0,<3.0.0',
 'pika>=1.2.0,<2.0.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['io-orbit = io_orbit:main']}

setup_kwargs = {
    'name': 'io-orbit',
    'version': '0.0.8',
    'description': 'Simple and flexible ML workflow engine',
    'long_description': '<br />\n<p align="center">\n  <a href="https://laccuna.com">\n    <img src="https://storage.googleapis.com/io-public-assets/io-arche-logo.png" alt="Logo" width="846" height="448">\n  </a>\n\n  <h3 align="center">🛰 Welcome to ioOrbit. 🛰</h3>\n\n  <p align="center">\n    Simple and flexible ML workflow engine. This library is meant to wrap all reusable code to simplify workflow implementation.\n    <br />\n    <br />\n  </p>\n</p>\n\n\n## Tools 🧰\n\n- Cloud config handler\n- Flexible logger \n- API to communicate with RabbitMQ\n- Workflow helper\n\n\n## License 🔐\n\nLicensed under the Apache License, Version 2.0.',
    'author': 'laccuna',
    'author_email': 'team@laccuna.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
