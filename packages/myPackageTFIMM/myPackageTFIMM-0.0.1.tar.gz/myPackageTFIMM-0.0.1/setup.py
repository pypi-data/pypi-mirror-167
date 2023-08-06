import os
from setuptools import find_packages, setup


setup(
    name="myPackageTFIMM",
    version="0.0.1",
    author="Alaa Elmor",
    author_email="alaa.m.elmor@gmail.com",
    description="image models",
    packages=["myPackageTFIMM"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)