# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pyextoverlay']
setup_kwargs = {
    'name': 'pyextoverlay',
    'version': '1.0.2',
    'description': 'External overlay library',
    'long_description': None,
    'author': 'Xenely14',
    'author_email': 'a.maryatkin14@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
