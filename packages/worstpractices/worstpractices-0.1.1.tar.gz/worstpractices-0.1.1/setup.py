# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['worstpractices', 'worstpractices.rl']

package_data = \
{'': ['*']}

install_requires = \
['fire<1.0.0']

entry_points = \
{'console_scripts': ['worstrl = worstpractices.cmd:worstrl']}

setup_kwargs = {
    'name': 'worstpractices',
    'version': '0.1.1',
    'description': 'An opinionanted library of Python/ML practices',
    'long_description': '# Worst Practices\n\nThis python package is a codification of my major opinions on how to do stuff in Python/AI/ML.\nFeel free to reuse it, but beware: my tastes are unconventional',
    'author': 'Vadim Liventsev',
    'author_email': 'dev@vadim.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
