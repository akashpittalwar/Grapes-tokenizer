# setup.py
from setuptools import setup, find_packages

setup(
    name="sumtoken",
    version="0.1.0",
    packages=find_packages(exclude=["examples*"]),
    python_requires=">=3.6",
)
