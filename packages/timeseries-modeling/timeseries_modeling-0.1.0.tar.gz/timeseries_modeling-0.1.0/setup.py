# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['timeseries_modeling',
 'timeseries_modeling.dataframes',
 'timeseries_modeling.predictors',
 'timeseries_modeling.predictors.autoregression',
 'timeseries_modeling.predictors.decomposition']

package_data = \
{'': ['*']}

install_requires = \
['Quandl>=3.7.0,<4.0.0',
 'matplotlib>=3.6.0,<4.0.0',
 'numpy>=1.23.3,<2.0.0',
 'pandas>=1.4.4,<2.0.0',
 'statsmodels>=0.13.2,<0.14.0',
 'yfinance>=0.1.74,<0.2.0']

setup_kwargs = {
    'name': 'timeseries-modeling',
    'version': '0.1.0',
    'description': 'Package to handle time series data, make predictions, and assess them',
    'long_description': 'None',
    'author': 'David Rodriguez',
    'author_email': 'davidrp1996@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
