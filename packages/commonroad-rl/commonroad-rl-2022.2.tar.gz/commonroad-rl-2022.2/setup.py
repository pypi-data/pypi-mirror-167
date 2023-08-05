#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""commonroad_rl setup file."""

import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    print("Please install or upgrade setuptools or pip to continue")
    sys.exit(1)

setup(
    name="commonroad-rl",
    version="2022.2",
    packages=find_packages(
        exclude=["tests", "utils_run"]
    ),
    package_data={"": ["*.xml", "*.pickle"]},
    description="Tools for applying reinforcement learning on commonroad scenarios.",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    test_suite="commonroad_rl.tests",
    keywords="autonomous automated vehicles driving motion planning".split(),
    url="https://commonroad.in.tum.de/",
    install_requires=[
        "aenum",
        "networkx",
        "triangle",
        "gym==0.21.0",
        "Polygon3",
        "pybind11",
        "stable_baselines==2.10.0",
        "commonroad-io==2022.1",
        "commonroad-vehicle-models",
        "commonroad-drivability-checker==2022.1",
        "commonroad-route-planner==2022.1",
        "SALib==1.3.13"
    ],
    extras_require={
        "utils_run": ["optuna", "PyYAML"],
        "tests": ["pytest"],
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Operating System :: POSIX :: Linux"
    ],
)
