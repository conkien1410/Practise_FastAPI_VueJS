#!usr/bin/env python

from setuptools import setup

setup(
    name='Distutils',
    version='1.0',
    description='Python Distribution Utilities',
    author='Greg Ward',
    author_email='gward@python.net',
    install_requires=['fastapi', 'uvicorn', 'Distutils'],
    entry_points={
        "console_scripts": [
            "startAPI=main:start"
        ]
    }

)