# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fractal_tasks_core']

package_data = \
{'': ['*']}

install_requires = \
['PyQt5-Qt5>=5.15.2,<6.0.0',
 'PyQt5-sip>=12.11.0,<13.0.0',
 'PyQt5>=5.15.7,<6.0.0',
 'anndata>=0.8.0,<0.9.0',
 'cellpose==2',
 'dask>=2022.6,<2022.8',
 'defusedxml>=0.7.1,<0.8.0',
 'graphviz>=0.20,<0.21',
 'imagecodecs>=2022.2.22,<2023.0.0',
 'llvmlite>=0.39.1,<0.40.0',
 'napari-skimage-regionprops>=0.5.3,<0.6.0',
 'napari-workflows>=0.2.3,<0.3.0',
 'ome-zarr>=0.5.1,<0.6.0',
 'pandas>=1.2.0,<2.0.0',
 'scikit-image>=0.19.3,<0.20.0']

setup_kwargs = {
    'name': 'fractal-tasks-core',
    'version': '0.1.3',
    'description': '',
    'long_description': '# fractal-tasks-core\nMain tasks for the Fractal analytics platform\n',
    'author': 'Jacopo Nespolo',
    'author_email': 'jacopo.nespolo@exact-lab.it',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/fractal-analytics-platform/fractal-tasks-core',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
