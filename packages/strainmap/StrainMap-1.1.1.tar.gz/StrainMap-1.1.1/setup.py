# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['strainmap', 'strainmap.gui', 'strainmap.models']

package_data = \
{'': ['*'], 'strainmap.gui': ['icons/*']}

install_requires = \
['h5py<=3.6',
 'keras<=2.8',
 'matplotlib>=3.5.3,<4.0.0',
 'natsort>=8.2.0,<9.0.0',
 'netCDF4>=1.6.1,<2.0.0',
 'nibabel>=4.0.2,<5.0.0',
 'opencv-python>=4.6.0,<5.0.0',
 'openpyxl>=3.0.10,<4.0.0',
 'pydicom>=2.3.0,<3.0.0',
 'python-decouple>=3.6,<4.0',
 'scipy>=1.9.1,<2.0.0',
 'tensorflow<=2.8',
 'tensorlayer<=2.2',
 'tqdm>=4.64.1,<5.0.0',
 'xarray>=2022.6.0,<2023.0.0']

setup_kwargs = {
    'name': 'strainmap',
    'version': '1.1.1',
    'description': '',
    'long_description': None,
    'author': 'RSE Team, Research Computing Service, Imperial College London',
    'author_email': 'ict-rse-team@imperial.ac.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/imperialcollegelondon/strainmap',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
