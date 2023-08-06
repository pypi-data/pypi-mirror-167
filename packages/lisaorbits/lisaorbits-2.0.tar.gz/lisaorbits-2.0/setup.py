#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-module-docstring,exec-used

import setuptools


with open("README.md", 'r', encoding='utf-8') as file:
    long_description = file.read()

meta = {}
with open("lisaorbits/meta.py", 'r', encoding='utf-8') as file:
    exec(file.read(), meta)

setuptools.setup(
    name="lisaorbits",
    version=meta['__version__'],
    author=meta['__author__'],
    author_email=meta['__email__'],
    description="LISA Orbits generates orbit files containing spacecraft positions and velocities, proper pseudo-ranges, and spacecraft proper times.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.in2p3.fr/lisa-simulation/orbits",
    packages=setuptools.find_packages(),
    install_requires=[
        'h5py',
        'numpy',
        'scipy',
        'matplotlib',
        'lisaconstants',
        'oem', 'lxml', 'defusedxml', 'astropy',
        'packaging',
    ],
    tests_require=['pytest'],
    python_requires='>=3.7',
)
