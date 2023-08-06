# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pandas_lineage',
 'pandas_lineage.custom_types',
 'pandas_lineage.io',
 'pandas_lineage.io.parsers',
 'pandas_lineage.tests',
 'pandas_lineage.tests.types']

package_data = \
{'': ['*']}

install_requires = \
['openlineage-python==0.13.1', 'pandas==1.4.4']

setup_kwargs = {
    'name': 'pandas-lineage',
    'version': '0.0.1',
    'description': 'A pandas extension built for OpenLineage',
    'long_description': "# pandas-lineage\nBEWARE: This project is in very early stages (as of 2022-09-12)\n\npandas-lineage is intended to extend the functionality of I/O and standard transform operations on a pandas dataframe to emit OpenLineage RunEvents. I am starting just with read/write operations emiting RunEvents with schema facets.\n\n## Badges:\n![python-package](https://github.com/gage-russell/pandas-lineage/actions/workflows/python-package.yml/badge.svg)\n\n## Examples:\n* [marquez-examples](examples/marquez-example/)\n  * contains getting started code and a script for running Marquez locally in Docker\n* [mock-api-example](examples/mock-api-example)\n  * contains getting started code and a simple Flask API for sending lineage events to which will just always return a 200 status code\n\n## References:\n* :green_heart: [Marquez](https://github.com/MarquezProject/marquez) :green_heart:\n* :green_heart: [OpenLineage](https://github.com/OpenLineage/OpenLineage) :green_heart:\n* :green_heart: [Pandas](https://github.com/pandas-dev/pandas) :green_heart:\n\n## Contributing:\n[Issues](https://github.com/gage-russell/pandas-lineage/issues)\n\nI have not created any sort of contribution guide yet, but I don't want that to stop anyone!\nIf you are interested in contributing, fork this repository and open a PR. As this becomes more feature-rich/useful, we will establish a contributors workflow. For now, please just use the pre-commit hooks.\n\n## Notes:\n* The pandas-lineage directory structure (for now) will mirror the directory structure of pandas for the components that it is extending.\n",
    'author': 'Gage Russell',
    'author_email': 'gage.russell.dev@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
