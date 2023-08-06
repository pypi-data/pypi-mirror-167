"""
This file is essential if you intend to build the actual module in question.

will contain information about your package, specifically the name of 
the package, its version, platform-dependencies and a whole lot more. 
"""

from setuptools import setup, find_packages

VERSION = '0.0.6'
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="simple_package_023",
    version=VERSION,
    author="Mustafa Hakimi",
    author_email="test@test.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    py_modules=['simple_package'],
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
