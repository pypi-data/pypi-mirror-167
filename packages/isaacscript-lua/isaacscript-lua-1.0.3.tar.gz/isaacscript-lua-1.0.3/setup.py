# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['isaacscript_lua']
entry_points = \
{'console_scripts': ['isaacscript-lua = isaacscript_lua:main']}

setup_kwargs = {
    'name': 'isaacscript-lua',
    'version': '1.0.3',
    'description': 'a script to manage IsaacScript libraries in a Lua mod',
    'long_description': None,
    'author': 'Zamiell',
    'author_email': '5511220+Zamiell@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
