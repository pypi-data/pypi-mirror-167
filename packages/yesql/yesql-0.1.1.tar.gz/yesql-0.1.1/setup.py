# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yesql',
 'yesql.bin',
 'yesql.core',
 'yesql.core.drivers',
 'yesql.core.drivers.postgresql']

package_data = \
{'': ['*']}

install_requires = \
['PyPika>=0.48.0,<0.49.0', 'sqlparse>=0.4.2,<0.5.0', 'typical>=2.8,<3.0']

extras_require = \
{'asyncpg': ['asyncpg>=0.25.0,<0.26.0', 'orjson>=3.5.1,<4.0.0'],
 'docs': ['mkdocs>=1.2.2,<2.0.0',
          'mkdocs-material>=8.0,<9.0',
          'mkdocs-awesome-pages-plugin>=2.5.0,<3.0.0'],
 'lint': ['mypy>=0.910,<0.911',
          'black>=22,<23',
          'flake8>=3.9.2,<4.0.0',
          'types-orjson>=0.1.1,<0.2.0'],
 'psycopg': ['orjson>=3.5.1,<4.0.0', 'psycopg[pool,binary]>=3.0,<4.0'],
 'tests': ['asyncpg>=0.25.0,<0.26.0',
           'orjson>=3.5.1,<4.0.0',
           'psycopg[pool,binary]>=3.0,<4.0',
           'pytest>=6.2.4,<7.0.0',
           'pytest-asyncio>=0.15.1,<0.16.0',
           'pytest-cov>=3.0,<4.0',
           'pytest-benchmark>=3.4.1,<4.0.0',
           'factory-boy>=3.2.1,<4.0.0']}

setup_kwargs = {
    'name': 'yesql',
    'version': '0.1.1',
    'description': 'YeSQL is a SQL-first data manipulation library that will replace your ORM.',
    'long_description': None,
    'author': 'Sean Stewart',
    'author_email': 'sean_stewart@me.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
