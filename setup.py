#!/usr/bin/env python
from setuptools import setup, find_packages
from setuptools.command.install import install
import os

here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


class CustomInstall(install):

    def run(self):
        install.run(self)
        os.system("sudo python -m spacy download en")


setup(name='tensechanger',
      version='0.1',
      description='Change the tense of text',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Shashi Tripathi, Rahul Kumar Yadav',
      author_email='tripathi.shashi@tcs.com',
      url='https://github.com/itsshavar/tensechanger',
      packages=find_packages(exclude='test'),
      install_requires=['spacy', 'pattern'],
      cmdclass={'install': CustomInstall},
      extras_require={
          'test': ['pytest'],
      },
      )
