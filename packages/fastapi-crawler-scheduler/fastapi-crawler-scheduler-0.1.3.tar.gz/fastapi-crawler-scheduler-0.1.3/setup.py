# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_crawler_scheduler']

package_data = \
{'': ['*']}

install_requires = \
['redis>=4.3.4,<5.0.0', 'uhashring==2.1']

setup_kwargs = {
    'name': 'fastapi-crawler-scheduler',
    'version': '0.1.3',
    'description': '',
    'long_description': '',
    'author': 'laowang',
    'author_email': '847063657@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
