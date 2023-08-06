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
    'version': '1.2.1',
    'description': '',
    'long_description': '[![Test and build](https://github.com/ImperialCollegeLondon/strainmap/actions/workflows/ci.yml/badge.svg)](https://github.com/ImperialCollegeLondon/strainmap/actions/workflows/ci.yml)\n[![GitHub\nPages](https://github.com/ImperialCollegeLondon/strainmap/actions/workflows/docs.yml/badge.svg)](https://imperialcollegelondon.github.io/strainmap/)\n[![PyPI version shields.io](https://img.shields.io/pypi/v/strainmap.svg)](https://pypi.python.org/pypi/strainmap/)\n[![PyPI status](https://img.shields.io/pypi/status/strainmap.svg)](https://pypi.python.org/pypi/strainmap/)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/strainmap.svg)](https://pypi.python.org/pypi/strainmap/)\n[![PyPI license](https://img.shields.io/pypi/l/strainmap.svg)](https://pypi.python.org/pypi/strainmap/)\n\n# StrainMap\n\nCopyright (c) 2022, Imperial College London\nAll rights reserved.\n\nStrainMap provides a user-friendly and efficient way to analyse MRI data acquired with a\nnovel, high temporal and spatial resolution velocity-encoded MRI technique suitable for\nregional strain analysis in a short breath-hold. These images include magnitude and\nphase components.\n\nThe segmentation stage lets the user select the inner and outer\nwalls of the heart. This needs to be done for all images taken over a heartbeat and for\nas many slices (cross-sections of the heart) as available. The process can be manual –\nvery long – or assisted by several machine learning technologies such as snakes\nsegmentation or a deep neural network. The segmented heart, together with the phase\ninformation can be used in the next stage to extract information of the instantaneous,\nspatially-resolved velocity of the myocardium during the heartbeat in the form of\nvelocity curves ad heatmaps. All this information can be exported for further analysis\nelsewhere.\n\n## Instalation\n\n### Recommended way \n\nThe recomended way for end users to access and use the tool is via `pipx`:\n\n1. Install and configure [`pipx`](https://pypa.github.io/pipx/) following the\n   instructions appropriate for your operative system. Make sure it works well before\n   moving on.\n2. Install StrainMap with `pipx install strainmap`\n3. To run StrainMap just open a terminal and execute `strainmap`. You might want to\n   create a shortcut for this command in the desktop, for convenience.\n\nWhenever there is a new version of StrainMap, just run `pipx upgrade strainmap` and\nit will be downloaded and installed with no fuss.\n\n### Use a StrainMap executable\n\nAlternatively, you can download from the [release\npage](https://github.com/ImperialCollegeLondon/strainmap/releases) the self-contained\nexecutable corresponding to the version you are interested in. Bear in mind that these\nexecutables contain StrainMap and *all its dependencies*, meaning that each download can\nbe, potentially, very large.\n\n## For developers\n\nThis installation instructions assume the following pre-requisites:\n\n- Python >=3.8\n- [Poetry](https://python-poetry.org/) >= 1.11\n- Git\n\nIf these are already installed and the path correctly configured, the following should download the last version of StrainMap, create and activate a virtual environment, install all StrainMap dependencies and, finally, install StrainMap itself in development mode. \n\n```bash\ngit clone https://github.com/ImperialCollegeLondon/strainmap.git\ncd strainmap\npoetry install\n```\n\nTo use StrainMap simply run:\n\n```bash\npoetry run python -m strainmap\n```\n',
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
