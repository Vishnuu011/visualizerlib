from setuptools import setup, find_packages
from pathlib import Path


def read_requirements():
    return Path(__file__).parent.joinpath("requirements.txt").read_text().splitlines()

dis = """""
A simple visualization and EDA helper package and also agent execute for plot insights
and ml helper classes and functions preprocessor, imputer, chain pipeline, columtrasformer
"""

setup(
    name="visualizerlib",  
    version="0.2.0",        
    packages=find_packages(),
    install_requires=read_requirements(),
    author="Vishnu",
    author_email="vishnurrajeev@gmail.com",
    description=dis,
    long_description=Path(__file__).parent.joinpath("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/Vishnuu011/visualizerlib/tree/main",  
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

