# encoding: utf-8

from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

setup(
    name='django_addanother',
    version='2.2.2',
    author='Jonas Haag, James Pic',
    author_email='jonas@lophus.org, jamespic@gmail.com',
    packages=find_packages(exclude=['test_project']),
    zip_safe=False,
    include_package_data=True,
    url='https://github.com/jonashaag/django-addanother',
    description='"Add another" buttons outside the Django admin',
    long_description=long_description,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]
)
