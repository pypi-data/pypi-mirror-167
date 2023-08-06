# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aquiche']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aquiche',
    'version': '0.0.1',
    'description': 'Async cache in-memory',
    'long_description': '# aquiche\n\nAsync cache in-memory\n\nNOT READY FOR USE, JUST A PLACEHOLDER FOR THE NAME. REAL VERSION COMING SOON!',
    'author': 'Jakub Jantosik',
    'author_email': 'jakub.jantosik@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
