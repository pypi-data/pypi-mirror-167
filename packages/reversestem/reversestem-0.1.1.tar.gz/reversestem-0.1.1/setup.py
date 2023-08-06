# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reversestem',
 'reversestem.dmo',
 'reversestem.dto',
 'reversestem.dto.a',
 'reversestem.dto.b',
 'reversestem.dto.c',
 'reversestem.dto.d',
 'reversestem.dto.e',
 'reversestem.dto.f',
 'reversestem.dto.g',
 'reversestem.dto.h',
 'reversestem.dto.i',
 'reversestem.dto.j',
 'reversestem.dto.k',
 'reversestem.dto.l',
 'reversestem.dto.m',
 'reversestem.dto.n',
 'reversestem.dto.o',
 'reversestem.dto.p',
 'reversestem.dto.q',
 'reversestem.dto.r',
 'reversestem.dto.s',
 'reversestem.dto.t',
 'reversestem.dto.u',
 'reversestem.dto.v',
 'reversestem.dto.w',
 'reversestem.dto.x',
 'reversestem.dto.y',
 'reversestem.dto.z',
 'reversestem.svc']

package_data = \
{'': ['*']}

install_requires = \
['baseblock', 'unicodedata2']

setup_kwargs = {
    'name': 'reversestem',
    'version': '0.1.1',
    'description': 'Unigram Lexicon for Reverse Stem Lookups',
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
