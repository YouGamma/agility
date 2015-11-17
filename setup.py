# =============================================================
# AGILITY SETUP
#
# Encoding: UTF-8
# =============================================================

"""
Setup script for Agility

USAGE:
    python setup.py install
    python setup.py nosetests
"""

import sys
import os.path

LOC0 = os.path.dirname(__file__) or os.curdir
os.chdir(LOC0)

LOC = os.curdir
sys.path.insert(0, LOC)

from setuptools import find_packages, setup

"""
Feature: Get this library's root
    Given this setup runs at the root of the library
    Then it should return the base path of the library
"""
AGILITY = os.path.join(LOC, "agility")

"""
Feature: Include only what is needed
    Given a root package
    Then it should find and include all sub-packages
"""
def find_packages_by_root(where):
    root = os.path.basename(where)
    packages = [ "%s.%s" % (root, package) for package in find_packages(where) ]
    packages.insert(0, root)
    return packages

setup(
    name = "agility",
    version = "0.0.1.dev0",
    description = "Full behavior driven toolset for python",
    author = "YouGamma",
    author_email = "hosein@yougamma.com",
    url = "https://github.com/YouGamma/agility",
    packages = find_packages_by_root(AGILITY),
    classifiers = [
        "Development Status :: 0 - Alpha",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT",
    ],
    license = "MIT",
    zip_safe = True,
    install_requires = requirements,
    entry_points = { "console_scripts": [ "agility = agility.bin:main" ] },
)
