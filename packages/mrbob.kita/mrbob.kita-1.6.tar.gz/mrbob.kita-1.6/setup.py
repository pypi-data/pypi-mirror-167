#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name="mrbob.kita",
    version='1.6',
    description="mr.bob templates for kitayazilim's Odoo projects",
    long_description=open("README.rst").read(),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: "
        "GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Odoo",
    ],
    license="LGPLv3",
    author="kitayazilim.com",
    author_email="info@kitayazilim.com",
    install_requires=["mr.bob"],
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
)
