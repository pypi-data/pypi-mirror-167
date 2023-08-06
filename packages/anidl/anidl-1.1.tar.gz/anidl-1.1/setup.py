#!/usr/bin/env python
from setuptools import setup
import anidl

setup(
    name='anidl',
    version=anidl.VERSION,
    description='Adl wrapper script written in python.',
    url='https://github.com/cronyakatsuki/py-adl',
    author='Crony Akatsuki',
    author_email='cronyakatsuki@gmail.com',
    license='GPL-3.0',
    py_modules=['anidl'],
    entry_points={
        'console_scripts': [
            'anidl=anidl:main',
        ],
    },
    keywords=['trackma', 'animld', 'anime', 'adl', 'linux', 'windows'],
)
