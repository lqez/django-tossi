#!/usr/bin/env python
import os
from setuptools import setup, find_packages

classifiers = [
    'Topic :: Utilities',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'License :: OSI Approved :: MIT License',
]

setup(
    name='django-template-korean',
    version='0.1.0',
    packages=find_packages(),
    author='Park, Hyunwoo',
    author_email='ez.amiryo' '@' 'gmail.com',
    maintainer='Park, Hyunwoo',
    maintainer_email='ez.amiryo' '@' 'gmail.com',
    url='http://github.com/lqez/django-template-korean',
    description='Django template filter for Korean via korean module',
    classifiers=classifiers,
    install_requires=[
        'korean>=0.1.4',
    ],
)
