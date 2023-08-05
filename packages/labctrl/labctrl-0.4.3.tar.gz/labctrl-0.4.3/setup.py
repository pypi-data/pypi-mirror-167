# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['labctrl']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'Pyro5>=5.13.1,<6.0.0',
 'h5py>=3.6.0,<4.0.0',
 'loguru>=0.6.0,<0.7.0',
 'numpy>=1.21.3,<2.0.0']

entry_points = \
{'console_scripts': ['server = labctrl.server:main']}

setup_kwargs = {
    'name': 'labctrl',
    'version': '0.4.3',
    'description': 'A unified framework for controlling and visualizing data collected from programmable lab instruments',
    'long_description': 'None',
    'author': 'Atharv Joshi',
    'author_email': 'atharvjoshi@ymail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
