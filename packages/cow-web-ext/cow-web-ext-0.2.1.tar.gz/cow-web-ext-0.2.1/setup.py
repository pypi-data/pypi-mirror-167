#!/usr/bin/python
'''Cow web ext installation configuration.'''
from pathlib import Path
from os import makedirs
from re import compile as re_compile
from subprocess import CalledProcessError
from subprocess import DEVNULL
from subprocess import check_output

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

setup(
    name='cow-web-ext',
    description='Host application for the Content Override & Watch web extension.',
    long_description=(Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    keywords=['Web Extension', 'Live Reload', 'firefox'],
    packages=[
        'cow_web_ext',
    ],
    package_dir = {'': 'host'},
    entry_points = {
        'console_scripts': [
            'cow-web-ext=cow_web_ext:cli',
            'cow-web-ext-host=cow_web_ext:host'
        ],
    },
    license='WTFPL',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'watchdog',
        'click'
    ],
    author='An Otter World',
    author_email='an-otter-world@ki-dour.org',
    url='https://github.com/an-otter-world/cow',
    zip_safe=False,
    setuptools_git_versioning={
        "enabled": True,
    },
    setup_requires=["setuptools-git-versioning"],
)
