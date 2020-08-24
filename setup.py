#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages
import os
import pfxposter

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='pfxposter',
    version=pfxposter.__version__,
    description='A simple PixelFed to Mastodon/Twitter crossposter',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ooguz/pfxposter',
    author='Özcan Oğuz',
    author_email='ozcan@oyd.org.tr',
    license='GLWTS(Good Luck With That Shit) Public License',
    packages=find_packages(),
    zip_safe=False,
    project_urls={
        "Bug Tracker": "https://github.com/ooguz/pfxposter/issues",
        "Source Code": "https://github.com/ooguz/pfxposter",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: No Input/Output (Daemon)",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
    ],
    data_files=[('/home/{}/.pfxposter', ['data/config.toml'])],
    python_requires=">=3.6",
    install_requires=['Mastodon.py>=1.5.1', 'atoma>=0.0.17', 'toml>=0.10.1']
)  
