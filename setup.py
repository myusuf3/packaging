#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="packaging",
    version="0.1",

    description="Possible implementation of Packaging primitives for Python",
    #long_description=open("README.rst").read(),
    url="https://github.com/dstufft/packaging/",

    author="Donald Stufft",
    author_email="donald.stufft@gmail.com",

    install_requires=[
        "six",
    ],

    extras_require={
        "tests": ["pytest", "pytest-cov", "pytest-pep8"],
    },

    packages=find_packages(exclude=["tests"]),
    package_data={},
    include_package_data=True,

    zip_safe=False,
)
