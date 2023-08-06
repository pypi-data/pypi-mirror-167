from setuptools import setup

setup(
    name='mma_fighters_sdk',
    version='1.2.0',
    description='SDK for mma_fighters_sdk',
    url='https://github.com/hallrizon-io/mma_fighters_game_sdk',
    author='Kostiantyn Minkov',
    author_email='hallrizon.usa@gmail.com',
    license='BSD 2-clause',
    packages=[],
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    python_requires=">=3.6"
)

import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

