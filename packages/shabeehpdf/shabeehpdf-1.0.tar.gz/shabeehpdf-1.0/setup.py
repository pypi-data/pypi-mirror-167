import setuptools
from pathlib import Path


setuptools.setup(name="shabeehpdf",
                 version=1.0,
                 long_description=Path("README.md").read_text(),
                 packages=setuptools.find_packages(exclude=["tests and data"])   # This method will find and automatically identify the packages
                 )