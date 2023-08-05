import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "rss-reader-bektur",
    version = "2.0",
    author = "Bektur Soltobaev",
    author_email = "bektur_soltobaev@epam.com",
    description = ("RSS reader for final task in Python educational course"),
    license = "BSD",
    keywords = "rss reader exam",
    url = "http://packages.python.org/rss-reader",
    packages=['rss_reader', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)