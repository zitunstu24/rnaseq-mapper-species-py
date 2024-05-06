from setuptools import setup, find_packages

setup(
    name="RnaseqMapper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyYAML==6.0",
        "subprocess==0.0.5"
    ],
    entry_points={
        "console_scripts": [
            "RnaseqMapper=main:main",  # Change the script name here (use "RnaseqMapper")
        ]
    },
)
