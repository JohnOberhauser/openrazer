#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name="openrazer",
    version="2.8.2",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
)
