from setuptools import setup, find_packages

setup (
    name = 'eskomfunctions',
    version = '0.1',
    packages = find_packages(exclude=['tests*']),
    license = 'MIT',
    description = 'Package to sort data received from Eskom',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = 'https://github.com/banelengemntu123/eskomproject123.git',
    author = 'team24'
)
