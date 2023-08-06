import os
from setuptools import find_packages, setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="myPackageTFIMM",
    version="0.0.2",
    author="Alaa Elmor",
    author_email="alaa.m.elmor@gmail.com",
    description="image models",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["myPackageTFIMM"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)