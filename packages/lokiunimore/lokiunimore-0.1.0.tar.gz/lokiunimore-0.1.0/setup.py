# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lokiunimore',
 'lokiunimore.config',
 'lokiunimore.matrix',
 'lokiunimore.matrix.templates',
 'lokiunimore.sql',
 'lokiunimore.utils',
 'lokiunimore.web',
 'lokiunimore.web.extensions']

package_data = \
{'': ['*'], 'lokiunimore.web': ['static/*', 'templates/*']}

install_requires = \
['Authlib>=1.0.1,<2.0.0',
 'Flask-SQLAlchemy>=2.5.1,<3.0.0',
 'Flask>=2.2.2,<3.0.0',
 'cfig[cli]>=0.3.0,<0.4.0',
 'coloredlogs>=15.0.1,<16.0.0',
 'gunicorn>=20.1.0,<21.0.0',
 'matrix-nio[e2e]>=0.19.0,<0.20.0',
 'psycopg2>=2.9.3,<3.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['lokiunimore = lokiunimore.__main__:main']}

setup_kwargs = {
    'name': 'lokiunimore',
    'version': '0.1.0',
    'description': 'Matrix room gatekeeper bot for the unofficial Unimore space',
    'long_description': '# `lokiunimore`\n\nMatrix room gatekeeper bot for the unofficial Unimore space\n',
    'author': 'Stefano Pigozzi',
    'author_email': 'me@steffo.eu',
    'maintainer': 'Stefano Pigozzi',
    'maintainer_email': 'me@steffo.eu',
    'url': 'https://github.com/Steffo99/lokiunimore',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
