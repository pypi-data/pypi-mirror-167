# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['st_mui_multiselect']

package_data = \
{'': ['*'],
 'st_mui_multiselect': ['frontend/*',
                        'frontend/build/*',
                        'frontend/build/static/js/*',
                        'frontend/public/*',
                        'frontend/src/*']}

install_requires = \
['streamlit>=1.12.2,<2.0.0']

setup_kwargs = {
    'name': 'st-mui-multiselect',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Nathan Lloyd',
    'author_email': 'nat272@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8, !=2.7.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*',
}


setup(**setup_kwargs)
