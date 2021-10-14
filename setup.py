#!/usr/bin/env python3
from setuptools import setup

setup(name='raphaella',
      version='0.1',
      packages=['dev_aberto'],
      python_requires=">=3",
      author = 'Raphael Azevedo',
      plataforms = ['Linux', 'Windows', 'MAC OS'],
      install_requires=["requests"],
      scripts=['scripts/hello.py']
      )