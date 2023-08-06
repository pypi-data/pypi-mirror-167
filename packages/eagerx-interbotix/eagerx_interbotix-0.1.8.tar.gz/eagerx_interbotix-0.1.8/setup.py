# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eagerx_interbotix',
 'eagerx_interbotix.camera',
 'eagerx_interbotix.ik',
 'eagerx_interbotix.overlay',
 'eagerx_interbotix.reset',
 'eagerx_interbotix.safety',
 'eagerx_interbotix.solid',
 'eagerx_interbotix.solid.real',
 'eagerx_interbotix.xseries',
 'eagerx_interbotix.xseries.pybullet',
 'eagerx_interbotix.xseries.real']

package_data = \
{'': ['*'],
 'eagerx_interbotix.camera': ['assets/*'],
 'eagerx_interbotix.solid': ['assets/*']}

install_requires = \
['eagerx-pybullet>=0.1.10,<0.2.0',
 'eagerx-reality>=0.1.12,<0.2.0',
 'modern_robotics>=1.1.0,<2.0.0',
 'opencv-contrib-python>=4.6.0,<5.0.0',
 'scipy>=1.0,<2.0',
 'stable-baselines3[extra]>=1.5.0,<2.0.0',
 'urdf-parser-py>=0.0.4,<0.0.5',
 'xacro>=1.13.3,<2.0.0']

setup_kwargs = {
    'name': 'eagerx-interbotix',
    'version': '0.1.8',
    'description': 'EAGERx interface to interbotix robot arms.',
    'long_description': 'None',
    'author': 'Jelle Luijkx',
    'author_email': 'j.d.luijkx@tudelft.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/eager-dev/eagerx_interbotix',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
