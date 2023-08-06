# setup.py

from setuptools import setup, find_packages

setup(
    name="vuln-checkphone",
    version="0.1.6",
    description="YEah",
    packages=["checkphone"],
    package_data={'': ['libs/checkphone']},
    include_package_data=True,
    author='Jarle Kittilsen',
    author_email='jarle.spam@gmail.com',
    license='MIT License',

    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ]
)