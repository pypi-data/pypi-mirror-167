#!/usr/bin/env python3

import os

from setuptools import find_packages, setup

# get key package details from vmc_reporter/__version__.py
about = {}  # type: ignore
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "vmc_reporter", "__version__.py"), encoding="utf-8") as f:
    exec(f.read(), about)

# load the README file and use it as the long_description for PyPI
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# package configuration - for reference see:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#id9
setup(
    name=about["__title__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=find_packages(),
    package_data={"": ["py.typed"]},
    include_package_data=True,
    python_requires=">=3.10.*",
    install_requires=["requests", "jsonschema", "packaging"],
    license=about["__license__"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="",
)
