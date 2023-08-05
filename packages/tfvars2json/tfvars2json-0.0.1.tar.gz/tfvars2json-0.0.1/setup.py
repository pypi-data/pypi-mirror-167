# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tfvars2json']

package_data = \
{'': ['*']}

install_requires = \
['pyhcl>=0.4.4,<0.5.0']

entry_points = \
{'console_scripts': ['tfvars2json = tfvars2json.__main__:main']}

setup_kwargs = {
    'name': 'tfvars2json',
    'version': '0.0.1',
    'description': 'TFvars 2 Json',
    'long_description': None,
    'author': 'Flavio Augusto Rodrigues Tavares',
    'author_email': 'flaviotvrs@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
