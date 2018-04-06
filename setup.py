#!/usr/bin/env python
"""Setup script for python-bseindia
"""
from setuptools import setup

setup(name='python-bseindia',
      version='0.1',
      description='API to access data on Bombay Stock Exchange',
      url='https://github.com/rpkharche/python-bseindia',
      author='Ravindra Kharche',
      author_email='rpkharche@gmail.com',
      license='MIT',
      packages=['python-bseindia'],
	  install_requires=[
          'pytest',
		  'beautifulsoup4'
      ],
      zip_safe=False)