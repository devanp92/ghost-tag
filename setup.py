#!/usr/bin/env python

import os
from setuptools import setup
from ghost_tag import _version


setup(name="ghosttag",
      version=_version.__version__,
      description="Tag updater for Ghost",
      long_description=open("README.me").read(),
      author="Devan Patel",
      author_email="devanppatel92@gmail.com",
      url="https://github.com/devanp92/ghost-tag-updater",
      license="MIT",
      packages=["ghosttag"],
      entry_points={"console_scripts": ["ghosttag = ghosttag.ghosttag:main"]},
      install_requires=['docopt==0.6.1',  'tabulate==0.7.5']
    )