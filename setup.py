#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='secrets2env',
    version='0.1.3',
    description='Command-line tool for generating environment variables from AWS Secrets',
    long_description=open('README.md').read(),
    # setuptools>=38.6.0 - https://packaging.python.org/specifications/core-metadata/#description-content-type
    long_description_content_type='text/markdown',
    maintainer='Eren Güven',
    maintainer_email='erengueven0@gmail.com',
    url='https://github.com/eguven/secrets2env',
    py_modules=['secrets2env'],
    install_requires=open('requirements.txt').read().split(),
    entry_points={
        'console_scripts': ['secrets2env=secrets2env:run'],
    },
    keywords='aws secrets environment deployment',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Security',
        'Topic :: Utilities',
    ]
)
