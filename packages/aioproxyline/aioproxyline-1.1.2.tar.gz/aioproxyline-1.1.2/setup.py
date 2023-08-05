# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aioproxyline',
 'aioproxyline.core',
 'aioproxyline.core.abc',
 'aioproxyline.core.methods',
 'aioproxyline.exceptions',
 'aioproxyline.types']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0', 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'aioproxyline',
    'version': '1.1.2',
    'description': 'Asynchronous wrapper to interact with proxyline.net API',
    'long_description': '[![Downloads](https://pepy.tech/badge/aioproxyline)](https://pepy.tech/project/aioproxyline)\n[![Downloads](https://pepy.tech/badge/aioproxyline/month)](https://pepy.tech/project/aioproxyline)\n[![Downloads](https://pepy.tech/badge/aioproxyline/week)](https://pepy.tech/project/aioproxyline)\n[![Code Quality Score](https://api.codiga.io/project/34554/score/svg)](https://api.codiga.io/project/34554/score/svg)\n[![Code Grade](https://api.codiga.io/project/34554/status/svg)](https://api.codiga.io/project/34554/status/svg)\n\n## 🔗 Links\n* 🎓 **Documentation:** [*CLICK*](https://aioproxyline.readthedocs.io/en/latest/)\n* 🖱️ **Developer contacts:** [![Dev-Telegram](https://img.shields.io/badge/Telegram-blue.svg?style=flat-square&logo=telegram)](https://t.me/marple_tech)\n## 🐦 Dependencies  \n\n| Library  |                       Description                       |\n|:--------:|:-------------------------------------------------------:|\n| aiohttp  | Asynchronous HTTP Client/Server for asyncio and Python. |\n| pydantic |                   JSON Data Validator                   |\n\n---\n',
    'author': 'Marple',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/marple-git/aioproxyline',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
