# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geospatial_lib',
 'geospatial_lib.core',
 'geospatial_lib.db',
 'geospatial_lib.misc']

package_data = \
{'': ['*']}

install_requires = \
['GeoAlchemy2>=0.12.5,<0.13.0',
 'SQLAlchemy-Utils>=0.38.3,<0.39.0',
 'geopandas>=0.11.1,<0.12.0',
 'psycopg2-binary>=2.9.3,<3.0.0',
 'xlrd>=2.0.1,<3.0.0']

setup_kwargs = {
    'name': 'geospatial-lib',
    'version': '0.30.3',
    'description': 'A library with some geo functions',
    'long_description': 'GeoLib\n=====\n[![RunTest](https://github.com/amauryval/geolib/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/amauryval/geolib/actions/workflows/main.yml)\n[![codecov](https://codecov.io/gh/amauryval/geolib/branch/master/graph/badge.svg)](https://codecov.io/gh/amauryval/geolib)\n\n',
    'author': 'amauryval',
    'author_email': 'amauryval@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
