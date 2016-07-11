#!/usr/local/env python3
from pip.req import parse_requirements
from setuptools import setup

requirements = parse_requirements('requirements.txt', session=False)
requirements = [str(r.req) for r in requirements]

setup(
    name='swagger-filter',
    description='Allows for filtering extension properties in yaml and json',
    author='Mechazawa',
    url='https://github.com/Mechazawa/swagger-filter',
    version='0.1',
    scripts=['bin/swagger-filter'],
    install_requires=requirements,
)
