#!/usr/bin/env python
"""
pip setup file
"""
import os
import re

from setuptools import setup

__library__ = "python-lambda-utils"
__user__ = "https://github.com/cdgeorge7"


with open("README.md") as readme:
    LONG_DESCRIPTION = readme.read()


def find_version(*file_paths):
    """
    This pattern was modeled on a method from the Python Packaging User Guide:
        https://packaging.python.org/en/latest/single_source_version.html
    We read instead of importing so we don't get import errors if our code
    imports from dependencies listed in install_requires.
    """
    base_module_file = os.path.join(*file_paths)
    with open(base_module_file) as module_file:
        base_module_data = module_file.read()
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", base_module_data, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="python-lambda-utils",
    version=find_version("python-lambda-utils", "__init__.py"),
    description=("Custom utils package for AWS Lambda"),
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Chris George",
    author_email="cdgeorge7@gmail.com",
    url=f"{__user__}/{__library__}.git",
    download_url=f"{__user__}/{__library__}.git",
    license="LICENSE",
    packages=["python-lambda-utils"],
    install_requires=[
        "typing_extensions; python_version >= '3.5'"
    ],  # don't know proper python version
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    zip_safe=False,
    # extras_require={"cli": ["fire==0.1.3"]}, # TODO: DELETE, don't think i need this
    # entry_points={"console_scripts": ["utils=utils.__main__:main"]}, # TODO: DELETE, don't think i need this
)
