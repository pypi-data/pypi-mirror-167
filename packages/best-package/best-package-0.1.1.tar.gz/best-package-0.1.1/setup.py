# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['best_package',
 'best_package.d00_data_access',
 'best_package.d00_data_access.datasets.dataset01_dataset',
 'best_package.d00_data_access.model',
 'best_package.d00_data_access.services',
 'best_package.d01_pre_processing',
 'best_package.d01_pre_processing.model',
 'best_package.d01_pre_processing.services',
 'best_package.d02_modelling',
 'best_package.d02_modelling.model',
 'best_package.d02_modelling.services',
 'best_package.d03_outputting',
 'best_package.d03_outputting.model',
 'best_package.d03_outputting.services',
 'best_package.d_utils']

package_data = \
{'': ['*'],
 'best_package.d00_data_access.datasets.dataset01_dataset': ['dummy_data/*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'colored>=1.4.3,<2.0.0',
 'flax>=0.6.0,<0.7.0',
 'ipython>=8.5.0,<9.0.0',
 'ml-collections>=0.1.1,<0.2.0',
 'nbformat>=5.4.0,<6.0.0',
 'notebook>=6.4.12,<7.0.0',
 'optax>=0.1.3,<0.2.0',
 'pandas>=1.4.4,<2.0.0',
 'pyfiglet>=0.8.post1,<0.9',
 'tensorflow-datasets>=4.6.0,<5.0.0',
 'tensorflow>=2.10.0,<3.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'best-package',
    'version': '0.1.1',
    'description': '',
    'long_description': '',
    'author': 'Zaher Joukhadar',
    'author_email': 'zaher@joukhadar.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
