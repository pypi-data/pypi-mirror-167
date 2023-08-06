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
    'version': '0.1.2',
    'description': "Multiselect component for Streamlit using Material UI's tool",
    'long_description': '# Material UI Multiselect component for Streamlit\n\n> Multiselect component for Streamlit using Material UI\'s tool.\n\n### Installation\n\n```\n$ pip install st-mui-multiselect\n```\n\n### Usage\n\n```\nimport streamlit as st\nfrom st_mui_multiselect import st_mui_multiselect\n\noptions = ["Mayo", "Lettuce", "Pickles", "Tomatoes", "Onions", "Mushrooms", "Ketchup", "Jalapeños"]\nselections = st_mui_multiselect(options, size=select_size)\nst.markdown("You selected %s" % ", ".join(selections))\n```\n\n## Development\n\n### Setup\n\n```\n$ poetry install\n$ cd st_mui_multiselect/frontend\n$ npm install\n```\n\n### Run dev\n\nYou need to run *both* npm dev server for the JS component frontend as well as streamlit\n```\n$ cd st_mui_multiselect/frontend\n$ npm run start\n```\n```\n$ poetry run streamlit run app.py\n```\n\n### Tooling\n\nInstall pre-commit hooks:\n```\n$ poetry run pre-commit install\n$ poetry run pre-commit install -t pre-push\n```\n\n### Publish\n\n```\n$ poetry build\n$ poetry publish\n```\n',
    'author': 'Nathan Lloyd',
    'author_email': 'nat272@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/supern8ent/st-mui-multiselect',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8, !=2.7.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*',
}


setup(**setup_kwargs)
