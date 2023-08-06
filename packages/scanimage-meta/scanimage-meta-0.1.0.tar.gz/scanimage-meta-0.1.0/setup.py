# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scanimage_meta']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19', 'scanimage-tiff-reader>=1.4.1,<2.0.0']

setup_kwargs = {
    'name': 'scanimage-meta',
    'version': '0.1.0',
    'description': '"Provides a more convenient and object oriented wrapper for the metadata coming from Scannimagetiffreader"',
    'long_description': "Nicer metadata format wrapper for scanimage tif reader:\nhttps://pypi.org/project/scanimage-tiff-reader/\n\nProvides more convenient and object oriented access \n\nCurrent status: \n    Works, but not thouroughly tested \n\n\n\nExample:\n\nmeta = ScanimageMeta.fromfilepath('scanimagetif.tif')\nprint(meta.SI.hRoiManger.scanFrameRate)\n",
    'author': 'Joe Donovan',
    'author_email': 'joe311@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
