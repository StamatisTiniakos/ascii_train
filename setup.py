from setuptools import find_packages, setup
from ascii_train import __author__, __version__

with open('requirements.txt') as f:
    requires = tuple(l[:-1] for l in f if not l.startswith('--'))

setup(
    name='ascii train',
    version=__version__,
    install_requires=requires,
    author=__author__,
    license='MIT',
    description='ascii art train library for Python 3',
    keywords='ascii art train',
    packages=find_packages(exclude=['tests*'])
)
