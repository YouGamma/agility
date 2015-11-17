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
Feature: Include only what is needed
    Given a root package
    Then it should find and include all sub-packages
"""
def find_packages_by_root(where):
    root = os.path.basename(where)
    packages = [ "%s.%s" % (root, package) for package in find_packages(where) ]
    packages.insert(0, root)
    return packages
