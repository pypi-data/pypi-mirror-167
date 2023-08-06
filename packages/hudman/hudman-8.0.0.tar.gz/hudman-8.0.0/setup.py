# coding=utf-8

# SPDX-FileCopyrightText: 2016-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fr:
    requirements = fr.read().splitlines()

setup(
    name='hudman',
    version='8.0.0',
    packages=find_packages(),
    package_dir={
        'hudman': 'hudman',
    },
    url='https://github.com/xvitaly/hudman',
    license='GPLv3',
    entry_points={
        'console_scripts': [
            'hudman = hudman.app.run:main',
        ],
    },
    install_requires=requirements,
    author='Vitaly Zaitsev',
    author_email='vitaly@easycoding.org',
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='HUD Manager is a simple tool for creating a local HUD mirror',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
