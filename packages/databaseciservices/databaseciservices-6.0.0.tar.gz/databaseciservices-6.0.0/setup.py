# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['databaseciservices']

package_data = \
{'': ['*']}

install_requires = \
['click', 'migra', 'psycopg2-binary', 'py', 'pyyaml', 'requests']

entry_points = \
{'console_scripts': ['databaseci = databaseci:command.cli']}

setup_kwargs = {
    'name': 'databaseciservices',
    'version': '6.0.0',
    'description': 'databaseci.com client',
    'long_description': '# databaseciservices\n\n## For using DatabaseCI services. Go to [databaseci.com](https://databaseci.com/) for more details.\n',
    'author': 'Robert Lechte',
    'author_email': 'rob@databaseci.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://databaseci.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
