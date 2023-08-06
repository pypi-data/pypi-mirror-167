# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['journal_prompts', 'journal_prompts.dto', 'journal_prompts.svc']

package_data = \
{'': ['*']}

install_requires = \
['baseblock']

setup_kwargs = {
    'name': 'journal-prompts',
    'version': '0.1.0',
    'description': 'Corpus of Random Journal Prompts',
    'long_description': None,
    'author': 'Craig Trim',
    'author_email': 'craigtrim@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.8.5',
}


setup(**setup_kwargs)
