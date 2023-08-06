# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chemex',
 'chemex.configuration',
 'chemex.containers',
 'chemex.experiments',
 'chemex.experiments.catalog',
 'chemex.nmr',
 'chemex.optimize',
 'chemex.parameters',
 'chemex.plotters',
 'chemex.printers',
 'chemex.tools']

package_data = \
{'': ['*']}

install_requires = \
['cachetools>=5.2.0,<6.0.0',
 'lmfit>=1.0.3,<2.0.0',
 'matplotlib>=3.5.3,<4.0.0',
 'numpy>=1.23.3,<2.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'rapidfuzz>=2.8.0,<3.0.0',
 'rich>=12.5.1,<13.0.0',
 'scipy>=1.9.1,<2.0.0',
 'tomli>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['chemex = chemex.chemex:main']}

setup_kwargs = {
    'name': 'chemex',
    'version': '2022.0.0',
    'description': 'ChemEx is an analysis program for chemical exchange detected by NMR',
    'long_description': '# ChemEx\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n\n## Overview\n\nChemEx is an analysis program for chemical exchange detected by NMR.\n\nIt is designed to take almost any kind of NMR data to aid the analysis,\nbut the principle techniques are CPMG relaxation dispersion and Chemical\nExchange Saturation Transfer.\n\n## Installation\n\nThe easiest way to install `chemex` is via [conda](http://conda.pydata.org):\n\n```bash\nconda install -c conda-forge chemex\n```\n\nIf your version of python is less than 3.9, you can also install `chemex` in a separate conda environment enforcing the use of python 3.9+:\n\n```bash\nconda create -c conda-forge -n chemex python=3.10 chemex\nconda activate chemex\n```\n\n`chemex` is also available via the [Python package index](https://pypi.python.org/pypi/chemex) using `pip`:\n\n```bash\npip install chemex\n```\n\nThe development version can be installed directly from github via `pip`:\n\n```bash\npip install git+https://github.com/gbouvignies/chemex.git\n```\n',
    'author': 'Guillaume Bouvignies',
    'author_email': 'gbouvignies@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://gbouvignies.github.io/ChemEx/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
