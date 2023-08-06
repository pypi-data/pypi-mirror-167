# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['acac']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'lxml>=4.9.1,<5.0.0',
 'pydantic>=1.10.1,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.5.1,<13.0.0',
 'tomli-w>=1.0.0,<2.0.0',
 'tomli>=2.0.1,<3.0.0',
 'typing-extensions>=4.3.0,<5.0.0']

entry_points = \
{'console_scripts': ['acac = acac.__main__:main']}

setup_kwargs = {
    'name': 'acac',
    'version': '0.1.0',
    'description': '競プロ便利ツール。AtCoder と アルゴ式 に対応。',
    'long_description': '# acac\n\n競プロ便利ツール。[AtCoder](https://atcoder.jp/) と [アルゴ式](https://algo-method.com/) に対応。\n',
    'author': 'seijinrosen',
    'author_email': '86702775+seijinrosen@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/seijinrosen',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
