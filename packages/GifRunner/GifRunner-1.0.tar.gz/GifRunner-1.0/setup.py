from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0'
DESCRIPTION = 'help to exceute the gif file.'
LONG_DESCRIPTION = 'A package performance based on your processor, for any query :- rajputkaramveer2@gmail.com.'

# Setting up
setup(
    name="GifRunner",
    version=VERSION,
    author="Karamveer Rajput",
    author_email="rajputkaramveer2@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['gif', 'giffile', 'gifrun', 'python gif run', 'karamveer rajput', 'python','gifrunner', 'python gif runner'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix",
    ]
)