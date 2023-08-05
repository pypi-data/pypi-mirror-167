# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jupyterhub_nomad_spawner',
 'jupyterhub_nomad_spawner.consul',
 'jupyterhub_nomad_spawner.nomad']

package_data = \
{'': ['*'], 'jupyterhub_nomad_spawner': ['templates/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'attrs>=21.4.0,<22.0.0',
 'httpx>=0.23.0,<0.24.0',
 'jupyterhub>=2.2.2,<3.0.0',
 'notebook>=6.4.11,<7.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'tenacity>=8.0.1,<9.0.0',
 'traitlets>=5.1.1,<6.0.0']

entry_points = \
{'jupyterhub.spawners': ['nomad-spawner = '
                         'jupyterhub_nomad_spawner.spawner:NomadSpawner']}

setup_kwargs = {
    'name': 'jupyterhub-nomad-spawner',
    'version': '0.0.4',
    'description': '',
    'long_description': 'None',
    'author': 'Max Fröhlich',
    'author_email': 'maxbruchmann@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
