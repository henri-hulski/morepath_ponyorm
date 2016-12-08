# -*- coding: utf-8 -*-

import io
from setuptools import setup, find_packages

name = 'morepath_ponyorm'
description = (
    'Morepath PonyORM Demo'
)
long_description = (
    io.open('README.rst', encoding='utf-8').read() + '\n\n' +
    io.open('CHANGES.rst', encoding='utf-8').read())
version = '0.1.dev0'

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    author='Morepath developers',
    author_email='morepath@googlegroups.com',
    license='BSD',
    url="https://github.com/morepath/morepath_ponyorm",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'morepath >= 0.16.1',
        'pony >= 0.7',
    ],
    extras_require=dict(
        test=[
            'pytest >= 2.9.1',
            'pytest-remove-stale-bytecode',
            'WebTest >= 2.0.14',
        ],
        pep8=[
            'flake8',
            'pep8-naming',
        ],
        coverage=[
            'pytest-cov',
        ],
    ),
    entry_points=dict(
        console_scripts=[
            'run-app = morepath_ponyorm.run:run',
        ],
    ),
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
