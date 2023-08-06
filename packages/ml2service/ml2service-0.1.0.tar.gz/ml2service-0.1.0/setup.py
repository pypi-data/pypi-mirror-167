# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ml2service',
 'ml2service.models',
 'ml2service.serializers',
 'ml2service.services',
 'ml2service.services.runners',
 'ml2service.services.runners.fastapi',
 'ml2service.storages']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'pydantic>=1.9.1,<2.0.0']

extras_require = \
{'fastapi-uvicorn': ['fastapi>=0.79.0,<0.80.0',
                     'uvicorn[standard]>=0.18.2,<0.19.0']}

entry_points = \
{'console_scripts': ['ml2service = ml2service.cli:cli']}

setup_kwargs = {
    'name': 'ml2service',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'zerlok',
    'author_email': 'denergytro@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
