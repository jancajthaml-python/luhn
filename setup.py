from setuptools import setup, find_packages

from os import path

with open('README.md') as f:
  readme = f.read()

with open('LICENSE') as f:
  license = f.read()

setup(
  name='luhn',
  description='A sample Python project',
  long_description=readme,
  version='0.1.0',
  author='Jan Cajthaml',
  author_email='jan.cajthaml@gmail.com',
  license=license,
  keywords='luhn checkdigit checksum',
  url='https://github.com/jancajthaml-python/luhn',
  packages=find_packages(exclude=('tests')),
  extras_require={
    'test': ['coverage'],
  },
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Topic :: Utilities"
  ],
)
