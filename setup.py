#!/usr/local/env python3
from pip.req import parse_requirements
from setuptools import setup

requirements = parse_requirements('requirements.txt', session=False)
requirements = [str(r.req) for r in requirements]

setup(
    name='swagger-filter',
    description='Allows for filtering extension properties in yaml and json',
    author='MapCreator',
    author_email='bas.bieling@mapcreator.eu',
    url='https://github.com/MapOnline/swagger-filter',
    version='0.1.1',
    scripts=['bin/swagger-filter'],
    install_requires=requirements,
)
