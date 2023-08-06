#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '0.5'

def read(name):
    with open(name) as f:
        return f.read()

long_description=(
        read('README.rst')
        + '\n' +
        read('CHANGES.rst')
    )

setup(name="xupdate-processor",
      version=version,
      description="XUpdate Processor",
      long_description=long_description,
      author="Nicolas DELABY",
      author_email="nicolas@nexedi.com",
      url="https://lab.nexedi.com/nexedi/xupdate_processor",
      license="GPL",
      packages=find_packages('src'),
      package_dir={'': 'src'},
      scripts=["xuproc"],
      install_requires=['six', 'lxml', 'erp5diff >= 0.7'],
      classifiers=['License :: OSI Approved :: GNU General Public License (GPL)',
                  'Operating System :: OS Independent',
                  'Topic :: Text Processing :: Markup :: XML',
                  'Topic :: Utilities'],
      include_package_data=True,
      zip_safe=False,
     )
