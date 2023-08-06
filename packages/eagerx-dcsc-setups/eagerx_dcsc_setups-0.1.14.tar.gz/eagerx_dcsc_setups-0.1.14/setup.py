# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eagerx_dcsc_setups',
 'eagerx_dcsc_setups.pendulum',
 'eagerx_dcsc_setups.pendulum.ode',
 'eagerx_dcsc_setups.pendulum.real']

package_data = \
{'': ['*']}

install_requires = \
['eagerx-gui>=0.2.14,<0.3.0',
 'eagerx-ode>=0.1.26,<0.2.0',
 'eagerx-reality>=0.1.12,<0.2.0',
 'eagerx>=0.1.32,<0.2.0',
 'stable-baselines3>=1.2.0,<2.0.0',
 'tensorboard>=2.9.0,<3.0.0']

setup_kwargs = {
    'name': 'eagerx-dcsc-setups',
    'version': '0.1.14',
    'description': 'EAGERx interface to dcsc_setups.',
    'long_description': 'None',
    'author': 'Jelle Luijkx',
    'author_email': 'j.d.luijkx@tudelft.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/eager-dev/eagerx_dcsc_setups',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
