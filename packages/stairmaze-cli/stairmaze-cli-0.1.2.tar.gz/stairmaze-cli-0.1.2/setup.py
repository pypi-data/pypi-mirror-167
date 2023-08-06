#!/usr/bin/env python3.8

from distutils.core import setup
import os

import setuptools

packages = setuptools.find_packages(exclude=("tests.*", "tests"))

folder = os.path.dirname(__file__)
with open(os.path.join(folder, "requirements.txt")) as f:
    required = f.read().splitlines()
# required.extend(["setuptools==65.3.0"])

setup(
    name="stairmaze-cli",
    version="0.1.2",
    author="Emilio G. Ortiz García",
    author_email="",
    packages=packages,
    include_package_data=True,
    url="",
    license="LICENSE",
    description="Stairmaze cli",
    long_description=open("README.md").read(),
    install_requires=required,
    entry_points={"console_scripts": ["stairmaze=stairmaze.cli.app:app"]},
)
