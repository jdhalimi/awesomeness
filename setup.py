#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pathlib
import re
from setuptools import setup, find_packages

PACKAGE = 'awesomeness'
PACKAGE_NAME = 'awesomeness'


def read_version():
    p = pathlib.Path(__file__)
    p = p.parent / PACKAGE / '__init__.py'
    with p.open('r') as f:
        for line in f:
            if line.startswith('__version__'):
                line = line.split('=')[1].strip()
                match = re.match(r"^['\"](\d+\.\d+\.\d+\w*)['\"]", line)
                if match:
                    return match.group(1)
    raise ValueError('Unable to compute version')


def read(fname):
    file_path = pathlib.Path(__file__).parent / fname
    with file_path.open('r', encoding='utf-8') as f:
        return f.read()


setup(
    name=PACKAGE_NAME,
    version=read_version(),
    author='Jean-David Halimi',
    author_email='jdhalimi@free.fr',
    maintainer='Jean-David Halimi',
    maintainer_email='jdhalimi@free.fr',
    license='MIT',
    project_urls=dict(Source='https://github.com/jdhalimi/awesomeness',
                      Tracker='https://github.com/jdhalimi/awesomeness/issues'),
    url='https://awesomeness.readthedocs.io/',
    description='Project for opensource process testing.',
    long_description=read('README.rst'),
    packages=find_packages('.', exclude=('tests', 'example', 'docs')),
    python_requires='>=3.5',
    install_requires=['requests'],
    options={"bdist_wheel": {"universal": False}},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
            'awesomeness = ' + PACKAGE + '.__main__',
        ],
    },
)
