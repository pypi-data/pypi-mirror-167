# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pybaqus', 'pybaqus.plot_utils']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.2.1,<4.0.0',
 'numpy>=1.18.2,<2.0.0',
 'pyvista>=0.31.0,<0.32.0',
 'scipy>=1.4.1,<2.0.0',
 'tqdm>=4.62.3,<5.0.0',
 'vtk>=9.0.3,<10.0.0']

setup_kwargs = {
    'name': 'pybaqus',
    'version': '0.2.2',
    'description': '',
    'long_description': 'None',
    'author': 'Cristóbal Tapia Camú',
    'author_email': 'crtapia@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/cristobaltapia/pybaqus',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.7,<4.0.0',
}


setup(**setup_kwargs)
