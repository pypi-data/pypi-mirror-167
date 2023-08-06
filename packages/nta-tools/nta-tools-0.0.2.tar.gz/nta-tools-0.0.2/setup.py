# Modify from https://github.com/navdeep-G/setup.py/blob/master/setup.py
import os
import re
from setuptools import setup, find_packages

__path__ = os.path.abspath(os.path.dirname(__file__))

# Package meta-data.
NAME = "nta-tools"
DESCRIPTION = 'A collection of network traffic analysis tools.'
URL = 'https://github.com/well-shark/nta'
EMAIL = 'wellshark.net@gmail.com'
AUTHOR = 'WellShark'
REQUIRES_PYTHON = '>=3.6.0'

REQUIRED = [
    "numpy",
    "pandas",
    "tqdm",
    "nfstream"
]

# https://github.com/wookayin/gpustat/blob/master/setup.py
def read_readme():
    with open("README.md", "r") as f:
        return f.read()

def read_version():
    with open(os.path.join(__path__, 'nta/__init__.py')) as f:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  f.read(), re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find __version__ string")

__version__ = read_version()

setup(
    name=NAME,
    version=read_version(),
    python_requires=REQUIRES_PYTHON,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    license="MIT",
    url=URL,
    packages=find_packages(),
    zip_safe=True,
    install_requires=REQUIRED,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)