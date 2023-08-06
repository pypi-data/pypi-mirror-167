from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'Plot on origin automatically'
LONG_DESCRIPTION = 'A package that plot on origin automatically.'

# Setting up
setup(
    name="originpy",
    version=VERSION,
    author="Shaohan Tian",
    author_email="<shaohan.tian@hotmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['originpro', 'numpy', 'pandas'],
    keywords=['python', 'test', 'orginpy'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
