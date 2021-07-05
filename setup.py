#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    author="Ittay Eyal, Adam Matan",
    author_email='ittay@technion.ac.il, adam@matan.name',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    description="Persistent memoization to disk allows inter-process memoization",
    license="MIT license",
    keywords=['memoization', 'decorator', 'persistent', 'cache'],
    name='memoize',
    packages=find_packages(),
    url='https://github.com/IttayEyal/memoization',
    version='0.1.0',
)
