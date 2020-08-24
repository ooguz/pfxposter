#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages
import os
import pfxposter
from crontab import CronTab

with open("README.md", "r") as fh:
    long_description = fh.read()

def _post_install():
    conf_includes = 'updated = 2020-08-24 00:00:00+00:00\n\n[mastodon]\n   mastodon_url = "https://oyd.social"\naccess_token = "your_access_token_here"\n\n[pixelfed]\npixelfed_url = "https://pixelfed.social"\nusername = "username"'
    cron_job = CronTab(user=os.getenv("USER"))
    autochecker = cron_job.new(command='pfxposter')
    autochecker.minute.every(1)
    cron_job.write()
    with open("{}/.pfxposter".format(os.getenv("HOME")), "w") as conf:
        conf.write(conf_includes)

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
    include_package_data=True,
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
    entry_points={"console_scripts": ["pfxposter = pfxposter.pfxposter:main"]},
    data_files=[('/home/{}/.pfxposter'.format(os.getenv("USER")), ['data/config.toml'])],
    python_requires=">=3.6",
    install_requires=['Mastodon.py>=1.5.1', 'atoma>=0.0.17', 'toml>=0.10.1', 'python-crontab>=2.5.1']
)  

_post_install()
