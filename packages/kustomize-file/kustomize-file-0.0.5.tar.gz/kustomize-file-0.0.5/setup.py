# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kustomize_file']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'pyyaml>=6.0,<7.0']

entry_points = \
{'console_scripts': ['kustomize-file = kustomize_file.main:app']}

setup_kwargs = {
    'name': 'kustomize-file',
    'version': '0.0.5',
    'description': 'Take a single kubernetes manifest containing multiple resources and split it to many files with a kustomization file',
    'long_description': 'None',
    'author': 'Martin Højland',
    'author_email': 'martin@goautonomous.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
