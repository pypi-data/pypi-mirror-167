import os

from setuptools import setup

consts = {}
with open(os.path.join("elvia", "const.py")) as fp:
    exec(fp.read(), consts)

setup(
    name="pyElvia",
    packages=["elvia"],
    install_requires=[
        "aiohttp==3.8.1",
        "urllib3>=1.26.12",
        "pykson>=0.9.9.8.7",
    ],
    version=consts["__version__"],
    description="A python3 library to read meter from Elvia",
    python_requires=">=3.9.0",
    author="Brage Skjønborg",
    author_email="bskjon@outlook.com",
    url="https://github.com/bskjon/pyElvia",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)