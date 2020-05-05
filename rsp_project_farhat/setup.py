import setuptools
from setuptools import setup, find_packages

setup(
    name="rsp_project_farhat",
    version="0.1.0",
    author="Farhat Jahan",
    author_email="",
    description="DHT11 sensor on Raspberry Pi",
    # packages=['dht11'],
    packages=setuptools.find_packages(),
    install_requires=["RPi.GPIO"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)