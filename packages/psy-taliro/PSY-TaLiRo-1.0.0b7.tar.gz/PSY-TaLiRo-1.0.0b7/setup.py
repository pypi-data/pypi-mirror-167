# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['staliro', 'staliro.core', 'staliro.parser']

package_data = \
{'': ['*'], 'staliro.parser': ['grammar/*']}

install_requires = \
['antlr4-python3-runtime>=4.7',
 'attrs>=21.0.0,<22.0.0',
 'matplotlib>=3.5.2,<4.0.0',
 'numpy>=1.21.5,<2.0.0',
 'py-taliro>=0.2.1,<0.3.0',
 'scipy>=1.6.2,<2.0.0',
 'typing-extensions>=4.2.0,<5.0.0']

setup_kwargs = {
    'name': 'psy-taliro',
    'version': '1.0.0b7',
    'description': 'System-level verification library using STL',
    'long_description': 'None',
    'author': 'Quinn Thibeault',
    'author_email': 'qthibeau@asu.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
