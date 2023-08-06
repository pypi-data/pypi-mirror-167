from ctypes.wintypes import LONG
from setuptools import setup, find_packages

with open("README.md", "r") as f:
  long_description  =  f.read()

setup(
    name = "cardano-method",
    version = '1.2.0',
    author = "Krish Shah",
    author_email = "shahkrish2016@gmail.com",
    description = "A basic cubic equation solver",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/isobarbaric/CardanoMethod",
    packages = find_packages(),
    install_requires = [],
    keywords = ['algebra', 'cardano', 'cardano-method', 'coefficients', 'complex', 'complex numbers', 'cubic', 'cubic equation', 'depressed cubic', 'equation', 'imaginary', 'method', 'polynomial', 'quadratic equation', 'real', 'roots', 'square root', 'zeroes'],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
