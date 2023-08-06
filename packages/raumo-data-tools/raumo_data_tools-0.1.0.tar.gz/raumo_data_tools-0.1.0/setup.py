# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['raumo_data_tools']

package_data = \
{'': ['*']}

install_requires = \
['influxdb-client>=1.28.0,<2.0.0', 'pandas>=1.4.0,<2.0.0']

setup_kwargs = {
    'name': 'raumo-data-tools',
    'version': '0.1.0',
    'description': 'Package containing core functions for data ETL workloads.',
    'long_description': '# data_toolbox\ndata handler package\n\n# Installation\n\n\n# Importbeispiele\n`from raumo_data_handler.data_handler import MatomoHandler`\n\n`from raumo_data_handler.influx_writer import InfluxDbWriter`\n\n`from raumo_data_handler.config_handler import ConfigHandler`\n',
    'author': 'Tanja Klopper',
    'author_email': 't.klopper@raumobil.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/raumobil/data_toolbox',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
