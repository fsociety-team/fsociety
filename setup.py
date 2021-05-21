#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = "fsociety"
DESCRIPTION = "A Modular Penetration Testing Framework"
URL = "https://fsociety.dev/"
GIT_URL = "https://github.com/fsociety-team/fsociety"
PROJECT_URLS = {
    "Packages": GIT_URL + "/blob/main/PACKAGES.md",
    "Changelog": GIT_URL + "/blob/main/CHANGELOG.md",
    "Funding": "https://github.com/sponsors/thehappydinoa",
    "Tracker": GIT_URL + "/issues",
    "Source": GIT_URL,
}
EMAIL = "contact@fsociety.dev"
AUTHOR = "fsociety-team"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = None

here = os.path.abspath(os.path.dirname(__file__))

pkg_vars = {}  # type: ignore
with open(os.path.join(here, NAME, "__version__.py")) as f:
    exec(f.read(), pkg_vars)

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


class TagCommand(Command):
    """Support setup.py push_tag."""

    description = "Push latest version as tag."
    user_options = []

    @staticmethod
    def status(s):
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.status("Pushing git tags…")
        os.system("git tag v{0}".format(pkg_vars["__version__"]))
        os.system("git push --tags")

        sys.exit()


setup(
    name=NAME,
    version=pkg_vars["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    project_urls=PROJECT_URLS,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    entry_points={
        "console_scripts": ["fsociety=fsociety:cli"],
    },
    install_requires=["rich>=9.2.0", "requests>=2.25.1", "gitpython"],
    extras_require={
        "dev": [
            "twine==3.4.1",
            "mypy==0.812",
            "flake8==3.9.2",
            "flake8-simplify==0.14.1",
            "flake8-comprehensions==3.5.0",
            "flake8-black==0.2.1",
            "black==21.5b1",
        ]
    },
    include_package_data=True,
    license="MIT",
    keywords=NAME,
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Topic :: Internet",
        "Topic :: Security",
        "Framework :: Flake8",
        "Environment :: Console",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    # python setup.py upload
    cmdclass={"push_tag": TagCommand},
)
