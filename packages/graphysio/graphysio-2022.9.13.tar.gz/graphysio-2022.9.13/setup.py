# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graphysio',
 'graphysio.algorithms',
 'graphysio.plotwidgets',
 'graphysio.readdata',
 'graphysio.transformations',
 'graphysio.ui',
 'graphysio.writedata']

package_data = \
{'': ['*']}

install_requires = \
['Pint>=0.19.2,<0.20.0',
 'numexpr==2.8.3',
 'pandas>=1.4.3,<2.0.0',
 'pathvalidate>=2.5.0,<3.0.0',
 'physiocurve>=2022.7.14,<2023.0.0',
 'pyqtgraph>=0.12.4,<0.13.0',
 'scipy>=1.8.1,<2.0.0']

entry_points = \
{'console_scripts': ['graphysio = graphysio.main:main']}

setup_kwargs = {
    'name': 'graphysio',
    'version': '2022.9.13',
    'description': 'Visualizer and analyser for biometric signals',
    'long_description': '# GraPhysio\nGraPhysio is a graphical time series visualizer created for biometric data\nsignals from ICU patient monitors. It is however not limited to this. It can\nhandle low frequency and high frequency data as well as aggregating and\nsynchronizing signals from different sources. GraPhysio supports basic\nmathematical operations and filters and can help selecting and exporting time\nperiods. GraPhysio can read data from CSV, Parquet and EDF files and can write\nCSV, Parquet, EDF and Matlab files.\n\n## Install instructions\nFor the best experience, conda is recommended:\n\nconda install -c conda-forge graphysio\n\nAlternatively you can then install the latest version of GraPhysio from PyPi by\ntying the following command:\n\n> python -m pip install graphysio\n\nYou can launch GraPhysio by typing:\n\n> python -m graphysio\n',
    'author': 'Jona Joachim',
    'author_email': 'jona@joachim.cc',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jaj42/GraPhysio',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
