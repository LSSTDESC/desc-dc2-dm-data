#!/usr/bin/env python
"""
desc_dc2_dm_data
Providing consistent access to DC2 DM data products in DESC Python environments.

BSD 3-Clause License
Copyright (c) 2018, LSST Dark Energy Science Collaboration (DESC)
All rights reserved.
"""

import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'desc_dc2_dm_data', 'version.py')) as f:
    exec(f.read()) # pylint: disable=W0122

setup(
    name='desc_dc2_dm_data',
    version=__version__, # pylint: disable=E0602
    description='Providing consistent access to DC2 DM data products in DESC Python environments.',
    url='https://github.com/LSSTDESC/desc-dc2-dm-data',
    author='Yao-Yuan Mao',
    author_email='yymao.astro@gmail.com',
    maintainer='Yao-Yuan Mao',
    maintainer_email='yymao.astro@gmail.com',
    license='BSD 3-Clause License',
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='DESC DC2',
    packages=['desc_dc2_dm_data'],
)
