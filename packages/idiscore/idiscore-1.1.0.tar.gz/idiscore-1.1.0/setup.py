# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['idiscore']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0', 'dicomgenerator>=0.4.0,<0.5.0']

setup_kwargs = {
    'name': 'idiscore',
    'version': '1.1.0',
    'description': 'Pure-python deidentification of DICOM images using Attribute Confidentiality Options',
    'long_description': 'None',
    'author': 'sjoerdk',
    'author_email': 'sjoerd.kerkstra@radboudumc.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
