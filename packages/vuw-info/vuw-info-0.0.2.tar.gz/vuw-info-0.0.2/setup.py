from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'Python Information'
LONG_DESCRIPTION = 'A python module to get computer information'

# Setting up
setup(
    name="vuw-info",
    version=VERSION,
    author="Hazzahs",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['gspread', 'pywin32', 'pycryptodome'],
    keywords=['python', 'information', 'osint', 'pentester', 'ngoto'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)