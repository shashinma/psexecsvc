#!/usr/bin/env python3
"""Setup script for psexecsvc."""

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding="utf-8").read()

setup(
    name="psexecsvc",
    version="1.0.0",
    author="deft_, cablethief, randomwalksp (reino)",
    author_email="",
    description="PSExeSVC remote orchestrator",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/sensepost/psexecsvc",
    py_modules=["psexecsvc"],
    scripts=["psexecsvc.py"],
    python_requires=">=3.6",
    install_requires=[
        "impacket",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security",
        "Topic :: System :: Networking",
    ],
    keywords="psexec smb impacket remote execution pentesting security",
    license="GPLv3",
)
