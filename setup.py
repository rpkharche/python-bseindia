#!/usr/bin/env python
"""Setup script for pyBSE
"""
from setuptools import setup

setup(name='pybseindia',
      version='0.1',
      description='API to access data on Bombay Stock Exchange',
      url='https://github.com/rpkharche/python-bseindia',
      author='Ravindra Kharche',
      author_email='rpkharche@gmail.com',
      license='MIT',
      packages=['pybseindia'],
	  install_requires=[
          'pytest',
		  'beautifulsoup4'
      ],
      zip_safe=False)