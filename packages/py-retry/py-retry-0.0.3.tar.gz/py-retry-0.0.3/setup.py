# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['retry']

package_data = \
{'': ['*']}

install_requires = \
['mock>=4.0.3,<5.0.0', 'poetry-core>=1.0.7,<2.0.0', 'pytest>=6.2.5,<7.0.0']

setup_kwargs = {
    'name': 'py-retry',
    'version': '0.0.3',
    'description': 'A nice tool for retrying tasks when they are failed.',
    'long_description': '# PyRetry\n\nA nice decorator tool for retrying tasks when they failed. Forked from [retry](https://github.com/invl/retry)\n',
    'author': 'Abeautifulsnow',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Abeautifulsnow/PyRetry',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
