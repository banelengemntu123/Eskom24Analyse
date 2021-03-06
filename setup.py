from setuptools import setup, find_packages

setup (
    name = 'eskomfunctions',
    version = '0.1',
    packages = find_packages(exclude=['tests*']),
    license = 'MIT',
    description = 'Package to calculate and visually display data received from Eskom',
    long_description = open('README.md').read(),
    install_requires = ['numpy', 'pandas'],
    url = 'https://github.com/banelengemntu123/Eskom24Analyse.git',
    author = 'team24'
)
