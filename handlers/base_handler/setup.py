from setuptools import setup, find_packages
import os

setup(
    name="base_handler",
    version="0.0.0",
    packages=find_packages(exclude=("tests",)),
)